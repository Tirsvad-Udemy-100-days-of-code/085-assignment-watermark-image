[English](Reflection) · **Dansk** · [Bahasa Malaysia](Reflection-ms)

# Refleksion

Opgaven slutter med en refleksion: hvordan projektet blev grebet an, hvad der var svært og let, og hvad der skal gøres anderledes. Dette er et udkast; Product Owner omskriver det med egne ord.

## Hvordan greb jeg projektet an?

Jeg skrev planen og designet før koden: hvem programmet er til, ét use case (upload, tilføj vandmærke, gem), en domænemodel og et klassediagram. Derefter byggede jeg det i fire trin, én gren og én pull request pr. trin, med et skærmbillede for hvert, så hvert trin kunne kontrolleres for sig.

## Hvad var svært?

- **Tkinter alene er ikke nok.** Det kan ikke læse JPEG-filer eller blande et vandmærke med gennemsigtighed, så Pillow blev den ene afhængighed ved kørsel.
- **At holde vinduet adskilt fra reglerne.** Billedet og vandmærkets regler ligger i lag, der ikke kender Tkinter; vinduet viser dem kun. Det krævede mere omtanke i starten og betalte sig senere.
- **At teste et vindue.** En grafisk test må ikke overtage skrivebordet, så grafiske tests og skærmbilleder kører i en Linux-container med en virtuel skærm.

## Hvad var let?

- At placere et vandmærke på et af ni steder er almindelig regning, når reglen om margen er skrevet ned.
- Vandmærkets regler var lette at teste, fordi de ikke kræver et vindue.

## Hvad var min største læring?

At skrive use casen og kontrakterne først gjorde hvert trin lille og klart. Koden fulgte for det meste designet, og når den ikke gjorde, ændrede jeg designet bevidst og gennemgik det igen.

## Hvad ville jeg gøre anderledes?

- Starte med beslutningen om Pillow, så den første kode, der læser billeder, skrives én gang.
- Tage skærmbillederne fra første trin i stedet for at tilføje værktøjet senere.
- Prøve to vandmærker på samme tid (tekst og logo sammen) og en samling billeder som næste projekt.
