"""
Generate sw_eigenfunctions.png:
  Left:  Rayleigh-wave displacement eigenfunctions r_x(z), r_z(z) for a
         Poisson half-space, showing the r_x sign change at z ~ 0.19 lambda
         (retrograde -> prograde transition) and the slight sub-surface
         maximum of r_z at z ~ 0.08 lambda.
  Right: Love-wave eigenfunctions l(z) (fundamental + 1st higher mode) for
         a soft layer over a faster half-space at a fixed frequency.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8.5,
})

# ══ Rayleigh eigenfunctions, Poisson solid (nu = 0.25) ═══════════════
VR_VS = 0.9194
VR_VP = VR_VS / np.sqrt(3)

eta_a = np.sqrt(1 - VR_VP**2)          # ~0.848  P-wave vertical decay
eta_b = np.sqrt(1 - VR_VS**2)          # ~0.393  S-wave vertical decay
w_x   = 2 * eta_a * eta_b / (1 + eta_b**2)   # r_x S-term weight ~0.577
s_z   = 2 / (1 + eta_b**2)                   # r_z S-term weight ~1.732

def r_x(kz):
    """Horizontal (radial) eigenfunction, normalised to 1 at z = 0."""
    return (np.exp(-eta_a * kz) - w_x * np.exp(-eta_b * kz)) / (1 - w_x)

def r_z(kz):
    """Vertical eigenfunction, normalised to 1 at z = 0."""
    return (s_z * np.exp(-eta_b * kz) - np.exp(-eta_a * kz)) / (s_z - 1)

# true surface amplitude ratio |u_x/u_z| (ellipticity, ~0.681)
ellip = (1 - w_x) / (eta_a * (s_z - 1))

z_lam = np.linspace(0, 1.4, 900)       # depth in wavelengths
kz    = 2 * np.pi * z_lam

z_node = np.log(1 / w_x) / (eta_a - eta_b) / (2 * np.pi)   # ~0.19 lambda
z_peak = np.log(eta_a / (s_z * eta_b)) / (eta_a - eta_b) / (2 * np.pi)  # ~0.077

fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
fig.suptitle('Surface-Wave Eigenfunctions', fontsize=11, fontweight='bold')

ax = axes[0]
ax.plot(r_z(kz),          z_lam, color='#3498db', lw=2.3,
        label=r'Vertical $r_z(z)$')
ax.plot(ellip * r_x(kz),  z_lam, color='#e74c3c', lw=2.3, ls='--',
        label=r'Horizontal $r_x(z)$ (true relative amplitude)')
ax.axvline(0, color='gray', lw=0.8, ls=':')

ax.axhline(z_node, color='#8e44ad', lw=1.0, ls=':')
ax.annotate(r'$r_x$ node at $z \approx 0.19\lambda$' '\n'
            'retrograde above / prograde below',
            xy=(0, z_node), xytext=(0.25, z_node + 0.13),
            fontsize=8, color='#8e44ad',
            arrowprops=dict(arrowstyle='->', color='#8e44ad', lw=0.9))
ax.annotate(r'$r_z$ max $\approx 1.05$ at $z \approx 0.08\lambda$',
            xy=(r_z(2 * np.pi * z_peak), z_peak), xytext=(0.42, 0.52),
            fontsize=8, color='#2471a3',
            arrowprops=dict(arrowstyle='->', color='#2471a3', lw=0.9))
ax.text(0.62, 0.035, fr'surface ellipticity $|r_x/r_z| \approx {ellip:.2f}$',
        fontsize=8, color='#555555')

ax.invert_yaxis()
ax.set_xlim(-0.25, 1.15)
ax.set_xlabel('Normalised displacement')
ax.set_ylabel(r'Depth  $z/\lambda$')
ax.set_title('Rayleigh wave, homogeneous Poisson half-space\n'
             r'($\nu = 0.25$,  $V_R \approx 0.919\,V_S$)')
ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)

# ══ Love eigenfunctions: layer over half-space ═══════════════════════
b1, b2   = 200.0, 400.0        # S velocities (m/s)
rho1, rho2 = 1800.0, 2300.0    # densities (kg/m^3)
H        = 20.0                # layer thickness (m)
f        = 12.0                # frequency (Hz)
mu1, mu2 = rho1 * b1**2, rho2 * b2**2
om       = 2 * np.pi * f

def disp(c):
    """Love dispersion function: zero at modal phase velocities."""
    nu1 = om * np.sqrt(1 / b1**2 - 1 / c**2)
    nu2 = om * np.sqrt(1 / c**2 - 1 / b2**2)
    return mu1 * nu1 * np.sin(nu1 * H) - mu2 * nu2 * np.cos(nu1 * H)

c_scan = np.linspace(b1 * 1.0005, b2 * 0.9995, 4000)
g = disp(c_scan)
roots = [brentq(disp, c_scan[i], c_scan[i + 1])
         for i in range(len(c_scan) - 1) if g[i] * g[i + 1] < 0]

def love_eig(c, z):
    nu1 = om * np.sqrt(1 / b1**2 - 1 / c**2)
    nu2 = om * np.sqrt(1 / c**2 - 1 / b2**2)
    return np.where(z <= H, np.cos(nu1 * z),
                    np.cos(nu1 * H) * np.exp(-nu2 * (z - H)))

z = np.linspace(0, 60, 700)
ax2 = axes[1]

for n, (c_n, col) in enumerate(zip(roots[:2], ['#3498db', '#e74c3c'])):
    ax2.plot(love_eig(c_n, z), z, color=col, lw=2.3,
             ls='-' if n == 0 else '--',
             label=fr'Mode {n}:  $c = {c_n:.0f}$ m/s')

ax2.axvline(0, color='gray', lw=0.8, ls=':')
ax2.axhline(H, color='#7f8c8d', lw=1.2, ls='--')
ax2.text(-0.93, H + 2.5, fr'layer base $H = {H:.0f}$ m', fontsize=8,
         color='#7f8c8d')
ax2.text(-0.93, 55,
         fr'$\beta_1 = {b1:.0f}$ m/s,  $\beta_2 = {b2:.0f}$ m/s' '\n'
         fr'$f = {f:.0f}$ Hz', fontsize=8, color='#555555',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#f8f9fa', alpha=0.85))

ax2.invert_yaxis()
ax2.set_xlim(-1.0, 1.1)
ax2.set_xlabel(r'Normalised displacement  $l(z)$')
ax2.set_ylabel('Depth (m)')
ax2.set_title('Love wave, low-velocity layer over half-space\n'
              '(oscillatory in layer, evanescent below)')
ax2.legend(loc='lower right')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('docs/assets/images/sw_eigenfunctions.png', dpi=150,
            bbox_inches='tight')
plt.close()
print("Saved sw_eigenfunctions.png")
print(f"eta_a = {eta_a:.4f}, eta_b = {eta_b:.4f}, ellipticity = {ellip:.4f}")
print(f"r_x node at z = {z_node:.4f} lambda, r_z max at z = {z_peak:.4f} lambda")
print(f"Love modes at {f:.0f} Hz: " + ", ".join(f"{c:.1f} m/s" for c in roots))
