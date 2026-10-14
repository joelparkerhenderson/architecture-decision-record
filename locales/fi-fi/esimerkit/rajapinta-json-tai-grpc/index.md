# Arkkitehtuuripäätöstietue: rajapinta JSON:lla vai gRPC:llä

## Tila

Hyväksytty

## Konteksti

Suunnittelemme rajapintaa uudelle palvelulle, jota useat asiakkaat käyttävät. Olemme harkinneet kahta vaihtoehtoa rajapinnan toteuttamiseksi: JSON HTTP:n yli tai gRPC.

JSON HTTP:n yli on laajasti käytetty lähestymistapa rajapintojen rakentamiseen, ja monet ohjelmointikielet ja kehykset tukevat sitä. Tämä lähestymistapa on yksinkertainen, kevyt ja helposti ymmärrettävä, mikä tekee siitä hyvän valinnan monille projekteille. Se voi kuitenkin olla vähemmän tehokas kuin muut vaihtoehdot, erityisesti suurten tietomäärien käsittelyssä.

gRPC puolestaan on uudempi teknologia, joka tarjoaa tehokkaamman tavan rakentaa rajapintoja. Se käyttää binääristä serialisointia tiedon siirtoon, mikä voi olla nopeampaa ja tiiviimpää kuin JSON:n käyttö. gRPC tukee myös kaksisuuntaista suoratoistoa, mikä tekee siitä hyvän valinnan reaaliaikaisille sovelluksille.

## Päätös

Molempien vaihtoehtojen hyvät ja huonot puolet harkittuamme olemme päättäneet käyttää gRPC:tä rajapinnassamme. Vaikka JSON HTTP:n yli on yksinkertaisempi vaihtoehto, uskomme, että gRPC tarjoaa tehokkaamman ja skaalautuvamman ratkaisun palvelullemme. Odotamme myös, että rajapintamme käsittelee suuren määrän dataa, ja gRPC:n binäärinen serialisointi on tehokkaampaa tähän käyttötapaukseen.

Lisäksi uskomme, että gRPC:n tuki kaksisuuntaiselle suoratoistolle hyödyttää reaaliaikaisia sovelluksia, joita voimme kehittää tulevaisuudessa.

## Seuraukset

Valitsemalla gRPC:n joudumme käyttämään erilaisia työkaluja ja kirjastoja rajapintamme rakentamiseen verrattuna JSON:n käyttöön HTTP:n yli. Tämä voi vaatia lisäaikaa ja -vaivaa näiden teknologioiden oppimiseen ja toteuttamiseen. Lisäksi asiakkaiden, jotka haluavat käyttää rajapintaamme, on käytettävä gRPC-yhteensopivia kirjastoja, joita ei välttämättä tueta yhtä laajasti kuin JSON HTTP:n yli -kirjastoja.

Uskomme kuitenkin, että gRPC:n käytön hyödyt ovat näitä mahdollisia haittoja suuremmat, ja olemme varmoja, että tämä päätös johtaa tehokkaampaan ja skaalautuvampaan rajapintaan.
