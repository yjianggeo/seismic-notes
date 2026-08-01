"""
Generate das_coupling.png:
  Left:  Schematic cross-sections of loose-tube vs tight-buffered cable
  Right: Coupling transfer functions for 4 deployment scenarios
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8.5,
})

fig = plt.figure(figsize=(13, 5.5))
fig.suptitle('DAS Cable Coupling', fontsize=12, fontweight='bold')

# ─── Left: cable cross-sections ──────────────────────────────────────
ax_cab = fig.add_subplot(1, 2, 1)
ax_cab.set_xlim(-4.5, 4.5)
ax_cab.set_ylim(-3.2, 3.2)
ax_cab.set_aspect('equal')
ax_cab.axis('off')
ax_cab.set_title('Cable Cross-Section\n(Loose Tube vs Tight Buffered)', fontsize=10)

def draw_cable(cx, cy, title, loose=True):
    """Draw schematic cable cross-section centered at (cx, cy)."""
    # Outer jacket
    jacket = plt.Circle((cx, cy), 1.5, fc='#aab7b8', ec='#717d7e', lw=1.5)
    ax_cab.add_patch(jacket)

    if loose:
        # Loose tube: hollow tube in center, fiber floats in gel
        tube = plt.Circle((cx, cy), 0.9, fc='#f9e79f', ec='#d4ac0d', lw=1.2)
        ax_cab.add_patch(tube)
        gel = plt.Circle((cx, cy), 0.75, fc='#fdf2ca', ec='none')
        ax_cab.add_patch(gel)
        # Fibers floating off-center
        for angle in [30, 120, 210, 300]:
            fx = cx + 0.4 * np.cos(np.radians(angle))
            fy = cy + 0.4 * np.sin(np.radians(angle))
            ax_cab.add_patch(plt.Circle((fx, fy), 0.1, fc='#2ecc71', ec='#1a7a3a', lw=0.8))
        ax_cab.text(cx, cy - 2.0, title, ha='center', fontsize=8.5,
                    fontweight='bold', color='#5d6d7e')
        ax_cab.text(cx, cy - 2.45, '(loosely coupled)', ha='center', fontsize=7.5,
                    color='#7f8c8d')
    else:
        # Tight-buffered: polymer buffer directly around each fiber
        for angle in [0, 72, 144, 216, 288]:
            fx = cx + 0.7 * np.cos(np.radians(angle))
            fy = cy + 0.7 * np.sin(np.radians(angle))
            # Buffer
            ax_cab.add_patch(plt.Circle((fx, fy), 0.3, fc='#aed6f1', ec='#2471a3', lw=0.8))
            # Fiber core
            ax_cab.add_patch(plt.Circle((fx, fy), 0.12, fc='#2ecc71', ec='#1a7a3a', lw=0.6))
        ax_cab.text(cx, cy - 2.0, title, ha='center', fontsize=8.5,
                    fontweight='bold', color='#5d6d7e')
        ax_cab.text(cx, cy + 2.0, '(tightly coupled)', ha='center', fontsize=7.5,
                    color='#7f8c8d')

draw_cable(-2.2, 0.3, 'Loose-tube', loose=True)
draw_cable( 2.2, 0.3, 'Tight-buffered', loose=False)

# Labels
ax_cab.annotate('Outer jacket',   xy=(-2.2+1.5, 0.3), xytext=(-0.5, 1.9),
                fontsize=7.5, color='#717d7e',
                arrowprops=dict(arrowstyle='->', color='#717d7e', lw=0.8))
ax_cab.annotate('Loose tube\n(gel-filled)', xy=(-2.2+0.9, 0.3), xytext=(-3.8, 1.5),
                fontsize=7.5, color='#d4ac0d',
                arrowprops=dict(arrowstyle='->', color='#d4ac0d', lw=0.8))
ax_cab.annotate('Fiber\n(free)', xy=(-2.2+0.4*np.cos(np.radians(30)),
                                     0.3+0.4*np.sin(np.radians(30))),
                xytext=(-4.2, -0.5),
                fontsize=7.5, color='#1a7a3a',
                arrowprops=dict(arrowstyle='->', color='#1a7a3a', lw=0.8))
ax_cab.annotate('Polymer buffer\n(bonded to fiber)', xy=(2.2+0.7, 0.3),
                xytext=(1.0, 2.3),
                fontsize=7.5, color='#2471a3',
                arrowprops=dict(arrowstyle='->', color='#2471a3', lw=0.8))
ax_cab.annotate('Fiber\n(strain-coupled)', xy=(2.2+0.7, 0.3),
                xytext=(0.6, -1.8),
                fontsize=7.5, color='#1a7a3a',
                arrowprops=dict(arrowstyle='->', color='#1a7a3a', lw=0.8))

# eta labels
ax_cab.text(-2.2, -2.85, r'$\eta_\mathrm{fiber} \approx 0$', ha='center',
            fontsize=9, color='#c0392b', fontweight='bold')
ax_cab.text( 2.2, -2.85, r'$\eta_\mathrm{fiber} \approx 0.8$–$1.0$', ha='center',
            fontsize=9, color='#27ae60', fontweight='bold')

# ─── Right: coupling transfer functions ──────────────────────────────
ax_tf = fig.add_subplot(1, 2, 2)
f = np.logspace(-1, 3, 600)    # 0.1 – 1000 Hz

def coupling_lp(f, fc):
    """Simple 1st-order low-pass coupling model: C(f) = 1/sqrt(1+(f/fc)^2)."""
    return 1.0 / np.sqrt(1 + (f / fc)**2)

scenarios = [
    ('Cemented borehole',    np.ones_like(f),          '#2ecc71', '-',  5000),
    ('Frozen in ice',        coupling_lp(f, 3000),     '#3498db', '-',  3000),
    ('Buried 0.3 m (soil)',  coupling_lp(f, 300),      '#e67e22', '--', 300),
    ('Surface-laid (loose)', coupling_lp(f, 30),       '#e74c3c', ':',  30),
]

for label, C, col, ls, fc in scenarios:
    ax_tf.semilogx(f, 20*np.log10(np.abs(C)), color=col, ls=ls, lw=2.2, label=label)
    if np.isfinite(fc) and fc < 1000:
        ax_tf.axvline(fc, color=col, lw=0.8, ls=':', alpha=0.5)

ax_tf.axhline(-3, color='gray', lw=0.8, ls='--', alpha=0.6)
ax_tf.text(0.13, -3.9, '−3 dB', fontsize=7.5, color='gray')
ax_tf.fill_between(f, -60, 20*np.log10(coupling_lp(f, 300)),
                   where=f > 300, alpha=0.06, color='#e67e22')
ax_tf.set(xlabel='Frequency (Hz)',
          ylabel='Coupling efficiency (dB)',
          title='Cable-to-Medium Coupling Transfer Function\n'
                r'$C(f) = 1\,/\,\sqrt{1+(f/f_c)^2}$',
          xlim=[0.1, 1000], ylim=[-45, 3])
ax_tf.legend(loc='lower left')
ax_tf.grid(True, which='both', alpha=0.3)

# Annotate cutoff frequencies
for label_short, fc, ypos, col in [
    ('$f_c\\approx30$ Hz\n(surface loose)', 30, -28, '#e74c3c'),
    ('$f_c\\approx300$ Hz\n(buried 0.3 m)', 300, -14, '#e67e22'),
]:
    ax_tf.annotate(label_short, xy=(fc, -3), xytext=(fc*0.35, ypos),
                   fontsize=7.5, color=col,
                   arrowprops=dict(arrowstyle='->', color=col, lw=0.8))

plt.tight_layout()
plt.savefig('docs/assets/images/das_coupling.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved das_coupling.png")
