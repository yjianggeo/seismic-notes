"""
Generate geom_rt_coeff.png:
  Left:  plane P wave incident on a welded interface — reflected P/S and
         transmitted P/S rays with Snell-angle relations
  Right: exact Zoeppritz reflection/transmission coefficients vs incidence
         angle (shale over Class-III gas sand)
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

# ─── model: shale over Class-III gas sand ────────────────────────────
a1, b1, r1 = 2600.0, 1300.0, 2.25    # upper layer: shale
a2, b2, r2 = 2200.0, 1400.0, 2.00    # lower layer: gas sand (low Poisson)

def zoeppritz_pp(i_deg):
    """Exact Zoeppritz coefficients for incident P wave."""
    i1 = np.radians(i_deg)
    p = np.sin(i1) / a1                      # ray parameter
    j1 = np.arcsin(np.clip(p * b1, 0, 1))    # reflected S
    i2 = np.arcsin(np.clip(p * a2, 0, 1))    # transmitted P
    j2 = np.arcsin(np.clip(p * b2, 0, 1))    # transmitted S
    ea1, eb1 = np.cos(i1) / a1, np.cos(j1) / b1
    ea2, eb2 = np.cos(i2) / a2, np.cos(j2) / b2
    m1, m2 = r1 * b1**2, r2 * b2**2          # shear moduli
    q1 = r1 * (1 - 2 * b1**2 * p**2)
    q2 = r2 * (1 - 2 * b2**2 * p**2)
    M = np.array([
        [p,              eb1,              -p,              eb2],
        [-ea1,           p,                -ea2,           -p ],
        [2*m1*p*ea1,     m1*(eb1**2-p**2),  2*m2*p*ea2,    -m2*(eb2**2-p**2)],
        [-q1,            2*m1*p*eb1,        q2,             2*m2*p*eb2],
    ])
    rhs = np.array([-p, -ea1, 2*m1*p*ea1, q1])
    Rpp, Rps, Tpp, Tps = np.linalg.solve(M, rhs)
    # convert from potential ratios to displacement-amplitude ratios
    # (incident P displacement amplitude ~ omega*phi/a1)
    return Rpp, Rps * a1 / b1, Tpp * a1 / a2, Tps * a1 / b2

ang = np.linspace(0, 45, 200)
coef = np.array([zoeppritz_pp(i) for i in ang])
Rpp, Rps, Tpp, Tps = coef.T

fig, axs = plt.subplots(1, 2, figsize=(12, 4.9))
fig.suptitle('Reflection / Transmission Coefficients at an Elastic Interface',
             fontsize=12, fontweight='bold')

# ─── Left: ray schematic ────────────────────────────────────────────
ax = axs[0]
ax.set_title('Partitioning of an Incident P Wave', fontsize=10)
ax.axhline(0, color='#1a5276', lw=2.5)

i = np.radians(30)
L = 900.0
def ray(frac_angle_from_vertical, length, direction, color, label, lw=2.2):
    """direction: 'down' (transmitted) or 'up' (reflected)."""
    sgn = -1 if direction == 'down' else 1
    x_end = length * np.sin(frac_angle_from_vertical)
    z_end = sgn * length * np.cos(frac_angle_from_vertical)
    ax.annotate('', xy=(x_end, z_end), xytext=(0, 0),
                arrowprops=dict(arrowstyle='-|>', color=color, lw=lw))
    ax.text(x_end * 1.12, z_end * 1.12, label, fontsize=8.5, color=color,
            ha='center', va='center')

# incident P (upper left → origin)
xi, zi = -L * np.sin(i), L * np.cos(i)
ax.annotate('', xy=(0, 0), xytext=(xi, zi),
            arrowprops=dict(arrowstyle='-|>', color='#c0392b', lw=2.6))
ax.text(xi * 1.05, zi * 1.12, 'incident P\n($i_1$)', fontsize=9,
        color='#c0392b', ha='center')

# angle relations from Snell's law
p_ray = np.sin(i) / a1
j1 = np.arcsin(p_ray * b1)
i2 = np.arcsin(p_ray * a2)
j2 = np.arcsin(p_ray * b2)

ray(i,  L * 0.92, 'up',   '#e67e22', f'reflected P  $R_{{PP}}$\n($i_1$)')
ray(j1, L * 0.62, 'up',   '#8e44ad', f'reflected S  $R_{{PS}}$\n($j_1$)')
ray(i2,  L * 0.92, 'down', '#1e8449', f'transmitted P  $T_{{PP}}$\n($i_2$)')
ray(j2,  L * 0.62, 'down', '#2471a3', f'transmitted S  $T_{{PS}}$\n($j_2$)')

# normal (dashed)
ax.plot([0, 0], [-L, L], color='#7f8c8d', lw=1.0, ls='--')
# incidence angle arc
th = np.linspace(90 - np.degrees(i), 90, 40)
ax.plot(-300 * np.cos(np.radians(th)), 300 * np.sin(np.radians(th)),
        color='#c0392b', lw=1.1)
ax.text(-390, 260, '$i_1$', fontsize=10, color='#c0392b')

# layer labels (upper medium above the interface, lower below)
ax.text(-820, 420, f'$v_{{P1}}$ = {a1:.0f} m/s\n$v_{{S1}}$ = {b1:.0f} m/s\n'
        f'$\\rho_1$ = {r1} g/cm³', fontsize=8.5, color='#5d6d7e')
ax.text(-820, -700, f'$v_{{P2}}$ = {a2:.0f} m/s\n$v_{{S2}}$ = {b2:.0f} m/s\n'
        f'$\\rho_2$ = {r2} g/cm³', fontsize=8.5, color='#1a5276')
ax.text(0, -1020, 'Snell:  $\\dfrac{\\sin i_1}{v_{P1}} = '
        '\\dfrac{\\sin j_1}{v_{S1}} = \\dfrac{\\sin i_2}{v_{P2}} = '
        '\\dfrac{\\sin j_2}{v_{S2}} = p$',
        fontsize=9.5, color='#1a5276', ha='center')
ax.set(xlim=(-1050, 1050), ylim=(-1120, 1080))
ax.set_aspect('equal')
ax.axis('off')

# ─── Right: Zoeppritz curves ────────────────────────────────────────
ax = axs[1]
ax.plot(ang, Rpp, color='#e67e22', lw=2.4, label='$R_{PP}$')
ax.plot(ang, Rps, color='#8e44ad', lw=2.0, label='$R_{PS}$')
ax.plot(ang, Tpp, color='#1e8449', lw=2.0, label='$T_{PP}$')
ax.plot(ang, Tps, color='#2471a3', lw=2.0, label='$T_{PS}$')
ax.axhline(0, color='k', lw=0.7)

R0 = (r2 * a2 - r1 * a1) / (r2 * a2 + r1 * a1)
ax.plot(0, R0, 'o', color='#e67e22', ms=8, mec='white', mew=1.2, zorder=5)
ax.annotate('normal incidence\n$R = \\dfrac{Z_2 - Z_1}{Z_2 + Z_1}'
            f' = {R0:.2f}$',
            xy=(0, R0), xytext=(4, -0.45), fontsize=8.5, color='#b9770e',
            arrowprops=dict(arrowstyle='->', color='#b9770e', lw=1.0))
ax.text(24, -0.55, 'gas sand:\n$R_{PP}$ grows more\nnegative with angle\n'
        '(Class III AVO)', fontsize=8.5, color='#c0392b', ha='center',
        bbox=dict(boxstyle='round,pad=0.35', fc='#fdf2e9', ec='#e67e22',
                  lw=0.8))
ax.set(xlabel='Incidence angle $i_1$ (°)', ylabel='Amplitude coefficient',
       title='Exact Zoeppritz Coefficients\n(shale → Class-III gas sand)',
       xlim=(0, 45), ylim=(-0.75, 1.3))
ax.legend(loc='upper right', fontsize=8.5)
ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('docs/assets/images/geom_rt_coeff.png', dpi=150,
            bbox_inches='tight')
plt.close()
print("Saved geom_rt_coeff.png")
