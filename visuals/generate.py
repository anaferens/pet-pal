#!/usr/bin/env python3
"""
Generate the PetPal image set with Nano Banana (gemini-2.5-flash-image).

    export GEMINI_API_KEY=…            # https://aistudio.google.com/apikey
    python3 visuals/generate.py                 # every missing image
    python3 visuals/generate.py pet-cat-1       # just one
    python3 visuals/generate.py --force         # regenerate everything
    python3 visuals/generate.py --model gemini-3-pro-image-preview   # Nano Banana Pro

The treatment below is the same paragraph documented in README.md. Keep the two in step:
it is what makes a later image look like it came from the same shoot.

Standard library only — no pip install.
"""
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_MODEL = "gemini-2.5-flash-image"
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

# ---------------------------------------------------------------------------
# The shared treatment. Prepended to every prompt — this is the whole point.
# Temperature is matched to DESIGN.md: a white canvas carrying one amber #ffbf00,
# so the photography sits in the same warm family instead of fighting it.
# ---------------------------------------------------------------------------
TREATMENT = (
    "Photographed in soft, warm daylight at roughly 5400K, from a single window to one "
    "side. Colour is warm-neutral: highlights lean gently gold, shadows stay warm grey "
    "and never drift blue, teal or green. Blacks are slightly lifted for a calm, matte "
    "finish - no crushed contrast, no HDR, no vignette, no filter look, no colour "
    "grading gimmick. Natural, unstyled, quietly documentary. Shallow depth of field "
    "with the subject fully sharp. Square 1:1 composition, subject centred and well "
    "clear of the edges. No text, no logos, no watermarks, no visible brand names."
)

PET_SCENE = (
    "The setting is a real home in daylight, tidy but visibly lived-in: a slightly "
    "rumpled blanket, a worn rug, a toy just out of place, an ordinary sofa or floor. "
    "Not a studio, not a set, not staged perfection. The animal is relaxed and alert, "
    "looking toward the camera or just past it. No costume, no bandana, no branded collar."
)

PORTRAIT_SCENE = (
    "A head-and-shoulders portrait against a flat, solid colour background with no "
    "texture, gradient or shadow falloff. Relaxed, natural expression - a calm "
    "half-smile or none at all, never a broad grin. Everyday clothing in muted tones. "
    "No props, no glasses glare, no hands in frame."
)

# Backgrounds come from the DESIGN.md palette so a portrait can sit on any surface.
TINT, SURFACE, GROUND = "#fdf3d3", "#f4f4f4", "#eaeaea"

PETS = {
    # 3 dogs
    "pet-dog-miso":    "A Border Terrier, female, with a wiry tan-and-black coat, sitting on a living-room rug.",
    "pet-dog-pixel":   "A Welsh Corgi about two years old, standing on a wooden floor.",
    "pet-dog-1":       "A medium-sized mixed-breed dog with a short brown coat, lying on a rug.",
    # 3 cats
    "pet-cat-cheetah": "A brown-grey mackerel tabby cat, female, curled on a sofa arm.",
    "pet-cat-nala":    "A short-haired black-and-white cat sitting on a windowsill.",
    "pet-cat-1":       "A ginger short-haired cat sitting upright on a kitchen chair.",
}

PEOPLE = {
    # 3 pet owners
    "owner-eva":  ("A woman in her early thirties, shoulder-length dark blonde hair.", TINT),
    "owner-maya": ("A woman in her mid twenties, straight black hair.", SURFACE),
    "owner-tom":  ("A man in his early thirties, short brown hair, light stubble.", GROUND),
}


def prompt_for(name: str) -> str:
    if name in PETS:
        return f"{PETS[name]} {PET_SCENE} {TREATMENT}"
    subject, bg = PEOPLE[name]
    return (
        f"{subject} {PORTRAIT_SCENE} The background is a flat solid {bg}. {TREATMENT}"
    )


def generate(name: str, model: str, key: str) -> bytes:
    body = json.dumps({"contents": [{"parts": [{"text": prompt_for(name)}]}]}).encode()
    req = urllib.request.Request(
        ENDPOINT.format(model=model) + "?key=" + key,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            payload = json.load(r)
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")[:400]
        raise SystemExit(f"  ! HTTP {e.code} for {name}\n    {detail}")

    for cand in payload.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            blob = part.get("inlineData") or part.get("inline_data")
            if blob and blob.get("data"):
                return base64.b64decode(blob["data"])
    raise SystemExit(
        f"  ! {name}: no image in the response. Full payload:\n"
        + json.dumps(payload)[:600]
    )


def main() -> None:
    args = [a for a in sys.argv[1:]]
    force = "--force" in args
    args = [a for a in args if a != "--force"]
    model = DEFAULT_MODEL
    if "--model" in args:
        i = args.index("--model")
        model = args[i + 1]
        del args[i : i + 2]

    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        raise SystemExit(
            "GEMINI_API_KEY is not set.\n"
            "  Get one at https://aistudio.google.com/apikey then:\n"
            "    export GEMINI_API_KEY=…"
        )

    all_names = list(PETS) + list(PEOPLE)
    wanted = args or all_names
    unknown = [n for n in wanted if n not in all_names]
    if unknown:
        raise SystemExit(f"Unknown name(s): {', '.join(unknown)}\nKnown: {', '.join(all_names)}")

    made = skipped = 0
    for name in wanted:
        out = HERE / f"{name}.jpg"
        if out.exists() and not force:
            print(f"  · {name}.jpg exists — skipping (use --force to redo)")
            skipped += 1
            continue
        print(f"  → {name}.jpg …", flush=True)
        out.write_bytes(generate(name, model, key))
        print(f"    saved {out.stat().st_size // 1024} KB")
        made += 1

    print(f"\n{made} generated, {skipped} skipped, model={model}")
    if made:
        print("The kit already points at these paths — reload ui/kit.html to see them.")


if __name__ == "__main__":
    main()
