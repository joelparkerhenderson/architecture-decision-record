# Architectuurbeslissingsdocument voor Google Cloud Platform

## Context

Google Cloud Platform (GCP) is een prominent cloudcomputingplatform dat verschillende clouddiensten biedt, waaronder oplossingen voor computing, opslag en netwerken. Deze ADR heeft als doel de architectuurbeslissingen te documenteren die zijn genomen voor het ontwikkelen en implementeren van een op GCP gebaseerde infrastructuur voor onze organisatie.

## Beslissing

Onze organisatie heeft besloten Google Cloud Platform te gebruiken als cloudinfrastructuur voor onze applicatie. De belangrijkste overwegingen voor deze beslissing zijn:

   - Kosteneffectiviteit

   - Schaalbaarheid

   - Betrouwbaarheid

   - Flexibiliteit

## Keuzes

De volgende diensten van GCP zijn geselecteerd om aan onze eisen te voldoen:

   - Compute Engine voor virtuele machines en rekenbronnen

   - Cloud Storage voor objectopslag en bestandshosting

   - Cloud SQL voor beheerde databaseservice

   - Firebase voor appontwikkeling en hosting

## Onderbouwing

   - Kosteneffectiviteit: Google Cloud Platform is zeer kosteneffectief vergeleken met andere cloudplatforms, waardoor het een aantrekkelijke optie is voor organisaties met budgetbeperkingen.

   - Schaalbaarheid: de gemakkelijk te schalen infrastructuur van GCP maakt het mogelijk elke hoeveelheid verkeer in realtime te verwerken.

   - Betrouwbaarheid: de beheerde diensten van GCP bieden hoge betrouwbaarheid, met geautomatiseerde back-ups en disaster-recoverymogelijkheden die zorgen voor hoge beschikbaarheid van bronnen en data.

   - Flexibiliteit: het platform biedt verschillende tools en diensten op diverse domeinen zoals AI, data-analyse en IoT, waardoor het zeer veelzijdig is.

## Gevolgen

Migreren naar Google Cloud Platform vereist het trainen van onze teams in GCP-diensten, het herontwerpen van de applicatie zodat die compatibel is met de geselecteerde diensten en het bijwerken van de infrastructuurcode om GCP-diensten te ondersteunen. Verwacht wordt echter dat we, zodra de migratie is voltooid, een zeer schaalbare, betrouwbare en kosteneffectieve infrastructuur hebben voor het hosten van onze applicatie. Ook moeten we de lopende kosten van het provisioneren van bronnen op GCP beheren.

## Conclusie

Google Cloud Platform is een uitstekende keuze voor onze cloudinfrastructuur vanwege de kosteneffectiviteit, schaalbaarheid, betrouwbaarheid en flexibiliteit. Door de geselecteerde diensten te gebruiken, kunnen we een zeer beschikbare en robuuste infrastructuur voor onze applicatie bieden.
