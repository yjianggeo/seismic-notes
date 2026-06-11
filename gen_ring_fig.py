"""
Generate das_ring_curvature.png:
  Left:  polar directional response of a curved-gauge DAS channel
         R(theta) = 1/2 * [1 + sinc(dphi) * cos(2 theta)]
         for several arc angles dphi = L/R
  Right: directional modulation depth m = sinc(dphi) vs L/R,
         with design thresholds marked
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

def sinc(x):
    """sin(x)/x with sinc(0)=1 (mathematical sinc, not numpy's normalized)."""
    return np.sinc(x / np.pi)

fig = plt.figure(figsize=(13, 5.5))
fig.suptitle('Curved-Cable DAS: Gauge Arc Angle and Directional Response',
             fontsize=12, fontweight='bold')

# ─── Left: polar response patterns ──────────────────────────────────
ax1 = fig.add_subplot(1, 2, 1, projection='polar')
theta = np.linspace(0, 2*np.pi, 720)

cases = [
    (0.0,          '#3498db', '-',  r'$\Delta\varphi = 0$ (straight)'),
    (np.pi/3,      '#2ecc71', '-',  r'$\Delta\varphi = 60°$  ($L/R \approx 1.05$)'),
    (2*np.pi/3,    '#e67e22', '--', r'$\Delta\varphi = 120°$ ($L/R \approx 2.09$)'),
    (np.pi,        '#e74c3c', '-.', r'$\Delta\varphi = 180°$ (half circle)'),
]

for dphi, col, ls, lbl in cases:
    m = sinc(dphi)
    resp = 0.5 * (1 + m * np.cos(2*theta))
    ax1.plot(theta, resp, color=col, ls=ls, lw=2.2, label=lbl)

ax1.set_title('P-wave directional response\n'
              r'$\bar{R}(\theta) = \frac{1}{2}\,[\,1 + \mathrm{sinc}(\Delta\varphi)\cos 2\theta\,]$',
              fontsize=9.5, pad=18)
ax1.set_theta_zero_location('E')
ax1.set_rlabel_position(67.5)
ax1.set_rlim(0, 1.05)
ax1.legend(loc='lower left', bbox_to_anchor=(-0.18, -0.18), fontsize=8)

# ─── Right: modulation depth vs L/R ─────────────────────────────────
ax2 = fig.add_subplot(1, 2, 2)
LR = np.linspace(0, 2*np.pi, 600)       # L/R = dphi (radians)
m  = sinc(LR)

ax2.plot(LR, m, color='#8e44ad', lw=2.5)
ax2.axhline(0.9, color='#27ae60', lw=1.2, ls='--')
ax2.axhline(0.0, color='gray', lw=0.8)

# Threshold: m > 0.9  ->  dphi < 0.786 rad (45 deg)
dphi_09 = 0.786
ax2.axvline(dphi_09, color='#27ae60', lw=1.2, ls=':')
ax2.fill_betweenx([-0.3, 1.05], 0, dphi_09, alpha=0.08, color='#27ae60')
ax2.annotate('Directional zone\n$m > 0.9$\n'
             r'$\Delta\varphi < 45°$ ($L < 0.79\,R$)',
             xy=(dphi_09, 0.9), xytext=(1.5, 0.82),
             fontsize=8.5, color='#1e8449',
             arrowprops=dict(arrowstyle='->', color='#1e8449', lw=0.9))

# pi: isotropic
ax2.axvline(np.pi, color='#e74c3c', lw=1.2, ls=':')
ax2.annotate('Half circle ($\\Delta\\varphi = 180°$)\nnearly isotropic',
             xy=(np.pi, sinc(np.pi)), xytext=(3.6, 0.35),
             fontsize=8.5, color='#c0392b',
             arrowprops=dict(arrowstyle='->', color='#c0392b', lw=0.9))

# 2*pi: full circle, m = 0 exactly
ax2.plot(2*np.pi, 0, 'o', color='#e74c3c', ms=7, zorder=5)
ax2.annotate('Full circle ($\\Delta\\varphi = 360°$)\n$m = 0$: perfectly isotropic',
             xy=(2*np.pi, 0), xytext=(4.0, -0.22),
             fontsize=8.5, color='#c0392b',
             arrowprops=dict(arrowstyle='->', color='#c0392b', lw=0.9))

# Secondary x-axis labels in degrees
deg_ticks = np.radians([0, 45, 90, 135, 180, 270, 360])
ax2.set_xticks(deg_ticks)
ax2.set_xticklabels(['0°', '45°', '90°', '135°', '180°', '270°', '360°'])

ax2.set(xlabel=r'Gauge arc angle $\Delta\varphi = L/R$',
        ylabel=r'Directional modulation depth  $m = \mathrm{sinc}(\Delta\varphi)$',
        title='Directionality vs gauge arc angle',
        xlim=[0, 2*np.pi], ylim=[-0.3, 1.05])
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('docs/assets/images/das_ring_curvature.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved das_ring_curvature.png")
print("Check values: sinc(45deg)={:.3f}, sinc(180deg)={:.3f}, sinc(360deg)={:.5f}".format(
    sinc(0.786), sinc(np.pi), sinc(2*np.pi)))
