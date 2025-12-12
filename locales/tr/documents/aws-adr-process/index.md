# AWS Mimari Karar Kayıtları Süreci

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Bir mimari karar kaydı (ADR), ekibin oluşturmayı planladığı yazılım mimarisinin önemli bir yönü hakkında yaptığı bir seçimi açıklayan bir belgedir. Her ADR, mimari kararı, bağlamını ve sonuçlarını açıklar. ADR'lerin durumları vardır ve bu nedenle bir yaşam döngüsünü takip ederler. Bir ADR örneği için eke bakın.

ADR süreci, mimari karar kayıtlarından oluşan bir koleksiyon oluşturur. Bu koleksiyon, karar günlüğünü oluşturur. Karar günlüğü, proje bağlamının yanı sıra ayrıntılı uygulama ve tasarım bilgileri sağlar. Proje üyeleri, proje bağlamına genel bir bakış elde etmek için her ADR'nin başlıklarını gözden geçirir. Proje uygulamalarına ve tasarım seçeneklerine derinlemesine dalmak için ADR'leri okurlar.

Ekip bir ADR'yi kabul ettiğinde, ADR değişmez hale gelir. Yeni bilgiler farklı bir karar gerektiriyorsa, ekip yeni bir ADR önerir. Ekip yeni ADR'yi kabul ettiğinde, önceki ADR'nin yerini alır.

## ADR sürecinin kapsamı

Proje üyeleri, yazılım projesini veya ürününü etkileyen mimari açıdan önemli her karar için bir ADR oluşturmalıdır, buna aşağıdakiler dahildir (Richards ve Ford 2020):

* Yapı (örneğin, mikro hizmetler gibi desenler)

* İşlevsel olmayan gereksinimler (güvenlik, yüksek kullanılabilirlik ve hata toleransı)

* Bağımlılıklar (bileşenlerin bağlanması)

* Arayüzler (API'ler ve yayınlanmış sözleşmeler)

* İnşaat teknikleri (kütüphaneler, çerçeveler, araçlar ve süreçler)

* İşlevsel ve işlevsel olmayan gereksinimler, ADR sürecine en yaygın girdilerdir.


## ADR içeriği

Ekip bir ADR ihtiyacını belirlediğinde, bir ekip üyesi proje çapında bir şablona göre ADR'yi yazmaya başlar. (Örnek şablonlar için ADR GitHub kuruluşuna bakın.) Şablon, ADR oluşturmayı basitleştirir ve ADR'nin ilgili tüm bilgileri yakalamasını sağlar. Her ADR, en azından kararın bağlamını, kararın kendisini ve kararın proje ve çıktıları üzerindeki sonuçlarını tanımlamalıdır. (Bu bölümlerin örnekleri için eke bakın.) ADR yapısının en güçlü yönlerinden biri, ekibin kararı nasıl uyguladığından ziyade kararın nedenine odaklanmasıdır. Ekibin kararı neden verdiğini anlamak, diğer ekip üyelerinin kararı benimsemesini kolaylaştırır ve karar verme sürecine dahil olmayan diğer mimarların gelecekte bu kararı geçersiz kılmasını önler.


## ADR benimseme süreci

Her ekip üyesi bir ADR oluşturabilir, ancak ekip bir ADR için bir sahiplik tanımı oluşturmalıdır. Bir ADR'nin sahibi olan her yazar, ADR içeriğini aktif olarak sürdürmeli ve iletmelidir. Bu sahipliği netleştirmek için bu kılavuz, aşağıdaki bölümlerde ADR yazarlarını ADR sahipleri olarak adlandırır. Diğer ekip üyeleri her zaman bir ADR'ye katkıda bulunabilir. Bir ADR'nin içeriği ekip ADR'yi kabul etmeden önce değişirse, mal sahibi bu değişiklikleri onaylamalıdır.

Ekip bir mimari kararı ve sahibini belirledikten sonra, ADR sahibi sürecin başında **Önerilen** durumunda ADR'yi sağlar. Önerilen durumdaki ADR'ler incelemeye hazırdır.

ADR sahibi daha sonra ADR için inceleme sürecini başlatır. ADR inceleme sürecinin amacı, ekibin ADR'yi kabul edip etmediğine, yeniden çalışılması gerektiğine karar verip vermediğine veya ADR'yi reddedip etmediğine karar vermektir. Sahibi de dahil olmak üzere proje ekibi ADR'yi inceler. İnceleme toplantısı, ADR'yi okumak için ayrılmış bir zaman dilimi ile başlamalıdır. Ortalama olarak 10 ila 15 dakika yeterli olacaktır. Bu süre zarfında, her ekip üyesi belgeyi okur ve belirsiz konuları işaretlemek için yorumlar ve sorular ekler. İnceleme aşamasından sonra, ADR sahibi her yorumu okur ve ekiple tartışır.

Ekip ADR'yi iyileştirmek için eylem noktaları bulursa, ADR'nin durumu **Önerilen** olarak kalır. ADR sahibi eylemleri formüle eder ve ekiple işbirliği içinde her eyleme bir atanan ekler. Her ekip üyesi eylem noktalarına katkıda bulunabilir ve bunları çözebilir. İnceleme sürecini yeniden planlamak ADR sahibinin sorumluluğundadır.

Ekip ayrıca ADR'yi reddetmeye de karar verebilir. Bu durumda, ADR sahibi gelecekte aynı konuda tartışmaları önlemek için ret nedenini ekler. Sahip, ADR durumunu **Reddedildi** olarak değiştirir.

Ekip ADR'yi onaylarsa, mal sahibi bir zaman damgası, sürüm ve paydaş listesi ekler. Sahip daha sonra durumu **Kabul Edildi** olarak günceller.

ADR'ler ve oluşturdukları karar günlüğü, ekip tarafından alınan kararları temsil eder ve tüm kararların bir geçmişini sağlar. Ekip, mümkün olan yerlerde kod ve mimari incelemeler sırasında ADR'leri referans olarak kullanır. Kod incelemeleri, tasarım görevleri ve uygulama görevlerini gerçekleştirmenin yanı sıra, ekip üyeleri ürün için stratejik kararlar için ADR'lere danışmalıdır.

İyi bir uygulama olarak, her yazılım değişikliği akran değerlendirmelerinden geçmeli ve en az bir onay gerektirmelidir. Kod incelemesi sırasında, bir kod incelemecisi bir veya daha fazla ADR'yi ihlal eden değişiklikler bulabilir. Bu durumda, incelemeci kod değişikliğinin yazarından kodu güncellemesini ister ve ADR'ye bir bağlantı paylaşır. Yazar kodu güncellediğinde, akran incelemecileri tarafından onaylanır ve ana kod tabanına birleştirilir.


## ADR inceleme süreci

Ekip, ADR'leri kabul ettikten veya reddettikten sonra değişmez belgeler olarak ele almalıdır. Mevcut bir ADR'de değişiklik yapmak, yeni bir ADR oluşturmayı, yeni ADR için bir inceleme süreci oluşturmayı ve ADR'yi onaylamayı gerektirir. Ekip yeni ADR'yi onaylarsa, mal sahibi eski ADR'nin durumunu **Geçersiz Kılındı** olarak değiştirmelidir.
