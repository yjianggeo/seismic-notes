"""
Generate geometrical seismology figures (part 2):
  geom_ray_geom.png   — reflection ray geometry: horizontal vs dipping interface
                        (image-source method)
  geom_traveltime.png — travel-time curves: hyperbola + asymmetric dipping case
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

# =====================================================================
# Figure 4 — interface geometry schematics (horizontal / dipping)
# =====================================================================
fig, axs = plt.subplots(1, 2, figsize=(12, 4.6))
fig.suptitle('Reflection Geometry and the Image-Source Method',
             fontsize=12, fontweight='bold')

# ─── Left: horizontal interface ─────────────────────────────────────
ax = axs[0]
v, h, x = 2000.0, 1000.0, 1600.0
ax.set_title('Horizontal Interface', fontsize=10)

ax.axhline(0, color='#5d6d7e', lw=2)                       # surface
ax.axhline(-h, color='#1a5276', lw=2.5)                    # reflector
ax.plot(0, 0, '^', color='#e74c3c', ms=12, mec='k', mew=0.8)      # shot
ax.plot(x, 0, 'v', color='#2ecc71', ms=12, mec='k', mew=0.8)      # receiver
ax.text(0, 110, 'Shot $S$', ha='center', fontsize=9, color='#e74c3c')
ax.text(x, 110, 'Geophone $G$', ha='center', fontsize=9, color='#1e8449')

# ray paths via reflection point at x/2
ax.plot([0, x / 2], [0, -h], color='#e67e22', lw=2)
ax.plot([x / 2, x], [-h, 0], color='#e67e22', lw=2)
ax.plot(x / 2, -h, 'o', color='#e67e22', ms=7, mec='k', mew=0.8)
ax.text(x / 2, -h - 140, 'reflection point', ha='center', fontsize=8,
        color='#b9770e')

# image source at depth 2h, dashed straight ray to receiver
ax.plot(0, -2 * h, '^', color='#e74c3c', ms=11, mec='k', mew=0.8, mfc='none')
ax.plot([0, x], [-2 * h, 0], color='#7f8c8d', lw=1.4, ls='--')
ax.plot([0, 0], [-h, -2 * h], color='#7f8c8d', lw=1.0, ls=':')
ax.text(-90, -2 * h, 'image source $S^{*}$', fontsize=8.5,
        color='#5d6d7e', va='center', ha='right')

# annotations: depth h and offset x
ax.annotate('', xy=(x * 0.13, -h), xytext=(x * 0.13, 0),
            arrowprops=dict(arrowstyle='<->', color='#1a5276', lw=1.2))
ax.text(x * 0.13 + 50, -h / 2, '$h$', fontsize=11, color='#1a5276')
ax.annotate('', xy=(x, 260), xytext=(0, 260),
            arrowprops=dict(arrowstyle='<->', color='#5d6d7e', lw=1.2))
ax.text(x / 2, 350, 'offset $x$', ha='center', fontsize=10, color='#5d6d7e')

ax.text(x / 2, -2 * h - 280, '$t_0 = 2h/v$', ha='center', fontsize=10,
        color='#1a5276')
ax.set(xlim=(-520, x + 350), ylim=(-2 * h - 450, 560))
ax.set_aspect('equal')
ax.axis('off')

# ─── Right: dipping interface ───────────────────────────────────────
ax = axs[1]
phi = np.radians(12)
h0 = 900.0                       # perpendicular distance below the shot
ax.set_title('Dipping Interface', fontsize=10)

ax.axhline(0, color='#5d6d7e', lw=2)
# interface line: x*tanφ + z + h0 = 0  (dipping down to the right)
a, b, c = np.tan(phi), 1.0, h0
xs = np.array([-300, 2300])
ax.plot(xs, -(c + a * xs), color='#1a5276', lw=2.5)
ax.text(1960, -(c + a * 2050) - 90, 'dipping reflector',
        fontsize=8.5, color='#1a5276', rotation=-11, ha='center')

xg = 1500.0
ax.plot(0, 0, '^', color='#e74c3c', ms=12, mec='k', mew=0.8)
ax.plot(xg, 0, 'v', color='#2ecc71', ms=12, mec='k', mew=0.8)
ax.text(0, 110, '$S$', ha='center', fontsize=10, color='#e74c3c')
ax.text(xg, 110, '$G$', ha='center', fontsize=10, color='#1e8449')

# image of S across the interface
d = (a * 0 + b * 0 + c) / (a**2 + b**2)
S_img = np.array([-2 * a * d, -2 * b * d])
ax.plot(S_img[0], S_img[1], '^', color='#e74c3c', ms=11, mec='k', mew=0.8,
        mfc='none')
ax.plot([S_img[0], xg], [S_img[1], 0], color='#7f8c8d', lw=1.4, ls='--')
ax.text(S_img[0] - 70, S_img[1], 'image source $S^{*}$', fontsize=8.5,
        color='#5d6d7e', va='center', ha='right')

# reflection point: intersection of the image ray with the interface
t_int = -(a * S_img[0] + b * S_img[1] + c) / (a * (xg - S_img[0])
                                             + b * (0 - S_img[1]))
RP = S_img + t_int * (np.array([xg, 0.0]) - S_img)
ax.plot([0, RP[0]], [0, RP[1]], color='#e67e22', lw=2)
ax.plot([RP[0], xg], [RP[1], 0], color='#e67e22', lw=2)
ax.plot(RP[0], RP[1], 'o', color='#e67e22', ms=7, mec='k', mew=0.8)
ax.annotate('reflection point\n(shifted updip of midpoint)',
            xy=(RP[0], RP[1]), xytext=(RP[0] - 480, RP[1] - 520),
            fontsize=8, color='#b9770e',
            arrowprops=dict(arrowstyle='->', color='#b9770e', lw=0.9))
ax.plot([0, xg / 2], [0, 0], lw=0)  # anchor
ax.plot(xg / 2, 0, '|', color='#5d6d7e', ms=10)
ax.text(xg / 2, 110, 'midpoint', ha='center', fontsize=8, color='#5d6d7e')

# dip angle arc at right end of the interface
x_arc = 2080
z_arc = -(c + a * x_arc)
ax.plot([x_arc - 340, x_arc], [-(c + a * (x_arc - 340)), z_arc],
        color='#7f8c8d', lw=0.9, ls=':')
ax.plot([x_arc - 340, x_arc], [-(c + a * (x_arc - 340))] * 2,
        color='#7f8c8d', lw=0.9, ls=':')
ax.text(x_arc - 40, z_arc + 130, '$\\varphi$', fontsize=11, color='#5d6d7e')

ax.text(700, -2150, '$t^2 = (4h^2 + x^2 + 4hx\\sin\\varphi)\\,/\\,v^2$',
        fontsize=10, color='#1a5276', ha='center')
ax.set(xlim=(-560, 2450), ylim=(-2380, 560))
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('docs/assets/images/geom_ray_geom.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved geom_ray_geom.png")

# =====================================================================
# Figure 5 — travel-time curves
# =====================================================================
fig, axs = plt.subplots(1, 2, figsize=(12, 4.9))
fig.suptitle('Travel-Time Curves', fontsize=12, fontweight='bold')

# ─── Left: horizontal-interface hyperbola ───────────────────────────
ax = axs[0]
v = 2000.0
x = np.linspace(-1600, 1600, 800)
for t0, col, lab in [(0.8, '#1a5276', '$t_0$ = 0.8 s'),
                     (1.4, '#2e86c1', '$t_0$ = 1.4 s')]:
    t = np.sqrt(t0**2 + (x / v)**2)
    ax.plot(x, t, color=col, lw=2.2, label=f'reflection, {lab}')
# direct wave = asymptote of the hyperbola
ax.plot(x, np.abs(x) / v, color='#e74c3c', lw=1.5, ls='--',
        label='direct wave  $t = |x|/v$ (asymptote)')
# NMO annotation at x = 1200 on the shallow event
xa, t0a = 1200, 0.8
ta = np.sqrt(t0a**2 + (xa / v)**2)
ax.annotate('', xy=(xa, ta), xytext=(xa, t0a),
            arrowprops=dict(arrowstyle='<->', color='#e67e22', lw=1.6))
ax.text(xa + 60, (ta + t0a) / 2, '$\\Delta t_\\mathrm{NMO}$', fontsize=10,
        color='#b9770e', va='center')
ax.plot([-xa, xa], [t0a, t0a], color='#e67e22', lw=0.9, ls=':')
ax.plot(0, 0.8, 'o', color='#1a5276', ms=6)
ax.text(80, 0.735, '$t_0$', fontsize=11, color='#1a5276')
ax.set(xlabel='Offset $x$ (m)', ylabel='Travel time $t$ (s)',
       title='Horizontal Interface — Hyperbola\n'
             '$t^2 = t_0^2 + x^2/v^2$',
       xlim=(-1700, 1700), ylim=(1.85, 0.55))
ax.legend(loc='upper right', fontsize=8)
ax.grid(alpha=0.3)

# ─── Right: dipping interface — asymmetric curve ────────────────────
ax = axs[1]
h, phi = 1000.0, np.radians(12)
t_dip = np.sqrt(4 * h**2 + x**2 + 4 * h * x * np.sin(phi)) / v
t_hor = np.sqrt(4 * h**2 + x**2) / v
ax.plot(x, t_hor, color='#909497', lw=1.6, ls='--',
        label='horizontal ($\\varphi = 0$)')
ax.plot(x, t_dip, color='#1a5276', lw=2.4,
        label='dipping ($\\varphi = 12°$)')
xmin = -2 * h * np.sin(phi)
tmin = np.sqrt(4 * h**2 + xmin**2 + 4 * h * xmin * np.sin(phi)) / v
ax.plot(xmin, tmin, 'o', color='#e74c3c', ms=8, mec='white', mew=1.2, zorder=5)
ax.annotate('minimum shifted updip\n$x_\\mathrm{min} = -2h\\sin\\varphi$',
            xy=(xmin, tmin), xytext=(-1500, 0.82), fontsize=8.5,
            color='#c0392b',
            arrowprops=dict(arrowstyle='->', color='#c0392b', lw=1.0))
ax.axvline(0, color='#5d6d7e', lw=0.9, ls=':')
ax.text(60, 1.74, 'shot', fontsize=8.5, color='#5d6d7e')
ax.annotate('', xy=(900, 1.30), xytext=(-900, 1.30),
            arrowprops=dict(arrowstyle='->', color='#5d6d7e', lw=1.0))
ax.text(300, 1.35, 'downdip', fontsize=8.5, color='#5d6d7e', ha='center')
ax.set(xlabel='Offset $x$ (m)', ylabel='Travel time $t$ (s)',
       title='Dipping Interface — Asymmetric Curve\n'
             '$t^2 = (4h^2 + x^2 + 4hx\\sin\\varphi)/v^2$',
       xlim=(-1700, 1700), ylim=(1.85, 0.55))
ax.legend(loc='upper right', fontsize=8)
ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('docs/assets/images/geom_traveltime.png', dpi=150,
            bbox_inches='tight')
plt.close()
print("Saved geom_traveltime.png")
