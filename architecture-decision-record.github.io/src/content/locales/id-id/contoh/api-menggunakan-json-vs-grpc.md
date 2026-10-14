# Catatan Keputusan Arsitektur: API menggunakan JSON vs. gRPC

## Status

Diterima

## Konteks

Kami sedang merancang API untuk layanan baru yang akan digunakan oleh banyak klien. Kami telah mempertimbangkan dua opsi untuk mengimplementasikan API: menggunakan JSON melalui HTTP atau menggunakan gRPC.

JSON melalui HTTP adalah pendekatan yang banyak digunakan untuk membangun API, dan didukung oleh banyak bahasa pemrograman dan kerangka kerja. Pendekatan ini sederhana, ringan, dan mudah dipahami, sehingga menjadi pilihan yang baik untuk banyak proyek. Namun, pendekatan ini bisa kurang efisien dibandingkan opsi lain, terutama dalam menangani data dalam jumlah besar.

gRPC, di sisi lain, adalah teknologi yang lebih baru yang menawarkan cara yang lebih efisien untuk membangun API. gRPC menggunakan serialisasi biner untuk mentransfer data, yang bisa lebih cepat dan lebih ringkas dibandingkan menggunakan JSON. gRPC juga mendukung streaming dua arah, sehingga menjadi pilihan yang baik untuk aplikasi real-time.

## Keputusan

Setelah mempertimbangkan kelebihan dan kekurangan kedua opsi, kami memutuskan untuk menggunakan gRPC untuk API kami. Meskipun JSON melalui HTTP adalah opsi yang lebih sederhana, kami yakin gRPC akan memberikan solusi yang lebih efisien dan dapat diskalakan untuk layanan kami. Kami juga mengantisipasi bahwa API kami akan menangani data dalam jumlah besar, dan serialisasi biner gRPC akan lebih efisien untuk kasus penggunaan ini.

Selain itu, kami yakin dukungan gRPC untuk streaming dua arah akan bermanfaat bagi aplikasi real-time yang mungkin kami kembangkan di masa depan.

## Konsekuensi

Dengan memilih gRPC, kami perlu menggunakan serangkaian alat dan pustaka yang berbeda untuk membangun API kami dibandingkan menggunakan JSON melalui HTTP. Hal ini mungkin memerlukan waktu dan upaya tambahan untuk mempelajari dan mengimplementasikan teknologi tersebut. Selain itu, klien yang ingin menggunakan API kami perlu menggunakan pustaka yang kompatibel dengan gRPC, yang mungkin tidak didukung seluas pustaka JSON melalui HTTP.

Namun, kami yakin manfaat menggunakan gRPC lebih besar daripada kekurangan potensial ini, dan kami percaya bahwa keputusan ini akan menghasilkan API yang lebih efisien dan dapat diskalakan.
