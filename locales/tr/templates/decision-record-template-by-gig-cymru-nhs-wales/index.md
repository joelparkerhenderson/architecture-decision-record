# {Başlığınız Buraya}

!!! info

    **Durum**: { Önerildi | İnceleniyor | Kabul Edildi | Reddedildi | Yerini Aldı | Kullanımdan Kaldırıldı }

    **Güncellendi**: {YYYY-AA-GG}

## Özet

{Bu, ADR'nizin 'yönetici özeti' veya 'asansör konuşmasıdır'. Birkaç
özlü cümlede (genellikle 2-4), bu ADR'nin ele aldığı temel sorunu, soruyu veya
fırsatı açıkça belirtin. Alınan karara veya odak alanına kısa bir ipucu ekleyin.
Amaç, okuyucuların bu ADR'nin ne hakkında olduğunu hızlıca anlamalarına ve
belgenin tamamını okumaya gerek kalmadan kendileri için uygun olup olmadığına
karar vermelerine yardımcı olmaktır. Bunu teknik bir makalenin özeti veya ana
konuya çok kısa bir giriş olarak düşünün.}

## Etkenler

{Bu bölüm bu kararın neden **şimdi** alındığını açıklar. Bu mimari kararı
gerektiren birincil motivasyonları, ihtiyaçları veya sorunları açıkça
ifade edin. Temel nedenleri ve baskıları düşünün.}

* {örn. ... gerektiren yeni bir özellik/yetenek geliştiriyoruz}

* {örn. Performansı iyileştirmemiz, erişilebilirliği artırmamız, borcu temizlememiz gerekiyor...}

* {örn. Kullanıcılardan gelen geri bildirimler ... öneriyor}

* {örn. Mevcut yaklaşım bu sınırlamaları getiriyor...}

## Seçenekler

{Burada değerlendirdiğiniz farklı seçenekleri listelersiniz. Gerçeklere bağlı kalın
ve görüşlerden kaçının, sonraki bölüm analizi kapsar. Kısa bir açıklama,
ilgili belgelere veya örneklere bağlantılar ekleyin.

Sonuçta seçilmemiş olsalar bile, araştırdığınız tüm önemli alternatifleri dahil edin.
Amaç, değerlendirmeye dalmadan önce okuyuculara her alternatif hakkında açık,
tarafsız bir anlayış sağlamaktır.}

### {Seçenek 1 Başlığı}

{Seçeneği açıklayın, bir özet sağlayın, gerçekleri listeleyin, bağlantılar verin vb.}

### {Seçenek n Başlığı}

...

## Seçenek Analizi

{Burada *Seçenekler* bölümünde sunulan her seçeneği eleştirel olarak
değerlendirirsiniz. Her seçenek için avantajları, dezavantajları ve diğer
ilgili değerlendirmeler veya değiş tokuşların dengeli bir görünümünü sağlayın.
Spesifik olun ve mümkünse noktalarınızı *Etkenler*e geri bağlayın.

Şu gibi yönleri düşünün:

* Maliyet (geliştirme, operasyonel, lisanslama)

* Karmaşıklık (uygulama, bakım, öğrenme eğrisi)

* Riskler (teknik, operasyonel, güvenlik)

* Mimari ilkeler veya mevcut standartlarla uyum

* Performans, ölçeklenebilirlik, kullanılabilirlik, bakım kolaylığı,
    güvenlik vb. üzerindeki etki

Gerektiği kadar Artı/Eksi/Diğer ifadesi ekleyin.
}

### {Seçenek 1 Değerlendirmesi}

* Artı: {Bu seçeneğin belirli bir avantajı veya faydası.}

* Eksi: {Bu seçenekle ilişkili belirli bir dezavantaj, risk veya maliyet.}

* Diğer: {Kesinlikle artı veya eksi olmayan ilgili bir nokta.}

### {Seçenek n Değerlendirmesi}

...

## Öneri

{Burada nihai kararı açıkça belirtir ve seçilen seçeneği açıkça adlandırırsınız.
Bu seçeneğin **neden** seçildiğini ayrıntılı olarak açıklayın. Seçilen seçeneğin
*Etkenler*i en iyi nasıl ele aldığını ve temel gereksinimleri karşıladığını veya
belirtilen sorunu çözdüğünü açıkça ifade etmelisiniz.}

### Sonuçlar

{Bu bölüm **isteğe bağlıdır**.}

{Artık bir karar alındığına göre, hem olumlu hem de olumsuz beklenen sonuçlar ve
etkiler nelerdir? Bu karar alınarak hangi bilinen sınırlamalar, maliyetler veya
riskler kabul ediliyor? Bu karar farklı paydaşları, diğer sistemleri, geliştirme
uygulamalarını, operasyonel prosedürleri veya kullanıcı deneyimini nasıl
etkileyecek?}

* Artı: {Bu karardan beklenen belirli bir olumlu sonuç veya fayda.}

* Eksi: {Bu karardan kaynaklanan belirli bir kabul edilen dezavantaj, maliyet veya risk.}

* Diğer: {Kesinlikle artı veya eksi olmayan bir sonuç.}

### Onay

{Bu bölüm **isteğe bağlıdır**.}

{Bu kararın uygulanmasının nasıl doğrulanacağını ve devam eden uyumun nasıl
sağlanacağını özetleyin. Bu, kararın sadece teorik olmadığını, aktif olarak
uygulamaya konulacağını ve izleneceğini göstermeye yardımcı olur.

Kararın doğru şekilde uygulandığını nasıl kontrol edeceksiniz? (örn. kod
incelemeleri, belirli testler, gösteriler, akran değerlendirmesi).

Bu karara bağlılık zaman içinde nasıl sürdürülecek? (örn. otomatik
kontroller, periyodik denetimler, ekip yönergelerinde güncellemeler, eğitim).

Kararın amaçlanan olumlu sonuçları elde ettiğini gösterecek belirli metrikler
veya göstergeler var mı? (örn. performans kıyaslamaları, benimseme oranları,
belirli hatalarda azalma, kullanıcı geri bildirim puanları).

Bunu denetlemekten kim sorumlu ve karar izlenmezse ne olur?}

## Daha Fazla Bilgi

{Bu bölüm **isteğe bağlıdır**.}

{Bu bölümü, kararı destekleyen, bağlam ekleyen veya gelecekteki eylemleri
yönlendiren ek bilgiler sağlamak için kullanın. Diğer kararlara ve kaynaklara
bağlantılar da burada görünebilir.

Karar alma sürecine kimlerin dahil olduğunu ve uzlaşmaya nasıl/varılıp
varılmadığını kısaca not edebilirsiniz. Ayrıca gelecekte bu kararın yeniden
değerlendirilmesini tetikleyebilecek bir zaman çerçevesi veya belirli olaylar
önermek isteyebilirsiniz.}
