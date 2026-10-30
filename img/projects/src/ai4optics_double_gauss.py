"""Draw the AI4optics project images: a ray-traced double Gauss lens.

Prescription: the classic f ~ 100 mm, 28 degree field double Gauss
(Zemax sample "Double Gauss 28 degree field"), d-line indices.
Rays are traced in 2D (meridional plane) with Snell's law through the
spherical surfaces and clipped by each clear semi-diameter.

Usage: python ai4optics_double_gauss.py OUT_DIR
Writes OUT_DIR/ai4optics.png (1600x900, the project card). The banner is
made by ai4optics_banner.py.
"""
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

N_SK2, N_SK16, N_F5 = 1.6074, 1.6204, 1.6034
INF = np.inf

# radius, thickness to next surface, index after the surface, semi-diameter
SURFACES = [
    (54.153, 8.747, N_SK2, 32.0),
    (152.522, 0.500, 1.0, 31.0),
    (35.951, 14.000, N_SK16, 26.5),
    (INF, 3.777, N_F5, 26.5),
    (22.270, 14.253, 1.0, 18.5),
    (INF, 12.428, 1.0, 16.5),        # aperture stop
    (-25.685, 3.777, N_F5, 17.0),
    (INF, 10.834, N_SK16, 21.0),
    (-36.980, 0.500, 1.0, 21.0),
    (196.417, 6.858, N_SK16, 23.5),
    (-67.148, 57.315, 1.0, 23.5),
]
STOP = 5
# glass pieces as (first surface, last surface, colour role)
ELEMENTS = [(0, 1, "crown"), (2, 3, "crown"), (3, 4, "flint"),
            (6, 7, "flint"), (7, 8, "crown"), (9, 10, "crown")]

Z = np.concatenate([[0.0], np.cumsum([s[1] for s in SURFACES])])  # vertex z
Z_IMAGE = Z[-1]


def sag(i, y):
    r = SURFACES[i][0]
    if np.isinf(r):
        return Z[i] + 0 * y
    return Z[i] + r - np.sign(r) * np.sqrt(r * r - y * y)


def trace(y0, angle_deg, z0):
    """Trace one ray; return its path as a list of (z, y), or None if vignetted."""
    d = np.array([np.cos(np.radians(angle_deg)), np.sin(np.radians(angle_deg))])
    p = np.array([z0, y0])
    n1 = 1.0
    path = [p.copy()]
    for i, (r, _, n2, sd) in enumerate(SURFACES):
        if np.isinf(r):
            t = (Z[i] - p[0]) / d[0]
            hit = p + t * d
            normal = np.array([-1.0, 0.0])
        else:
            c = np.array([Z[i] + r, 0.0])
            oc = p - c
            b = oc @ d
            disc = b * b - (oc @ oc - r * r)
            if disc < 0:
                return None
            ts = [-b - np.sqrt(disc), -b + np.sqrt(disc)]
            hits = [p + t * d for t in ts if t > 1e-9]
            if not hits:
                return None
            hit = min(hits, key=lambda h: abs(h[0] - Z[i]))
            normal = (hit - c) / r
        if abs(hit[1]) > sd:
            return None
        if normal @ d > 0:
            normal = -normal
        cos_i = -(normal @ d)
        eta = n1 / n2
        k = 1 - eta * eta * (1 - cos_i * cos_i)
        if k < 0:
            return None
        d = eta * d + (eta * cos_i - np.sqrt(k)) * normal
        d /= np.linalg.norm(d)
        p, n1 = hit, n2
        path.append(p.copy())
    t = (Z_IMAGE - p[0]) / d[0]
    path.append(p + t * d)
    return path


def fan(angle_deg, z0, n_rays):
    """n_rays evenly spread over the unvignetted part of the beam."""
    # a ray launched at z0 with height h reaches the first vertex at h - z0*tan(angle)
    heights = z0 * np.tan(np.radians(angle_deg)) + np.linspace(-45, 45, 1801)
    ok = [h for h in heights if trace(h, angle_deg, z0) is not None]
    lo, hi = min(ok), max(ok)
    margin = 0.02 * (hi - lo)
    return [trace(h, angle_deg, z0) for h in np.linspace(lo + margin, hi - margin, n_rays)]


def element_outline(a, b):
    """Polygon of a glass piece between surfaces a and b, with stepped edges."""
    ha, hb = SURFACES[a][3], SURFACES[b][3]
    H = max(ha, hb)
    ys = np.linspace(-ha, ha, 80)
    pts = list(zip(sag(a, ys), ys))
    if ha < H:
        pts.append((sag(a, ha), H))
    if hb < H:
        pts.append((sag(b, hb), H))
    ys = np.linspace(hb, -hb, 80)
    pts += list(zip(sag(b, ys), ys))
    if hb < H:
        pts.append((sag(b, hb), -H))
    if ha < H:
        pts.append((sag(a, ha), -H))
    return np.array(pts)


NAVY = "#001158"
EDGE = "#c9e6ff"
GLASS = {"crown": ("#9fd3ff", 0.16), "flint": ("#5f8dff", 0.26)}
FIELDS = [(0.0, "#5bc8f5"), (10.0, "#7cc56f"), (14.0, "#ffc94d")]


def draw(path, w_px, h_px, xlim, ylim, z0, n_rays, lw, extend=False):
    fig = plt.figure(figsize=(w_px / 100, h_px / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    fig.patch.set_facecolor(NAVY)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")

    # soft radial background: slightly lighter behind the lens
    gx, gy = np.meshgrid(np.linspace(-1, 1, 400), np.linspace(-1, 1, 400))
    glow = np.exp(-((gx * 1.1) ** 2 + (gy * 1.6) ** 2))
    bg = np.empty(gx.shape + (3,))
    for k, (lo, hi) in enumerate(zip((0x00, 0x11, 0x58), (0x0c, 0x24, 0x7a))):
        bg[..., k] = (lo + (hi - lo) * glow) / 255
    ax.imshow(bg, extent=(*xlim, *ylim), zorder=0, aspect="auto")

    # faint optical axis and image plane
    ax.plot(xlim, [0, 0], color=EDGE, lw=0.6, alpha=0.18, ls=(0, (6, 6)), zorder=1)
    ax.plot([Z_IMAGE, Z_IMAGE], [-30, 30], color=EDGE, lw=1.2, alpha=0.55, zorder=4)

    for a, b, kind in ELEMENTS:
        colour, alpha = GLASS[kind]
        ax.add_patch(Polygon(element_outline(a, b), closed=True, facecolor=colour,
                             alpha=alpha, edgecolor="none", zorder=2))
        ax.add_patch(Polygon(element_outline(a, b), closed=True, facecolor="none",
                             edgecolor=EDGE, lw=lw * 0.9, alpha=0.9, zorder=5))
    # aperture stop
    sd = SURFACES[STOP][3]
    for s in (1, -1):
        ax.plot([Z[STOP], Z[STOP]], [s * sd, s * (sd + 6)], color=EDGE, lw=lw * 1.4, zorder=5)

    for angle, colour in FIELDS:
        for ray in fan(angle, z0, n_rays):
            ray = np.array(ray)
            ax.plot(ray[:, 0], ray[:, 1], color=colour, lw=lw * 4, alpha=0.08,
                    solid_capstyle="round", zorder=3)
            ax.plot(ray[:, 0], ray[:, 1], color=colour, lw=lw, alpha=0.9,
                    solid_capstyle="round", zorder=3)
            ax.scatter([ray[-1, 0]], [ray[-1, 1]], s=lw * 14, color=colour, zorder=6, lw=0)
            if extend:
                # let the beam carry on past the focus, fading out
                (za, ya), (zb, yb) = ray[-2], ray[-1]
                slope = (yb - ya) / (zb - za)
                zs = np.linspace(zb, xlim[1], 30)
                for k in range(len(zs) - 1):
                    ax.plot(zs[k:k + 2], yb + slope * (zs[k:k + 2] - zb), color=colour, lw=lw,
                            alpha=0.55 * (1 - k / len(zs)), zorder=3)

    fig.savefig(path, dpi=100, facecolor=NAVY)
    plt.close(fig)


if __name__ == "__main__":
    out = sys.argv[1]
    draw(f"{out}/ai4optics.png", 1600, 900, xlim=(-28, 142), ylim=(-47.8, 47.8),
         z0=-28, n_rays=7, lw=1.8)
