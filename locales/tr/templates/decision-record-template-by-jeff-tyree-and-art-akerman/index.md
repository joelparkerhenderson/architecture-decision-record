# Jeff Tyree ve Art Akerman tarafından karar kaydı şablonu

Bu, ["Architecture Decisions: Demystifying Architecture" (Jeff Tyree ve Art Akerman, Capital One Financial)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf) makalesinde yayınlanan mimari karar açıklama şablonudur.

* **Sorun**: Ele aldığınız mimari tasarım sorununu açıklayın, bu sorunu neden şimdi ele aldığınız konusunda hiçbir soru bırakmayın. Minimalist bir yaklaşım izleyerek, yalnızca yaşam döngüsünün çeşitli noktalarında ele alınması gereken sorunları belgeleyin.

* **Karar**: Mimarinin yönünü açıkça belirtin—yani seçtiğiniz pozisyonu.

* **Durum**: Kararın durumu, beklemede, karara bağlandı veya onaylandı gibi.

* **Grup**: Karar setini düzenlemeye yardımcı olmak için entegrasyon, sunum, veri vb. gibi basit bir gruplama kullanabilirsiniz. Ayrıca, olay, takvim ve konum gibi daha soyut kategoriler içeren John Kyaruzi ve Jan van Katwijk'inkiler gibi daha sofistike bir mimari ontoloji de kullanabilirsiniz. Örneğin, bu ontolojiyi kullanarak, sistemin bilgi gerektirdiği olaylarla ilgili kararları olay altında gruplandırırsınız.

* **Varsayımlar**: Kararı aldığınız ortamdaki temel varsayımları açıkça tanımlayın—maliyet, program, teknoloji vb. Çevresel kısıtlamaların (kabul edilmiş teknoloji standartları, kurumsal mimari, yaygın olarak kullanılan kalıplar vb. gibi) değerlendirdiğiniz alternatifleri sınırlayabileceğini unutmayın.

* **Kısıtlamalar**: Seçilen alternatifin (kararın) ortama getirebileceği ek kısıtlamaları yakalayın.

* **Pozisyonlar**: Değerlendirdiğiniz pozisyonları (uygulanabilir seçenekler veya alternatifler) listeleyin. Bunlar genellikle uzun açıklamalar, bazen modeller ve diyagramlar bile gerektirir. Bu kapsamlı bir liste değildir. Ancak, son bir inceleme sırasında "Bunu düşündünüz mü...?" sorusunu duymak istemezsiniz; bu, güvenilirlik kaybına ve diğer mimari kararların sorgulanmasına yol açar. Bu bölüm ayrıca başkalarının fikirlerini duyduğunuzdan emin olmanıza yardımcı olur; diğer görüşleri açıkça belirtmek, savunucularını kararınıza dahil etmenize yardımcı olur.

* **Argüman**: Uygulama maliyeti, toplam sahip olma maliyeti, pazara çıkış süresi ve gerekli geliştirme kaynaklarının kullanılabilirliği gibi öğeler dahil olmak üzere neden bir pozisyon seçtiğinizi özetleyin. Bu muhtemelen kararın kendisi kadar önemlidir.

* **Etkiler**: REMAP metamodelinin gösterdiği gibi, bir karar birçok etkiyle birlikte gelir. Örneğin, bir karar başka kararlar alma ihtiyacı doğurabilir, yeni gereksinimler oluşturabilir veya mevcut gereksinimleri değiştirebilir; ortama ek kısıtlamalar koyabilir; müşterilerle kapsam veya program yeniden müzakere etmeyi gerektirebilir; veya ek personel eğitimi gerektirebilir. Kararınızın etkilerini açıkça anlamak ve belirtmek, destek kazanmada ve mimari uygulama için bir yol haritası oluşturmada çok etkili olabilir.

* **İlgili kararlar**: Birçok kararın birbiriyle ilişkili olduğu açıktır; bunları burada listeleyebilirsiniz. Ancak, pratikte bir izlenebilirlik matrisi, karar ağaçları veya metamodellerin daha yararlı olduğunu bulduk. Metamodeller, karmaşık ilişkileri diyagramatik olarak göstermek için yararlıdır (Rose modelleri gibi).

* **İlgili gereksinimler**: Kararlar iş odaklı olmalıdır. Hesap verebilirliği göstermek için, kararlarınızı açıkça hedefler veya gereksinimlerle eşleştirin. Bu ilgili gereksinimleri burada listeleyebilirsiniz, ancak bir izlenebilirlik matrisine başvurmanın daha uygun olduğunu bulduk. Her mimari kararın her gereksinimi karşılamaya katkısını değerlendirebilir ve ardından gerekliliğin tüm kararlar arasında ne kadar iyi karşılandığını değerlendirebilirsiniz. Bir karar bir gereksinimi karşılamaya katkıda bulunmuyorsa, o kararı almayın.

* **İlgili eserler**: Bu kararın etkilediği ilgili mimari, tasarım veya kapsam belgelerini listeleyin.

* **İlgili ilkeler**: Kuruluşun üzerinde anlaşılmış bir ilke seti varsa, kararın bunlardan bir veya daha fazlasıyla tutarlı olduğundan emin olun. Bu, etki alanları veya sistemler arasında uyum sağlamaya yardımcı olur.

* **Notlar**: Karar verme süreci haftalar sürebileceğinden, sosyalleştirme sürecinde ekibin tartıştığı notları ve sorunları yakalamayı yararlı bulduk.
