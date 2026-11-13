"""Shrink rendered event banners (256-colour PNG, about 3x smaller, no visible change).

    python img/events/src/compress.py img/events/*.png
"""
import sys
from PIL import Image

for path in sys.argv[1:]:
    im = Image.open(path)
    if im.mode == "P":
        continue  # already compressed
    im.convert("RGB").quantize(256, method=Image.Quantize.MEDIANCUT,
                               dither=Image.Dither.FLOYDSTEINBERG).save(path, optimize=True)
