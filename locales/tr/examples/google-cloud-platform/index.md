# Google Cloud Platform için Mimari Karar Kaydı

## Bağlam

Google Cloud Platform (GCP), bilgi işlem, depolama ve ağ çözümleri dahil olmak üzere çeşitli bulut hizmetleri sunan önde gelen bir bulut bilişim platformudur. Bu ADR, kuruluşumuz için GCP tabanlı bir altyapı geliştirmek ve uygulamak için alınan mimari kararları belgelemeyi amaçlamaktadır.

## Karar

Kuruluşumuz, uygulamamız için bulut altyapısı olarak Google Cloud Platform'u kullanmaya karar vermiştir. Bu kararın birincil değerlendirmeleri şunlardır:

   - Maliyet etkinliği

   - Ölçeklenebilirlik

   - Güvenilirlik

   - Esneklik

## Seçimler

Gereksinimlerimizi karşılamak için GCP'den aşağıdaki hizmetler seçilmiştir:

   - Sanal makineler ve bilgi işlem kaynakları için Compute Engine

   - Nesne depolama ve dosya barındırma için Cloud Storage

   - Yönetilen veritabanı hizmeti için Cloud SQL

   - Uygulama geliştirme ve barındırma için Firebase

## Gerekçe

   - Maliyet Etkinliği: Google Cloud Platform, diğer bulut platformlarına kıyasla oldukça uygun maliyetlidir ve bütçe kısıtlamaları olan kuruluşlar için cazip bir seçenek haline getirir.

   - Ölçeklenebilirlik: GCP'nin kolayca ölçeklenebilen altyapısı, her türlü trafiği gerçek zamanlı olarak işlemeyi sağlar.

   - Güvenilirlik: GCP'nin yönetilen hizmetleri, kaynakların ve verilerin yüksek kullanılabilirliğini sağlayan otomatik yedeklemeler ve olağanüstü durum kurtarma yetenekleri ile yüksek güvenilirlik sunar.

   - Esneklik: Platform, yapay zeka, veri analizi ve IoT gibi farklı alanlarda çeşitli araçlar ve hizmetler sunarak oldukça çok yönlüdür.

## Sonuçlar

Google Cloud Platform'a geçiş, ekiplerimizi GCP hizmetleri konusunda eğitmeyi, uygulamayı seçilen hizmetlerle uyumlu olacak şekilde yeniden tasarlamayı ve GCP hizmetlerini desteklemek için altyapı kodunu güncellemeyi gerektirecektir. Ancak, geçiş tamamlandıktan sonra, uygulamamızı barındırmak için yüksek oranda ölçeklenebilir, güvenilir ve uygun maliyetli bir altyapıya sahip olmamız beklenmektedir. Ayrıca, GCP'de kaynak sağlama maliyetlerini yönetmemiz gerekecektir.

## Sonuç

Google Cloud Platform, maliyet etkinliği, ölçeklenebilirliği, güvenilirliği ve esnekliği nedeniyle bulut altyapımız için mükemmel bir seçimdir. Seçilen hizmetleri kullanarak, uygulamamız için yüksek oranda kullanılabilir ve sağlam bir altyapı sağlayabiliriz.