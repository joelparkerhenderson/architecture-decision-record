# arc42 tarafından karar kaydı şablonu

<https://arc42.org/overview>

## 1. Giriş ve Hedefler

Gereksinimlerin kısa açıklaması, itici güçler, gereksinimlerin özeti (veya özet). Ana paydaşlar için en yüksek önceliğe sahip mimari için en önemli üç (maksimum beş) kalite hedefi. Mimari ile ilgili beklentileri olan önemli paydaşların tablosu.

## 1.1 Gereksinimler Genel Bakışı

### İçerik

İşlevsel gereksinimlerin, itici güçlerin, gereksinimlerin özeti (veya özet) kısa açıklaması. (Umarız var olan) gereksinim belgelerine bağlantılar ve nerede bulunacağı bilgisi.

### Motivasyon

Son kullanıcıların bakış açısından, bir sistem bir iş faaliyetini desteklemeyi iyileştirmek ve/veya kaliteyi artırmak için oluşturulur veya değiştirilir.

### Biçim

Kısa metinsel açıklama, muhtemelen tablo kullanım durumu formatında. Gereksinim belgeleri varsa, bu genel bakış bu belgelere başvurmalıdır.

Bu alıntıları mümkün olduğunca kısa tutun. Bu belgenin okunabilirliğini gereksinim belgeleriyle olası fazlalıkla dengeleyin.

## 1.2 Kalite hedefleri

### İçerik

Ana paydaşlar için en yüksek öneme sahip mimari için en önemli üç (maksimum beş) kalite hedefi. Mimari için gerçekten kalite hedeflerini kastediyoruz. Bunları proje hedefleriyle karıştırmayın. Bunlar mutlaka aynı değildir. ISO 25010 standardı ilgi çekici olası konuların güzel bir genel bakışını sağlar.

### Motivasyon

En önemli paydaşlarınızın kalite hedeflerini bilmelisiniz, çünkü bunlar temel mimari kararları etkileyecektir. Bu kaliteler hakkında çok somut olduğunuzdan emin olun, moda sözcüklerden kaçının. Bir mimar olarak işinizin kalitesinin nasıl değerlendirileceğini bilmiyorsanız …

### Biçim

En önemli kalite hedeflerini ve somut senaryoları içeren, önceliklere göre sıralanmış bir tablo.

## 1.3 Paydaş

### İçerik

Sistemin paydaşlarının açık genel bakışı, yani tüm kişiler, roller veya kuruluşlar:

- mimariyi bilmeli

- mimariye ikna edilmeli

- mimari veya kodla çalışmak zorunda

- işleri için mimari belgelerine ihtiyaç duyar

- sistem veya geliştirilmesi hakkında kararlar almak zorunda

### Motivasyon

Sistemin geliştirilmesinde yer alan veya sistemden etkilenen tüm tarafları bilmelisiniz. Aksi takdirde, geliştirme sürecinde daha sonra kötü sürprizlerle karşılaşabilirsiniz. Bu paydaşlar çalışmanızın ve sonuçlarının kapsamını ve ayrıntı düzeyini belirler.

### Biçim

Rol adları, kişi adları ve mimari ve belgeleriyle ilgili beklentileri içeren tablo.

## 2. Kısıtlamalar

Tasarım ve uygulama kararlarında veya ilgili süreçlerle ilgili kararlarda ekipleri kısıtlayan her şey. Bazen bireysel sistemlerin ötesine geçebilir ve tüm kuruluşlar ve şirketler için geçerli olabilir.

### İçerik

Yazılım mimarlarını tasarım ve uygulama kararlarında veya geliştirme süreci hakkındaki kararlarda özgürlüklerinde kısıtlayan herhangi bir gereksinim. Bu kısıtlamalar bazen bireysel sistemlerin ötesine geçer ve tüm kuruluşlar ve şirketler için geçerlidir.

### Motivasyon

Mimarlar, tasarım kararlarında nerede özgür olduklarını ve nerede kısıtlamalara uymaları gerektiğini tam olarak bilmelidir. Kısıtlamalarla her zaman uğraşılmalıdır; yine de pazarlığa açık olabilirler.

### Biçim

Açıklamalarla basit kısıtlama tabloları. Gerekirse bunları teknik kısıtlamalar, organizasyonel ve politik kısıtlamalar ve kurallar (örn. programlama veya sürümleme yönergeleri, belgeleme veya adlandırma kuralları) olarak alt bölümlere ayırabilirsiniz.

## 3. Bağlam ve Kapsam

Sisteminizi (harici) iletişim ortaklarından (komşu sistemler ve kullanıcılar) sınırlar. Harici arayüzleri belirtir. İş/alan perspektifinden (her zaman) veya teknik perspektiften (isteğe bağlı) gösterilir.

### İçerik

Sistem kapsamı ve bağlamı - adından da anlaşılacağı gibi - sisteminizi (yani kapsamınız) tüm iletişim ortaklarından (komşu sistemler ve kullanıcılar, yani sisteminizin bağlamı) sınırlar. Böylece harici arayüzleri belirtir.

Gerekirse, iş bağlamını (alana özgü girdiler ve çıktılar) teknik bağlamdan (kanallar, protokoller, donanım) ayırt edin.

### Motivasyon

İletişim ortaklarına alan arayüzleri ve teknik arayüzler sisteminizin en kritik yönleri arasındadır. Bunları tamamen anladığınızdan emin olun.

### Biçim

- Çeşitli bağlam diyagramları

- İletişim ortaklarının ve arayüzlerinin listeleri.

## 3.1 İş bağlamı

### İçerik

Alana özgü girdiler ve çıktılar veya arayüzlerin açıklamalarıyla tüm iletişim ortaklarının (kullanıcılar, BT sistemleri, …) belirtimi. İsteğe bağlı olarak alana özgü formatlar veya iletişim protokolleri ekleyebilirsiniz.

### Motivasyon

Tüm paydaşlar, sistemin çevresiyle hangi verilerin değiş tokuş edildiğini anlamalıdır.

### Biçim

Sistemi kara kutu olarak gösteren ve iletişim ortaklarına alan arayüzlerini belirten her türlü diyagram.

Alternatif olarak (veya ek olarak) bir tablo kullanabilirsiniz. Tablonun başlığı sisteminizin adıdır, üç sütun iletişim ortağının adını, girdileri ve çıktıları içerir.

## 3.2 Teknik bağlam

### İçerik

Sisteminizi çevresine bağlayan teknik arayüzler (kanallar ve iletim ortamları). Ek olarak, alana özgü girdi/çıktının kanallara eşlenmesi, yani hangi I/O'nun hangi kanalı kullandığının açıklaması.

### Motivasyon

Birçok paydaş, sistem ve bağlamı arasındaki teknik arayüzlere dayalı mimari kararlar alır. Özellikle altyapı veya donanım tasarımcıları bu teknik arayüzlere karar verir.

### Biçim

Örneğin, komşu sistemlere kanalları açıklayan UML dağıtım diyagramı, kanallar ve girdi/çıktı arasındaki ilişkileri gösteren bir eşleme tablosuyla birlikte.

## 4. Çözüm Stratejisi

Mimariyi şekillendiren temel kararların ve çözüm stratejilerinin özeti. Teknoloji, üst düzey ayrıştırma, en önemli kalite hedeflerine ulaşma yaklaşımları ve ilgili organizasyonel kararları içerebilir.

### İçerik

Sistemin mimarisini şekillendiren temel kararların ve çözüm stratejilerinin kısa bir özeti ve açıklaması. Bunlar şunları içerir:

- teknoloji kararları

- sistemin üst düzey ayrıştırılması hakkındaki kararlar, örn. mimari kalıp veya tasarım kalıbı kullanımı

- temel kalite hedeflerine nasıl ulaşılacağına dair kararlar

- ilgili organizasyonel kararlar, örn. bir geliştirme süreci seçmek veya belirli görevleri üçüncü taraflara devretmek.

### Motivasyon

Bu kararlar mimariniz için temel taşlarını oluşturur. Birçok diğer ayrıntılı karar veya uygulama kuralı için temeldir.

### Biçim

Bu temel kararların açıklamasını kısa tutun.

Problem tanımınıza, kalite hedeflerinize ve temel kısıtlamalara dayanarak neye karar verdiğinizi ve neden bu şekilde karar verdiğinizi motive edin. Aşağıdaki bölümlerdeki ayrıntılara bakın (yapısal ayrıntılar için bölüm 5, kesişen kavramlar için bölüm 8).

Çözüm yaklaşımlarının bir listesini veya bir tablo kullanabilirsiniz.

## 5. Yapı Taşı Görünümü

Sistemin statik ayrıştırması, kaynak kodun soyutlamaları, uygun ayrıntı düzeyine kadar beyaz kutuların (siyah kutular içeren) hiyerarşisi olarak gösterilir.

### İçerik

Yapı taşı görünümü, sistemin yapı taşlarına (modüller, bileşenler, alt sistemler, sınıflar, arayüzler, paketler, kütüphaneler, çerçeveler, katmanlar, bölümler, seviyeler, fonksiyonlar, makrolar, işlemler, veri yapıları, …) statik ayrıştırmasını ve bunların bağımlılıklarını (ilişkiler, ilişkilendirmeler, …) gösterir.

Bu görünüm her mimari belgeleme için zorunludur. Bir ev analojisinde bu kat planıdır.

### Motivasyon

Yapısını soyutlama yoluyla anlaşılır hale getirerek kaynak kodunuzun genel bakışını koruyun.

Bu, paydaşlarınızla uygulama ayrıntılarını açıklamadan soyut bir düzeyde iletişim kurmanıza olanak tanır.

### Biçim

Yapı taşı görünümü, siyah kutuların ve beyaz kutuların (aşağıdaki şekle bakın) ve açıklamalarının hiyerarşik bir koleksiyonudur.

## 5.1 Beyaz Kutu Genel Sistem

Burada, aşağıdaki beyaz kutu şablonunu kullanarak genel sistemin ayrıştırmasını açıklarsınız. Şunları içerir:

- bir genel bakış diyagramı

- ayrıştırma için bir motivasyon

- içerilen yapı taşlarının siyah kutu açıklamaları. Bunlar için alternatifler sunuyoruz:

  - tüm içerilen yapı taşlarının ve arayüzlerinin kısa ve pragmatik bir genel bakışı için bir tablo kullanın

  - siyah kutu şablonuna göre yapı taşlarının siyah kutu açıklamalarının bir listesini kullanın (aşağıya bakın). Araç seçiminize bağlı olarak bu liste alt bölümler (metin dosyalarında), alt sayfalar (Wiki'de) veya iç içe öğeler (modelleme aracında) olabilir.

  - (isteğe bağlı:) bir yapı taşının siyah kutu şablonlarında açıklanmayan, ancak beyaz kutuyu anlamak için çok önemli olan önemli arayüzler.

Arayüzleri belirtmenin pek çok yolu olduğundan, onlar için belirli bir şablon sağlamıyoruz.

En iyi durumda örnekler veya basit imzalarla yetineceksiniz.

## 5.2 Seviye 2

Burada, seviye 1'den (bazı) yapı taşlarının iç yapısını beyaz kutular olarak belirtebilirsiniz.

Sisteminizin hangi yapı taşlarının böyle ayrıntılı bir açıklamayı haklı kılacak kadar önemli olduğuna karar vermelisiniz. Lütfen tamlık yerine alaka düzeyini tercih edin. Önemli, şaşırtıcı, riskli, karmaşık veya değişken yapı taşlarını belirtin. Sisteminizin normal, basit, sıkıcı veya standartlaştırılmış kısımlarını atlayın.

### 5.2.1 Yapı taşı 1 için Beyaz Kutu

Yapı taşı 1'in iç yapısını belirtir.

Beyaz kutu şablonunu kullanın (yukarıya bakın).

## 6. Çalışma Zamanı Görünümü

Önemli kullanım durumlarını veya özellikleri, kritik harici arayüzlerdeki etkileşimleri, işletim ve yönetim artı hata ve istisna davranışını kapsayan senaryolar olarak yapı taşlarının davranışı.

### İçerik

Çalışma zamanı görünümü, sistemin yapı taşlarının somut davranışını ve etkileşimlerini aşağıdaki alanlardan senaryolar şeklinde açıklar:

- önemli kullanım durumları veya özellikler: yapı taşları bunları nasıl yürütür?

- kritik harici arayüzlerdeki etkileşimler: yapı taşları kullanıcılar ve komşu sistemlerle nasıl işbirliği yapar?

- işletim ve yönetim: başlatma, başlangıç, durdurma

- hata ve istisna senaryoları

Not: Olası senaryoların (diziler, iş akışları) seçimi için ana kriter mimari alaka düzeyleridir. Çok sayıda senaryo tanımlamak önemli değildir. Bunun yerine temsili bir seçim belgelemelisiniz.

### Motivasyon

Sisteminizdeki yapı taşlarının (örneklerinin) çalışma zamanında işlerini nasıl yaptığını ve nasıl iletişim kurduğunu anlamalısınız. Mimarinizi statik modelleri (yapı taşı görünümü, dağıtım görünümü) okumaya ve anlamaya daha az istekli veya yetenekli paydaşlara iletmek için belgelerinizde esas olarak senaryoları yakalayacaksınız.

### Biçim

Senaryoları tanımlamak için birçok gösterim vardır, örn.

- adımların numaralandırılmış listesi (doğal dilde)

- aktivite diyagramları veya akış şemaları

- sıra diyagramları

- BPMN veya EPC'ler (olay süreç zincirleri)

- durum makineleri

- vb.

## 6.n Çalışma Zamanı Senaryosu n (1, 2, 3, vb.)

Senaryonun çalışma zamanı diyagramını veya metinsel açıklamasını ekleyin.

Bu diyagramda gösterilen yapı taşı örnekleri arasındaki etkileşimlerin dikkat çekici yönlerinin açıklamasını ekleyin.

## 7. Dağıtım Görünümü

Ortamlar, bilgisayarlar, işlemciler, topolojilerle teknik altyapı. (Yazılım) yapı taşlarının altyapı öğelerine eşlenmesi.

### İçerik

Dağıtım görünümü şunları açıklar:

- sisteminizi yürütmek için kullanılan teknik altyapı, coğrafi konumlar, ortamlar, bilgisayarlar, işlemciler, kanallar ve ağ topolojileri gibi altyapı öğeleri ve diğer altyapı öğeleri ile

- (yazılım) yapı taşlarının bu altyapı öğelerine eşlenmesi.

Sistemler genellikle farklı ortamlarda yürütülür, örn. geliştirme ortamı, test ortamı, üretim ortamı. Bu gibi durumlarda tüm ilgili ortamları belgelemelisiniz.

Özellikle yazılımınız birden fazla bilgisayar, işlemci, sunucu veya konteyner ile dağıtılmış bir sistem olarak yürütüldüğünde veya kendi donanım işlemcilerinizi ve çiplerinizi tasarlayıp oluşturduğunuzda dağıtım görünümünü belgeleyin.

Yazılım perspektifinden, altyapının yapı taşlarınızın dağıtımını göstermek için gereken öğelerini yakalamak yeterlidir. Donanım mimarları bunun ötesine geçebilir ve ihtiyaç duydukları herhangi bir ayrıntı düzeyinde altyapıyı tanımlayabilir.

### Motivasyon

Yazılım donanım olmadan çalışmaz. Bu temel altyapı sisteminizi ve/veya bazı kesişen kavramları etkileyebilir ve etkileyecektir. Bu nedenle, altyapıyı bilmeniz gerekir.

### Biçim

Belki en üst düzey dağıtım diyagramı zaten bölüm 3.2'de kendi altyapınızla TEK bir siyah kutu olarak teknik bağlam olarak yer almaktadır. Bu bölümde ek dağıtım diyagramları kullanarak bu siyah kutuya yakınlaşacaksınız.

- UML bu görünümü ifade etmek için dağıtım diyagramları sunar. Altyapınız daha karmaşıksa, muhtemelen iç içe diyagramlarla kullanın.

- (Donanım) paydaşlarınız UML dağıtım diyagramı yerine diğer tür diyagramları tercih ediyorsa, altyapının düğümlerini ve kanallarını gösterebilen herhangi bir türü kullanmalarına izin verin.

## 7.1 Altyapı Seviyesi 1

Açıklayın (genellikle diyagramlar, tablolar ve metin kombinasyonunda):

- sisteminizin birden çok konuma, ortama, bilgisayara, işlemciye dağılımı, vb. ve aralarındaki fiziksel bağlantılar

- bu dağıtım yapısı için önemli gerekçe veya motivasyon

- altyapının kalite ve/veya performans özellikleri

- yazılım eserlerinin (yapı taşları) altyapı öğelerine eşlenmesi

Birden fazla ortam veya alternatif dağıtımlar için lütfen arc42'nin bu bölümünü tüm ilgili ortamlar için kopyalayın. **

## 7.2 Altyapı Seviyesi 2

Burada altyapı seviyesi 1'den (bazı) altyapı öğelerinin iç yapısını ekleyebilirsiniz.

Lütfen her seçili öğe için seviye 1'den yapıyı kopyalayın.

## 8. Kesişen Kavramlar

Sistemin birden çok bölümünde (→ kesişen) ilgili genel, temel düzenlemeler ve çözüm yaklaşımları. Kavramlar genellikle birden çok yapı taşıyla ilişkilidir. Alan modelleri, mimari kalıplar ve stiller, belirli teknoloji kullanım kuralları ve uygulama kuralları gibi farklı konuları içerir.

### İçerik

Bu bölüm kesişen kavramları (uygulamalar, kalıplar, düzenlemeler veya çözüm fikirleri) açıklar. Bu tür kavramlar genellikle birden çok yapı taşıyla ilişkilidir. Birçok farklı konu içerebilirler.

### Motivasyon

Kavramlar, mimarinin kavramsal bütünlüğü (tutarlılık, homojenlik) için temel oluşturur. Bu nedenle, sisteminizin iç niteliklerine ulaşmak için önemli bir katkıdır.

Bu, bu tür kavramların uyumlu bir belirtimi için şablonda sağladığımız yerdir.

Bu kavramların çoğu yapı taşlarınızdan birkaçını etkiler veya birkaçıyla ilişkilidir.

### Biçim

Biçim değişebilir:

- herhangi bir yapıya sahip kavram belgeleri

- özellikle teknik kavramlar için örnek uygulamalar

- mimari görünümlerin gösterimlerini kullanan kesişen model alıntıları veya senaryolar

### Bu bölümün yapısı

Sisteminiz için yalnızca en çok ihtiyaç duyulan konuları seçin ve bu bölümde her birine seviye-2 başlığı atayın (örn. 8.1, 8.2 vb).

- Yukarıda belirtilen diyagramın tüm konularını kapsamaya ÇALIŞMAYIN.

### Arka Plan

Sistemlerdeki bazı konular genellikle birden çok yapı taşı, donanım öğesi veya geliştirme sürecini ilgilendirir. Bu tür kesişen konuları, bunları ilgili yapı taşları, donanım öğeleri veya geliştirme süreçlerinin açıklamasında tekrarlamak yerine merkezi bir konumda iletmek veya belgelemek daha kolay olabilir.

Belirli kavramlar bir sistemin tüm öğelerini ilgilendirebilir, diğerleri yalnızca birkaçıyla ilgili olabilir.

## 9. Mimari Kararlar

Gerekçeler dahil önemli, pahalı, kritik, büyük ölçekli veya riskli mimari kararlar.

### İçerik

Gerekçeler dahil önemli, pahalı, büyük ölçekli veya riskli mimari kararlar. "Kararlar" ile verilen kriterlere dayalı bir alternatif seçmeyi kastediyoruz.

Bir mimari kararın burada bu merkezi bölümde mi yoksa yerel olarak mı (örn. bir yapı taşının beyaz kutu şablonunda) belgelenmesi gerektiğine karar vermek için yargınızı kullanın. Tekrarlanan metinlerden kaçının. Mimarinizin en önemli kararlarını zaten yakaladığınız bölüm 4'e bakın.

### Motivasyon

Sisteminizin paydaşları kararlarınızı anlayabilmeli ve takip edebilmelidir.

### Biçim

- Her önemli karar için ADR (mimari karar kaydı)

- önem ve sonuçlara göre sıralanmış liste veya tablo veya

- karar başına ayrı bölümler şeklinde daha ayrıntılı

### Arka Plan (ADR'ler hakkında)

Daha küçük belgeleme parçalarının okunması, oluşturulması ve bakımı daha kolaydır. Mimari kararlar söz konusu olduğunda, geliştirme ekipleri genellikle:

- kararı bilecektir, örn. kaynak kodunda görünür olduğu için, ama

- bu kararın arkasındaki motivasyonu kaçıracaktır (bkz. Nygard 2011)

Bu nedenle, birkaç önemli kararı motivasyonları ve gerekçeleriyle birlikte belgelemelisiniz.

### Kararlar hakkındaki önerimiz

Yapı, kalite karakteristikleri, önemli (özellikle harici) bağımlılıklar ve arayüzler veya yapım tekniklerini etkileyen mimari açıdan önemli kararların bir koleksiyonunu tutun (bu öneri için Michael Nygard'a teşekkürler).

## 10. Kalite Gereksinimleri

Üst düzey genel bakış sağlamak için kalite ağacıyla birlikte senaryolar olarak kalite gereksinimleri. En önemli kalite hedefleri bölüm 1.2'de (kalite hedefleri) açıklanmış olmalıdır.

### İçerik

Bu bölüm tüm ilgili kalite gereksinimlerini içerir.

Bu gereksinimlerin en önemlileri zaten bölüm 1.2'de (kalite hedefleri) açıklanmıştır, bu nedenle burada yalnızca atıfta bulunulmalıdır. Bu bölüm 10'da ayrıca tam olarak başarılamadığında yüksek riskler oluşturmayacak daha az öneme sahip kalite gereksinimlerini de yakalamalısınız (ancak olması güzel olabilir).

### Motivasyon

Kalite gereksinimleri mimari kararları çok etkileyeceğinden, paydaşlarınız için hangi niteliklerin gerçekten önemli olduğunu spesifik ve ölçülebilir bir şekilde bilmelisiniz.

### Daha Fazla Bilgi

https://quality.arc42.org adresindeki kapsamlı Q42 kalite modeline bakın.

## 10.1 Kalite Gereksinimleri Genel Bakışı

### İçerik

Kalite gereksinimlerinin bir genel bakışı veya özeti.

### Motivasyon

Genellikle düzinelerce (hatta yüzlerce) ayrıntılı kalite gereksinimle karşılaşırız. Bu genel bakış bölümünde, örneğin kategorileri veya konuları (ISO 25010:2023 veya Q42 tarafından önerildiği gibi) açıklayarak özetlemeye çalışmalısınız.

Bu özet açıklamalar zaten yeterince kesin, spesifik ve ölçülebilirse, bölüm 10.2'yi atlayabilirsiniz.

### Biçim

Her satırın bir kategori veya konu ve kalite gereksiniminin kısa bir açıklamasını içerdiği basit bir tablo kullanın. Alternatif olarak, bu kalite gereksinimlerini yapılandırmak için bir zihin haritası kullanabilirsiniz.

Literatürde, genel "kalite" terimini kök olarak koyan ve "kalite" teriminin ağaç benzeri bir iyileştirmesini kullanan kalite nitelik ağacı fikri de tanımlanmıştır. [Bass+21] bu amaç için "Kalite Niteliği Fayda Ağacı" terimini tanıttı.

## 10.2 Kalite Senaryoları

### İçerik

Kalite senaryoları kalite gereksinimlerini somutlaştırır ve bunların yerine getirilip getirilmediğine (kabul kriterleri anlamında) karar vermeye izin verir. Senaryolarınızın spesifik ve ölçülebilir olduğundan emin olun.

İki tür senaryo özellikle yararlıdır:

- Kullanım senaryoları (uygulama senaryoları veya kullanım durumu senaryoları olarak da adlandırılır), sistemin belirli bir uyarana çalışma zamanı tepkisini tanımlar. Bu ayrıca sistemin verimliliğini veya performansını tanımlayan senaryoları da içerir. Örnek: Sistem, bir kullanıcının isteğine bir saniye içinde tepki verir.

- Değişiklik senaryoları, sistemin veya yakın çevresinin bir değişikliğinin veya uzantısının istenen etkisini tanımlar. Örnek: Ek işlevsellik uygulanır veya bir kalite niteliği için gereksinimler değişir ve değişikliğin çabası veya süresi ölçülür.

### Biçim

Ayrıntılı senaryolar için tipik bilgiler şunları içerir:

Kısa biçimde (Q42 modelinde tercih edilir):

- Bağlam/Arka Plan: Ne tür bir sistem veya bileşen, ortam veya durum nedir?

- Kaynak/Uyaran: Kim veya ne bir davranışı, tepkiyi veya eylemi başlatır veya tetikler.

- Metrik/Kabul Kriterleri: Bir ölçüm veya metrik içeren bir yanıt

Senaryoların uzun biçimi (SEI ve [Bass+21] tarafından tercih edilir) daha ayrıntılıdır ve aşağıdaki bilgileri içerir:

- Senaryo Kimliği: Senaryo için benzersiz bir tanımlayıcı.

- Senaryo Adı: Senaryo için kısa, açıklayıcı bir ad.

- Kaynak: Senaryoyu başlatan varlık (kullanıcı, sistem veya olay).

- Uyaran: Sistemin ele alması gereken tetikleyici olay veya koşul.

- Ortam: Sistemin uyaranı deneyimlediği işletimsel bağlam veya koşul.

- Eser: Uyarandan etkilenen sistemin yapı taşları veya diğer öğeleri.

- Yanıt: Sistemin uyarana tepki olarak sergilediği sonuç veya davranış.

- Yanıt Ölçümü: Sistemin yanıtının değerlendirildiği kriter veya metrik.

### Ayrıca bakınız

Ocak 2023'ten bu yana, arc42 kalite gereksinimlerini #flexible, #efficient, #usable, #operable, #testable, #secure, #safe, #reliable gibi hashtag'ler veya etiketlerle etiketlemeyi öneren pragmatik bir kalite modeli sağlamaktadır.

## 11. Riskler ve Teknik Borç

Bilinen teknik riskler veya teknik borç. Sistem içinde veya çevresinde hangi potansiyel sorunlar var? Geliştirme ekibi ne konusunda mutsuz hissediyor?

### İçerik

Önceliğe göre sıralanmış tanımlanmış teknik risklerin veya teknik borçların listesi

### Motivasyon

"Risk yönetimi yetişkinler için proje yönetimidir" (Tim Lister, Atlantic Systems Guild.)

Bu, yönetim paydaşları (örn. proje yöneticileri, ürün sahipleri) tarafından genel risk analizi ve ölçüm planlamasının bir parçası olarak ihtiyaç duyulacak olan mimarideki risklerin ve teknik borçların sistematik tespiti ve değerlendirmesi için mottonuz olmalıdır.

### Biçim

Riskleri en aza indirmek, azaltmak veya önlemek veya teknik borçları azaltmak için önerilen önlemleri muhtemelen içeren risklerin ve/veya teknik borçların listesi.
