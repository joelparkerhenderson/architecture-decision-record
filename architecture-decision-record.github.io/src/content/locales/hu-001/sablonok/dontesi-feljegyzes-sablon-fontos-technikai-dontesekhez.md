# Döntési feljegyzés sablon Fontos Technikai Döntésekhez (ITD)

Ez a Fontos Technikai Döntések (angolul Important Technical Decisions, ITD) sablonja, amelyet a következő ír le:
[ITDs: a lean ADR for executive technical decision-making at scale - Ignacio Larrañaga](https://ignaciolarranaga.medium.com/itds-a-lean-adr-for-executive-technical-decision-making-at-scale-e18bb3f6a563).

Az ITD-k az ADR-ek célzott továbbfejlesztései, amelyeket a sebességre, az érthetőségre
és a vezetői jóváhagyásra optimalizáltak. Míg az ADR azt dokumentálja, mit döntöttek, az ITD egy
karcsú, döntés-központú artefaktum, amely magát a döntést teszi átvizsgálhatóvá, így
az érdekelt felek gyorsan átfuthatják és könnyen megkérdőjelezhetik. Az ITD-k jól illeszkednek
az olyan technikai döntésekhez, amelyek nem szigorúan architekturálisak, például egy
modell, egy könyvtár vagy egy CI/CD-stratégia kiválasztásához.

Minden ITD-fájlban írja meg ezeket a szakaszokat:

# Cím

Magát a döntést fogalmazza meg, ne a téma leírását.
Például: „A Qwen2.5 1.5B Instruct használata az eszközön történő fordításhoz”.

## A probléma

Egyetlen mondat arról, mit próbálunk megoldani.

## Megfontolt lehetőségek

Az asztalon lévő alternatívák, a kiválasztott lehetőség **félkövérrel**.

## Indoklás

Csak a választáshoz vezető döntő tényezők, nem az összes előny és hátrány
kimerítő listája.

## Megjegyzések

Nem kötelező. Bármilyen további, rögzítésre érdemes háttér, például megszorítások,
feltevések vagy hivatkozások.
