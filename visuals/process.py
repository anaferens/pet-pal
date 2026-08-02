#!/usr/bin/env python3
"""
photos/ → visuals/  — square, kit-sized, content-named.

    python3 visuals/process.py

Every slot in the kit is a circle or a rounded square, so the crop is baked rather than
left to CSS: it guarantees the framing is right at 22px and at 120px alike.

The focal point is the reason this script exists. Most of the originals are portrait
orientation with the animal's head in the upper third, and a plain centre crop decapitates
them. `fy` is where the head sits as a fraction of image height — 0.5 is dead centre,
lower crops toward the top. The values below were set by inspecting each photograph
inside the circular avatar mask, not guessed.

Requires Pillow.
"""
from pathlib import Path

from PIL import Image, ImageOps

SRC = Path(__file__).resolve().parent.parent / "photos"
OUT = Path(__file__).resolve().parent
SIZE = 512
QUALITY = 82

#        source file            kit name              fx    fy
JOBS = [
    ("dog 1 - miso.jpg",       "pet-dog-miso.jpg",    0.50, 0.50),
    ("dog 2.jpg",              "pet-dog-1.jpg",       0.50, 0.45),
    ("dog 3.jpg",              "pet-dog-2.jpg",       0.50, 0.36),
    ("cat 1 - cheetah.png",    "pet-cat-cheetah.jpg", 0.50, 0.50),
    ("cat 2.jpg",              "pet-cat-1.jpg",       0.50, 0.36),
    ("cat 3.jpg",              "pet-cat-2.jpg",       0.50, 0.50),
    ("cat 4.jpg",              "pet-cat-3.jpg",       0.52, 0.34),
]


def process(src: Path, dst: Path, fx: float, fy: float) -> None:
    im = Image.open(src)
    im = ImageOps.exif_transpose(im)   # honour camera rotation before measuring
    im = im.convert("RGB")             # also flattens the PNG
    w, h = im.size
    side = min(w, h)
    # centre the square on the focal point, clamped inside the frame
    left = max(0, min(w - side, int(w * fx - side / 2)))
    top = max(0, min(h - side, int(h * fy - side / 2)))
    im = im.crop((left, top, left + side, top + side))
    im = im.resize((SIZE, SIZE), Image.LANCZOS)
    # saving without an exif= argument drops the original metadata
    im.save(dst, "JPEG", quality=QUALITY, optimize=True, progressive=True)


def main() -> None:
    missing = [s for s, _, _, _ in JOBS if not (SRC / s).exists()]
    if missing:
        raise SystemExit(f"Not found in {SRC}:\n  " + "\n  ".join(missing))

    for src, dst, fx, fy in JOBS:
        process(SRC / src, OUT / dst, fx, fy)
        kb = (OUT / dst).stat().st_size // 1024
        print(f"  {src:22} → {dst:22} {SIZE}x{SIZE}  {kb} KB")

    before = sum((SRC / s).stat().st_size for s, _, _, _ in JOBS)
    after = sum((OUT / d).stat().st_size for _, d, _, _ in JOBS)
    print(f"\n  {before / 1_048_576:.0f} MB of originals → {after // 1024} KB in the kit")


if __name__ == "__main__":
    main()
