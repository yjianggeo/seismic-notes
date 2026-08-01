"""
Regenerate corrected figures for:
  1. sw_dispersion.png   — group velocity now stays positive (Lorentzian c(f))
  2. fk_analysis.png     — proper synthetic gather with P-wave + surface wave events
  3. radon_transform.py  — proper CMP gather for L2 vs sparse Radon comparison
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from numpy.fft import rfft, irfft

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
})

# ─────────────────────────────────────────────────────────────────────
# Figure 1: Surface-wave dispersion (sw_dispersion.png)
# Fix: replace steep tanh with Lorentzian → group velocity stays > 0
# ─────────────────────────────────────────────────────────────────────

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Surface Wave Analysis', fontsize=12, fontweight='bold')

f = np.linspace(0.5, 50, 600)
Vs1, Vs2 = 200.0, 600.0
VR1, VR2 = Vs1 * 0.919, Vs2 * 0.919
h = 20.0  # layer thickness (m)

# Lorentzian transition: c(f) = VR1 + (VR2-VR1) / (1 + (f/f_trans)^2)
# U(f) = VR1 + (VR2-VR1)*(1-x^2)/(1+x^2)^2  where x=f/f_trans  → always > 0
f_trans = (VR1 + VR2) / 2 / (2 * h)   # same transition frequency
x = f / f_trans
c_ph = VR1 + (VR2 - VR1) / (1 + x**2)
U    = VR1 + (VR2 - VR1) * (1 - x**2) / (1 + x**2)**2

ax = axes[0]
ax.fill_between(f, U, c_ph, where=(c_ph >= U), alpha=0.15, color='#3498db',
                label='c − U (dispersion zone)')
ax.plot(f, c_ph, color='#3498db', lw=2.5, label='Phase velocity $c(f)$')
ax.plot(f, U,    color='#e74c3c', lw=2.5, ls='--', label='Group velocity $U(f)$')
ax.axhline(VR2, color='gray', lw=0.8, ls=':', alpha=0.7)
ax.axhline(VR1, color='gray', lw=0.8, ls=':', alpha=0.7)
ax.text(48, VR2 + 8, f'$V_{{R2}}$ ≈ {VR2:.0f} m/s', ha='right', fontsize=7.5, color='gray')
ax.text(48, VR1 + 8, f'$V_{{R1}}$ ≈ {VR1:.0f} m/s', ha='right', fontsize=7.5, color='gray')
ax.set(xlabel='Frequency (Hz)', ylabel='Velocity (m/s)',
       title='Rayleigh Wave Dispersion Curve\n(2-layer: soft over hard)',
       xlim=[0.5, 50], ylim=[0, VR2 * 1.12])
ax.legend(fontsize=8.5)
ax.grid(True, alpha=0.3)

# Depth sensitivity kernels
z = np.linspace(0, 120, 400)
ax = axes[1]
for fi, col in zip([5, 15, 30, 50], ['#2ecc71', '#3498db', '#e67e22', '#e74c3c']):
    idx = np.argmin(np.abs(f - fi))
    c_fi = c_ph[idx]
    z_pk = c_fi / (3.0 * fi)
    sig  = max(z_pk * 0.55, 1.0)
    K    = np.exp(-(z - z_pk)**2 / (2 * sig**2))
    ax.plot(K / K.max(), z, color=col, lw=2.2,
            label=f'$f$ = {fi} Hz (peak ≈ {z_pk:.0f} m)')
ax.set(xlabel='Normalised sensitivity $\\partial c/\\partial V_S(z)$',
       ylabel='Depth (m)',
       title='Depth Sensitivity Kernels\n(Rayleigh wave, fundamental mode)',
       ylim=[120, 0], xlim=[-0.05, 1.15])
ax.legend(fontsize=8, loc='lower right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('docs/assets/images/sw_dispersion.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved sw_dispersion.png  — U_min = {:.1f} m/s (positive OK)".format(float(U.min())))


# ─────────────────────────────────────────────────────────────────────
# Figure 2: F-K analysis & fan filtering (fk_analysis.png)
# Fixes:
#   1. wav_len << nt so events are actually inserted
#   2. dx=10m to avoid spatial aliasing of 350 m/s surface wave
#   3. Correct F-K imshow orientation (no transpose; origin='lower')
#   4. Correct velocity lines drawn in (f, k) space
# ─────────────────────────────────────────────────────────────────────

def ricker(f0, dt, n):
    tc = np.arange(n) * dt - n * dt / 2.0
    return (1 - 2 * (np.pi * f0 * tc)**2) * np.exp(-(np.pi * f0 * tc)**2)

dt = 0.004; dx = 10.0          # dx=10 m → f_alias(350m/s) = 350/20 = 17.5 Hz
nt = 256;   nx = 72            # ~720 m aperture
t_ax = np.arange(nt) * dt     # 0 … 1.02 s
x_ax = np.arange(nx) * dx     # 0 … 710 m
wav_len = 48                   # short wavelet: 0.192 s

wav_P  = ricker(30.0, dt, wav_len)
wav_SW = ricker(7.0,  dt, wav_len)   # 7 Hz surface wave

data = np.zeros((nx, nt))

# P-wave reflections (hyperbolic moveout, 3 events)
for t0, v_int in [(0.25, 2000.0), (0.55, 2100.0), (0.80, 2200.0)]:
    for ix, xi in enumerate(x_ax):
        t_hyp = np.sqrt(t0**2 + (xi / v_int)**2)
        it = int(round(t_hyp / dt))
        if 0 <= it <= nt - wav_len:
            data[ix, it:it + wav_len] += wav_P * np.exp(-t_hyp * 0.4)

# Surface wave (linear moveout, 350 m/s)
for ix, xi in enumerate(x_ax):
    it = int(round((0.02 + xi / 350.0) / dt))
    if 0 <= it <= nt - wav_len:
        data[ix, it:it + wav_len] += 3.0 * wav_SW

# Mild random noise
rng = np.random.default_rng(42)
data += 0.06 * np.abs(data).max() * rng.standard_normal(data.shape)

# ── 2-D FFT ──
# FK shape: (nx, nt) = (k-axis, f-axis)
FK   = np.fft.fftshift(np.fft.fft2(data))
f_fk = np.fft.fftshift(np.fft.fftfreq(nt, dt))   # length nt
k_fk = np.fft.fftshift(np.fft.fftfreq(nx, dx))   # length nx, in 1/m

# ── Fan filter in FK space ──
# Build KK and FF with shape matching FK: (nx, nt)
KK, FF = np.meshgrid(k_fk, f_fk, indexing='ij')   # both (nx, nt)
eps   = 1e-9
v_app = np.abs(FF / (KK + eps))
mask  = np.where((np.abs(KK) < eps) | (v_app >= 700.0), 1.0, 0.0)
mask  = gaussian_filter(mask.astype(float), sigma=1.5)
data_filt = np.real(np.fft.ifft2(np.fft.ifftshift(FK * mask)))

# ── Plot ──
fig, axes = plt.subplots(2, 2, figsize=(11, 8))
fig.suptitle('F-K Analysis and Fan Filtering', fontsize=12, fontweight='bold')

# Helper: seismic gather imshow (x-axis=offset, y-axis=time↓)
def plot_gather(ax, d, x, t, title):
    vmax = np.percentile(np.abs(d), 98)
    # d shape (nx, nt) → .T gives (nt, nx): rows=time, cols=space
    ax.imshow(d.T, aspect='auto', cmap='seismic',
              extent=[x[0]/1e3, x[-1]/1e3, t[-1], t[0]],
              vmin=-vmax, vmax=vmax)
    ax.set(xlabel='Offset (km)', ylabel='Time (s)', title=title)

plot_gather(axes[0, 0], data,      x_ax, t_ax, 'Original gather')
plot_gather(axes[1, 1], data_filt, x_ax, t_ax, 'After F-K fan filtering')

# F-K spectrum: FK shape (nx, nt) = (k, f)
# imshow without .T: rows→k (y), cols→f (x)
# Use origin='lower' so row 0 (k_fk[0], most negative) is at bottom
fk_amp = np.log10(np.abs(FK) + 1)   # shape (nx, nt)
k_km   = k_fk * 1e3                  # convert to 1/km
fk_ext = [f_fk[0], f_fk[-1], k_km[0], k_km[-1]]   # [fmin, fmax, kmin, kmax]
axes[0, 1].imshow(fk_amp, aspect='auto', cmap='hot_r', origin='lower',
                  extent=fk_ext)
axes[0, 1].set(xlabel='Frequency (Hz)', ylabel='Wavenumber (1/km)',
               title='F-K spectrum (log amplitude)', xlim=[-125, 125])

# Velocity lines: k = f/v  (in 1/km when f in Hz, v in km/s)
f_pos = np.linspace(0, 125, 300)
k_Nyq = 1e3 / (2 * dx)              # Nyquist in 1/km
for v_ms, col, ls, lbl in [(2000, 'w', '-', '2000 m/s'), (350, 'c', '--', '350 m/s')]:
    v_kms = v_ms / 1000.0           # km/s
    k_line = f_pos / v_kms          # in 1/km (f in Hz, v in km/s → k in 1/km)
    # Clip to Nyquist
    fmask = k_line <= k_Nyq
    axes[0, 1].plot( f_pos[fmask],  k_line[fmask], color=col, ls=ls, lw=1.5, label=lbl)
    axes[0, 1].plot(-f_pos[fmask], -k_line[fmask], color=col, ls=ls, lw=1.5)
axes[0, 1].set_ylim([k_km[0], k_km[-1]])
axes[0, 1].legend(loc='upper left', fontsize=8)

# Fan filter mask (same axes as FK spectrum)
axes[1, 0].imshow(mask, aspect='auto', cmap='gray', origin='lower',
                  extent=fk_ext)
axes[1, 0].set(xlabel='Frequency (Hz)', ylabel='Wavenumber (1/km)',
               title='Fan filter mask (white = pass)', xlim=[-125, 125])

plt.tight_layout()
plt.savefig('docs/assets/images/fk_analysis.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved fk_analysis.png")


# ─────────────────────────────────────────────────────────────────────
# Figure 3: Radon transform comparison (radon_transform.png)
# Fix: proper CMP gather, L2 vs sparse IRLS Radon
# ─────────────────────────────────────────────────────────────────────

dt  = 0.004; dx = 25.0
nt  = 256;   nx = 48
t_ax = np.arange(nt) * dt
x_ax = np.arange(nx) * dx
wav_len = 48
wav  = ricker(28.0, dt, wav_len)

# CMP gather: 3 hyperbolic reflection events + mild noise
data_r = np.zeros((nx, nt))
for t0, v_nmo in [(0.3, 2000.0), (0.5, 2200.0), (0.75, 2400.0)]:
    for ix, xi in enumerate(x_ax):
        t_h = np.sqrt(t0**2 + (xi / v_nmo)**2)
        it = int(round(t_h / dt))
        if 0 <= it <= nt - wav_len:
            data_r[ix, it:it + wav_len] += wav * np.exp(-t_h * 0.3)

rng = np.random.default_rng(7)
data_r += 0.06 * np.abs(data_r).max() * rng.standard_normal(data_r.shape)

# Linear Radon (tau-p) in frequency domain
p_vals = np.linspace(-0.5e-3, 1.5e-3, 100)  # s/m
nf   = nt // 2 + 1
D    = rfft(data_r, axis=1)               # (nx, nf)
L    = np.exp(-2j * np.pi * np.outer(p_vals, x_ax))  # (np, nx)
LLH  = L @ np.conj(L).T                  # (np, np)

M_L2 = np.zeros((len(p_vals), nf), dtype=complex)
M_hr = np.zeros((len(p_vals), nf), dtype=complex)

for iif in range(1, nf):
    d_f = D[:, iif]
    freq = iif / (nt * dt)
    Lf  = np.exp(-2j * np.pi * freq * np.outer(p_vals, x_ax))
    LfLfH = Lf @ np.conj(Lf).T
    rhs  = Lf @ d_f
    eps  = max(0.5e-3 * np.dot(d_f.conj(), d_f).real / nx, 1e-10)

    m_L2 = np.linalg.solve(LfLfH + eps * np.eye(len(p_vals)), rhs)
    M_L2[:, iif] = m_L2

    # IRLS sparse (one iteration)
    w    = 1.0 / (np.abs(m_L2) + 0.05 * np.abs(m_L2).max() + 1e-12)
    M_hr[:, iif] = np.linalg.solve(LfLfH + eps * np.diag(w), rhs)

radon_L2 = irfft(M_L2, n=nt, axis=1).real
radon_hr = irfft(M_hr, n=nt, axis=1).real
p_ms     = p_vals * 1e3  # s/km for display

fig, axes = plt.subplots(1, 3, figsize=(14, 6))
fig.suptitle('Linear Radon Transform (τ-p Slant Stack)', fontsize=12, fontweight='bold')

vmax_d = np.percentile(np.abs(data_r), 98)
axes[0].imshow(data_r.T, aspect='auto', cmap='seismic',
               extent=[0, x_ax[-1]/1e3, t_ax[-1], t_ax[0]],
               vmin=-vmax_d, vmax=vmax_d)
axes[0].set(xlabel='Offset (km)', ylabel='Time (s)',
            title='Original CMP gather\n(hyperbolic moveout events)')

vmax_L2 = np.percentile(np.abs(radon_L2), 99)
axes[1].imshow(radon_L2.T, aspect='auto', cmap='seismic',
               extent=[p_ms[0], p_ms[-1], t_ax[-1], t_ax[0]],
               vmin=-vmax_L2, vmax=vmax_L2)
axes[1].set(xlabel='Slowness $p$ (s/km)', ylabel='Intercept time τ (s)',
            title='Linear Radon (τ-p)\nConventional L2 (smeared)')

vmax_hr = np.percentile(np.abs(radon_hr), 99)
axes[2].imshow(radon_hr.T, aspect='auto', cmap='seismic',
               extent=[p_ms[0], p_ms[-1], t_ax[-1], t_ax[0]],
               vmin=-vmax_hr, vmax=vmax_hr)
axes[2].set(xlabel='Slowness $p$ (s/km)', ylabel='Intercept time τ (s)',
            title='Linear Radon (τ-p)\nSparse/IRLS (focused)')

plt.tight_layout()
plt.savefig('docs/assets/images/radon_transform.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved radon_transform.png")
print("Done.")
