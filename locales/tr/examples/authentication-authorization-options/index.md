# Mimari Karar Kaydı: kimlik doğrulama yetkilendirme seçenekleri

<!--

ChatGPT istemi:

Web uygulaması kimlik doğrulama yetkilendirmesini açıklayın.

Açıklama: OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Sosyal SSO Sağlayıcıları.

-->

Web uygulaması kimlik doğrulaması ve yetkilendirme, uygulamalara ve hizmetlere erişimi güvence altına almada iki önemli kavramdır. Her ikisi de kullanıcıların kimliği ve izinlerin nasıl verildiği ile ilgilenir, ancak farklı yönlere odaklanırlar:

- **Kimlik doğrulama**, bir kullanıcının veya sistemin kimliğini doğrulama işlemidir.
- **Yetkilendirme**, kimliği doğrulanmış kullanıcının veya sistemin hangi kaynaklara veya eylemlere erişebileceğini belirleme işlemidir.

Şimdi, modern web uygulamalarında kimlik doğrulama ve yetkilendirmeyi yönetmek için yaygın olarak kullanılan, bahsettiğiniz belirli protokollere ve teknolojilere dalalım.

### 1. **OAuth (Açık Yetkilendirme)**

**OAuth**, yetkilendirme için açık bir standarttır. Bir kullanıcının, kimlik bilgilerini paylaşmadan üçüncü taraf bir uygulamanın kaynaklarına sınırlı erişim vermesine olanak tanır. Anahtar fikir **temsilci erişimidir**. OAuth, kullanıcıların üçüncü taraf bir hizmete (örneğin, Google ile oturum açma) doğrudan kullanıcı adlarını ve şifrelerini vermeden giriş yapabildiği durumlarda sıklıkla kullanılır.

- **Akış**: OAuth genellikle, bir yetkilendirme sunucusunun üçüncü taraf uygulamasına bir erişim belirteci verdiği **belirteç tabanlı** bir akışı izler. Bu belirteç, kullanıcının izinlerini temsil eder ve uygulama, bir API'den kullanıcının verilerine veya kaynaklarına erişmek için onu kullanır.
- **Örnek**: Bir kullanıcı, Google hesabını kullanarak üçüncü taraf bir uygulamada oturum açar. Google, kullanıcının kimliğini doğrular ve ardından üçüncü taraf uygulamanın bazı Google verilerine (örneğin, Google Takvim) erişmesine izin veren bir belirteç verir.

OAuth, kimlik doğrulamayı doğrudan **ele almaz**; erişim izni vermekle ilgilidir. Kimlik doğrulama için OAuth, genellikle **OpenID Connect** gibi diğer protokollerle eşleştirilir.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)**, OAuth'un yetkilendirme yeteneklerine kimlik doğrulama ekleyen **OAuth 2.0** üzerine kurulu bir kimlik katmanıdır. Esasen, OpenID Connect, **kullanıcı kimlik doğrulamasını** işlemek için OAuth'u genişletir ve uygulamaların bir kullanıcının kimliğini doğrulaması için standartlaştırılmış bir yol sağlar.

- **Akış**: Bir kullanıcı OpenID Connect kullanarak oturum açtığında, üçüncü taraf uygulaması (OAuth erişim belirtecine ek olarak) bir kimlik belirteci talep eder. Kimlik belirteci, kullanıcı hakkında (kullanıcı adı, e-posta ve diğer talepler gibi) bilgiler içerir. Bu, uygulamanın kullanıcının kim olduğunu ve kimliğinin doğrulanıp doğrulanmadığını bilmesini sağlar.
- **Örnek**: Google hesabınızı (Google'ın OpenID Connect sağlayıcısı olduğu) kullanarak Slack gibi bir hizmette oturum açmak, OpenID Connect aracılığıyla kimlik doğrulamayı içerirken, OAuth Google kaynaklarınıza erişimi yönetir.

OIDC, üçüncü taraf uygulamaların, bu uygulamaların hangi kaynaklara erişebileceği üzerinde ayrıntılı denetime izin verirken **kullanıcıların kimliğini doğrulamayı** kolaylaştırır.

### 3. **SAML (Güvenlik Onaylama İşaretleme Dili)**

**SAML**, özellikle **Tek Oturum Açma (SSO)** senaryolarında taraflar arasında kimlik doğrulama ve yetkilendirme verilerini değiştirmek için kullanılan daha eski, XML tabanlı bir standarttır. Öncelikle kurumsal ortamlarda, kullanıcıların bir kez kimlik doğrulaması yapmasına ve kimlik bilgilerini yeniden girmeden birden çok uygulamaya erişmesine olanak sağlamak için kullanılır.

- **Akış**: Kullanıcı önce bir kimlik sağlayıcı (IdP) ile kimlik doğrulaması yapar. IdP, kullanıcının kimliğini ve ilgili niteliklerini içeren imzalı bir **SAML onayı** oluşturur. Onay, hizmet sağlayıcıya (SP) gönderilir ve SP, uygulamaya erişimi yetkilendirmek için onu kullanır.
- **Örnek**: Bir çalışan, kurumsal portallarına (IdP) giriş yapar ve kimlik bilgilerini yeniden girmeden e-posta, CRM vb. gibi diğer sistemlere otomatik olarak giriş yapar. Kimlik doğrulama işlemi, IdP tarafından gönderilen SAML onayına dayanır.

SAML, **kurumsal SSO çözümlerinde** yaygın olarak kullanılır ve kurumsal ortamlardaki web uygulamaları için iyi çalışır, ancak OAuth/OIDC'ye kıyasla daha az mobil uyumludur.

### 4. **WS-Federation (Web Hizmetleri Federasyonu)**

**WS-Federation**, özellikle Microsoft tabanlı kurumsal ortamlarda **Tek Oturum Açma (SSO)** için kullanılan başka bir protokoldür. **WS-* (Web Hizmetleri)** belirtim ailesinin bir parçasıdır ve farklı güvenlik alanları (farklı kuruluşlar arasında veya farklı hizmetler arasında gibi) arasında kimlik federasyonuna izin verir.

- **Akış**: WS-Federation, **güvenilir bir kimlik sağlayıcının (IdP)** kullanıcıların kimliğini doğrulamasına ve hizmet sağlayıcının yetkilendirme için kullanabileceği belirteçler vermesine olanak tanır. SAML'ye benzer, ancak genellikle Microsoft teknolojilerine büyük ölçüde dayanan senaryolarda kullanılır.
- **Örnek**: Bir kullanıcı, Microsoft Azure Active Directory (AD) tarafından barındırılan bir kurumsal uygulamada oturum açar ve kimliği, üçüncü taraf satıcılar tarafından barındırılan uygulamalar da dahil olmak üzere diğer birleşik hizmetlere erişmek için kullanılabilir.

WS-Federation, birçok modern web ortamında OAuth2.0 ve OpenID Connect gibi daha yeni protokollerle büyük ölçüde değiştirilmiş olsa da, özellikle Microsoft merkezli işletmelerde eski sistemlerde hala kullanılmaktadır.

### 5. **LDAP (Hafif Dizin Erişim Protokolü)**

**LDAP**, genellikle **kullanıcı kimlik bilgilerini depolamak** ve merkezi bir dizinde (genellikle **Dizin Hizmeti** olarak adlandırılır) erişim denetimini yönetmek için kullanılan dizin hizmetlerine erişmek ve bunları yönetmek için kullanılan bir protokoldür. LDAP, özellikle kimlik doğrulama veya yetkilendirme ile ilgili değildir, ancak bu işlemlerde kullanılan kimlik verilerini depolamak ve almak için kullanılır.

- **Kimlik Doğrulama**: LDAP, bir uygulamanın kimlik bilgileri (şifreler gibi) için dizin hizmetini sorgulayarak kullanıcıların kimliğini doğrulamasına olanak tanır.
- **Yetkilendirme**: Ayrıca kullanıcı rollerini ve izinlerini yöneterek bir kullanıcının belirli kaynaklara erişip erişemeyeceğini belirlemeye yardımcı olur.
- **Örnek**: Birçok işletme, özellikle Windows ortamlarında kimlik doğrulama ve yetkilendirme için LDAP tabanlı dizinleri (örneğin, **Active Directory**) kullanır.

LDAP, işletmelerin dahili sistemler arasında kullanıcı erişimini yönetmesi için çok önemlidir, ancak modern bir web bağlamında LDAP, daha eksiksiz bir kimlik yönetimi için genellikle SAML veya OAuth gibi diğer protokollerle entegre edilir.

### 6. **Sosyal SSO Sağlayıcıları**

**Facebook**, **Google**, **Twitter**, **GitHub** gibi sosyal **Tek Oturum Açma (SSO)** sağlayıcıları, kullanıcıların sosyal medya kimlik bilgilerini kullanarak üçüncü taraf uygulamalarda kimlik doğrulaması yapmasına olanak tanır. Bu, üçüncü taraf hizmetin (örneğin, Google) kimlik sağlayıcısı olduğu bir **OAuth tabanlı kimlik doğrulama** türüdür.

- **Akış**: Kullanıcı "Google ile giriş yap" (örneğin) seçeneğine tıklar. Uygulama, kullanıcının (henüz giriş yapmadıysa) giriş yaptığı Google'a yönlendirir. Google daha sonra, kullanıcının kimliğini doğrulamak ve muhtemelen verilerine erişmek için kullanılabilecek bir erişim belirteci veya kimlik belirteci sağlar.
- **Örnek**: Birçok uygulama, Google veya Facebook kimlik bilgilerinizi kullanarak giriş yapmanıza olanak tanır. Uygulama, kimliğinizi doğrulamak ve bazı durumlarda belirli sosyal medya verilerine erişmek için arka planda OAuth veya OpenID Connect'i kullanır.

Sosyal SSO, kullanıcılar için başka bir kullanıcı adı ve şifre oluşturmak istemeyebilecekleri için sürtünmeyi azalttığı için kullanışlı ve yaygın olarak benimsenen bir kimlik doğrulama yöntemidir.

---

### Farklılıkların Özeti:

- **OAuth**: Yetkilendirme için kullanılır, üçüncü taraf uygulamaların kimlik bilgilerini ifşa etmeden kullanıcı verilerine erişmesine olanak tanır.
- **OpenID Connect**: Uygulamaların kullanıcı kimliğini doğrulamasına olanak tanıyan kimlik doğrulama sağlamak için OAuth'u genişletir.
- **SAML**: Genellikle kurumsal ortamlarda SSO için kullanılan XML tabanlı protokol.
- **WS-Federation**: Eski sistemlerde kullanılan kimlik federasyonu için Microsoft'a özgü bir protokol.
- **LDAP**: Kullanıcıların kimliğini doğrulamak ve yetkilendirmeyi yönetmek için dizin hizmetlerini sorgulamak için kullanılan bir protokol.
- **Sosyal SSO Sağlayıcıları**: Üçüncü taraf uygulamaların sosyal medya kimlik bilgilerini kullanarak kullanıcıların kimliğini doğrulamasına olanak tanıyan OAuth tabanlı sistemler (Google, Facebook gibi).

Bu teknolojilerin her birinin kendi güçlü yönleri ve kullanım durumları vardır ve modern uygulamalarda, güvenliğin farklı yönleri için bunların bir kombinasyonunun kullanıldığını görebilirsiniz (örneğin, API erişimi için OAuth/OIDC, kurumsal SSO için SAML).