# Rejestr decyzji architektonicznych dla Google Cloud Platform

## Kontekst

Google Cloud Platform (GCP) to wiodąca platforma przetwarzania w chmurze, która oferuje różne usługi chmurowe, w tym rozwiązania obliczeniowe, magazynowe i sieciowe. Ten ADR ma udokumentować decyzje architektoniczne podjęte w celu opracowania i wdrożenia infrastruktury opartej na GCP dla naszej organizacji.

## Decyzja

Nasza organizacja postanowiła użyć Google Cloud Platform jako infrastruktury chmurowej dla naszej aplikacji. Główne względy tej decyzji to:

   - Opłacalność

   - Skalowalność

   - Niezawodność

   - Elastyczność

## Wybory

Aby spełnić nasze wymagania, wybrano następujące usługi GCP:

   - Compute Engine dla maszyn wirtualnych i zasobów obliczeniowych

   - Cloud Storage dla magazynu obiektów i hostingu plików

   - Cloud SQL dla zarządzanej usługi bazy danych

   - Firebase do tworzenia i hostowania aplikacji

## Uzasadnienie

   - Opłacalność: Google Cloud Platform jest bardzo opłacalna w porównaniu z innymi platformami chmurowymi, co czyni ją atrakcyjną opcją dla organizacji z ograniczeniami budżetowymi.

   - Skalowalność: Łatwo skalowalna infrastruktura GCP pozwala obsłużyć dowolną ilość ruchu w czasie rzeczywistym.

   - Niezawodność: Zarządzane usługi GCP oferują wysoką niezawodność, z automatycznymi kopiami zapasowymi i możliwościami odtwarzania po awarii, które zapewniają wysoką dostępność zasobów i danych.

   - Elastyczność: Platforma udostępnia różne narzędzia i usługi w różnych dziedzinach, takich jak AI, analityka danych i IoT, co czyni ją bardzo wszechstronną.

## Konsekwencje

Migracja do Google Cloud Platform będzie wymagała przeszkolenia naszych zespołów w zakresie usług GCP, przeprojektowania aplikacji tak, by była zgodna z wybranymi usługami, oraz aktualizacji kodu infrastruktury w celu obsługi usług GCP. Oczekuje się jednak, że po zakończeniu migracji będziemy mieć wysoce skalowalną, niezawodną i opłacalną infrastrukturę do hostowania naszej aplikacji. Będziemy też musieli zarządzać bieżącymi kosztami udostępniania zasobów w GCP.

## Podsumowanie

Google Cloud Platform to doskonały wybór dla naszej infrastruktury chmurowej ze względu na opłacalność, skalowalność, niezawodność i elastyczność. Korzystając z wybranych usług, możemy zapewnić wysoce dostępną i solidną infrastrukturę dla naszej aplikacji.
