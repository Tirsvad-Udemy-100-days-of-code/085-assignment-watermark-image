[**Dansk**](Step-3-Logo-Watermark-da) · [English](Step-3-Logo-Watermark) · [Bahasa Malaysia](Step-3-Logo-Watermark-ms)

# Trin 3: et logovandmærke

I dette trin kan vandmærket være et lille billede i stedet for en tekst. Vælg **Logo** som vandmærketype, tryk på **Choose logo**, vælg en billedfil, sæt størrelsen som en procent af billedets bredde, og tilføj det med de samme kontroller til sted og synlighed som til teksten.

## Sådan ser det ud

Et logovandmærke lagt over billedet:

![Trin 3: et logovandmærke](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-3-logo.png)

Samme logo flyttet til nederste højre hjørne med større synlighed:

![Trin 3: logoet placeret i et hjørne](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-3-placed.png)

## Sådan prøver du det

```powershell
python -m watermark_image
```

Upload et billede, vælg **Logo**, vælg en logofil (en PNG med gennemsigtig baggrund virker bedst), flyt skyderen for størrelsen, og tryk på **Add watermark**. En logofil, der ikke kan læses, afvises med en besked, og billedet bliver, som det var.

## Hvad vi lærte i dette trin

- **At udvide ved at tilføje en type.** `LogoWatermark` er en ny slags `Watermark` ved siden af `TextWatermark`. De fælles regler (synlighed) blev i grundklassen, og brugsfaldet og tegneren fik én gren hver i stedet for at ændre den eksisterende tekstkode.
- **Genberegning af pixels.** Logoet skaleres med Lanczos-metoden, som holder kanterne bløde, når et stort logo gøres lille.
- **Gennemsigtighed.** Et logo med gennemsigtig baggrund lader billedet skinne igennem, fordi logoets egen alfa bevares og ganges med synligheden.
- **Én placeringsregel.** De ni steder og afstanden til kanten beregnes i én funktion, som både teksten og logoet bruger.
- **At genbruge en port.** Logofilen læses gennem den samme `ImageReader`-port som billedet, så den får samme fejlhåndtering og samme test med en falsk afløser.

Næste: [Trin 4](Step-4-Save-da) gemmer resultatet.
