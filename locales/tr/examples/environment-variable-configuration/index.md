# Ortam değişkeni yapılandırması

İçindekiler:

* [Özet](#özet)
  * [Sorun](#sorun)
  * [Karar](#karar)
  * [Durum](#durum)
* [Ayrıntılar](#ayrıntılar)
  * [Varsayımlar](#varsayımlar)
  * [Kısıtlamalar](#kısıtlamalar)
  * [Pozisyonlar](#pozisyonlar)
  * [Argüman](#argüman)
  * [Etkiler](#etkiler)
* [İlgili](#ilgili)
  * [İlgili kararlar](#ilgili-kararlar)
  * [İlgili gereksinimler](#ilgili-gereksinimler)
  * [İlgili eserler](#ilgili-eserler)
  * [İlgili ilkeler](#ilgili-ilkeler)
* [Notlar](#notlar)


## Özet


### Sorun

Uygulamalarımızın, dağıtım ortamına bağlı olarak farklı davranabilmesi için yapıtlar/ikili dosyalar/kaynak kodunun ötesinde yapılandırılabilir olmasını istiyoruz.

  * Bunu başarmak için ortam değişkeni yapılandırmasını kullanmak istiyoruz.

  * Yapılandırmayı sürüm kontrolü yapabileceğimiz dosyaları kullanarak yönetmek istiyoruz.

  * Nelerin yapılandırılabileceği ve ilgili varsayılanlar gibi bazı geliştirici deneyimi ergonomisi sağlamak istiyoruz.


### Karar

İlgili varsayılan dosya ve şema dosyası ile .env dosyalarına karar verildi.


### Durum

Karar verildi. Ortaya çıkan yeni yetenekleri değerlendirmeye açığız.


## Ayrıntılar


### Varsayımlar

Uygulama kodunu ve ortam kodunu ayırmayı tercih ediyoruz. Uygulamanın geliştirme ortamı, test ortamı, demo ortamı, üretim ortamı vb. gibi farklı ortamlarda farklı çalışması gerektiğini varsayıyoruz.

"12 faktörlü uygulama" endüstri uygulamasını ve hatta daha da ilgili olan "15 faktörlü uygulama" uygulamasını tercih ediyoruz.

Önceki projelerimizin çoğu, bir `.env` dosyası veya benzeri `.env` dizini kuralını kullanmıştır. Bunları sürüm kontrolünden uzak tutmak ve bunun yerine bunları dağıtmak, sürümlemek ve yönetmek için başka bir yol kullanmak tipik bir uygulamadır.


### Kısıtlamalar

Gizli bilgileri kaynak kod yönetim (SCM) sürüm kontrol sistemimizden (VCS) uzak tutmak istiyoruz.

Popüler yazılım çerçeveleri ve kütüphaneleriyle uyumluluğu hedeflemek istiyoruz. Örneğin, Node'un ortam değişkeni yapılandırmasını okumak için "dotenv" adlı bir modülü vardır.


### Pozisyonlar

Birkaç yaklaşımı değerlendirdik:

  * Yapılandırmayı `config.js` dosyası gibi uygulamada depolayın.

  * Yapılandırmayı `.env` dosyası gibi ortamda depolayın.

  * Yapılandırmayı lisans sunucusu gibi bilinen bir konumdan alın.


### Argüman

.env dosyası yaklaşımını seçtik çünkü:

  * Uzmanlar da dahil olmak üzere popülerdir.

  * Ekiplerimizin birçok projede defalarca başarıyla kullandığı `.env` dosyaları modelini takip eder.

  * Basittir. Özellikle, bir lisans sunucusu yaklaşımına kıyasla denetim yeteneklerinin eksikliği gibi gördüğümüz önemli ödünleşimlerle şimdilik sorun yaşamıyoruz.


### Etkiler

Ortam değişkeni yapılandırmasını genelden herhangi bir gizli bilgi yönetiminden ayırmanın bir yolunu bulmamız gerekiyor.


## İlgili


### İlgili kararlar

Tüm uygulamalarımızın bu yaklaşımı kullanmasını bekliyoruz.

İkili dosyada veya kaynak kodda sabit kodlama gibi daha az yetenekli bir yaklaşım kullanan uygulamalarımızı yükseltmeyi planlayacağız.

Lisans sunucusu gibi daha yetenekli bir yaklaşım kullanan uygulamalarımızı olduğu gibi tutacağız.


### İlgili gereksinimler

Dosyalar için kancalar, testler ve sürekli entegrasyon dahil olmak üzere devops yetenekleri ekleyeceğiz.

Bu karar hakkında tüm geliştirici ekip arkadaşlarını eğitmemiz gerekiyor.



### İlgili eserler

Dağıttığımız her alanın kendi .env dosyasına ve ilgili dosyalara ihtiyacı olacaktır.


### İlgili ilkeler

Kolayca geri döndürülebilir.


## Notlar


Örnek `.env` dosyası:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Örnek `.env.defaults` dosyası:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Sadece anahtarları içeren örnek `.env.schema` dosyası:

```env
NAME
EMAIL
```