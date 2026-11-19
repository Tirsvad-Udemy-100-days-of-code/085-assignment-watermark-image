# Wireframe: Watermark an image

The wireframe of the main window of use case UC-001. The Product Owner gave no wireframe, so this is the first edition, built from the use case. It changes only on input from the Product Owner or from the use case; the code follows it.

## Layout

```text
+--------------------------------------------------------------+
| Watermark Image                                      [_][x]  |
+--------------------------------------------------------------+
| [ Upload image ]  [ Save image ]                             |
+------------------------------------------+-------------------+
|                                          | Watermark type    |
|                                          |  (o) Text ( ) Logo|
|                                          | Text: [_________] |
|            Preview area                  | Size:  [ 48 ]     |
|        (picture scaled to fit)           | Colour:[#ffffff]  |
|                                          | Logo:  [Choose..] |
|                                          | Scale: [--o----]  |
|                                          | Place: [7][8][9]  |
|                                          |        [4][5][6]  |
|                                          |        [1][2][3]  |
|                                          | Opacity:[---o---] |
|                                          | [ Add watermark ] |
+------------------------------------------+-------------------+
| Status: message line                                         |
+--------------------------------------------------------------+
```

The button `Choose..` reads "Choose logo" and the chosen file name is shown beside it. The logo controls and the text controls are shown together in step 3; in step 2 only the text controls exist. The place buttons are the nine places of the use case; the selected one is highlighted.

## States

| State | Preview area | Controls | Status line |
| --- | --- | --- | --- |
| Empty | blank | Upload enabled; Save and watermark controls disabled | "Upload an image to begin" |
| Picture loaded | the picture, scaled to fit | Watermark controls enabled; Save disabled | "Loaded <file name>" |
| Text watermark | the picture with the text | Add watermark and Save enabled | "Text watermark added" |
| Logo watermark | the picture with the logo | Add watermark and Save enabled | "Logo watermark added" |
| Saved | unchanged | all enabled | "Saved <file name>" |
| Error | unchanged | unchanged | the reason, for example "Not a readable image" |
