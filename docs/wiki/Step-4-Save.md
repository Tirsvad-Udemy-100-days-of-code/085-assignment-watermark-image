[Dansk](Step-4-Save-da) · **English** · [Bahasa Malaysia](Step-4-Save-ms)

# Step 4: save the result

The last step adds **Save image**. When a watermark has been added, the button opens a save dialog and writes the marked picture to a new file. This is the assignment function `save_image`. The original file is never overwritten.

## What it looks like

The window with a watermark added and the **Save image** button enabled:

![Step 4: the window ready to save](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-4-save.png)

After saving, the status line names the file:

![Step 4: the picture saved](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-4-saved.png)

## How to try it

```powershell
python -m watermark_image
```

Upload a picture, add a watermark and press **Save image**. Choose a name that ends in `.png`, `.jpg` or `.jpeg`. Choosing the original file again is refused and nothing is written; an unsupported ending or a folder that cannot be written to gives a message, and the marked picture is kept so you can try another name.

## What we gained in this step

- **Ports at both ends.** The picture comes in through the `ImageReader` port and goes out through the `ImageWriter` port. The use case `SaveImage` knows no file format and is tested with a fake writer.
- **Protecting the original.** The rule that the target must not be the original file lives in the domain (`Image.is_source`), compares resolved paths so two spellings of one file are caught, and is tested without touching the disk.
- **Error handling.** Every failure becomes a named error with its cause kept (`raise ... from`), and the view model turns each into a plain message. Nothing is swallowed.
- **JPEG has no transparency.** The adapter flattens the picture onto a solid white background before saving a JPEG; PNG keeps its transparency.
- **The whole path tested.** One test uploads a real file, adds a watermark, saves and reads the result back, and checks that the original file is byte for byte the same.

That is the whole program: upload, mark, save. Back to [Home](Home).
