"""Reproduce the explicitly schematic surface-wave teaching figure.

No observed data or elastic eigenvalue solver is used. The phase curve is
prescribed analytically; group velocity is derived from k=2*pi*f/c. The
right-hand curves are normalized Gaussian illustrations, not sensitivity
kernels computed for a layered medium. Original tracked artwork remains
recoverable from Git history. This script intentionally replaces that figure.
"""

from pathlib import Path
import hashlib
import json

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "docs" / "assets" / "images"
COLORS = ["#0072B2", "#D55E00", "#009E73", "#000000"]


def phase(f):
    """Prescribed demonstration curve, with f in Hz and speed in m/s."""
    slow, fast = 200.0 * 0.919, 600.0 * 0.919
    transition_hz = (slow + fast) / 2 / (2 * 20.0)
    x = np.asarray(f) / transition_hz
    c = slow + (fast - slow) / (1 + x**2)
    derivative = -2 * (fast - slow) * x / (transition_hz * (1 + x**2)**2)
    return c, derivative


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    f = np.linspace(0.5, 50, 600)
    c, dc_df = phase(f)
    group = c / (1 - f * dc_df / c)
    k = 2 * np.pi * f / c
    finite_difference = np.gradient(2 * np.pi * f, k)
    relative_check = float(np.max(np.abs((finite_difference[2:-2] - group[2:-2]) / group[2:-2])))
    assert np.all(np.isfinite(group)) and np.all(group > 0)
    assert np.all(group <= c)
    assert relative_check < 1e-4

    z = np.linspace(0, 120, 400)
    frequencies = [5.0, 15.0, 30.0, 50.0]
    weights = []
    for fi in frequencies:
        ci, _ = phase(fi)
        peak = float(ci / (3 * fi))
        width = max(0.55 * peak, 1.0)
        curve = np.exp(-0.5 * ((z - peak) / width)**2)
        weights.append((curve / curve.max(), peak))

    style = {
        "font.family": "DejaVu Sans", "font.size": 11,
        "axes.titlesize": 12, "axes.labelsize": 11,
        "legend.fontsize": 9, "xtick.labelsize": 10, "ytick.labelsize": 10,
        "axes.spines.top": False, "axes.spines.right": False,
        "figure.facecolor": "white", "axes.facecolor": "white",
        "savefig.facecolor": "white", "text.color": "#202521",
        "axes.labelcolor": "#202521", "axes.edgecolor": "#59625d",
    }
    with plt.rc_context(style):
        fig, axes = plt.subplots(1, 2, figsize=(11, 5), layout="constrained")
        fig.suptitle("Surface-wave intuition: analytical schematics", fontsize=15, fontweight="bold")
        axes[0].plot(f, c, color=COLORS[0], lw=2.6, label="Prescribed phase velocity c(f)")
        axes[0].plot(f, group, color=COLORS[1], lw=2.6, ls="--", label="Derived group velocity U(f)")
        axes[0].set(xlabel="Frequency (Hz)", ylabel="Velocity (m/s)",
                    title="(a) Group velocity from the same phase curve",
                    xlim=(0.5, 50), ylim=(0, 620))
        axes[0].text(0.98, 0.95, r"$U=c/[1-(f/c)\,\mathrm{d}c/\mathrm{d}f]$",
                     transform=axes[0].transAxes, ha="right", va="top", fontsize=12)
        axes[0].legend(loc="upper right", bbox_to_anchor=(1, 0.85), frameon=False)

        for idx, (fi, (curve, peak)) in enumerate(zip(frequencies, weights)):
            axes[1].plot(curve, z, color=COLORS[idx], ls=["-", "--", "-.", ":"][idx],
                         lw=2.4, label=f"{fi:g} Hz; peak {peak:.1f} m")
        axes[1].set(xlabel="Illustrative weighting / its maximum", ylabel="Depth (m)",
                    title="(b) Toy depth weighting, not computed kernels",
                    xlim=(0, 1.05), ylim=(120, 0))
        axes[1].legend(loc="lower right", frameon=False)
        axes[1].text(0.05, 0.07, r"Peaks placed at $c(f)/(3f)$" "\nGaussian shapes chosen for illustration",
                     transform=axes[1].transAxes, fontsize=9, va="bottom")
        for ax in axes:
            ax.grid(color="#dce1dd", lw=0.7)
            ax.set_axisbelow(True)
        target = DEST / "sw_dispersion.png"
        fig.savefig(target, dpi=180, transparent=False)
        plt.close(fig)

    np.savetxt(DEST / "sw_dispersion_curves.csv", np.column_stack([f, c, group]),
               delimiter=",", header="frequency_hz,phase_velocity_mps,group_velocity_mps", comments="")
    np.savetxt(DEST / "sw_dispersion_weightings.csv", np.column_stack([z] + [w[0] for w in weights]),
               delimiter=",", header="depth_m,toy_5hz,toy_15hz,toy_30hz,toy_50hz", comments="")
    with Image.open(target) as im:
        size = list(im.size)
        dpi = list(im.info.get("dpi", ()))
        mode = im.mode
        if "A" in im.getbands():
            assert im.getchannel("A").getextrema() == (255, 255)
    manifest = {
        "purpose": "Web teaching figure; not observational data or a layered elastic solution",
        "uncertainty": "None: deterministic analytical illustration",
        "missing_data": "None",
        "transformation": "Prescribed Lorentzian phase curve; U=d(2*pi*f)/d(2*pi*f/c); peak-normalized toy Gaussian weightings",
        "group_derivative_max_relative_difference": relative_check,
        "matplotlib": matplotlib.__version__, "numpy": np.__version__,
        "pixels": size, "dpi": dpi, "mode": mode,
        "background": "opaque white", "figure_inches": [11, 5],
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "image_sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
    }
    (DEST / "sw_dispersion_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
