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
s     = 2 / (1 + eta_b**2)       # S-term weight of vertical component ≈ 1.732

norm0 = s - 1   # r_z(0) of unnormalised form → normalisation constant

def r_z(kz):
    """Vertical displacement eigenfunction, normalised to 1 at z = 0."""
    return (s * np.exp(-eta_b * kz) - np.exp(-eta_a * kz)) / norm0

def eps_zz(kz):
    """Vertical strain eigenfunction d(r_z)/d(kz), normalised to unit maximum."""
    deriv = -s * eta_b * np.exp(-eta_b * kz) + eta_a * np.exp(-eta_a * kz)
    deriv /= norm0
    return deriv / np.max(np.abs(deriv))

kz = np.linspace(0, 6.5, 700)
kz_R = np.linspace(0, 10, 900)   # deeper range for the log-amplitude panel

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

# Annotate the two decay scales and the strain node
kz_P = 1.0 / eta_a    # ≈ 1.18 — P-wave 1/e depth
kz_S = 1.0 / eta_b    # ≈ 2.54 — S-wave 1/e depth
kz_node = np.log(eta_a / (s * eta_b)) / (eta_a - eta_b)   # ≈ 0.48 — strain node

for kz_val, col, label in [(kz_P, '#e67e22', r'P-wave 1/$e$ depth $\approx 1.2/k$'),
                            (kz_S, '#27ae60', r'S-wave 1/$e$ depth $\approx 2.5/k$')]:
    ax.axhline(kz_val, color=col, lw=1.0, ls=':', alpha=0.8)
    ax.text(0.62, kz_val + 0.12, label, color=col, fontsize=7.5)

ax.annotate(fr'strain node at $kz \approx {kz_node:.2f}$',
            xy=(0.0, kz_node), xytext=(0.28, 0.75),
            fontsize=7.5, color='#c0392b',
            arrowprops=dict(arrowstyle='->', color='#c0392b', lw=0.9))

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

log_uz = np.log(np.maximum(r_z(kz_R), 1e-9))

# S-wave asymptote (exact): ln[s/(s-1)] - eta_b * kz
log_asym = np.log(s / norm0) - eta_b * kz_R

ax2.plot(kz_R, log_uz,   color='#3498db', lw=2.3, label=r'$\ln |r_z(z)|$  (full eigenfunction)')
ax2.plot(kz_R, log_asym, color='#e67e22', lw=1.8, ls='--',
         label=r'S-wave asymptote $\propto e^{-\eta_\beta kz}$')

# Fitting zone: after the P-wave term has decayed sufficiently
kz_fit = 3.0
ax2.axvline(kz_fit, color='#27ae60', lw=1.0, ls=':')
ax2.fill_betweenx([-4.2, 0.8], kz_fit, 10, alpha=0.07, color='#27ae60')
ax2.annotate(
    f'Fitting zone  ($kz > {kz_fit:.0f}$)\nP-wave contribution < 15%',
    xy=(kz_fit, -1.4), xytext=(kz_fit + 0.7, -0.7),
    fontsize=8, color='#1e8449',
    arrowprops=dict(arrowstyle='->', color='#1e8449', lw=0.9))

# Annotate slope
mid_kz = 6.5
log_a  = np.log(s / norm0) - eta_b * mid_kz
log_a1 = np.log(s / norm0) - eta_b * (mid_kz + 1.5)
ax2.annotate('', xy=(mid_kz + 1.5, log_a1),
             xytext=(mid_kz,       log_a),
             arrowprops=dict(arrowstyle='->', color='#c0392b', lw=1.4))
ax2.text(mid_kz + 0.15, log_a - 0.65,
         r'slope $= -\eta_\beta = -\sqrt{1 - V_R^2/V_S^2}$' '\n'
         r'$\Rightarrow\;V_S = V_R\,/\,\sqrt{1 - \eta_\beta^2}$',
         fontsize=8.2, color='#c0392b')

ax2.set_xlabel(r'Normalised depth  $kz$')
ax2.set_ylabel(r'$\ln |r_z(z)|$')
ax2.set_title(r'Log-amplitude vs depth:  slope $\rightarrow$ extract $V_S$')
ax2.set_xlim([0, 10])
ax2.set_ylim([-4.2, 0.8])
ax2.legend(loc='upper right')
ax2.grid(True, alpha=0.3)

# Summary box
textstr = (
    fr'Poisson solid ($\nu=0.25$):' '\n'
    fr'  $\eta_\alpha={eta_a:.3f}$,  $\eta_\beta={eta_b:.3f}$,  $s={s:.3f}$' '\n'
    fr'  $r_z$ max $\approx 1.05$ at $kz \approx 0.48$' '\n'
    fr'  asymptotic slope $= -{eta_b:.3f}$'
)
ax2.text(0.02, 0.04, textstr, transform=ax2.transAxes,
         fontsize=8, verticalalignment='bottom',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#f8f9fa', alpha=0.85))

plt.tight_layout()
plt.savefig('docs/assets/images/das_borehole_sw.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved das_borehole_sw.png")
print(f"eta_alpha = {eta_a:.4f},  eta_beta = {eta_b:.4f},  s = {s:.4f},  norm0 = {norm0:.4f}")
print(f"Strain node at kz = {kz_node:.2f}; fit zone starts at kz = {kz_fit:.2f}")
