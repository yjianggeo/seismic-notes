"""
Generate figures for glacier seismology note:
  1. glacier_signals.png  — synthetic icequake waveforms (4 types)
  2. glacier_das.png      — DAS deployment schematics + example gather
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from scipy.signal import butter, filtfilt

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
})

rng = np.random.default_rng(2024)

# ─── Helpers ─────────────────────────────────────────────────────────
def ricker(f0, dt, n):
    tc = np.arange(n)*dt - n*dt/2
    return (1-2*(np.pi*f0*tc)**2)*np.exp(-(np.pi*f0*tc)**2)

def bandpass(sig, lo, hi, fs, order=4):
    b, a = butter(order, [lo/(fs/2), hi/(fs/2)], btype='band')
    return filtfilt(b, a, sig)

def coda_envelope(t, t0, f0, Q):
    out = np.zeros_like(t)
    mask = t > t0
    dt_arr = t[mask] - t0
    out[mask] = np.exp(-np.pi*f0*dt_arr/Q)
    return out

# ─────────────────────────────────────────────────────────────────────
# Figure 1: Icequake waveforms
# ─────────────────────────────────────────────────────────────────────
dt = 0.01; fs = 1/dt
t  = np.arange(0, 8, dt)

# 1. Surface crevasse (high frequency, impulsive)
ev1 = ricker(20.0, dt, len(t))
ev1 = np.roll(ev1, int(0.8/dt))
ev1[:int(0.8/dt)] = 0
ev1 += 0.04*rng.standard_normal(len(t))
ev1 = bandpass(ev1, 1.0, 40.0, fs)

# 2. Basal stick-slip (low freq, emergent onset)
ev2 = np.zeros(len(t))
t_start = int(1.5/dt); t_dur = int(1.2/dt)
env2 = np.hanning(t_dur) * 1.0
ev2[t_start:t_start+t_dur] = env2 * np.sin(2*np.pi*2.5*t[:t_dur])
ev2 += 0.04*rng.standard_normal(len(t))
ev2 = bandpass(ev2, 0.5, 8.0, fs)

# 3. Calving / ice-mass collapse (very long period, large amp)
ev3 = np.zeros(len(t))
t_start3 = int(0.5/dt); t_dur3 = int(4.0/dt)
env3 = np.exp(-np.linspace(0, 4, t_dur3)) * np.sin(2*np.pi*0.5*t[:t_dur3])
if t_start3+t_dur3 <= len(t):
    ev3[t_start3:t_start3+t_dur3] = env3
ev3 += 0.01*rng.standard_normal(len(t))
ev3 = bandpass(ev3, 0.1, 2.0, fs)

# 4. Hydraulic tremor (continuous, narrowband)
ev4 = np.zeros(len(t))
for f_dom in [3.5, 7.0, 10.5]:
    ev4 += 0.3*np.sin(2*np.pi*f_dom*t + rng.uniform(0, 2*np.pi))
ev4 *= np.clip(coda_envelope(t, 0.5, 3.5, 200)*1.4, 0, 1)
ev4 += 0.1*rng.standard_normal(len(t))
ev4 = bandpass(ev4, 1.5, 18.0, fs)

events = [ev1, ev2, ev3, ev4]
titles = [
    'Surface crevasse icequake\n(impulsive, 5–40 Hz)',
    'Basal stick-slip event\n(emergent, 0.5–8 Hz)',
    'Calving / ice-mass collapse\n(long-period, 0.1–2 Hz)',
    'Subglacial hydraulic tremor\n(continuous, narrowband)',
]
colors = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6']

fig, axes = plt.subplots(4, 1, figsize=(11, 8), sharex=True)
fig.suptitle('Glaciological Seismic Signal Types', fontsize=12, fontweight='bold')

for ax, sig, title, col in zip(axes, events, titles, colors):
    ax.plot(t, sig/np.abs(sig).max(), color=col, lw=0.9, alpha=0.92)
    ax.axhline(0, color='gray', lw=0.5, ls=':')
    ax.set_ylabel('Norm. amp.', fontsize=8)
    ax.set_title(title, loc='left', fontsize=9, color=col, fontweight='bold')
    ax.set_ylim(-1.5, 1.5)
    ax.grid(True, alpha=0.2)
    ax.spines[['top', 'right']].set_visible(False)

axes[-1].set_xlabel('Time (s)')
plt.tight_layout()
plt.savefig('docs/assets/images/glacier_signals.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved glacier_signals.png")


# ─────────────────────────────────────────────────────────────────────
# Figure 2: DAS deployment + synthetic DAS gather on glacier
# ─────────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(14, 6))
fig.suptitle('DAS Deployment on Glacier and Example Record', fontsize=12, fontweight='bold')

# ── Left: deployment schematic ────────────────────────────────────
ax1 = fig.add_subplot(1, 3, 1)
ax1.set_xlim(-0.5, 5.5); ax1.set_ylim(-4.5, 1.5)
ax1.set_aspect('equal'); ax1.axis('off')
ax1.set_title('Deployment Configurations', fontsize=10)

# Ice surface (irregular)
ice_x = np.linspace(-0.5, 5.5, 200)
ice_y = 0.15*np.sin(2*ice_x) + 0.05*np.sin(5*ice_x)
ax1.fill_between(ice_x, ice_y, 1.5, color='#d6eaf8', alpha=0.6)
ax1.plot(ice_x, ice_y, color='#2980b9', lw=1.5)

# Bedrock
ax1.fill_between([-0.5, 5.5], [-4.5, -4.5], [-3.5, -3.5],
                 color='#784212', alpha=0.7)
ax1.plot([-0.5, 5.5], [-3.5, -3.5], color='#6e2f0f', lw=2)
ax1.text(2.5, -4.1, 'Bedrock', ha='center', fontsize=8, color='#6e2f0f')

# Ice body
ax1.fill_between(ice_x, ice_y, -3.5, color='#aed6f1', alpha=0.5)
ax1.text(0.3, -1.8, 'Ice', fontsize=9, color='#2471a3', fontstyle='italic')

# Surface cable (A)
cable_x = np.linspace(0.3, 4.8, 100)
cable_y = 0.15*np.sin(2*cable_x) + 0.05*np.sin(5*cable_x) + 0.08
ax1.plot(cable_x, cable_y, color='#f39c12', lw=3, solid_capstyle='round',
         label='Surface cable (A)', zorder=5)
# Channel dots
for xi in np.linspace(0.5, 4.6, 8):
    yi = 0.15*np.sin(2*xi) + 0.05*np.sin(5*xi) + 0.08
    ax1.plot(xi, yi, 'o', color='#e67e22', ms=4, zorder=6)

# Borehole cable (B)
bh_x = 2.2
ax1.plot([bh_x, bh_x], [ice_y[int((bh_x+0.5)/6*200)], -3.4],
         color='#e74c3c', lw=2.5, ls='--', label='Borehole cable (B)', zorder=5)
for yi in np.linspace(-0.2, -3.3, 8):
    ax1.plot(bh_x, yi, 'D', color='#c0392b', ms=4, zorder=6)

# DAS interrogator
ax1.add_patch(mpatches.FancyBboxPatch((3.8, 0.4), 1.3, 0.7,
              boxstyle='round,pad=0.05', fc='#f8c471', ec='#d4ac0d', lw=1.5))
ax1.text(4.45, 0.75, 'DAS\nIU', ha='center', va='center', fontsize=7.5,
         fontweight='bold', color='#7d6608')
# Fiber connection line
yi_conn = 0.15*np.sin(2*3.9) + 0.05*np.sin(5*3.9) + 0.08
ax1.plot([3.9, 3.9], [yi_conn, 0.4], color='gray', lw=1, ls=':')

# Ice crevasse
crv_x = [1.0, 1.05, 0.95, 1.02]
crv_y = [ice_y[int(1.5/6*200)], -0.5, -1.2, -1.8]
ax1.plot(crv_x, crv_y, color='#2c3e50', lw=1.5, ls='--')
ax1.annotate('Crevasse', xy=(1.02, -0.9), xytext=(0.0, -0.5),
             fontsize=7.5, color='#2c3e50',
             arrowprops=dict(arrowstyle='->', color='#2c3e50', lw=0.8))

# Subglacial water
ax1.fill_between([3.0, 4.5], [-3.5, -3.5], [-3.3, -3.3],
                 color='#85c1e9', alpha=0.8)
ax1.text(3.75, -3.42, 'Subglacial\nwater', ha='center', fontsize=7, color='#1a5276')

ax1.legend(loc='lower right', fontsize=7.5,
           handles=[
               plt.Line2D([0],[0], color='#f39c12', lw=3, label='(A) Surface cable'),
               plt.Line2D([0],[0], color='#e74c3c', lw=2.5, ls='--', label='(B) Borehole cable'),
           ])
ax1.set_title('Deployment Configurations', fontsize=10)

# ── Middle: surface cable DAS gather ──────────────────────────────
ax2 = fig.add_subplot(1, 3, 2)
dt_d = 0.002; fs_d = 1/dt_d
t_d  = np.arange(0, 3.0, dt_d)
nx_d = 60; dx_d = 5.0         # 60 channels, 5 m spacing
x_d  = np.arange(nx_d)*dx_d

das_data = np.zeros((nx_d, len(t_d)))
wav_das = ricker(15.0, dt_d, 80)

# Icequake: origin at x=100m, t=0.3s, apparent velocity 1600 m/s (ice P)
for ix, xi in enumerate(x_d):
    t_arr = 0.30 + np.abs(xi - 100.0)/1600.0
    it = int(round(t_arr/dt_d))
    if 0 <= it <= len(t_d)-80:
        das_data[ix, it:it+80] += wav_das * (1.2 - xi/x_d[-1]*0.3)

# Surface wave (Rayleigh, 600 m/s)
for ix, xi in enumerate(x_d):
    t_arr = 0.30 + xi/600.0
    it = int(round(t_arr/dt_d))
    wav_sw = ricker(6.0, dt_d, 120)
    if 0 <= it <= len(t_d)-120:
        das_data[ix, it:it+120] += 0.6 * wav_sw

das_data += 0.04*np.abs(das_data).max()*rng.standard_normal(das_data.shape)
das_data = np.array([bandpass(row, 1.0, 60.0, fs_d) for row in das_data])

vmax = np.percentile(np.abs(das_data), 97)
ax2.imshow(das_data.T, aspect='auto', cmap='seismic',
           extent=[x_d[0], x_d[-1], t_d[-1], t_d[0]],
           vmin=-vmax, vmax=vmax)
ax2.set(xlabel='Along-cable distance (m)', ylabel='Time (s)',
        title='(A) Surface DAS — icequake record')
ax2.annotate('P-wave\n(1600 m/s)', xy=(200, 0.45), xytext=(240, 0.6),
             fontsize=7.5, color='white',
             arrowprops=dict(arrowstyle='->', color='white', lw=0.8),
             path_effects=[pe.withStroke(linewidth=1.5, foreground='black')])
ax2.annotate('Surface wave\n(Rayleigh, 600 m/s)', xy=(160, 0.72), xytext=(60, 1.0),
             fontsize=7.5, color='yellow',
             arrowprops=dict(arrowstyle='->', color='yellow', lw=0.8),
             path_effects=[pe.withStroke(linewidth=1.5, foreground='black')])

# ── Right: borehole DAS gather (VSP-style) ────────────────────────
ax3 = fig.add_subplot(1, 3, 3)
nz_d = 50; dz_d = 10.0    # 50 channels, 10 m depth spacing
z_d  = np.arange(nz_d)*dz_d   # 0 … 490 m depth

bh_data = np.zeros((nz_d, len(t_d)))
V_ice = 3700.0   # P-wave velocity in ice (m/s)
z_bed = 480.0    # bed depth

for iz, zi in enumerate(z_d):
    # Downgoing direct P
    t_down = zi/V_ice
    it = int(round(t_down/dt_d))
    if 0 <= it <= len(t_d)-60:
        bh_data[iz, it:it+60] += ricker(40.0, dt_d, 60) * 1.0
    # Upgoing bed reflection
    t_up = (2*z_bed - zi)/V_ice
    it2 = int(round(t_up/dt_d))
    if 0 <= it2 <= len(t_d)-60:
        bh_data[iz, it2:it2+60] += ricker(40.0, dt_d, 60) * 0.4

bh_data += 0.02*np.abs(bh_data).max()*rng.standard_normal(bh_data.shape)

vmax2 = np.percentile(np.abs(bh_data), 97)
ax3.imshow(bh_data.T, aspect='auto', cmap='seismic',
           extent=[z_d[0], z_d[-1], t_d[-1], t_d[0]],
           vmin=-vmax2, vmax=vmax2)
ax3.set(xlabel='Depth (m)', ylabel='Time (s)',
        title='(B) Borehole DAS — VSP-style record')
ax3.axhline(z_bed/V_ice, color='yellow', lw=1.0, ls=':', alpha=0.6)
ax3.annotate('Downgoing P', xy=(200, 0.055), xytext=(280, 0.12),
             fontsize=7.5, color='white',
             arrowprops=dict(arrowstyle='->', color='white', lw=0.8),
             path_effects=[pe.withStroke(linewidth=1.5, foreground='black')])
ax3.annotate('Bed reflection', xy=(200, 0.21), xytext=(280, 0.28),
             fontsize=7.5, color='yellow',
             arrowprops=dict(arrowstyle='->', color='yellow', lw=0.8),
             path_effects=[pe.withStroke(linewidth=1.5, foreground='black')])
ax3.axhline(z_bed/V_ice*2, color='#f39c12', lw=1.5, ls='--', alpha=0.5)

plt.tight_layout()
plt.savefig('docs/assets/images/glacier_das.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved glacier_das.png")
print("Done.")
