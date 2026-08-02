# PetPal — image set

Photography for every component that [`../ui/inventory.md`](../ui/inventory.md) marks
**Requires a photo**. The set is not chosen freshly here — the inventory's photo column
decides which slots exist, and the product's own content decides the subjects.

**These are real supplied photographs**, processed from [`../photos/`](../photos/) by
[`process.py`](process.py). [`generate.py`](generate.py) remains for *adding* to the set
with Nano Banana when a subject has no photograph — its prompt is tuned to match the grade
of what is already here.

---

## What the set has to cover

| Component | Slot | Subject | Covered |
|---|---|---|---|
| Avatar | 22 · 32 · 40 · 64 · 88 · 96px circles | pet **and** person | pets only |
| Arch hero | 88px circle on the arch line | the pet whose card it is | ✅ |
| Pet identity strip | `.pet-photo-s`, 40px | that screen's pet | ✅ |
| Pet toggle | `.pill-avatar`, 22px per pet | one per pet on the account | ✅ Miso + Cheetah |
| Photo upload area | 80px circle, the intake | the pet being added | ✅ |
| Recipient info block | `.recipient-avatar`, 40px | the person holding the link | ❌ **no photo** |
| Contact row | `.contact-avatar`, 32px | vet or emergency contact | ❌ **no photo** |
| Document card | `.doc-thumb`, 48px | a document scan | ❌ **no photo** |

**Three slots have no image.** The two person slots keep their initials (`TS` for Tierklinik
am Stadtpark); the document thumbnail keeps its photo ground. A pet photograph in an owner
or vet avatar would be a content mismatch, so those slots stay empty rather than borrow.
Six portraits and a document set would close it.

---

## The files

512×512 JPEG, quality 82, progressive, EXIF stripped. Square because every slot is a circle
or a rounded square; 512 because the largest use is a 120px tile at 2× and there is no
reason to ship more.

### Dogs

| File | Subject | Background hue | Where it appears |
|---|---|---|---|
| `pet-dog-miso.jpg` | Red-and-white shepherd type, facing camera | 56° warm | **The hero pet** — 146 references. Arch hero, pet toggle, avatar. |
| `pet-dog-1.jpg` | Black-and-white collie type | 53° warm | Generic slots, avatar sizes. |
| `pet-dog-2.jpg` | Black-and-tan shepherd type | 84° green | Generic slots. |

### Cats

| File | Subject | Background hue | Where it appears |
|---|---|---|---|
| `pet-cat-cheetah.jpg` | Brown mackerel tabby | **212° cool** ⚠ | The account's second pet — pet toggle, her own card. |
| `pet-cat-1.jpg` | Bengal-marked tabby on solid amber | **38° — the palette** | Avatar sizes. The best on-palette image in the set. |
| `pet-cat-2.jpg` | Dark short-haired cat | 42° warm | Avatar ring demo. |
| `pet-cat-3.jpg` | Grey tabby against a teal door | 129° green | Available, not currently placed. |

Signal amber is hue **45°**, so 38–56° is the family the palette lives in.
**`pet-cat-cheetah.jpg` is the one outlier** — a saturated blue sky at 212°, directly
opposite the amber. It is Cheetah's actual photograph and the wireframes name her 13 times,
so it stays; but on an amber band it is the one image that argues with the palette. A
warmer photograph of the same cat would resolve it.

---

## How these were processed

```bash
python3 visuals/process.py          # photos/ → visuals/
```

Each source is EXIF-rotated, converted to RGB, cropped square around a **per-image focal
point**, resized to 512 and saved at quality 82. The focal point matters: most of the
originals are portrait orientation with the animal's head in the upper third, so a plain
centre crop decapitates them. The fractions live in `process.py` and were set by looking at
each photograph inside the circular avatar mask.

17 MB of camera originals → 245 KB in the kit.

---

## Adding an image that matches

Keep this paragraph verbatim — it is what makes a later image look like the same shoot.
It is already the treatment inside `generate.py`.

> Photographed in **soft, warm daylight at roughly 5400K**, from a single window to one
> side. Colour is **warm-neutral**: highlights lean gently gold, shadows stay warm grey and
> **never drift blue, teal or green**. Blacks are slightly lifted for a calm, matte finish —
> no crushed contrast, no HDR, no vignette, no filter look. Natural, unstyled, quietly
> documentary. Shallow depth of field with the subject fully sharp. Square 1:1, subject
> centred and well clear of the edges. No text, no logos, no watermarks.

**Why this temperature.** [`../DESIGN.md`](../DESIGN.md) commits to a white canvas, near-black
ink and exactly one saturated hue — signal amber `#ffbf00`. A cool photograph fights that
amber every time the two meet on the arch. 5400K daylight with gold-leaning highlights sits
in the same family, so band and photograph read as one surface. Lifted blacks match the
system's calm register — the same reason `--ink` is `#141414` and not pure black.

For portraits, add: *head-and-shoulders against a flat solid background, relaxed natural
expression, everyday clothing in muted tones, no props.* Use palette colours for the
ground — `#fdf3d3` (`--signal-tint`), `#f4f4f4` (`--surface`), `#eaeaea` (`--photo-ground`) —
so a face sits on any product surface.

```bash
export GEMINI_API_KEY=…                     # https://aistudio.google.com/apikey
python3 visuals/generate.py owner-eva       # one subject
```
