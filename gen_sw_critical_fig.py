"""
Generate sw_critical_mode.png (based on Wang & Lu 2024, Earthquake Science):
  Left:  three canonical depth functions of Z(z): oscillatory (real kz),
         evanescent (imaginary kz), linear/constant (kz = 0, the critical case)
  Right: Love-wave eigendisplacements for a 5 km layer (vs = 1 km/s) over a
         half-space (vs = 3 km/s) — normal modes at c = 2 km/s decay
         exponentially in the half-space; critical modes at c = 3 km/s stay
         constant there. Eigenfunctions are computed by solving the exact
         Love-wave dispersion relation tan(kz1*h) = mu2*kz2/(mu1*kz1).
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

# ─── model (Model 2 of Wang & Lu 2024, simplified units) ────────────
h = 5.0                      # layer thickness (km)
b1, b2 = 1.0, 3.0            # S velocities (km/s)
r1, r2 = 1.0, 1.0            # densities (g/cm3)
m1, m2 = r1 * b1**2, r2 * b2**2

def love_eigen(c, n):
    """Return (f [Hz], z, Z) for mode index n at phase velocity c (km/s).

    Layer: Z = cos(kz1 * z); half-space: A * exp(-kz2 * (z - h))
    with A = cos(kz1 * h) (displacement continuity).
    Dispersion: tan(kz1 h) = m2 kz2 / (m1 kz1); solve for omega.
    Critical case kz2 == 0 is handled separately (constant in half-space).
    """
    kz1_of = lambda w: w * np.sqrt(1 / b1**2 - 1 / c**2)
    kz2_of = lambda w: w * np.sqrt(1 / c**2 - 1 / b2**2) if c < b2 else 0.0

    if c >= b2:  # critical mode: sin(kz1 h) = 0 -> kz1 h = n*pi
        w = n * np.pi / (h * np.sqrt(1 / b1**2 - 1 / c**2))
        f = w / (2 * np.pi)
        z = np.linspace(0, 12, 800)
        kz1 = kz1_of(w)
        Z = np.where(z <= h, np.cos(kz1 * z), np.cos(kz1 * h))
        return f, z, Z

    # normal mode: bracket the n-th root of tan(kz1 h) = m2 kz2/(m1 kz1)
    def dispersion(w):
        kz1, kz2 = kz1_of(w), kz2_of(w)
        return np.tan(kz1 * h) - m2 * kz2 / (m1 * kz1)

    # scan omega, find the n-th sign change of (tan - rhs) minus poles:
    # simpler robust approach: use atan-based phase counting
    ws = np.linspace(1e-4, 20, 200000)
    phase = np.unwrap(np.arctan2(
        dispersion(ws), np.ones_like(ws)))
    # count roots by tracking when kz1*h crosses pi/2 + n*pi with matching rhs
    # Instead: solve directly by bisection on each branch interval
    roots = []
    k1h = np.array([kz1_of(w) * h for w in ws])
    for m in range(0, 8):
        lo = (np.pi / 2 + m * np.pi) / (np.sqrt(1 / b1**2 - 1 / c**2) * h)
        hi = (np.pi / 2 + (m + 1) * np.pi) / (np.sqrt(1 / b1**2 - 1 / c**2) * h) * 0.999999
        lo *= 1.000001
        # on each branch, tan goes -inf..+inf monotonically; rhs>0 varies slowly
        flo = np.tan(kz1_of(lo) * h) - m2 * kz2_of(lo) / (m1 * kz1_of(lo))
        fhi = np.tan(kz1_of(hi) * h) - m2 * kz2_of(hi) / (m1 * kz1_of(hi))
        if flo * fhi < 0:
            for _ in range(80):
                mid = 0.5 * (lo + hi)
                fm = np.tan(kz1_of(mid) * h) - m2 * kz2_of(mid) / (m1 * kz1_of(mid))
                if flo * fm < 0:
                    hi, fhi = mid, fm
                else:
                    lo, flo = mid, fm
            roots.append(0.5 * (lo + hi))
    w = roots[n]
    f = w / (2 * np.pi)
    kz1, kz2 = kz1_of(w), kz2_of(w)
    z = np.linspace(0, 12, 800)
    A = np.cos(kz1 * h)
    Z = np.where(z <= h, np.cos(kz1 * z), A * np.exp(-kz2 * (z - h)))
    return f, z, Z

fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.9))
fig.suptitle('Critical Modes of Surface Waves (Wang & Lu, 2024)',
             fontsize=12, fontweight='bold')

# ─── Left: three canonical Z(z) ─────────────────────────────────────
ax = axs[0]
z = np.linspace(0, 10, 500)
ax.plot(np.cos(1.9 * z), -z, color='#3498db', lw=2.2,
        label='$k_z$ real: oscillatory (trapped)')
ax.plot(np.exp(-0.35 * z), -z, color='#2ecc71', lw=2.2,
        label='$k_z$ imaginary: evanescent (decaying)')
ax.plot(np.ones_like(z), -z, color='#e74c3c', lw=2.4,
        label='$k_z = 0$: constant / linear (critical)')
ax.plot(np.zeros_like(z), -z, color='gray', lw=0.8, ls=':')
ax.set(xlabel='$Z(z)$  (schematic)', ylabel='Depth $z$',
       title='General Solutions of $Z^{\\prime\\prime} + k_z^2 Z = 0$',
       xlim=(-0.35, 1.35), ylim=(-10.5, 0.5))
ax.set_yticks([])
ax.legend(loc='lower left', fontsize=8)
ax.grid(alpha=0.3)

# ─── Right: computed Love eigendisplacements ────────────────────────
ax = axs[1]
cases = [
    (2.0, 0, '#1f77b4', '-',  'normal,  $c$=2 km/s, mode 0'),
    (2.0, 1, '#6baed6', '-',  'normal,  $c$=2 km/s, mode 1'),
    (3.0, 1, '#e74c3c', '-',  'critical, $c$=3 km/s, mode 1'),
    (3.0, 2, '#f1948a', '--', 'critical, $c$=3 km/s, mode 2'),
]
for c, n, col, ls, lab in cases:
    f, z, Z = love_eigen(c, n)
    Z = Z / np.abs(Z).max()
    ax.plot(Z, -z, color=col, ls=ls, lw=2.0,
            label=f'{lab}  ($f$={f:.3f} Hz)')

ax.axhline(-h, color='#7f8c8d', lw=1.0, ls='--')
ax.text(-0.97, -h + 0.28, 'layer base $z = 5$ km', fontsize=7.5,
        color='#7f8c8d')
ax.axvline(0, color='gray', lw=0.8, ls=':')
# annotate the contrast inside the half-space
ax.annotate('normal: exponential decay\nin half-space', xy=(0.24, -8.5),
            xytext=(-0.75, -7.6), fontsize=8, color='#1f77b4',
            arrowprops=dict(arrowstyle='->', color='#1f77b4', lw=0.9))
ax.annotate('critical: constant\nin half-space', xy=(-1.0, -10.8),
            xytext=(-0.72, -11.4), fontsize=8, color='#e74c3c',
            arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=0.9))
ax.set(xlabel='Eigendisplacement (normalised)', ylabel='Depth (km)',
       title='Love-Wave Eigendisplacements\n'
             'layer $\\beta_1$=1 km/s ($h$=5 km) over half-space '
             '$\\beta_2$=3 km/s',
       xlim=(-1.25, 1.25), ylim=(-12.4, 0.4))
ax.legend(loc='lower right', fontsize=7.6)
ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('docs/assets/images/sw_critical_mode.png', dpi=150,
            bbox_inches='tight')
plt.close()
print("Saved sw_critical_mode.png")
