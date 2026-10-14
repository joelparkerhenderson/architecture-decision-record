# Arkitekturbeslutningspost: snake_case eller camelCase til et REST-API?

Beslutning: navngivningskonventionen snake_case bruges til REST-API-endpoints

Status: Accepteret

## Kontekst

I navngivningskonventioner for REST-API'er er der to populære formater: snake_case og camelCase. I snake_case adskilles hvert ord i navnet af understregninger, mens i camelCase er det første ord i navnet med små bogstaver, og de efterfølgende ord har deres første bogstav med stort. Denne beslutning afgør, hvilken navngivningskonvention der skal bruges til et REST-API.

## Beslutningsdrivkræfter

- Konsistens med eksisterende navngivningskonventioner i projektet

- Læsbarhed og klarhed for alle, der måtte arbejde på API'et

- Overensstemmelse med branchens best practices for navngivningskonventioner til REST-API'er

- Nem implementering og vedligeholdelse

## Beslutning

Navngivningskonventionen snake_case bruges til REST-API-endpoints. Dette valg drives af følgende faktorer:

1. **Konsistens**: projektet bruger allerede navngivningskonventionen snake_case til alle endpoints, og det ville være gavnligt at bevare denne konvention for at sikre konsistens i hele projektet.

2. **Læsbarhed og klarhed**: konventionen snake_case er mere læsbar og lettere at forstå. Understregningerne giver en tydelig adskillelse mellem ord, hvilket gør det lettere at tolke og forstå navnets betydning.

3. **Overensstemmelse med branchens best practices**: konventionen snake_case er meget udbredt i branchen og betragtes som en best practice for REST-API'er, hvilket gør den til et godt valg til projektet.

4. **Nem implementering og vedligeholdelse**: at fastholde den eksisterende navngivningskonvention er lettere at implementere og vedligeholde, da al eksisterende kode og dokumentation skulle opdateres, hvis der blev valgt en ny konvention.

## Konsekvenser

Der er potentielle konsekvenser af denne beslutning. 

* Hvis nye teammedlemmer, der slutter sig til projektet, ikke er fortrolige med navngivningskonventionen snake_case, kan det føre til forvirring og fejl i udviklingen. Da snake_case er en meget brugt konvention, er en sådan risiko dog minimal. 
  
* Hvis der bruges andre værktøjer eller frameworks i projektet, som i høj grad bygger på konventionen camelCase, kan det kræve ekstra indsats at konvertere mellem navngivningskonventioner. Det er dog ikke en væsentlig bekymring, da projektet er standardiseret på konventionen snake_case. 
 
Samlet set resulterer beslutningen om at bruge navngivningskonventionen snake_case til REST-API-endpoints i en konsistent, læsbar og branchestandard tilgang, der samtidig er nem at implementere og vedligeholde.

<h6>Kildehenvisning: Denne side er genereret af ChatGPT og derefter redigeret for klarhed og format.</h6>
