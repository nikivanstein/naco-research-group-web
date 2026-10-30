"""Draw the stylised AI4optics banner (1180x200): a double Gauss lens with a
dense, colour-graded fan of rays over many field angles, glowing foci and
beams that fan out past the image plane. Uses the tracer in
ai4optics_double_gauss.py (or double_gauss.py next to it).

Usage: python ai4optics_banner.py OUT_DIR
Writes OUT_DIR/ai4optics-wide-2x.png; scale it to 1180x200 as ai4optics-wide.png.
"""
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Polygon

try:
    import ai4optics_double_gauss as dg
except ImportError:
    import double_gauss as dg

W, H = 2360, 400                      # rendered at 2x, scaled down afterwards
XLIM = (-170, 260)
YLIM = (-(XLIM[1] - XLIM[0]) * H / W / 2, (XLIM[1] - XLIM[0]) * H / W / 2)
RAYS = LinearSegmentedColormap.from_list("rays", ["#5bc8f5", "#7cc56f", "#ffc94d", "#ff8a5c"])


def main(out):
    fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(*XLIM)
    ax.set_ylim(*YLIM)
    ax.set_aspect("equal")
    ax.axis("off")

    # background: deep navy with a soft glow around the lens and image plane
    gx, gy = np.meshgrid(np.linspace(*XLIM, 600), np.linspace(*YLIM, 120))
    glow = (np.exp(-(((gx - 60) / 120) ** 2 + (gy / 40) ** 2))
            + 0.6 * np.exp(-(((gx - dg.Z_IMAGE) / 45) ** 2 + (gy / 25) ** 2)))
    bg = np.empty(gx.shape + (3,))
    for k, (lo, hi) in enumerate(zip((0x00, 0x0a, 0x3d), (0x10, 0x2c, 0x8a))):
        bg[..., k] = (lo + (hi - lo) * np.clip(glow, 0, 1)) / 255
    ax.imshow(bg, extent=(*XLIM, *YLIM), origin="lower", zorder=0, aspect="auto")

    # faint stars
    rng = np.random.default_rng(7)
    sx = rng.uniform(*XLIM, 220)
    sy = rng.uniform(*YLIM, 220)
    ax.scatter(sx, sy, s=rng.uniform(0.5, 4, 220), color="white", alpha=0.25, lw=0, zorder=1)

    # glass
    for a, b, kind in dg.ELEMENTS:
        outline = dg.element_outline(a, b)
        ax.add_patch(Polygon(outline, closed=True, facecolor="#9fd3ff",
                             alpha=0.10 if kind == "crown" else 0.18, edgecolor="none", zorder=2))
        ax.add_patch(Polygon(outline, closed=True, facecolor="none", edgecolor="#d6ecff",
                             lw=1.4, alpha=0.75, zorder=6))

    # rays: many fields, each a fan; colour follows the field angle
    angles = np.linspace(-14, 14, 9)
    foci = []
    for angle in angles:
        colour = RAYS((angle + 14) / 28)
        rays = [np.array(r) for r in dg.fan(angle, XLIM[0], 9)]
        for ray in rays:
            (za, ya), (zb, yb) = ray[-2], ray[-1]
            slope = (yb - ya) / (zb - za)
            tail_z = np.linspace(zb, XLIM[1], 40)
            tail_y = yb + slope * (tail_z - zb)
            for width, alpha in ((7, 0.035), (3, 0.08), (1.0, 0.75)):
                ax.plot(ray[:, 0], ray[:, 1], color=colour, lw=width, alpha=alpha,
                        solid_capstyle="round", zorder=3)
            for k in range(len(tail_z) - 1):
                fade = (1 - k / len(tail_z)) ** 1.6
                ax.plot(tail_z[k:k + 2], tail_y[k:k + 2], color=colour, lw=1.0,
                        alpha=0.6 * fade, zorder=3)
        foci.append((rays[len(rays) // 2][-1], colour))

    # glowing foci on the image plane
    for (z, y), colour in foci:
        for size, alpha in ((900, 0.05), (300, 0.12), (60, 0.5), (14, 1.0)):
            ax.scatter([z], [y], s=size, color=colour, alpha=alpha, lw=0, zorder=7)
    ax.plot([dg.Z_IMAGE] * 2, [YLIM[0] * 0.9, YLIM[1] * 0.9], color="white", lw=1.0, alpha=0.25, zorder=5)

    fig.savefig(f"{out}/ai4optics-wide-2x.png", dpi=100, facecolor="#000a3d")
    plt.close(fig)


if __name__ == "__main__":
    main(sys.argv[1])
