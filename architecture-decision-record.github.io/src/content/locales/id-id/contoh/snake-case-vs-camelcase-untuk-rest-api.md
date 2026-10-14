# Catatan Keputusan Arsitektur: snake_case vs. camelCase untuk REST API?

Keputusan: konvensi penamaan snake_case akan digunakan untuk endpoint REST API

Status: Diterima

## Konteks

Dalam konvensi penamaan untuk REST API, ada dua format yang populer: snake_case dan camelCase. Format snake_case adalah ketika setiap kata dalam nama dipisahkan oleh garis bawah, sedangkan camelCase adalah ketika kata pertama dari nama ditulis dengan huruf kecil, dan kata-kata berikutnya memiliki huruf pertama yang dikapitalisasi. Keputusan ini akan menentukan konvensi penamaan mana yang sebaiknya digunakan untuk REST API.

## Pendorong Keputusan

- Konsistensi dengan konvensi penamaan yang ada dalam proyek

- Keterbacaan dan kejelasan bagi siapa pun yang mungkin mengerjakan API

- Keselarasan dengan praktik terbaik industri untuk konvensi penamaan REST API

- Kemudahan implementasi dan pemeliharaan

## Keputusan

Konvensi penamaan snake_case akan digunakan untuk endpoint REST API. Pilihan ini didorong oleh faktor-faktor berikut:

1. **Konsistensi**: Proyek sudah menggunakan konvensi penamaan snake_case untuk semua endpoint, dan akan bermanfaat untuk mempertahankan konvensi ini demi memastikan konsistensi di seluruh proyek.

2. **Keterbacaan dan kejelasan**: Konvensi snake_case lebih mudah dibaca dan dipahami. Garis bawah memberikan pemisahan yang jelas antarkata, sehingga lebih mudah menguraikan dan memahami makna nama tersebut.

3. **Keselarasan dengan praktik terbaik industri**: Konvensi snake_case banyak digunakan di industri dan dianggap sebagai praktik terbaik untuk REST API, sehingga menjadi pilihan yang baik untuk proyek ini.

4. **Kemudahan implementasi dan pemeliharaan**: Tetap menggunakan konvensi penamaan yang ada lebih mudah diimplementasikan dan dipelihara karena semua kode dan dokumentasi yang ada perlu diperbarui jika konvensi baru dipilih.

## Konsekuensi

Ada potensi konsekuensi dari keputusan ini. 

* Jika ada anggota tim baru yang bergabung dengan proyek dan tidak familier dengan konvensi penamaan snake_case, hal itu dapat menyebabkan kebingungan dan kesalahan dalam pengembangan. Namun, karena snake_case adalah konvensi yang banyak digunakan, risiko tersebut minimal. 
  
* Jika alat atau kerangka kerja lain yang digunakan dalam proyek sangat berbasis konvensi camelCase, mungkin diperlukan upaya ekstra untuk mengonversi antar konvensi penamaan. Namun, hal itu bukan kekhawatiran yang signifikan karena proyek telah menstandarkan konvensi snake_case. 
 
Secara keseluruhan, keputusan untuk menggunakan konvensi penamaan snake_case untuk endpoint REST API menghasilkan pendekatan yang konsisten, mudah dibaca, dan sesuai standar industri sekaligus mudah diimplementasikan dan dipelihara.

<h6>Kredit: halaman ini dihasilkan oleh ChatGPT, lalu disunting agar jelas dan rapi formatnya.</h6>
