# Cathetan Keputusan Arsitektur: API nganggo JSON utawa gRPC

## Status

Ditampa

## Konteks

Kita lagi ngrancang API kanggo layanan anyar sing bakal digunakake dening pirang-pirang klien. Kita wis nimbang rong pilihan kanggo ngimplementasikake API: nggunakake JSON liwat HTTP utawa nggunakake gRPC.

JSON liwat HTTP yaiku pendekatan sing akeh digunakake kanggo mbangun API, lan didhukung dening akeh basa pamrograman lan framework. Pendekatan iki prasaja, entheng, lan gampang dimangerteni, mula dadi pilihan apik kanggo akeh proyek. Nanging, bisa kurang efisien tinimbang pilihan liyane, utamane nalika nangani data akeh.

gRPC, ing sisih liya, yaiku teknologi sing luwih anyar sing nawakake cara sing luwih efisien kanggo mbangun API. Dheweke nggunakake serialisasi binar kanggo ngirim data, sing bisa luwih cepet lan luwih ringkes tinimbang nggunakake JSON. gRPC uga ndhukung streaming loro arah, mula dadi pilihan apik kanggo aplikasi real-time.

## Keputusan

Sawise nimbang kaluwihan lan kekurangan saka loro pilihan, kita mutusake nggunakake gRPC kanggo API kita. Sanajan JSON liwat HTTP pilihan sing luwih prasaja, kita pitados yen gRPC bakal menehi solusi sing luwih efisien lan bisa mundhak kanggo layanan kita. Kita uga ngira yen API kita bakal nangani data akeh, lan serialisasi binar gRPC bakal luwih efisien kanggo kasus panggunaan iki.

Saliyane iku, kita pitados yen dhukungan gRPC kanggo streaming loro arah bakal migunani kanggo aplikasi real-time sing mbok menawa bakal kita kembangake ing mbesuk.

## Akibat

Kanthi milih gRPC, kita kudu nggunakake kumpulan piranti lan pustaka sing beda kanggo mbangun API kita tinimbang nggunakake JSON liwat HTTP. Iki mbok menawa mbutuhake wektu lan upaya tambahan kanggo sinau lan ngimplementasikake teknologi-teknologi iki. Salajengipun, klien sing pengin nggunakake API kita kudu nggunakake pustaka sing kompatibel karo gRPC, sing mbok menawa ora didhukung sak amba pustaka JSON liwat HTTP.

Nanging, kita pitados yen kaluwihan nggunakake gRPC ngungkuli kekurangan potensial iki, lan kita yakin yen keputusan iki bakal ngasilake API sing luwih efisien lan bisa mundhak.
