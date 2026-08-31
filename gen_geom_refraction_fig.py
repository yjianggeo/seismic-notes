"""
Generate geom_refraction.png:
  Left:  two-layer refraction geometry (direct / reflected / head-wave rays,
         critical angle, blind zone)
  Right: travel-time diagram with direct, reflected and refracted branches,
         critical distance, crossover distance and intercept time
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

v1, v2, h = 2000.0, 4000.0, 800.0
ic = np.arcsin(v1 / v2)                      # critical angle from vertical
x1 = h * np.tan(ic)                          # horizontal leg of one slant ray
x_c = 2 * x1                                 # critical distance
t_i = 2 * h * np.cos(ic) / v1                # intercept time
x_cr = 2 * h * np.sqrt((v2 + v1) / (v2 - v1))  # crossover distance

fig, axs = plt.subplots(1, 2, figsize=(12, 4.9))
fig.suptitle('Refraction (Head Wave) in a Two-Layer Model',
             fontsize=12, fontweight='bold')

# ─── Left: ray geometry ─────────────────────────────────────────────
ax = axs[0]
ax.set_title(f'Ray Geometry ($v_1$ = {v1:.0f} m/s, $v_2$ = {v2:.0f} m/s, '
             f'$i_c$ = {np.degrees(ic):.0f}°)', fontsize=10)

ax.axhline(0, color='#5d6d7e', lw=2)
ax.axhline(-h, color='#1a5276', lw=2.5)
ax.text(2500, -h / 2, '$v_1$', fontsize=12, color='#5d6d7e', ha='center')
ax.text(2500, -h - 260, '$v_2 > v_1$', fontsize=12, color='#1a5276',
        ha='center')

# shot and receivers
ax.plot(0, 0, '^', color='#e74c3c', ms=12, mec='k', mew=0.8)
ax.text(0, 130, 'Shot $S$', ha='center', fontsize=9, color='#e74c3c')
xg_ref, xg_hw = 1200.0, 2100.0
for xg in (xg_ref, xg_hw):
    ax.plot(xg, 0, 'v', color='#2ecc71', ms=11, mec='k', mew=0.8)

# direct wave arrow along the surface
ax.annotate('', xy=(2600, 55), xytext=(150, 55),
            arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=1.6))
ax.text(1400, 150, 'direct wave', fontsize=8.5, color='#e74c3c', ha='center')

# reflected ray
ax.plot([0, xg_ref / 2], [0, -h], color='#e67e22', lw=1.8)
ax.plot([xg_ref / 2, xg_ref], [-h, 0], color='#e67e22', lw=1.8)
ax.text(880, -330, 'reflection', fontsize=8.5, color='#b9770e',
        rotation=-53, ha='center')

# head wave: down at ic, along interface, up at ic
ax.plot([0, x1], [0, -h], color='#8e44ad', lw=2.0)
ax.plot([x1, xg_hw - x1], [-h, -h], color='#8e44ad', lw=2.6)
ax.plot([xg_hw - x1, xg_hw], [-h, 0], color='#8e44ad', lw=2.0)
ax.text((x1 + xg_hw - x1) / 2, -h + 70, 'head wave along interface ($v_2$)',
        fontsize=8.5, color='#8e44ad', ha='center')

# critical-angle arcs (from vertical): short dashed verticals + arcs
ax.plot([0, 0], [0, -430], color='#7f8c8d', lw=0.9, ls=':')
th = np.linspace(90, 90 - np.degrees(ic), 40)
ax.plot(330 * np.cos(np.radians(th)), -330 * np.sin(np.radians(th)),
        color='#8e44ad', lw=1.1)
ax.text(150, -360, '$i_c$', fontsize=10, color='#8e44ad')
ax.plot([xg_hw, xg_hw], [0, -430], color='#7f8c8d', lw=0.9, ls=':')
ax.plot(xg_hw - 330 * np.cos(np.radians(th)), -330 * np.sin(np.radians(th)),
        color='#8e44ad', lw=1.1)
ax.text(xg_hw - 265, -360, '$i_c$', fontsize=10, color='#8e44ad')

# blind zone marker
ax.annotate('', xy=(x_c, -70), xytext=(0, -70),
            arrowprops=dict(arrowstyle='<->', color='#c0392b', lw=1.2))
ax.text(x_c / 2, -200, 'blind zone\n$x < x_c$', fontsize=8, color='#c0392b',
        ha='center')

ax.text(1400, -1500, '$\\sin i_c = v_1/v_2$', fontsize=10,
        color='#1a5276', ha='center')
ax.set(xlim=(-350, 2900), ylim=(-1700, 420))
ax.set_aspect('equal')
ax.axis('off')

# ─── Right: travel-time diagram ─────────────────────────────────────
ax = axs[1]
x = np.linspace(0, 4200, 800)
t0 = 2 * h / v1
t_direct = x / v1
t_refl = np.sqrt(t0**2 + (x / v1)**2)
mask = x >= x_c
t_refr = x / v2 + t_i

ax.plot(x, t_direct, color='#e74c3c', lw=2.2, label='direct  $t = x/v_1$')
ax.plot(x, t_refl, color='#e67e22', lw=2.0,
        label='reflection  $t^2 = t_0^2 + x^2/v_1^2$')
ax.plot(x[mask], t_refr[mask], color='#8e44ad', lw=2.2,
        label='refraction  $t = x/v_2 + t_i$')
ax.plot(x[~mask], t_refr[~mask], color='#8e44ad', lw=1.0, ls=':')

# critical distance (blind zone)
ax.axvspan(0, x_c, color='#c0392b', alpha=0.07)
ax.axvline(x_c, color='#c0392b', lw=1.0, ls='--')
ax.text(x_c + 60, 2.02, 'critical\ndistance $x_c$', fontsize=8,
        color='#c0392b')

# crossover distance
ax.axvline(x_cr, color='#1a5276', lw=1.0, ls='--')
ax.plot(x_cr, x_cr / v1, 'o', color='#1a5276', ms=8, mec='white', mew=1.2,
        zorder=5)
ax.text(x_cr + 60, 1.02, 'crossover $x_{cr}$\n(head wave arrives first)',
        fontsize=8, color='#1a5276')

# intercept time
ax.plot(0, t_i, 's', color='#8e44ad', ms=7, zorder=5)
ax.text(90, t_i - 0.075, '$t_i = 2h\\cos i_c / v_1$', fontsize=9,
        color='#8e44ad')

ax.set(xlabel='Offset $x$ (m)', ylabel='Travel time $t$ (s)',
       title='Travel-Time Diagram\n(first-arrival = lowest branch)',
       xlim=(0, 4200), ylim=(2.25, 0))
ax.legend(loc='upper left', fontsize=8)
ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('docs/assets/images/geom_refraction.png', dpi=150,
            bbox_inches='tight')
plt.close()
print("Saved geom_refraction.png")
