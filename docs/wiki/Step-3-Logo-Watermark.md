[Dansk](Step-3-Logo-Watermark-da) · **English** · [Bahasa Malaysia](Step-3-Logo-Watermark-ms)

# Step 3: a logo watermark

This step lets the watermark be a small picture instead of a text. Choose **Logo** as the watermark type, press **Choose logo**, pick a picture file, set its size as a percentage of the picture width and add it with the same place and opacity controls as the text.

## What it looks like

A logo watermark laid over the picture:

![Step 3: a logo watermark](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-3-logo.png)

The same logo moved to the bottom right corner with a stronger opacity:

![Step 3: the logo placed in a corner](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-3-placed.png)

## How to try it

```powershell
python -m watermark_image
```

Upload a picture, choose **Logo**, choose a logo file (a PNG with a transparent background works best), move the scale slider and press **Add watermark**. A logo file that cannot be read is refused with a message, and the picture stays as it was.

## What we gained in this step

- **Extending by adding a type.** `LogoWatermark` is a new kind of `Watermark` next to `TextWatermark`. The shared rules (opacity) stayed in the base class, and the use case and the renderer gained one branch each instead of changing the existing text code.
- **Resampling.** The logo is scaled with Lanczos resampling, which keeps edges smooth when a large logo is made small.
- **Transparency.** A logo with a transparent background lets the picture show through, because the logo's own alpha is kept and multiplied by the opacity.
- **One placement rule.** The nine places and the margin are computed in one function that the text and the logo both use.
- **Reusing a port.** The logo file is read through the same `ImageReader` port as the picture, so it gets the same error handling and the same tests with a fake.

Next: [Step 4](Step-4-Save) saves the result.
