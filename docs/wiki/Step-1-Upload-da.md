[**Dansk**](Step-1-Upload-da) · [English](Step-1-Upload) · [Bahasa Malaysia](Step-1-Upload-ms)

# Trin 1: vinduet og upload af billedet

I dette trin får programmet et vindue med knappen **Upload image** og et eksempelområde. Du vælger en JPEG-, PNG-, BMP-, GIF- eller WebP-fil, og billedet vises, skaleret så det passer. Det er opgavens funktion `upload_image`.

## Sådan ser det ud

Vinduet når programmet starter, uden noget indlæst:

![Trin 1: det tomme vindue](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-1-empty.png)

Vinduet efter et billede er uploadet:

![Trin 1: vinduet med et uploadet billede](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-1-loaded.png)

## Sådan prøver du det

```powershell
python -m watermark_image
```

Tryk på **Upload image**, vælg en billedfil, og se eksemplet og statuslinjen. Vælger du en fil, der ikke er et billede, siger statuslinjen det, og det tidligere billede bliver stående.

## Hvad vi lærte i dette trin

- **Et lagdelt design.** Koden er delt i `domain`, `application`, `infrastructure` og `presentation`. Reglerne importerer aldrig Tkinter eller Pillow, så de kan testes uden vindue og uden fil.
- **En port med en falsk afløser.** Brugsfaldet `UploadImage` beder en `ImageReader`-port om at læse et billede. I testene træder en lille falsk læser i stedet, så brugsfaldet testes på et øjeblik; `PillowImageReader` testes for sig mod rigtige filer.
- **Et vindue uden regler.** Vinduet tegner kun og sender klik videre. Visningsmodellen afgør, hvad statuslinjen siger, så adfærden testes uden at åbne et vindue.
- **Hvorfor Pillow.** Tkinter kan ikke læse JPEG-filer alene, så Pillow læser filen og laver den om til almindelige RGBA-bytes, som resten af programmet bruger.
- **En grafisk test, der aldrig tager din mus.** Skærmbillederne ovenfor er lavet i en Linux-container med en virtuel skærm, ikke på skrivebordet.

Næste: [Trin 2](Home-da) tilføjer et tekstvandmærke.
