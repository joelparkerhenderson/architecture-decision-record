# [000] Başlık
*Kolay referans ve kataloglama için her ADR'ye bir numara atayın* \
*NOT: Tüm italik metin ipuçları sağlar ve üretim için kaldırılmalıdır*

## Durum - TASLAK / AKTİF / [000] tarafından KULLANIMDAN KALDIRILDI / [000]'IN YERİNİ ALDI

## Bağlam
*Bu ADR'nin ele almayı amaçladığı sorunu/sorunları ve sorunların neden var olduğunu kısaca açıklayın.*

## Kararlaştırılan Yaklaşım
*Alınmış / alınacak mimari açıdan önemli kararı ayrıntılandırın ve Bağlam bölümünde özetlenen sorunları nasıl ele aldığını açıklayın.*

## Sonuçlar
*Bu kararın sistemin mimari karakteristikleri ve işlevsel gereksinimleri üzerindeki etkisi nedir?*

## Yönetişim
*Bu kararın sonuçları nasıl izlenecek?* \
*Bu karara uyum nasıl sağlanacak?*

## Seçenek Analizi
*Uygulanabilirse, bu belgede alınan karara ulaşmak için gerçekleştirilen herhangi bir değiş tokuş analizini dahil edin veya bağlantı verin.*

### Anahtar
*İsteğe bağlı: Paydaşlara olumlu ve olumsuz değiş tokuşları hızlıca fark etmelerine yardımcı olabilecek görsel yardımcılar sağlayın - örneğin olumlu veya olumsuz ön ekleri olan basit trafik ışığı vurgulamaları.*

<span style="background-color:#4bce97; color:black;">Yeşil</span> arka plan iyi bir uyumu gösterir, <span style="background-color:#f1c232; color:black;">sarı</span> ile kötüleşir, <span style="background-color:#e06666; color:black;">kırmızı</span> en kötü uyumdur. \
\+ olumlu etkili bir yorumu gösterir \
\- olumsuz etkili bir yorumu gösterir

### Üst Düzey Genel Bakış
*Her seçenek problem bağlamına bir bakışta ne kadar iyi uyuyor?*

<table>
  <thead>
    <tr>
      <th>Özet</th>
      <th>Seçenek 1</th>
      <th>Seçenek 2</th>
      <th>Seçenek 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Uygulama Kolaylığı</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Çok kolay
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Zor
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Uzman bilgisi gerektiren büyük uygulama
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Zaman Çizelgeleri</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Çok hızlı
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Oldukça yavaş
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Çok yavaş
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Stratejik Değer</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Stratejik değer yok, tamamen taktiksel
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Müşteri katılım deneyimini biraz iyileştirir
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Yaklaşan birleşme için ideal
        </span>
      </td>
    </tr>
  </tbody>
</table>

### İşlevsel Gereksinimler
*Her potansiyel seçenek istenen işlevsel gereksinimlere ne kadar iyi uyuyor?*

<table>
  <thead>
    <tr>
      <th>Senaryo</th>
      <th><i>Seçenek 1</i></th>
      <th><i>Seçenek 2</i></th>
      <th><i>Seçenek 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Senaryo 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Senaryo 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Senaryo 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*İsteğe bağlı: Bilinen gelecek senaryoları kapsamak için satır / başka bir tablo ekleyin.*

### İşlevsel Olmayan Gereksinimler
*Her potansiyel seçenek istenen mimari karakteristiklere ne kadar iyi uyuyor?
Not: 'Mimari Karakteristikler' daha uygun bir başlık olurdu, ancak bunu iş alanınız için tanıdık dile uyarlayın.*

<table>
  <thead>
    <tr>
      <th>Mimari </br> Karakteristik</th>
      <th><i>Seçenek 1</i></th>
      <th><i>Seçenek 2</i></th>
      <th><i>Seçenek 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Ölçeklenebilirlik</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Performans</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Kullanılabilirlik</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*İsteğe bağlı: İşiniz / ürününüz için geçerli olan mimari karakteristiklerin tanımlarını ekleyin veya bağlantı verin.*
