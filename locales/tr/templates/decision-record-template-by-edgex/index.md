# Mimari Karar Kaydı (ADR) şablonu <!-- Başlığı ADR başlığıyla değiştirin -->

Bu, EdgeX Foundry ADR için bir şablondur.

Kaynak: https://docs.edgexfoundry.org/2.3/design/adr/template/


### Gönderenler

ADR gönderenlerini listeleyin.

Biçim:

- Ad (Kuruluş)


## Değişiklik Günlüğü

Belgedeki değişiklikleri, durum, tarih ve PR URL'si dahil olmak üzere listeleyin.

Durum şunlardan biridir: beklemede, onaylandı, değiştirildi, kullanımdan kaldırıldı.

Tarih ISO 8601 (YYYY-AA-GG) biçiminde bir dizedir.

PR, fark, katkıda bulunanlar ve inceleyenler gibi bilgiler dahil değişikliği gönderen pull request'tir.

Biçim:

- \[ADR'nin durumu, örn. onaylandı, değiştirildi, vb.\]\(pull request URL'si\) YYYY-AA-GG


## Başvurulan Kullanım Durumu/Durumları

Tüm ilgili kullanım durumu / gereksinim belgelerini listeleyin.

ADR en az bir ilgili, onaylanmış kullanım durumu gerektirir.

Biçim:

- \[Kullanım Durumu Adı\]\(URL\)

ADR bir kullanım durumunun tüm gereksinimlerini karşılamıyorsa açıklama ekleyin.


## Bağlam

Açıklayın:

- tasarımın mimari açıdan nasıl önemli olduğu - bir ADR'yi gerektiren (basit bir sorun ve PR ile düzeltme yerine)

- üst düzey tasarım yaklaşımı (ayrıntılar aşağıdaki önerilen tasarımda açıklanmıştır)


## Önerilen Tasarım

Tasarımın ayrıntıları (mümkün olduğunca uygulamaya girmeden).

Taslak:

- etkilenecek (değiştirilecek) hizmetler/modüller

- eklenecek yeni hizmetler/modüller

- model ve DTO etkisi (değişiklikler/eklemeler/kaldırmalar)

- API etkisi (değişiklikler/eklemeler/kaldırmalar)

- genel yapılandırma etkisi (yeni bölümlerin oluşturulması, değişiklikler/eklemeler/kaldırmalar)

- devops etkisi


## Değerlendirmeler

ADR'nin tartışmasında ortaya çıkan alternatifleri, endişeleri, yan veya ilgili sorunları, soruları belgeleyin.

Bunların çözülüp çözülmediğini veya nasıl yatıştırıldığını belirtin.


## Karar

Üzerinde anlaşmaya varılan önemli uygulama ayrıntılarını, uyarıları, gelecekteki değerlendirmeleri, kalan veya ertelenen tasarım sorunlarını belgeleyin.

Önerilen tasarım tarafından karşılanmayan gereksinimlerin herhangi bir bölümünü belgeleyin.


## Diğer İlgili ADR'ler

İlgili ADR'leri listeleyin - örneğin bir özelliğin alt bileşeni için tasarım kararı, bu tasarım sonucunda kullanımdan kaldırılan bir tasarım vb.

Biçim:

- \[ADR Başlığı\]\(URL\) - İlgi


## Referanslar

Ek referansları listeleyin.

Biçim:

- \[Başlık\]\(URL\)
