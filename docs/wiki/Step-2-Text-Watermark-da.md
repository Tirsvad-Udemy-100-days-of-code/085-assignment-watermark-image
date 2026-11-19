[**Dansk**](Step-2-Text-Watermark-da) · [English](Step-2-Text-Watermark) · [Bahasa Malaysia](Step-2-Text-Watermark-ms)

# Trin 2: et tekstvandmærke med placering og synlighed

Dette trin tilføjer kontrolpanelet til højre i vinduet. Du skriver en tekst, vælger størrelse og farve, vælger et af ni steder og sætter synligheden, og eksemplet viser billedet med vandmærket. Det er opgavens funktion `add_watermark`.

## Sådan ser det ud

Et tekstvandmærke med standardplaceringen:

![Trin 2: et tekstvandmærke](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-2-text.png)

Det samme vandmærke flyttet til nederste højre hjørne med større synlighed:

![Trin 2: vandmærket placeret i et hjørne](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-2-placed.png)

## Sådan prøver du det

```powershell
python -m watermark_image
```

Upload et billede, skriv en tekst, tryk på **Add watermark**, og skift placering eller synlighed. En tom tekst, en størrelse under 1 eller en synlighed uden for 0 til 100 afvises, og statuslinjen siger, hvad der er galt; billedet bliver, som det var.

## Hvad vi lærte i dette trin

- **Værdiobjekter, der selv tjekker sig.** `TextWatermark`, `Position` og synligheden afviser en forkert værdi, når de oprettes, så intet forkert vandmærke kan findes i programmet, og reglerne testes uden bibliotek og uden vindue.
- **Alfablanding.** Teksten tegnes på et gennemsigtigt lag, lagets alfa ganges med synligheden, og laget blandes ind på billedet. Sådan kan et vandmærke være svagt uden at være ulæseligt.
- **Originalen ændres aldrig.** Tegneren arbejder på en kopi og giver et nyt `WatermarkedImage` tilbage, så en ny ændring af vandmærket altid starter fra den urørte original.
- **Ni steder ud fra én regel.** Stedet er en enkel opregning; afstanden til kanten er én konstant, og hjørneregnestykket findes ét sted og testes for alle ni steder.
- **En anden port.** `WatermarkRenderer` er en port som `ImageReader`: brugsfaldet testes med en falsk afløser, og Pillow-tegningen testes mod kendte pixels.

Næste: [Trin 3](Step-3-Logo-Watermark-da) tilføjer et logovandmærke.
