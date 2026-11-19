[English](Setup) · **Dansk** · [Bahasa Malaysia](Setup-ms)

# Opsætning

Denne side viser, hvordan du får projektet til at køre på din egen computer. Du skal bruge Python 3.13 eller nyere.

## Opret miljøet

Opret et lokalt virtuelt miljø med navnet `.venv` i projektmappen, aktivér det, og opgradér pip:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

På Linux og macOS aktiverer du det med `source .venv/bin/activate` i stedet.

## Installér projektet

```powershell
python -m pip install -e ".[dev]"
```

Kommandoen læser `pyproject.toml`. Pillow er den eneste afhængighed ved kørsel; gruppen `dev` tilføjer værktøjerne til test og kontrol.

## Kør testene

```powershell
python -m pytest
```

## Hvad vi fik ud af dette trin

- **Én konfigurationsfil.** `pyproject.toml` indeholder projektets navn, den Python-version det kræver, dets ene afhængighed ved kørsel og indstillingerne for alle værktøjer.
- **Et virtuelt miljø.** `.venv` holder projektets pakker adskilt fra resten af maskinen, så projektet kører ens overalt.
- **Tests fra første dag.** En første test kontrollerer allerede konstanterne, så vanen med at køre `pytest` begynder, før der findes nogen funktion.
- **Konstanter ét sted.** `constants.py` indeholder alle faste værdier, så intet tal gentages i koden.
- **Dokumenteret kildekode.** Doxygen-kommentarer og en `Doxyfile` gør kommentarerne til en manual, man kan bladre i.
- **En kvalitetsport.** `scripts/check.sh` kører test, linter, typekontrol og en sikkerhedsscanning før hver push.
