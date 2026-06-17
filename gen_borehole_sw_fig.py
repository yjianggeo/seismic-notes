"""
Generate das_borehole_sw.png:
  Left:  Rayleigh wave depth eigenfunctions r_z(z) and |epsilon_zz(z)| vs
         normalised depth kz for a Poisson solid (nu = 0.25).
  Right: ln|r_z| vs kz — shows two-exponential decay and the S-wave
         dominated linear regime from which V_S can be extracted.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8.5,
})

# Poisson solid: nu = 0.25 → Vp/Vs = sqrt(3), Vr/Vs ≈ 0.9194
VR_VS = 0.9194
VR_VP = VR_VS / np.sqrt(3)

eta_a = np.sqrt(1 - VR_VP**2)    # ≈ 0.848  (P-wave vertical decay)
eta_b = np.sqrt(1 - VR_VS**2)    # ≈ 0.393  (S-wave vertical decay)
w     = 2 * eta_a * eta_b / (1 + eta_b**2)  # coupling weight ≈ 0.577

norm0 = 1 - w   # r_z(0) of unnormalised form → normalisation constant

def r_z(kz):
    """Vertical displacement eigenfunction, normalised to 1 at z = 0."""
    return (np.exp(-eta_a * kz) - w * np.exp(-eta_b * kz)) / norm0

def eps_zz(kz):
    """Vertical strain eigenfunction d(r_z)/d(kz), normalised to unit |value| at z = 0."""
    deriv = -eta_a * np.exp(-eta_a * kz) + w * eta_b * np.exp(-eta_b * kz)
    deriv /= norm0
    return deriv / abs(deriv[0])   # normalise surface value to ±1

kz = np.linspace(0, 6.5, 700)

fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
fig.suptitle(
    r'Borehole DAS: Rayleigh-Wave Depth Eigenfunction  '
    r'(Poisson solid, $\nu = 0.25$,  $V_R/V_S \approx 0.919$)',
    fontsize=11, fontweight='bold')

# ── Left: displacement and strain eigenfunctions ─────────────────────
ax = axes[0]

uz  = r_z(kz)
ez  = eps_zz(kz)

ax.plot(uz,       kz, color='#3498db', lw=2.3,
        label=r'Displacement $r_z(z)$')
ax.plot(np.abs(ez), kz, color='#e74c3c', lw=2.3, ls='--',
        label=r'DAS strain $|\varepsilon_{zz}(z)|$ (normalised)')

# Annotate the two decay scales
kz_P = 1.0 / eta_a    # ≈ 1.18 — P-wave 1/e depth
kz_S = 1.0 / eta_b    # ≈ 2.54 — S-wave 1/e depth

for kz_val, col, label in [(kz_P, '#e67e22', r'P-wave 1/$e$ depth $\approx 1.2/k$'),
                            (kz_S, '#27ae60', r'S-wave 1/$e$ depth $\approx 2.5/k$')]:
    ax.axhline(kz_val, color=col, lw=1.0, ls=':', alpha=0.8)
    ax.text(0.62, kz_val + 0.12, label, color=col, fontsize=7.5)

ax.invert_yaxis()
ax.set_xlim(-0.05, 1.15)
ax.set_xlabel('Normalised amplitude')
ax.set_ylabel(r'Normalised depth  $kz = 2\pi z/\lambda$')
ax.set_title('Depth eigenfunctions\n'
             r'(vertical borehole DAS, $k = 2\pi f / V_R$)')
ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)
ax.set_yticks([0, 1, 2, 3, 4, 5, 6])

# ── Right: log-amplitude → slope extraction ──────────────────────────
ax2 = axes[1]

log_uz = np.log(np.maximum(uz, 1e-9))

# S-wave asymptote: fit constant at large kz
idx_ref = np.argmin(np.abs(kz - 5.0))
C_s = log_uz[idx_ref] + eta_b * kz[idx_ref]
log_asym = C_s - eta_b * kz

ax2.plot(kz, log_uz,   color='#3498db', lw=2.3, label=r'$\ln |r_z(z)|$  (full eigenfunction)')
ax2.plot(kz, log_asym, color='#e67e22', lw=1.8, ls='--',
         label=r'S-wave asymptote $\propto e^{-\eta_\beta kz}$')

# Fitting zone: after P-wave has decayed sufficiently
kz_fit = 1.5 / eta_a   # ≈ 1.77
ax2.axvline(kz_fit, color='#27ae60', lw=1.0, ls=':')
ax2.fill_betweenx([-10, 0.5], kz_fit, 6.5, alpha=0.07, color='#27ae60')
ax2.annotate(
    f'Fitting zone  ($kz > {kz_fit:.1f}$)\nP-wave contribution < 5%',
    xy=(kz_fit, -2.5), xytext=(kz_fit + 0.6, -1.8),
    fontsize=8, color='#1e8449',
    arrowprops=dict(arrowstyle='->', color='#1e8449', lw=0.9))

# Annotate slope
mid_kz = 4.8
idx_m  = np.argmin(np.abs(kz - mid_kz))
idx_m1 = np.argmin(np.abs(kz - (mid_kz + 1)))
ax2.annotate('', xy=(mid_kz + 1, log_asym[idx_m1]),
             xytext=(mid_kz,     log_asym[idx_m]),
             arrowprops=dict(arrowstyle='->', color='#c0392b', lw=1.4))
ax2.text(mid_kz + 0.1, log_asym[idx_m] - 0.4,
         r'slope $= -\eta_\beta = -\sqrt{1 - V_R^2/V_S^2}$' '\n'
         r'$\Rightarrow\;V_S = V_R\,/\,\sqrt{1 - \eta_\beta^2}$',
         fontsize=8.2, color='#c0392b')

ax2.set_xlabel(r'Normalised depth  $kz$')
ax2.set_ylabel(r'$\ln |r_z(z)|$')
ax2.set_title(r'Log-amplitude vs depth:  slope $\rightarrow$ extract $V_S$')
ax2.set_xlim([0, 6.5])
ax2.set_ylim([-9, 0.6])
ax2.legend(loc='upper right')
ax2.grid(True, alpha=0.3)

# Summary box
textstr = (
    fr'Poisson solid ($\nu=0.25$):' '\n'
    fr'  $\eta_\alpha={eta_a:.3f}$,  $\eta_\beta={eta_b:.3f}$' '\n'
    fr'  slope in fit zone $= {eta_b:.3f}$'
)
ax2.text(0.02, 0.04, textstr, transform=ax2.transAxes,
         fontsize=8, verticalalignment='bottom',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#f8f9fa', alpha=0.85))

plt.tight_layout()
plt.savefig('docs/assets/images/das_borehole_sw.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved das_borehole_sw.png")
print(f"eta_alpha = {eta_a:.4f},  eta_beta = {eta_b:.4f},  w = {w:.4f},  norm0 = {norm0:.4f}")
print(f"Fit zone starts at kz = {kz_fit:.2f}")
