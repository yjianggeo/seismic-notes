"""
Generate geometrical seismology figures:
  geom_gathers.png  — sorting of field data into shot / receiver / CMP / offset gathers
  geom_nmo.png      — synthetic CMP gather before / after NMO correction
  geom_velocity.png — interval, average, RMS and stacking velocities (Dix relation)
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
# Figure 1 — gather sorting diagram
# =====================================================================
fig, axs = plt.subplots(1, 4, figsize=(13, 3.4), sharey=True)
fig.suptitle('Sorting Field Geometry into Gathers', fontsize=12, fontweight='bold')

n = 13
shots, recs = np.meshgrid(np.arange(n), np.arange(n))
panels = [
    ('Common Shot Gather',     shots == 6,                 '#3498db'),
    ('Common Receiver Gather', recs == 6,                  '#2ecc71'),
    ('Common Midpoint Gather', (shots + recs) == 12,       '#e74c3c'),
    ('Common Offset Gather',   (recs - shots) == 4,        '#e67e22'),
]
for ax, (title, mask, col) in zip(axs, panels):
    ax.plot(shots[~mask], recs[~mask], '.', color='#c9d3d8', ms=7)
    ax.plot(shots[mask], recs[mask], 's', color=col, ms=8, mec='white', mew=0.6)
    ax.set(title=title, xlabel='Shot index', xlim=(-0.6, n - 0.4), ylim=(-0.6, n - 0.4))
    ax.set_aspect('equal')
axs[0].set_ylabel('Receiver index')

fig.text(0.5, -0.04,
         'Each point = one recorded trace (shot-receiver pair). '
         'A gather selects traces sharing one attribute of the acquisition geometry.',
         ha='center', fontsize=8.5, color='#5d6d7e')
plt.tight_layout(rect=[0, 0.04, 1, 1])
plt.savefig('docs/assets/images/geom_gathers.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved geom_gathers.png")

# =====================================================================
# Figure 2 — CMP gather before / after NMO
# =====================================================================
def ricker(f0, length, dt):
    t = np.arange(-length / 2, length / 2, dt)
    return (1 - 2 * (np.pi * f0 * t) ** 2) * np.exp(-(np.pi * f0 * t) ** 2), t

dt = 0.002
t_max = 2.6
t_axis = np.arange(0, t_max, dt)
offsets = np.arange(50, 1250, 50)          # 24 traces
events = [(0.60, 2000, 1.0), (1.10, 2400, 0.8), (1.70, 2800, 0.6)]  # t0, v_rms, amp
wav, t_wav = ricker(25, 0.24, dt)

def make_gather(nmo=False):
    data = np.zeros((len(t_axis), len(offsets)))
    for j, x in enumerate(offsets):
        for t0, v, a in events:
            t_evt = np.sqrt(t0**2 + (x / v)**2)
            if nmo:                      # kinematic moveout removal (no stretch mute)
                t_evt = t0
            i0 = int(round(t_evt / dt)) - len(t_wav) // 2
            sl = slice(max(i0, 0), min(i0 + len(t_wav), len(t_axis)))
            w_sl = slice(max(-i0, 0), len(t_wav) - max(i0 + len(t_wav) - len(t_axis), 0))
            data[sl, j] += a * wav[w_sl]
    return data

def plot_gather(ax, data, title):
    for j, x in enumerate(offsets):
        tr = data[:, j]
        tr = tr / (np.abs(tr).max() + 1e-9)
        y = -t_axis
        ax.plot(x + 22 * tr, y, color='k', lw=0.5)
        ax.fill_betweenx(y, x, x + 22 * tr, where=tr > 0, color='#1a5276', lw=0)
    ax.set(xlabel='Offset (m)', title=title, xlim=(0, 1300), ylim=(-t_max, 0))
    ax.set_yticks([-v for v in np.arange(0, t_max + 0.01, 0.5)])
    ax.set_yticklabels([f'{v:.1f}' for v in np.arange(0, t_max + 0.01, 0.5)])
    # overlay theoretical curves
    if 'Before' in title:
        for t0, v, _ in events:
            tt = np.sqrt(t0**2 + (offsets / v)**2)
            ax.plot(offsets, -tt, '--', color='#e74c3c', lw=1.2)
        ax.text(650, -0.32, r'$t^2 = t_0^2 + x^2/v_\mathrm{rms}^2$',
                color='#e74c3c', fontsize=9, ha='center')

fig, axs = plt.subplots(1, 2, figsize=(11, 5.2), sharey=True)
fig.suptitle('CMP Gather: NMO Correction', fontsize=12, fontweight='bold')
plot_gather(axs[0], make_gather(False), 'Before NMO — hyperbolic moveout')
plot_gather(axs[1], make_gather(True),  'After NMO — flattened events')
axs[0].set_ylabel('Two-way time (s)')
for t0, v, _ in events:
    axs[1].axhline(-t0, color='#e74c3c', ls='--', lw=1.0)
axs[1].text(650, -0.32, r'$t(x) \rightarrow t_0$', color='#e74c3c',
            fontsize=9, ha='center')
plt.tight_layout()
plt.savefig('docs/assets/images/geom_nmo.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved geom_nmo.png")

# =====================================================================
# Figure 3 — velocity definitions
# =====================================================================
thick = np.array([400, 600, 500, 700, 800])        # layer thicknesses (m)
vint  = np.array([1800, 2200, 2600, 2400, 3200])   # interval velocities (m/s)
depth_bot = np.cumsum(thick)
tt_bot = 2 * np.cumsum(thick / vint)               # two-way time to layer bottoms
tt_top = np.concatenate([[0], tt_bot[:-1]])

v_avg = depth_bot / (tt_bot / 2)                                   # z / t_1way
v_rms = np.sqrt(np.cumsum(vint**2 * (tt_bot - tt_top)) / tt_bot)   # Dix RMS

fig, axs = plt.subplots(1, 2, figsize=(11, 5.2))
fig.suptitle('Velocity Measures in a Layered Earth', fontsize=12, fontweight='bold')

# Left: interval velocity vs depth (step)
ax = axs[0]
top = np.concatenate([[0], depth_bot[:-1]])
for h0, h1, v in zip(top, depth_bot, vint):
    ax.plot([v, v], [h0, h1], color='#1a5276', lw=2.5)
    ax.plot([], [])
for i in range(len(vint) - 1):
    ax.plot([vint[i], vint[i + 1]], [depth_bot[i]] * 2, color='#1a5276', lw=2.5)
    ax.text((vint[i] + vint[i + 1]) / 2, depth_bot[i] - 60,
            f'interface {i + 1}', fontsize=7.5, color='#7f8c8d', ha='center')
for v, h0, h1 in zip(vint, top, depth_bot):
    ax.text(v + 60, (h0 + h1) / 2, f'$v_i$ = {v} m/s', fontsize=8,
            color='#1a5276', va='center')
ax.set(xlabel='Interval velocity (m/s)', ylabel='Depth (m)',
       title='Layered Model', xlim=(1500, 3900), ylim=(3100, 0))
ax.grid(alpha=0.3)

# Right: average / RMS / stacking velocity vs two-way time
ax = axs[1]
# extend curves vertically within each layer
for i in range(len(vint)):
    ax.plot([v_avg[i]] * 2, [tt_top[i], tt_bot[i]], color='#2ecc71', lw=2.2)
    ax.plot([v_rms[i]] * 2, [tt_top[i], tt_bot[i]], color='#e74c3c', lw=2.2)
    if i < len(vint) - 1:
        ax.plot([v_avg[i], v_avg[i + 1]], [tt_bot[i]] * 2, color='#2ecc71', lw=2.2)
        ax.plot([v_rms[i], v_rms[i + 1]], [tt_bot[i]] * 2, color='#e74c3c', lw=2.2)
# stacking velocity picks (hyperbola best-fit ≈ v_rms with scatter)
rng = np.random.default_rng(7)
v_stk = v_rms * (1 + rng.normal(0, 0.012, len(v_rms)))
ax.plot(v_stk, tt_bot, 'o', color='#f39c12', ms=9, mec='white', mew=1.2, zorder=5)
ax.plot([], [], color='#2ecc71', lw=2.2, label='Average velocity $v_\\mathrm{avg}$')
ax.plot([], [], color='#e74c3c', lw=2.2, label='RMS velocity $v_\\mathrm{rms}$')
ax.plot([], [], 'o', color='#f39c12', ms=9, mec='white', label='Stacking velocity $v_\\mathrm{stack}$ (picks)')

# Dix inversion annotation on deepest layer
v_dix = np.sqrt((vint[-1]**2))  # trivially recovered for illustration
ax.annotate('Dix: layer velocity from\n$v_i^2 = \\dfrac{v_{\\mathrm{rms},n}^2 t_n - '
            'v_{\\mathrm{rms},n-1}^2 t_{n-1}}{t_n - t_{n-1}}$',
            xy=(v_rms[-1], tt_bot[-1]), xytext=(2760, 1.9),
            fontsize=8, color='#5d6d7e',
            arrowprops=dict(arrowstyle='->', color='#7f8c8d', lw=0.9))
ax.set(xlabel='Velocity (m/s)', ylabel='Two-way time (s)',
       title='Velocity vs Two-way Time', xlim=(1600, 3600), ylim=(2.4, 0))
ax.legend(loc='lower left')
ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('docs/assets/images/geom_velocity.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved geom_velocity.png")
