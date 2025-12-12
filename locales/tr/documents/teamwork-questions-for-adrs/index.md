### ADR'yi kim oluşturabilir?

Belirli kişiler, belirli roller, belirli ekipler veya belirli departmanlar gibi alanları göz önünde bulundurun; ayrıca bir ADR'yi görevlendirebilecek, yani başka birinin yazacağı bir tane talep eden kişiler, roller, ekipler veya departman olup olmadığını da göz önünde bulundurun.

Örnek cevap: Kuruluşumuzda mimari karar kaydı README sayfasını okuyan herhangi bir kişi bir ADR önerebilir, yani kişi onu yazmaya başlayabilir ve ekiple paylaşabilir.

### ADR'yi gündeme getirmeyi ne haklı çıkarır?

Kuruluşunuzun ekip çalışma şekilleri, yazılım sistem yapınız, ekipler arası koordinasyon, uzun vadeli sürdürülebilirlik, harici arayüzler, kimden faydalanmak istediğiniz ve benzeri alanları göz önünde bulundurun.

Örnek cevap: Gelecekteki geliştiricilerin yaptıklarımızın “nedenini” anlamasını istediğimizde bir ADR oluşturmak istiyoruz.

### ADR'yi yükseltmemeyi ne haklı çıkarır?

Mimari ile ilgili olmayan veya minimum riskli veya kendi kendine yeten veya tek geliştirici gibi küçük olan veya standartlar veya politikalar veya belgeler gibi başka bir yerde zaten tamamen kapsanan veya geçici çözümler veya kavram kanıtları veya deneyler gibi geçici olan kararlar gibi alanları göz önünde bulundurun.

Örnek cevap: Bir kararın kapsam, zaman, risk ve maliyet açısından sınırlı olduğu veya başka bir yerde zaten kapsandığı durumlarda bir ADR'yi atlamak istiyoruz.

### ADR'nin yaşam döngüsü nedir?

Oluşturma süreci, araştırma süreci, karar verme süreci, uygulama süreci ve kullanımdan kaldırma süreci gibi alanları göz önünde bulundurun. ADR'yi bir durumdan diğerine nasıl taşıyacağınız ve bunu paydaşlara nasıl ileteceğiniz gibi ADR yaşam döngüsünü zaman içinde nasıl izleyeceğinizi düşünün.

Örnek cevap: Bir ADR'nin beş yaşam döngüsü aşamasına sahip olmasını istiyoruz: Başlatma → Araştırma → Değerlendirme → Uygulama → Sürdürme → Kullanımdan Kaldırma.

### ADR'nin yaşam döngüsü adımları için kriterler nelerdir?

Bir ADR için kabul kriterleri gibi alanları göz önünde bulundurun, yani bir yaşam döngüsü adımından diğerine geçmek için yeterince iyi olduğunu nasıl anlarsınız? Sorun açıkça ifade edilmiş mi? Alternatifler düşünüldü mü? Ödünleşimler yeterince anlaşılıp belgelendi mi?
Tüm ilgili bağlam yerinde mi? İlgili tüm paydaşlar dahil mi? Tüm geri bildirimler dahil edildi mi?

Örnek cevap: Aktif ekip 1) araştırmalarını tamamladığında, 2) değerlendirmelerini tamamladığında, 3) ADR teklifini yorum talebi ve bir haftalık bir zaman kutusu ile paydaşlara yayınladığında, 4) tüm paydaş yorumları dahil edilip ele alındığında paydaşlar tarafından bir ADR'ye oy verilmesini istiyoruz.

### Hangi roller ve sorumluluklar bir ADR ile etkileşime girer?

Teklif sahibi, araştırmacı, değerlendirici, gözden geçiren, onaylayan, sürdüren ve benzeri rolleri göz önünde bulundurun. Paydaşlarla iletişim, beklentilerin karşılandığından emin olma, web sitesinde veya intranette paylaşma, çalışmayı periyodik olarak ve özellikle ilgili değişiklikler olduğunda gözden geçirme gibi sorumlulukları göz önünde bulundurun.

Örnek cevap: Her ADR'nin her zaman bir birincil irtibat kişisi, ikincil irtibat kişisi ve sorumlu ekibe sahip olmasını istiyoruz; bunlar iletişim, yayınlar, bakım, yılda en az bir kez periyodik inceleme ve gerektiğinde nihai kullanımdan kaldırmadan sorumludur.

### Yönetişim bir ADR ile nasıl etkileşime girer?

Kuruluşunuzun çalışma şekilleri, yasal yönler veya insan kaynakları yönleri gibi özel uyumluluk ihtiyaçları, fikir birliği, çatışma ve tırmanmayı nasıl ele almak istediğiniz gibi alanları göz önünde bulundurun. Bir ADR ile ilgili olarak, onu onaylayabilme, oy kullanabilme veya veto edebilme gibi diğerlerinden daha fazla etkiye sahip olabilecek alanlar, kişiler veya ekipler var mı?

Örnek cevap: Bir ADR'nin yönetişimi şu öncelik sırasındadır: CEO, CTO, CLO, bir ADR'yi uygulayan ekip, ADD hakkında en bilgili olan ekipteki uzmanlar. ADR'de açıklanmadığı sürece başka hiç kimsenin yönetişimi yoktur.

### Hangi ilkeler bir ADR ile etkileşime girer?

Kuruluşunuzun hızlı hareket etme ve yavaş hareket etme, karar birliği ve karar çatışması, risk tercihleri ve güvenlik tercihleri, halka açık tartışma ve özel tartışma ve benzerlerini içeren çalışma şekilleri gibi alanları göz önünde bulundurun.

Örnek cevap: Eylem için önyargı, aynı fikirde olmama ve taahhüt etme, kolayca geri döndürülebilir, kolayca izole edilebilir kararlar için %70 tahminlerin yeterince iyi olduğu ve kuruluşumuzun gizlilik sözleşmesinde açıklanan gizli bilgiler haricinde halka açık çalışma şekilleri gibi liderlik ilkelerini kullanıyoruz.