# Mimari Karar Kaydı: CSS çerçevesi

İçindekiler:

- [Özet](#özet)
  - [Sorun](#sorun)
  - [Karar](#karar)
  - [Durum](#durum)
- [Ayrıntılar](#ayrıntılar)
  - [Varsayımlar](#varsayımlar)
  - [Kısıtlamalar](#kısıtlamalar)
  - [Pozisyonlar](#pozisyonlar)
  - [Argüman](#argüman)
  - [Etkiler](#etkiler)
- [İlgili](#ilgili)
  - [İlgili kararlar](#ilgili-kararlar)
  - [İlgili gereksinimler](#ilgili-gereksinimler)
  - [İlgili eserler](#ilgili-eserler)
  - [İlgili ilkeler](#ilgili-ilkeler)
- [Notlar](#notlar)


## Özet


### Sorun

Web uygulamalarımızı oluşturmak için bir CSS çerçevesi kullanmak istiyoruz:

  * Kullanıcı deneyiminin tüm popüler tarayıcılarda ve ekran boyutlarında hızlı ve güvenilir olmasını istiyoruz.

  * Tasarım, düzen, kullanıcı arayüzü/kullanıcı deneyimi vb. konularda hızlı yineleme istiyoruz.

  * Özellikle mobil cihazlardaki gibi daha küçük ekranlar, 4K geniş ekranlardaki gibi daha büyük ekranlar ve döndürülebilir ekranlar gibi dinamik ekranlar için duyarlı uygulamalar istiyoruz.


### Karar

Bulma'ya karar verildi.


### Durum

Bulma'ya karar verildi. Yeni CSS çerçevesi seçenekleri geldikçe onlara açığız.


## Ayrıntılar


### Varsayımlar

Modern, hızlı, güvenilir, duyarlı vb. web uygulamaları oluşturmak istiyoruz.

Tipik modern web uygulamaları, çeşitli nedenlerle jQuery kullanımını azaltıyor/kaldırıyor:

  * Modern JavaScript, jQuery'nin sağladığı birçok yeteneği aşamalı olarak kullanıma sunuyor, bu nedenle jQuery'ye daha az ihtiyaç duyuluyor ve belirli uygulamaları sağlayan daha iyi/daha hızlı/daha küçük modüller var

  * jQuery'nin geniş yaklaşımı, modern JavaScript çerçeveleri (ör. React, Vue, Svelte) için bir anti-desen olan doğrudan DOM manipülasyonu yapmaktır.

  * jQuery, iki kez yüklenirse kendi kendine müdahale eder, vb.


### Kısıtlamalar

jQuery kullanan bir CSS çerçevesi seçersek, jQuery'yi içe aktarmak zorunda kalırız. Örneğin, Semantic UI jQuery kullanır ve Tachyons kullanmaz.

Minimal bir CSS çerçevesi seçersek, şimdi veya yakında isteyebileceğimiz çerçeve bileşenlerinden vazgeçeriz. Örneğin, Semantic UI bir resim karuseli sağlar ve Tachyons sağlamaz.


### Pozisyonlar

Hiçbir çerçeve kullanmamayı düşündük. Bu, özellikle CSS ızgarası projemiz için ihtiyacımız olanın çoğunu sağladığı için hala uygulanabilir görünüyor.

Hızlı bir kısa liste üçlemesi kullanarak birçok CSS çerçevesini değerlendirdik: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons, vb. Daha derinlemesine inceleme için iki seçimimiz Semantic UI (en anlamsal yaklaşıma sahip olduğu için) ve Bulma (istediğimiz bileşenleri sağlayan en hafif yaklaşıma sahip olduğu için).

Semantic UI'yi düşündük. Bu, projemiz için istediğimiz sekmeler, ızgaralar, düğmeler vb. dahil olmak üzere birçok bileşen sağlar. Semantic UI ile iki şekilde bir pilot uygulama yaptık: tipik CDN dosyalarını kullanarak ve NPM depolarını kullanarak. Statik bir HTML sayfasında Semantic UI ile başarı elde ettik, ancak bir JavaScript SPA oluşturmak için zaman kutumuz içinde başarı elde edemedik (öncelikle jQuery yükleme sorunları nedeniyle). Diğer kodlayıcıların, sahip olduğumuz aynı nedenlerle Semantic UI geliştiricilerinden jQuery içermeyen bir sürüm oluşturmalarını istediğini keşfettik. Diğer kodlayıcılar uzun yıllardır jQuery içermeyen bir sürüm talep ediyorlardı, ancak geliştiriciler hayır dedi ve herhangi bir jQuery içermeyen sürümün yazılmasının çok zor olacağını belirtti, örneğin ~"Semantic UI projesinin jQuery kullanan 22.000'den fazla temas noktası var".

Anlamsal örnek:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alfa</a>
  <a class="item">Bravo</a>
</div>
```

Bulma'yı düşündük. Bulma, çok sayıda gelişmiş bileşene sahip olmasa da, Semantic UI'ye benzer birçok yeteneğe sahiptir. Bulma, jQuery'siz gibi modern tekniklerle oluşturulmuştur. Bulma'nın, bazılarını kullanmak isteyebileceğimiz bazı üçüncü taraf bileşenleri vardır.


Bulma ile örnek:
```html
<div class="tabs">
  <ul>
    <li><a>Alfa</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argüman

Yukarıdaki gibi.

Özellikle, Semantic UI, hem teknoloji (yani çok sayıda jQuery temas noktası) hem de liderlik (yani jQuery'siz, bir yol haritası denemek veya sürekli iyileştirme veya bağış toplama vb. yerine kesin bir hayırdı) açısından bir uyarı bayrağına sahip görünüyor.


### Etkiler

İyi bir jQuery olmayan CSS çerçevesi bulursak, bu genellikle genel olarak yararlı ve iyidir.


## İlgili


### İlgili kararlar

Seçtiğimiz CSS çerçevesi test edilebilirliği etkileyebilir.


### İlgili gereksinimler

Tamamen modern bir uygulamayı hızlı bir şekilde göndermek istiyoruz.

Eski çerçeveler (özellikle Semantic UI) üzerinde eski bağımlılıkları (özellikle jQuery) kullanarak zaman harcamak istemiyoruz.


### İlgili eserler

CSS'yi kullanacak tüm tipik HTML'yi etkiler.


### İlgili ilkeler

Kolayca geri döndürülebilir.

Hız ihtiyacı.


## Notlar

Buraya herhangi bir not ekleyin.