[**Dansk**](Step-4-Save-da) · [English](Step-4-Save) · [Bahasa Malaysia](Step-4-Save-ms)

# Trin 4: gem resultatet

Det sidste trin tilføjer **Save image**. Når et vandmærke er tilføjet, åbner knappen en gem-dialog og skriver det mærkede billede til en ny fil. Det er opgavens funktion `save_image`. Originalfilen bliver aldrig overskrevet.

## Sådan ser det ud

Vinduet med et tilføjet vandmærke og knappen **Save image** aktiv:

![Trin 4: vinduet klar til at gemme](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-4-save.png)

Efter gemningen nævner statuslinjen filen:

![Trin 4: billedet gemt](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-4-saved.png)

## Sådan prøver du det

```powershell
python -m watermark_image
```

Upload et billede, tilføj et vandmærke, og tryk på **Save image**. Vælg et navn, der slutter på `.png`, `.jpg` eller `.jpeg`. Vælger du originalfilen igen, afvises det, og intet bliver skrevet; en endelse, der ikke understøttes, eller en mappe, der ikke kan skrives i, giver en besked, og det mærkede billede bevares, så du kan prøve et andet navn.

## Hvad vi lærte i dette trin

- **Porte i begge ender.** Billedet kommer ind gennem `ImageReader`-porten og går ud gennem `ImageWriter`-porten. Brugsfaldet `SaveImage` kender intet filformat og testes med en falsk skriver.
- **Beskyttelse af originalen.** Reglen om, at målet ikke må være originalfilen, ligger i domænet (`Image.is_source`), sammenligner fuldt opløste stier, så to skrivemåder af samme fil fanges, og testes uden at røre disken.
- **Fejlhåndtering.** Hver fejl bliver til en navngiven fejl med årsagen bevaret (`raise ... from`), og visningsmodellen gør hver til en almindelig besked. Intet sluges.
- **JPEG har ingen gennemsigtighed.** Adapteren lægger billedet på en ensfarvet hvid baggrund, før en JPEG gemmes; PNG beholder sin gennemsigtighed.
- **Hele vejen testet.** Én test uploader en rigtig fil, tilføjer et vandmærke, gemmer, læser resultatet tilbage og tjekker, at originalfilen er byte for byte den samme.

Dermed er hele programmet færdigt: upload, mærk, gem. Tilbage til [Hjem](Home-da).
