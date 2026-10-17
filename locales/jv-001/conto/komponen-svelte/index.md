# Cathetan Keputusan Arsitektur (ADR) kanggo Komponen Svelte

<!--

Prompt:

Architecture decision record for Svelte components.

Compare options: SVAR, Carbon, Flowbite, SkeletonUI, MeltUI, SvelteUI, shadcn-svelte

The goal is full features for table, charts, lists, grids, gantt, 

-->

## Konteks

Kita lagi milih pustaka komponen UI Svelte kanggo nyedhiyakake fitur lengkap kanggo:
- **Tabel**
- **Grafik**
- **Dhaptar**
- **Kisi**
- **Grafik Gantt**

Tujuane yaiku milih pustaka sing ngimbangi gampange integrasi, dhukungan fitur lengkap, kinerja, lan kemampuan dijaga jangka dawa. Pilihan sing lagi dipikirake yaiku:

1. **SVAR**
2. **Carbon**
3. **Flowbite**
4. **SkeletonUI**
5. **MeltUI**
6. **SvelteUI**
7. **shadcn-svelte**

## Analisis Pilihan

### 1. **SVAR**
- **Ringkesan**: SVAR yaiku pustaka komponen modern sing sugih fitur kanggo Svelte, kanthi fokus ing sistem desain lan komponen siap enterprise.
- **Kaluwihan**:
  - Komponen lengkap, kalebu tabel, formulir, lan grafik.
  - Pilihan kustomisasi dhuwur kanthi dhukungan tema bawaan.
  - Dhukungan bawaan kanggo aksesibilitas lan responsivitas.
  - Didokumentasi kanthi apik kanthi kontribusi komunitas.
- **Kekurangan**:
  - Mbok menawa luwih abot dibandhingake pustaka sing luwih prasaja.
  - Dhukungan winates kanggo komponen tartamtu kayata grafik Gantt lan kisi canggih.
- **Paling Cocog Kanggo**: Aplikasi tingkat enterprise sing mbutuhake sistem desain lengkap.
- **Dhukungan Tabel/Grafik**: Sedhengan nganti apik.
- **Dhukungan Kisi/Gantt**: Minimal.

### 2. **Carbon**
- **Ringkesan**: Carbon Design System yaiku sistem desain open-source saka IBM, nawakake rangkaian komponen UI sing kuwat.
- **Kaluwihan**:
  - Desain kualitas dhuwur lan rapi kanthi dokumentasi ekstensif.
  - Aksesibel lan responsif banget.
  - Pustaka komponen gedhe, kalebu kisi, tabel, lan kontrol formulir.
- **Kekurangan**:
  - Ora fokus ing Svelte, mula integrasi bisa ngrepotake.
  - Mbok menawa mbutuhake kustomisasi tambahan kanggo kompatibilitas Svelte lengkap.
  - Ora ana dhukungan langsung kanggo komponen canggih kayata grafik Gantt utawa grafik kompleks.
- **Paling Cocog Kanggo**: Proyek skala gedhe sing mbutuhake UI konsisten lan rapi.
- **Dhukungan Tabel/Grafik**: Apik (kanthi integrasi pustaka grafik).
- **Dhukungan Kisi/Gantt**: Apik (dhukungan kisi ana, nanging ora ana grafik Gantt).

### 3. **Flowbite**
- **Ringkesan**: Flowbite yaiku pustaka komponen sing dibangun nganggo Tailwind CSS, nawakake macem-macem komponen lan unsur UI.
- **Kaluwihan**:
  - Adhedhasar Tailwind CSS, sing nggampangake kustomisasi.
  - Gampang diintegrasi lan digunakake karo Svelte.
  - Nyedhiyakake komponen sugih kayata tabel, grafik, lan kontrol UI.
- **Kekurangan**:
  - Kurang fitur canggih (upamane grafik Gantt utawa kisi kompleks).
  - Ora nduwe komponen grafik asli; gumantung marang pustaka njaba.
- **Paling Cocog Kanggo**: Proyek sing mbutuhake pangembangan cepet kanthi fokus ing integrasi Tailwind CSS.
- **Dhukungan Tabel/Grafik**: Apik (mbutuhake integrasi karo pustaka grafik pihak katelu).
- **Dhukungan Kisi/Gantt**: Minimal.

### 4. **SkeletonUI**
- **Ringkesan**: SkeletonUI yaiku pustaka komponen entheng kanggo Svelte, fokus ing kasederhanan lan minimalisme.
- **Kaluwihan**:
  - Entheng lan cepet banget.
  - API prasaja lan intuitif.
  - Apik kanggo proyek cilik utawa ing ngendi kinerja kritis.
- **Kekurangan**:
  - Komponen sing kalebu sithik banget, mula ora sugih fitur.
  - Kurang komponen tabel/kisi/grafik/Gantt canggih.
  - Dhukungan komunitas winates lan dokumentasi kurang lengkap.
- **Paling Cocog Kanggo**: Proyek sing mbutuhake komponen entheng kanthi overhead minimal.
- **Dhukungan Tabel/Grafik**: Minimal.
- **Dhukungan Kisi/Gantt**: Minimal.

### 5. **MeltUI**
- **Ringkesan**: MeltUI yaiku kumpulan komponen UI aksesibel kanggo Svelte, fokus ing kasederhanan lan kemampuan dikomposisi.
- **Kaluwihan**:
  - Entheng lan bisa disesuekake kebak.
  - Fitur aksesibilitas apik langsung saka kothak.
  - Desain modern lan minimalis.
- **Kekurangan**:
  - Kurang sugih fitur dibandhingake pustaka liyane.
  - Kurang komponen kisi lan tabel canggih.
  - Ora ana grafik Gantt utawa pilihan grafik kompleks.
- **Paling Cocog Kanggo**: Desain minimalis sing ngutamakake aksesibilitas lan kinerja.
- **Dhukungan Tabel/Grafik**: Minimal.
- **Dhukungan Kisi/Gantt**: Minimal.

### 6. **SvelteUI**
- **Ringkesan**: SvelteUI yaiku pustaka komponen UI Svelte sing lengkap lan bisa disesuekake, dirancang kanggo mbangun aplikasi web modern kanthi UI elegan.
- **Kaluwihan**:
  - Rangkaian komponen lengkap, kalebu tabel, kisi, grafik, lan formulir.
  - Nyedhiyakake dhukungan mode padhang lan peteng.
  - Bisa disesuekake banget lan gampang ditambah.
  - Integrasi bawaan kanggo pustaka grafik kayata `chart.js` utawa `d3.js`.
- **Kekurangan**:
  - Bisa luwih abot tinimbang pustaka komponen sing luwih prasaja.
  - Mbutuhake sawetara setelan kanggo ngintegrasi pustaka njaba kanggo fitur sing luwih kompleks kayata grafik Gantt.
- **Paling Cocog Kanggo**: Proyek sing mbutuhake rangkaian komponen sing lengkap lan bisa disesuekake.
- **Dhukungan Tabel/Grafik**: Apik banget (pustaka grafik didhukung).
- **Dhukungan Kisi/Gantt**: Apik (komponen kisi ana; Gantt mbutuhake integrasi njaba).

### 7. **shadcn-svelte**
- **Ringkesan**: Versi Svelte saka ShadCN, sing fokus ing desain utility-first lan nyedhiyakake komponen modern sing wis ditata.
- **Kaluwihan**:
  - Desain utility-first, dibangun ing ndhuwur Tailwind CSS, nggampangake kustomisasi.
  - Rangkaian komponen sugih lan wis ditata kebak langsung saka kothak.
  - Gampang diintegrasi karo pustaka liyane.
- **Kekurangan**:
  - Ora selengkap sawetara liyane babagan unsur UI canggih.
  - Kurang dhukungan bawaan kanggo tabel, grafik, utawa kisi.
  - Ora ana dhukungan langsung kanggo grafik Gantt.
- **Paling Cocog Kanggo**: Proyek cilik nganti sedhengan sing mbutuhake pendekatan utility-first lan bisa disesuekake.
- **Dhukungan Tabel/Grafik**: Minimal.
- **Dhukungan Kisi/Gantt**: Minimal.

## Keputusan

### Pilihan sing Disaranake: **SvelteUI**

- **Alasan**: SvelteUI nawakake rangkaian komponen sing lengkap lan seimbang sing nuhoni kabutuhan tabel, grafik, kisi, lan formulir. Dheweke bisa disesuekake banget, terintegrasi apik karo pustaka grafik liyane (kayata `chart.js` lan `d3.js`), lan nduwe imbangan apik antarane kinerja entheng lan kasugihan fitur. Sanajan mbok menawa ora nyedhiyakake dhukungan grafik Gantt langsung saka kothak, bisa gampang ditambah karo integrasi pihak katelu, ndadekake ideal kanggo solusi lengkap lan bisa mundhak.
  
  - **Kaluwihan**:
    - Dhukungan tabel lan grafik apik banget.
    - Komponen kisi lan tata letak lengkap.
    - Bisa disesuekake lan terintegrasi apik karo pustaka grafik njaba.
    - Komunitas lan dokumentasi apik.
  
  - **Kekurangan**:
    - Luwih abot tinimbang sawetara pustaka minimalis liyane.
    - Mbutuhake integrasi njaba kanggo grafik kompleks kayata grafik Gantt.
  
### Alternatif: **Flowbite** utawa **Carbon** (kanggo proyek enterprise sing luwih gedhe)
- Yen dibutuhake sistem desain sing rapi, adhedhasar Tailwind, utawa luwih konsisten, **Flowbite** (karo Tailwind CSS) utawa **Carbon** (kanggo solusi kelas enterprise) bisa dadi alternatif sing cocog. Nanging, mbok menawa mbutuhake upaya tambahan kanggo integrasi karo grafik lan komponen sing luwih kompleks.

## Kesimpulan

Sing paling cocog kanggo kabutuhanmu (fitur lengkap kanggo tabel, grafik, dhaptar, kisi, Gantt) yaiku **SvelteUI**, disusul **Flowbite** lan **Carbon** gumantung kabutuhan proyek lan preferensi desain.
