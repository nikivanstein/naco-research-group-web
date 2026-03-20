import numpy as np
import matplotlib.pyplot as plt


def make_naco_banner_svg(
    filename="naco_banner.svg",
    width=18,
    height=5,
    dpi=300,
    seed=7,
):
    rng = np.random.default_rng(seed)

    # -------------------------------------------------
    # Grid for synthetic "optimization landscape"
    # -------------------------------------------------
    x = np.linspace(-6, 6, 900)
    y = np.linspace(-2.2, 2.2, 320)
    X, Y = np.meshgrid(x, y)

    # Build a smooth landscape:
    # - one dominant basin
    # - a few gentle waves/ridges
    # - slight asymmetry for a more organic look
    Z = (
        0.9 * np.sin(0.7 * X) * np.exp(-0.35 * Y**2)
        + 0.35 * np.cos(1.5 * X + 0.6) * np.exp(-0.55 * (Y + 0.2) ** 2)
        + 0.22 * np.sin(2.2 * X - 1.2) * np.exp(-1.2 * (Y - 0.3) ** 2)
        + 0.12 * Y**2
    )

    # Central basin
    Z -= 2.8 * np.exp(-(((X - 0.1) / 1.35) ** 2 + ((Y + 0.15) / 0.55) ** 2))

    # Side shape to avoid perfect symmetry
    Z += 0.35 * np.exp(-(((X - 3.4) / 1.6) ** 2 + ((Y - 0.35) / 0.8) ** 2))
    Z += 0.18 * np.exp(-(((X + 3.8) / 1.9) ** 2 + ((Y + 0.15) / 0.9) ** 2))

    # -------------------------------------------------
    # Figure
    # -------------------------------------------------
    fig, ax = plt.subplots(figsize=(width, height), dpi=dpi)
    bg = "#f4f4f4"
    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)

    # Soft filled contours
    fill_levels = np.linspace(Z.min(), Z.max(), 12)
    ax.contourf(
        X, Y, Z,
        levels=fill_levels,
        cmap="Greens",
        alpha=0.20,
        antialiased=True
    )

    # Thin contour lines
    line_levels = np.linspace(Z.min() + 0.08, Z.max() - 0.05, 18)
    ax.contour(
        X, Y, Z,
        levels=line_levels,
        colors="#787878",
        linewidths=1.0,
        alpha=0.40,
        linestyles="solid"
    )

    # Darker inner basin rings
    basin_levels = np.linspace(Z.min() + 0.02, Z.min() + 0.55, 5)
    ax.contour(
        X, Y, Z,
        levels=basin_levels,
        colors="#555555",
        linewidths=1.35,
        alpha=0.75
    )

    # -------------------------------------------------
    # Faint network graph in the background
    # -------------------------------------------------
    graph_y_shift = 1.35
    left_nodes = np.array([
        [-5.2, graph_y_shift + 0.10],
        [-4.3, graph_y_shift + 0.38],
        [-3.5, graph_y_shift - 0.02],
        [-2.9, graph_y_shift + 0.28],
        [-2.1, graph_y_shift + 0.58],
        [-1.8, graph_y_shift + 0.18],
        [-1.2, graph_y_shift + 0.52],
        [-0.6, graph_y_shift + 0.08],
    ])

    right_nodes = np.array([
        [2.0, graph_y_shift + 0.10],
        [2.7, graph_y_shift + 0.40],
        [3.7, graph_y_shift + 0.15],
        [4.6, graph_y_shift + 0.28],
        [5.3, graph_y_shift + 0.04],
    ])

    nodes = np.vstack([left_nodes, right_nodes])

    edges = [
        (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (4, 6), (5, 7),
        (1, 3), (2, 4), (3, 5), (5, 6),
        (8, 9), (9, 10), (10, 11), (11, 12), (9, 10), (10, 12), (9, 11)
    ]

    for i, j in edges:
        ax.plot(
            [nodes[i, 0], nodes[j, 0]],
            [nodes[i, 1], nodes[j, 1]],
            color="#b8b8b8",
            lw=1.2,
            alpha=0.18,
            zorder=1
        )

    node_sizes = rng.integers(30, 180, size=len(nodes))
    ax.scatter(
        nodes[:, 0], nodes[:, 1],
        s=node_sizes,
        color="#aaaaaa",
        alpha=0.16,
        zorder=2,
        edgecolors="none"
    )

    # -------------------------------------------------
    # Optimization trajectories with small branches
    # -------------------------------------------------
    def bezier_curve(p0, p1, p2, p3, n=120):
        t = np.linspace(0, 1, n)[:, None]
        curve = (
            (1 - t) ** 3 * p0
            + 3 * (1 - t) ** 2 * t * p1
            + 3 * (1 - t) * t ** 2 * p2
            + t ** 3 * p3
        )
        return curve[:, 0], curve[:, 1]

    def draw_path_with_nodes(px, py, lw=2.2, alpha=0.95, n_nodes=13, z_line=5, z_nodes=6):
        ax.plot(
            px, py,
            color="white",
            lw=lw,
            alpha=alpha,
            zorder=z_line,
            solid_capstyle="round"
        )

        if n_nodes > 0:
            idx = np.linspace(8, len(px) - 8, n_nodes, dtype=int)
            sizes = np.linspace(28, 90, len(idx))
            if lw < 1.0:
                sizes *= 0.45
            elif lw < 1.5:
                sizes *= 0.65
            ax.scatter(
                px[idx], py[idx],
                s=sizes,
                color="white",
                alpha=alpha,
                zorder=z_nodes,
                edgecolors="#dddddd",
                linewidths=0.5
            )

    def make_branch(start, d1, d2, d3, n=80, wobble_amp=0.01, wobble_phase=0.0):
        p0 = np.array(start)
        p1 = p0 + np.array(d1)
        p2 = p0 + np.array(d2)
        p3 = p0 + np.array(d3)
        bx, by = bezier_curve(p0, p1, p2, p3, n=n)
        by = by + wobble_amp * np.sin(np.linspace(0, 4 * np.pi, len(bx)) + wobble_phase)
        return bx, by

    # Main trajectories
    main_paths = [
        (   
            np.array([-5.6, -0.8]),
            np.array([-4.1, -0.2]),
            np.array([-2.4, 0.25]),
            np.array([-0.9, 0.05]),
        ),
        (
            np.array([5.2, -1.05]),
            np.array([4.7, -0.2]),
            np.array([2.7, 0.0]),
            np.array([0.3, -0.35]),
        ),
    ]

    main_curves = []
    for k, (p0, p1, p2, p3) in enumerate(main_paths):
        px, py = bezier_curve(p0, p1, p2, p3, n=150)
        wobble = 0.02 * np.sin(np.linspace(0, 6 * np.pi, len(px)) + k)
        py = py + wobble
        draw_path_with_nodes(px, py, lw=2.2, alpha=0.95, n_nodes=13, z_line=5, z_nodes=6)
        main_curves.append((px, py))

    # -------------------------------------------------
    # First-level branches
    # -------------------------------------------------
    branch_specs = [
        # left main path
        dict(parent=0, anchor_idx=42, d1=(0.18, 0.06), d2=(0.42, 0.16), d3=(0.62, 0.22), n=55, phase=0.3),
        dict(parent=0, anchor_idx=68, d1=(0.20, 0.08), d2=(0.55, 0.24), d3=(0.86, 0.34), n=70, phase=0.9),
        dict(parent=0, anchor_idx=94, d1=(0.16, -0.05), d2=(0.36, -0.12), d3=(0.56, -0.15), n=50, phase=1.5),

        # right main path
        dict(parent=1, anchor_idx=36, d1=(-0.16, 0.05), d2=(-0.38, 0.15), d3=(-0.58, 0.22), n=52, phase=2.0),
        dict(parent=1, anchor_idx=61, d1=(-0.22, 0.07), d2=(-0.60, 0.24), d3=(-0.92, 0.34), n=72, phase=2.6),
        dict(parent=1, anchor_idx=88, d1=(-0.14, -0.04), d2=(-0.32, -0.10), d3=(-0.48, -0.13), n=48, phase=3.1),
    ]

    first_level_curves = []
    for spec in branch_specs:
        px_parent, py_parent = main_curves[spec["parent"]]
        i = spec["anchor_idx"]
        start = (px_parent[i], py_parent[i])

        bx, by = make_branch(
            start=start,
            d1=spec["d1"],
            d2=spec["d2"],
            d3=spec["d3"],
            n=spec["n"],
            wobble_amp=0.008,
            wobble_phase=spec["phase"]
        )

        draw_path_with_nodes(
            bx, by,
            lw=1.25,
            alpha=0.72,
            n_nodes=5,
            z_line=4,
            z_nodes=5
        )
        first_level_curves.append((bx, by))

    # -------------------------------------------------
    # Tiny second-level branches (branching branches)
    # -------------------------------------------------
    tiny_branch_specs = [
        # from first left upper branch
        dict(parent=1, anchor_idx=34, d1=(0.10, 0.04), d2=(0.20, 0.09), d3=(0.30, 0.12), n=34, phase=0.4),
        dict(parent=1, anchor_idx=48, d1=(0.08, -0.03), d2=(0.16, -0.06), d3=(0.24, -0.07), n=28, phase=1.2),

        # from first left lower branch
        dict(parent=2, anchor_idx=26, d1=(0.08, -0.02), d2=(0.16, -0.05), d3=(0.24, -0.06), n=26, phase=1.8),

        # from first right upper branch
        dict(parent=4, anchor_idx=36, d1=(-0.10, 0.04), d2=(-0.22, 0.10), d3=(-0.34, 0.13), n=34, phase=2.2),
        dict(parent=4, anchor_idx=52, d1=(-0.08, -0.03), d2=(-0.16, -0.05), d3=(-0.24, -0.06), n=26, phase=2.8),

        # from first right lower branch
        dict(parent=5, anchor_idx=22, d1=(-0.07, -0.02), d2=(-0.14, -0.04), d3=(-0.20, -0.05), n=24, phase=3.3),
    ]

    for spec in tiny_branch_specs:
        bx_parent, by_parent = first_level_curves[spec["parent"]]
        i = min(spec["anchor_idx"], len(bx_parent) - 3)
        start = (bx_parent[i], by_parent[i])

        tx, ty = make_branch(
            start=start,
            d1=spec["d1"],
            d2=spec["d2"],
            d3=spec["d3"],
            n=spec["n"],
            wobble_amp=0.005,
            wobble_phase=spec["phase"]
        )

        draw_path_with_nodes(
            tx, ty,
            lw=0.75,
            alpha=0.52,
            n_nodes=3,
            z_line=3,
            z_nodes=4
        )

    # -------------------------------------------------
    # Layout / export
    # -------------------------------------------------
    ax.set_xlim(-6, 6)
    ax.set_ylim(-2.0, 2.2)
    ax.axis("off")

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig(filename, format="svg", facecolor=bg, bbox_inches="tight", pad_inches=0)
    plt.close(fig)
    print(f"Saved: {filename}")


if __name__ == "__main__":
    make_naco_banner_svg("img/naco_banner.svg")