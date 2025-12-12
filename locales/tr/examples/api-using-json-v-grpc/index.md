# Mimari Karar Kaydı: JSON ve gRPC kullanan API

## Durum

Kabul edildi

## Bağlam

Birden çok istemci tarafından kullanılacak yeni bir hizmet için bir API tasarlıyoruz. API'yi uygulamak için iki seçeneği değerlendiriyoruz: HTTP üzerinden JSON kullanmak veya gRPC kullanmak.

HTTP üzerinden JSON, API'ler oluşturmak için yaygın olarak kullanılan bir yaklaşımdır ve birçok programlama dili ve çerçevesi tarafından desteklenir. Bu yaklaşım basit, hafif ve anlaşılması kolaydır, bu da onu birçok proje için iyi bir seçim haline getirir. Ancak, özellikle büyük miktarda veri işlerken diğer seçeneklerden daha az verimli olabilir.

öte yandan gRPC, API'ler oluşturmanın daha verimli bir yolunu sunan daha yeni bir teknolojidir. Veri aktarımı için ikili serileştirme kullanır, bu da JSON kullanmaktan daha hızlı ve daha kompakt olabilir. gRPC ayrıca çift yönlü akışı da destekler, bu da onu gerçek zamanlı uygulamalar için iyi bir seçim haline getirir.

## Karar

Her iki seçeneğin de artılarını ve eksilerini göz önünde bulundurduktan sonra, API'miz için gRPC kullanmaya karar verdik. HTTP üzerinden JSON daha basit bir seçenek olsa da, gRPC'nin hizmetimiz için daha verimli ve ölçeklenebilir bir çözüm sağlayacağına inanıyoruz. Ayrıca API'mizin büyük miktarda veri işleyeceğini ve gRPC'nin ikili serileştirmesinin bu kullanım durumu için daha verimli olacağını tahmin ediyoruz.

Ayrıca, gRPC'nin çift yönlü akış desteğinin gelecekte geliştirebileceğimiz gerçek zamanlı uygulamalar için faydalı olacağına inanıyoruz.

## Sonuçlar

gRPC'yi seçerek, API'mizi oluşturmak için HTTP üzerinden JSON kullanmaya kıyasla farklı bir araç ve kitaplık seti kullanmamız gerekecek. Bu, bu teknolojileri öğrenmek ve uygulamak için ek zaman ve çaba gerektirebilir. Ek olarak, API'mizi kullanmak isteyen istemcilerin, HTTP kitaplıkları üzerinden JSON kadar yaygın olarak desteklenmeyebilecek gRPC uyumlu kitaplıkları kullanması gerekecektir.

Ancak, gRPC kullanmanın faydalarının bu potansiyel dezavantajlardan daha ağır bastığına ve bu kararın daha verimli ve ölçeklenebilir bir API ile sonuçlanacağından eminiz.
