# Arkitektúrákvörðunarskrá fyrir Google Cloud Platform

## Samhengi

Google Cloud Platform (GCP) er áberandi skýjatölvuvettvangur sem býður upp á ýmsa skýjaþjónustu, þar á meðal lausnir fyrir tölvuvinnslu, geymslu og netkerfi. Þessi ADR miðar að því að skjalfesta arkitektúrákvarðanir sem teknar voru við þróun og innleiðingu GCP-byggðra innviða fyrir stofnun okkar.

## Ákvörðun

Stofnun okkar hefur ákveðið að nota Google Cloud Platform sem skýjainnviði fyrir forrit okkar. Helstu sjónarmið að baki þessari ákvörðun eru:

   - Hagkvæmni

   - Stigstærð

   - Áreiðanleiki

   - Sveigjanleiki

## Val

Eftirfarandi þjónustur frá GCP hafa verið valdar til að mæta kröfum okkar:

   - Compute Engine fyrir sýndarvélar og tölvuauðlindir

   - Cloud Storage fyrir hlutageymslu og skráahýsingu

   - Cloud SQL fyrir stýrða gagnagrunnsþjónustu

   - Firebase fyrir forritaþróun og hýsingu

## Rökstuðningur

   - Hagkvæmni: Google Cloud Platform er mjög hagkvæmt miðað við aðra skýjavettvanga, sem gerir það að aðlaðandi kosti fyrir stofnanir með takmarkað fjármagn.

   - Stigstærð: Auðstækkanlegir innviðir GCP gera kleift að meðhöndla hvaða umferð sem er í rauntíma.

   - Áreiðanleiki: Stýrðar þjónustur GCP bjóða upp á mikinn áreiðanleika, með sjálfvirkum afritum og getu til endurheimtar eftir hamfarir sem tryggja mikið aðgengi að auðlindum og gögnum.

   - Sveigjanleiki: Vettvangurinn býður upp á ýmis verkfæri og þjónustur á ólíkum sviðum eins og gervigreind, gagnagreiningu og IoT, sem gerir hann mjög fjölhæfan.

## Afleiðingar

Flutningur yfir á Google Cloud Platform mun krefjast þess að teymi okkar séu þjálfuð í GCP-þjónustum, að forritið sé endurhannað til að vera samhæft við valdar þjónustur og að innviðakóði sé uppfærður til að styðja GCP-þjónustur. Hins vegar er búist við að þegar flutningi er lokið munum við hafa mjög stigstæra, áreiðanlega og hagkvæma innviði fyrir hýsingu forrits okkar. Einnig þurfum við að stýra viðvarandi kostnaði við að útvega auðlindir á GCP.

## Niðurstaða

Google Cloud Platform er frábær kostur fyrir skýjainnviði okkar vegna hagkvæmni, stigstærðar, áreiðanleika og sveigjanleika. Með því að nýta valdar þjónustur getum við veitt mjög aðgengilega og öfluga innviði fyrir forrit okkar.
