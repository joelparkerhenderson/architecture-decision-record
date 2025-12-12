# Mimari Karar Kaydı: Bir Veritabanı Teknolojisi Seçimi

## Durum

Kabul edildi

## Bağlam

Verileri ölçeklenebilir ve performanslı bir şekilde depolamayı ve almayı gerektiren yeni bir uygulama tasarlıyoruz. Yaygın olarak kullanılan üç tür veritabanı teknolojisi belirledik: ilişkisel veritabanları, belge veritabanları ve olay veritabanları.

İlişkisel veritabanları, verileri sabit şemalara sahip tablolarda depolar ve katı veri bütünlüğü kısıtlamaları uygular. Karmaşık veri ilişkileri ve işlemleri gerektiren uygulamalar için uygundurlar. Örnekler arasında MySQL, PostgreSQL ve Oracle bulunur.

Belge veritabanları, verileri JSON benzeri belgelerde depolar ve şemasızdır. Esnek veri modelleri ve yatay ölçeklendirme gerektiren uygulamalar için çok uygundurlar. Örnekler arasında MongoDB, Couchbase ve Amazon DynamoDB bulunur.

Olay veritabanları, verileri bir dizi olay olarak depolar ve verilerdeki her değişikliği yakalar. Denetim, olay kaynağı oluşturma ve karmaşık veri işleme gerektiren uygulamalar için uygundurlar. Örnekler arasında Apache Kafka, Apache Pulsar ve AWS Kinesis bulunur.
Karar

Uygulamamızın gereksinimlerini ve kısıtlamalarını dikkatlice değerlendirdikten sonra, bir belge veritabanı kullanmaya karar verdik.

## Gerekçe

Bir belge veritabanı seçtik çünkü:

1. Uygulamamız, zamanla gelişebilecek esnek bir veri modeli gerektirir. Belge veritabanları, verileri şemasız bir biçimde depolamamıza olanak tanır, bu da veritabanı şemasını değiştirmek zorunda kalmadan yeni alanlar ekleyebileceğimiz veya mevcut belgelerin yapısını değiştirebileceğimiz anlamına gelir.

2. Uygulamamızın büyük hacimli veri ve trafiği işlemek için yatay olarak ölçeklenmesi gerekir. Belge veritabanları, verileri birden çok sunucuya dağıtmamızı ve yüksek okuma ve yazma verimini işlememizi sağlayan parçalama ve çoğaltma için yerleşik destek sağlar.

3. Uygulamamız hızlı ve verimli veri alımı gerektirir. Belge veritabanları, verileri hızlı ve verimli bir şekilde almamızı sağlayan güçlü dizinleme ve sorgulama yetenekleri sağlar.

4. Uygulamamız karmaşık işlemler veya veri ilişkileri gerektirmez. İlişkisel veritabanları, veri bütünlüğü kısıtlamalarını uygulamada ve karmaşık işlemleri işlemede mükemmel olsa da, uygulamamızın bu tür gereksinimleri yoktur. Belge veritabanları, kullanım durumumuz için yeterli tutarlılık ve dayanıklılık garantisi sağlayabilir.

## Sonuçlar

Bir belge veritabanı seçerek, kullanmayı seçtiğimiz belirli teknolojiyi öğrenmeye ve anlamaya yatırım yapmamız gerekecek. Ek olarak, performansı ve ölçeklenebilirliği en üst düzeye çıkarmak için uygulamamızın veri modelinin belge veritabanının veri modeliyle iyi bir şekilde eşleştiğinden emin olmamız gerekecektir.

Ancak, bir belge veritabanı kullanmanın faydalarının maliyetlerden daha ağır bastığına ve uygulamamızın gereksinimleri ve kısıtlamaları için en uygun olduğuna inanıyoruz.