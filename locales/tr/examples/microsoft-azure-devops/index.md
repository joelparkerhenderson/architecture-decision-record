# Microsoft Azure DevOps

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
  * [Microsoft Devops CI: Tatmin Edici Olmayan Bir Macera](#microsoft-devops-ci-tatmin-edici-olmayan-bir-macera)
  * [Hacker News tartışma öne çıkanları](#hacker-news-tartışma-öne-çıkanları)
  * [Windows Geliştirme MVP](#windows-geliştirme-mvp)
  * [Edward Thomson (Azure PM) özeti](#edward-thomson-azure-pm-özeti)


## Özet


### Sorun

Projelerimizi oluşturmak, entegre etmek, dağıtmak ve barındırmak için devops kullanmak istiyoruz. Microsoft Azure DevOps'u değerlendiriyoruz.

  * Devops kurulumu (örneğin yapılandırma) ve sürekli kullanım (örneğin hızlı derleme süreleri) için geliştirici deneyiminin hızlı ve güvenilir olmasını istiyoruz.
  
  * Proje uygulamalarını, veritabanlarını vb. barındırmak için Microsoft Azure'u bir bütün olarak kullanmayı düşünmek istiyoruz.


### Karar

Microsoft Azure DevOps'a karşı karar verildi.


### Durum

Karar verildi. Yeni önemli bilgiler geldiğinde/gelirse yeniden değerlendirmeye açığız.


## Ayrıntılar


### Varsayımlar

Accelerate kitabındaki gibi tüm olağan devops varsayımları.

  * Hızlı derlemeler önemli bir yardımdır. Bu, geri bildirim döngülerini hızlandırır.

  * Alternatif satıcılardan parçaları değiştirebiliriz, yani daha yüksek hızlı derleme sunucularımızı getirmek veya kendi sürüm kontrol sistemimizi seçmek veya kendi kendine barındırılan sürekli entegrasyon sunucusuyla koordine etmek isteyebiliriz.
  
  * Geliştirici deneyimi için ve dolayısıyla tutarlılık, netlik, güvenlik ve öğrenme eğrisinin kolaylığı gibi hassas alanlar için kolaylaştırılmış kullanılabilirlik önemli bir yardımdır.

  * Herhangi bir şey bozulduğunda veya sorunlu olduğunda, sorunu bildirmek için etkili bir yol istiyoruz. Bu, özellikle güvenlikle ilgili sorunlar için önemlidir.


### Kısıtlamalar

Bilinen bir kısıtlama yok. Azure, harici araçlarla iyi çalışmaya yönelik yayınlanmış bir taahhüde sahiptir.


### Pozisyonlar

Microsoft Azure Devops'u mevcut AWS'ye karşı kullanmayı düşündük.

Azure DevOps, Azure Pipelines, Azure Repo ve Terraform aracılığıyla yeni sunucu başlatma ile denemeler yaptık.

Microsoft temsilcilerinden destek alma konusunda denemeler yaptık.

Bloglardan ve Hacker News'ten akranlardan bilgi topladık.


### Argüman

Azure DevOps mükemmel bir teklif seti reklamı yapıyor, ancak bunlar ayakta durmuyor, birlikte iyi çalışmıyor ve destek zayıf.

İlk elden deneyimimiz:

  * Azure kurulumu, bazıları Microsoft hesaplarıyla çakışan, bazıları çakışmayan kullanıcı arayüzlerinin bir karmaşasıdır. Örneğin, bir Azure oturum açma, bir Microsoft.com oturum açma, bir Live.com oturum açma vb. vardır ve hepsi aynı anda devrededir.

  * Kurulum sırasında küçük bir güvenlik sorunuyla karşılaştık ve çözüm bulamadık. Birçok Microsoft temsilcisine birçok yolla bildirmeye çalıştık, ancak başarılı olamadık. Microsoft güvenliğine başarıyla bildirdik, ancak düzeltilmeyeceği yanıtını aldık.

  * Belgeler genellikle yanlış veya güncel değil. Bunun en azından bir kısmı Microsoft'un zayıf arama motorundan ve bir kısmı da yetersiz SEO'dan kaynaklanmaktadır.
  
  * Terraform kurulumu iyi belgelenmiştir ve çalışır. Ancak, Microsoft'un Terraform kurulum örnekleri aracılığıyla zincirleme yapmak için satıcılarla iş ilişkileri kurması nedeniyle Terraform desteği AWS'ye kıyasla zayıftır.

Akran deneyimlerimiz:

  * Kendi kör değerlendirmemizi yaptıktan sonra, akran deneyimlerini aradık. Bulduklarımız deneyimlerimizi doğruladı.

  * Akranlar, derleme süreleriyle ilgili ek sorunlar ve kendi derleme sunucunuzu getirme sorunları bildirdi. Bu sorunlar, kullanıcı arayüzü sorunlarından önemli ölçüde daha ciddidir, çünkü derleme yapmak bir derleme boru hattının temel amacıdır ve günde birçok kez yapmayı bekleriz.

  * Azure ekip arkadaşlarının tartışma alanlarına mükemmel katılımını bulduk. Microsoft'a bunun için teşekkür ederiz. Özellikle Edward Thomson, Azure PM ve kodlayıcı, katılımı, doğrudanlığı ve teknik açıklamaları nedeniyle bizi çok etkiledi.


### Etkiler

Microsoft Azure DevOps'u seçmek, Azure'u seçmemekten daha pahalı (~3 kat) zaman ve maliyet açısından daha pahalı olma olasılığı yüksek görünüyor.


## İlgili


### İlgili kararlar

Azure DevOps'u seçersek, Azure Repo, Azure Pipeline vb. dahil olmak üzere birçok ilgili teklif vardır. Azure Devops'u seçersek, bu, daha fazla Azure yeteneği kullanmayı kolaylaştırabilir veya diğer satıcıların yeteneklerini kullanmayı zorlaştırabilir.

Microsoft'un geliştirici deneyiminde büyük adımlar attığına inanıyoruz ve Microsoft'un geliştirici araçlarını (örneğin GitHub) ve bağımlılıklarını (örneğin Citus) büyük ölçüde satın aldığını görüyoruz.

Azure DevOps'u seçersek, Microsoft satın alma tekliflerini seçmeye vurgu yapmak isteyebiliriz ve potansiyel doku reddi, örneğin personel devir riski nedeniyle satın alma tekliflerine daha dikkatli/değerlendirmeyle yaklaşmak isteyebiliriz.


### İlgili gereksinimler

Derleme sürelerinin çok hızlı olmasını istiyoruz. Bunun için yüksek bir prim ödemeyi kabul ediyoruz. Bunun nedeni, çok hızlı yineleme yapmak istememizdir.

Güvenilirliğin çok yüksek olmasını istiyoruz. Bunun için yüksek bir prim ödemeyi kabul ediyoruz. Bunun nedeni, finansal işlemler, gizli işlemler vb. dahil olmak üzere yüksek değerli kullanım durumlarını test etmemizdir.

En iyi 4 devops KPI'mız, hızlı derlemeler ve yüksek güvenilirlik gerektiren ortalama kurtarma süresini içerir.


### İlgili eserler

Derleme sisteminin, Artifactory gibi diğer sistemlerde kullanıma uygun yapıtlar üretmesini istiyoruz.


### İlgili ilkeler

Kolayca geri döndürülebilir. Azure DevOps'u AWS ile paralel olarak değerlendirebiliriz.


## Notlar


### Microsoft Devops CI: Tatmin Edici Olmayan Bir Macera

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Blog yazısı.

"Bir yazılım geliştiricisi olarak, kaliteli ürünleri hızlı ve ucuza inşa etmenin ne kadar zor olduğunu ilk elden biliyorum. Bu, bazen doğru yaptığımız, bazen de Obama dönemi sağlık hizmetleri hükümet sitesine benzer bir şeye dönüşen bir sanat formudur. Ortaya çıkan ürün üzerindeki kontrol seviyemiz değişir ve başarısızlığın suçu genellikle karar alma hiyerarşisindeki yanlış kişilere düşer. Microsoft'un Azure DevOps (eski adıyla Visual Studio Team Services), açıkça iyi niyetlere rağmen, kötü kararların ve kötü uygulamanın mükemmel bir fırtınasıdır."


### Hacker News tartışma öne çıkanları

https://news.ycombinator.com/item?id=18983586

"İşimde Azure DevOps'u yoğun bir şekilde kullanıyoruz ve GitHub, Gitlab, kendi kendine barındırılan çözümler, Jenkins, TeamCity... kullandıktan sonra Azure DevOps son sırada yer alıyor."

"Kullanıcı arayüzü her yerde korkunç derecede hantal. Benim için en kötüsü çekme istekleri. Bir çekme isteği üzerinde insanlarla çalışmak inanılmaz derecede zor. Size "belirli" bir sorunu bile gösteremem - bizim için her yerde bozuk."

"Azure Devops sevmek istediğim bir şey. Kullanıcı arayüzü sürekli değişiyor, ancak yıllardır var olan temel hataları düzeltmiyor."

"Araçlar iyi entegre değil, kullanıcı arayüzü gerçekten yavaş, favori depolarım için aktif çekme istekleri, derlemeler, yayınlar vb. için bir gösterge paneli görünümü yok. Derleme/Dağıtım süreleri inanılmaz derecede yavaş."

"Azure Boards'u (İş Öğeleri, Panolar, İş Listeleri vb.) da kullanmaya çalıştık. Ah! Tamamen kopuk fikirlerin bir kullanıcı arayüzü karmaşası. Bir şeyi iyi uygulamak yerine, iki düzine şeyi korkunç bir şekilde uyguladılar."


### Windows Geliştirme MVP

Windows Geliştirme MVP olarak buradayım. Bu sorunlar hakkında daha yüksek sesle konuşmadığım için sorumluluğun bir kısmını üstlenmem gerektiğini hissediyorum. Ancak şunu söylemeliyim ki, UX sorunları hakkında "şaşırmış" olmanız beni hayal kırıklığına uğrattı. İnsanlarınıza UX'in korkunç olduğunu (örneğin lansman öncesinden beri) söylüyordum ve sürekli "biliyoruz, düzeltiyoruz" yanıtını alıyordum. Geri bildirimi resmileştirmeye başlayacağım ve boru hatlarından geçireceğim, takipte kalın. Ayrıca yerel (Bellevue) olarak da buradayım, nispeten basit oss .net/wpf/uwp uygulamamızı boru hattına sokmaya çalışmak isterim. Sanırım ikimiz için de göz açıcı olacaktır.

Bazı örnekler:

* Alt modüller içeren bir git deposuyla bir boru hattı oluşturamazsınız.

* Bazı özel araçlar için PATH'i düzenlemenin imkansız olduğunu gördüm.

* Yeni Boru Hattı deneyimi pek mantıklı değil, yeni kullanıcılar etrafa tıklayarak sonunda yanlış Belgelere ulaşacaklar.


### Edward Thomson (Azure PM) özeti

Çekme isteklerinizi birleştiren kodu ben yazdım. Microsoft'ta Azure DevOps için Program Yöneticisi; daha önce GitHub, Microsoft, SourceGear'da sürüm kontrol araçları üzerinde yazılım mühendisiydi.

https://www.edwardthomson.com/

libgit2'nin ortak bakımcısı. https://libgit2.github.io

Git hakkında Podcast olan All Things Git'in ortak sunucusu. https://www.allthingsgit.com/

Geliştirme araçları hakkında bir bülten olan Developer Tools Weekly'nin küratörü. https://developertoolsweekly.com/