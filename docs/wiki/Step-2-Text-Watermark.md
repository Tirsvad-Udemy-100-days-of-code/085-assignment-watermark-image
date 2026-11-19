[Dansk](Step-2-Text-Watermark-da) · **English** · [Bahasa Malaysia](Step-2-Text-Watermark-ms)

# Step 2: a text watermark with place and opacity

This step adds the control panel on the right of the window. You type a text, choose its size and colour, pick one of nine places and set the opacity, and the preview shows the picture with the watermark. This is the assignment function `add_watermark`.

## What it looks like

A text watermark added with the default place:

![Step 2: a text watermark](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-2-text.png)

The same watermark moved to the bottom right corner with a stronger opacity:

![Step 2: the watermark placed in a corner](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-2-placed.png)

## How to try it

```powershell
python -m watermark_image
```

Upload a picture, type a text, press **Add watermark** and change the place or the opacity. An empty text, a size below 1 or an opacity outside 0 to 100 is refused and the status line says what is wrong; the picture stays as it was.

## What we gained in this step

- **Value objects that validate themselves.** `TextWatermark`, `Position` and the opacity refuse a wrong value when they are created, so no wrong watermark can exist anywhere in the program and the rules are tested with no library and no window.
- **Alpha blending.** The text is drawn on a transparent layer, the layer's alpha is multiplied by the opacity, and the layer is blended onto the picture. This is how a watermark can be faint without being unreadable.
- **The original is never changed.** The renderer works on a copy and returns a new `WatermarkedImage`, so changing the watermark again always starts from the untouched original.
- **Nine places from one rule.** The place is a plain enum; the margin from the edge is one constant, and the corner arithmetic lives in one function that is tested for all nine places.
- **A second port.** `WatermarkRenderer` is a port like `ImageReader`: the use case is tested with a fake, and the Pillow drawing is tested against known pixels.

Next: [Step 3](Step-3-Logo-Watermark) adds a logo watermark.
