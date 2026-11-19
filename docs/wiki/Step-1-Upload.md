[Dansk](Step-1-Upload-da) · **English** · [Bahasa Malaysia](Step-1-Upload-ms)

# Step 1: the window and the image upload

In this step the program gets a window with an **Upload image** button and a preview area. You choose a JPEG, PNG, BMP, GIF or WebP file and the picture is shown, scaled to fit. This is the assignment function `upload_image`.

## What it looks like

The window when the program starts, with nothing loaded:

![Step 1: the empty window](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-1-empty.png)

The window after an image is uploaded:

![Step 1: the window with an uploaded image](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-1-loaded.png)

## How to try it

```powershell
python -m watermark_image
```

Press **Upload image**, choose a picture file and watch the preview and the status line. If you choose a file that is not a picture, the status line says so and the earlier picture stays.

## What we gained in this step

- **A layered design.** The code is split into `domain`, `application`, `infrastructure` and `presentation`. The rules never import Tkinter or Pillow, so they can be tested without a window and without a file.
- **A port with a fake.** The use case `UploadImage` asks an `ImageReader` port to read a picture. In the tests a small fake reader stands in, so the use case is tested in microseconds; `PillowImageReader` is tested separately against real files.
- **A view that holds no rule.** The window only draws and forwards clicks. The view model decides what the status line says, so the behaviour is tested without opening a window.
- **Why Pillow.** Tkinter alone cannot read JPEG files, so Pillow reads the file and converts it to plain RGBA bytes that the rest of the program uses.
- **A graphical test that never takes your mouse.** The screenshots above were made in a Linux container with a virtual display, not on the desktop.

Next: [Step 2](Step-2-Text-Watermark) adds a text watermark.
