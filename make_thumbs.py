"""Generate small WebP versions of the images the site shows at reduced size.

GitHub Pages cannot resize images at build time, so the thumbnails are
committed to the repository. Run this after adding or replacing a photo,
project image or news image:

    python make_thumbs.py

Each source image `img/<dir>/<name>` gets `img/thumbs/<dir>/<name>.webp`.
The templates fall back to the original image when a thumbnail is missing,
so forgetting to run this only costs page weight, never a broken image.
"""

from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).parent / "img"
OUT = ROOT / "thumbs"
SOURCE_TYPES = {".jpg", ".jpeg", ".png", ".webp"}

# directory -> (mode, size). "square" crops to a square of that side,
# "fit" scales down to fit within the box, keeping the aspect ratio.
TARGETS = {
    "people": ("square", 160),    # shown at 40-70px
    "projects": ("fit", (720, 720)),  # project cards are ~350px wide
    "posts": ("fit", (240, 180)),  # news thumbnails are 120x90
}
SINGLE_FILES = {
    "naco_banner.jpg": ("fit", (2592, 720)),  # homepage hero, same size
}


def make_thumb(src: Path, dst: Path, mode: str, size) -> bool:
    if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime:
        return False
    im = ImageOps.exif_transpose(Image.open(src))
    im = im.convert("RGBA" if im.mode in ("RGBA", "LA", "P") else "RGB")
    if mode == "square":
        # Bias the crop slightly upwards to keep faces in frame.
        im = ImageOps.fit(im, (size, size), Image.LANCZOS, centering=(0.5, 0.4))
    else:
        im.thumbnail(size, Image.LANCZOS)
    dst.parent.mkdir(parents=True, exist_ok=True)
    im.save(dst, "WEBP", quality=80, method=6)
    return True


def main():
    jobs = []
    for folder, (mode, size) in TARGETS.items():
        for src in sorted((ROOT / folder).iterdir()):
            if src.is_file() and src.suffix.lower() in SOURCE_TYPES:
                jobs.append((src, OUT / folder / (src.name + ".webp"), mode, size))
    for name, (mode, size) in SINGLE_FILES.items():
        jobs.append((ROOT / name, OUT / (name + ".webp"), mode, size))

    made = 0
    before = after = 0
    for src, dst, mode, size in jobs:
        made += make_thumb(src, dst, mode, size)
        before += src.stat().st_size
        after += dst.stat().st_size
    print(f"{made} thumbnails written, {len(jobs) - made} up to date; "
          f"{before / 1e6:.1f} MB of originals -> {after / 1e6:.1f} MB of thumbnails")


if __name__ == "__main__":
    main()
