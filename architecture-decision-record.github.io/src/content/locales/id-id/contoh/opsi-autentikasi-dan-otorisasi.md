# Catatan Keputusan Arsitektur: opsi autentikasi dan otorisasi

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Autentikasi dan otorisasi aplikasi web adalah dua konsep penting dalam mengamankan akses ke aplikasi dan layanan. Keduanya berkaitan dengan identitas pengguna dan cara izin diberikan, tetapi berfokus pada aspek yang berbeda:

- **Autentikasi** adalah proses memverifikasi identitas pengguna atau sistem.
- **Otorisasi** adalah proses menentukan sumber daya atau tindakan apa yang dapat diakses oleh pengguna atau sistem yang telah diautentikasi.

Sekarang, mari kita selami protokol dan teknologi spesifik yang Anda sebutkan, yang umum digunakan dalam aplikasi web modern untuk mengelola autentikasi dan otorisasi.

### 1. **OAuth (Open Authorization)**

**OAuth** adalah standar terbuka untuk otorisasi. OAuth memungkinkan pengguna memberikan akses terbatas kepada aplikasi pihak ketiga ke sumber daya mereka tanpa membagikan kredensial mereka. Gagasan utamanya adalah **akses terdelegasi**. OAuth sering digunakan dalam situasi di mana pengguna dapat masuk ke layanan pihak ketiga (misalnya, masuk dengan Google) tanpa memberikan nama pengguna dan kata sandi mereka secara langsung kepada pihak ketiga tersebut.

- **Alur**: OAuth biasanya mengikuti alur **berbasis token**, di mana server otorisasi menerbitkan token akses kepada aplikasi pihak ketiga. Token ini mewakili izin pengguna, dan aplikasi menggunakannya untuk mengakses data atau sumber daya pengguna dari sebuah API.
- **Contoh**: Seorang pengguna masuk ke aplikasi pihak ketiga menggunakan akun Google mereka. Google memverifikasi identitas pengguna lalu memberikan token yang memungkinkan aplikasi pihak ketiga mengakses sebagian data Google (misalnya, Google Calendar).

OAuth **tidak** menangani autentikasi secara langsung; OAuth berkaitan dengan pemberian akses. Untuk autentikasi, OAuth sering dipasangkan dengan protokol lain, seperti **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** adalah lapisan identitas yang dibangun di atas **OAuth 2.0** yang menambahkan autentikasi pada kemampuan otorisasi OAuth. Pada dasarnya, OpenID Connect memperluas OAuth untuk menangani **autentikasi pengguna** dan menyediakan cara standar bagi aplikasi untuk memverifikasi identitas pengguna.

- **Alur**: Ketika pengguna masuk menggunakan OpenID Connect, aplikasi pihak ketiga meminta token ID (selain token akses OAuth). Token ID berisi informasi tentang pengguna (seperti nama pengguna, email, dan klaim lainnya). Hal ini memungkinkan aplikasi mengetahui siapa pengguna tersebut dan apakah mereka telah diautentikasi.
- **Contoh**: Masuk ke layanan seperti Slack menggunakan akun Google Anda (Google sebagai penyedia OpenID Connect) melibatkan autentikasi melalui OpenID Connect, sedangkan OAuth mengelola akses ke sumber daya Google Anda.

OIDC memudahkan aplikasi pihak ketiga untuk **mengautentikasi pengguna** sambil tetap memungkinkan kontrol yang terperinci atas sumber daya apa yang dapat diakses aplikasi tersebut.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** adalah standar lama berbasis XML yang digunakan untuk bertukar data autentikasi dan otorisasi antarpihak, khususnya dalam skenario **Single Sign-On (SSO)**. SAML terutama digunakan di lingkungan perusahaan agar pengguna dapat mengautentikasi sekali dan mengakses banyak aplikasi tanpa memasukkan kredensial kembali.

- **Alur**: Pengguna pertama-tama mengautentikasi dengan penyedia identitas (IdP). IdP menghasilkan **pernyataan SAML** bertanda tangan yang mencakup identitas pengguna dan atribut terkait. Pernyataan tersebut dikirim ke penyedia layanan (SP), yang menggunakannya untuk mengotorisasi akses ke aplikasi.
- **Contoh**: Seorang karyawan masuk ke portal perusahaan mereka (IdP) dan otomatis masuk ke sistem lain seperti email, CRM, dll., tanpa memasukkan kredensial kembali. Proses autentikasi didasarkan pada pernyataan SAML yang dikirim oleh IdP.

SAML umum digunakan dalam **solusi SSO perusahaan** dan bekerja dengan baik untuk aplikasi web di lingkungan korporat, tetapi kurang ramah seluler dibandingkan OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** adalah protokol lain yang digunakan untuk **Single Sign-On (SSO)**, terutama di lingkungan perusahaan berbasis Microsoft. WS-Federation adalah bagian dari keluarga spesifikasi **WS-* (Web Services)** dan memungkinkan federasi identitas lintas domain keamanan yang berbeda (seperti antarorganisasi atau antarlayanan yang berbeda).

- **Alur**: WS-Federation memungkinkan **penyedia identitas (IdP) tepercaya** mengautentikasi pengguna dan menerbitkan token yang dapat digunakan penyedia layanan untuk otorisasi. Mirip dengan SAML tetapi sering digunakan dalam skenario yang sangat bergantung pada teknologi Microsoft.
- **Contoh**: Seorang pengguna masuk ke aplikasi perusahaan yang di-hosting di Microsoft Azure Active Directory (AD), dan identitas mereka dapat digunakan untuk mengakses layanan federasi lainnya, termasuk aplikasi yang di-hosting oleh vendor pihak ketiga.

Meskipun WS-Federation sebagian besar telah digantikan oleh protokol yang lebih baru seperti OAuth2.0 dan OpenID Connect di banyak lingkungan web modern, WS-Federation masih digunakan dalam sistem lama, terutama di perusahaan yang berpusat pada Microsoft.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** adalah protokol yang digunakan untuk mengakses dan mengelola layanan direktori, umum digunakan untuk **menyimpan kredensial pengguna** dan mengelola kontrol akses dalam direktori terpusat (sering disebut **Directory Service**). LDAP tidak secara khusus tentang autentikasi atau otorisasi tetapi digunakan untuk menyimpan dan mengambil data identitas, yang kemudian digunakan dalam proses-proses tersebut.

- **Autentikasi**: LDAP memungkinkan aplikasi mengautentikasi pengguna dengan menanyakan kredensial (seperti kata sandi) ke layanan direktori.
- **Otorisasi**: LDAP juga mengelola peran dan izin pengguna, membantu menentukan apakah pengguna memiliki akses ke sumber daya tertentu.
- **Contoh**: Banyak perusahaan menggunakan direktori berbasis LDAP (misalnya, **Active Directory**) untuk autentikasi dan otorisasi, terutama di lingkungan Windows.

LDAP sangat penting bagi perusahaan untuk mengelola akses pengguna di seluruh sistem internal, tetapi dalam konteks web modern, LDAP sering diintegrasikan dengan protokol lain seperti SAML atau OAuth untuk manajemen identitas yang lebih lengkap.

### 6. **Penyedia SSO Sosial**

Penyedia **Single Sign-On (SSO)** sosial seperti **Facebook**, **Google**, **Twitter**, **GitHub**, dan lainnya memungkinkan pengguna mengautentikasi ke aplikasi pihak ketiga menggunakan kredensial media sosial mereka. Ini adalah jenis **autentikasi berbasis OAuth** di mana layanan pihak ketiga (misalnya, Google) adalah penyedia identitas.

- **Alur**: Pengguna mengeklik "Masuk dengan Google" (misalnya). Aplikasi mengarahkan ke Google, tempat pengguna masuk (jika belum masuk). Google kemudian memberikan token akses atau token ID kepada aplikasi pihak ketiga, yang dapat digunakan untuk mengautentikasi pengguna dan mungkin mengakses data mereka.
- **Contoh**: Banyak aplikasi memungkinkan Anda masuk menggunakan kredensial Google atau Facebook Anda. Aplikasi akan menggunakan OAuth atau OpenID Connect di balik layar untuk memverifikasi identitas Anda dan, dalam beberapa kasus, mengakses data media sosial tertentu.

SSO sosial adalah metode autentikasi yang praktis dan banyak diadopsi karena mengurangi hambatan bagi pengguna, yang mungkin tidak ingin membuat nama pengguna dan kata sandi lagi.

---

### Ringkasan Perbedaan:

- **OAuth**: Digunakan untuk otorisasi, memungkinkan aplikasi pihak ketiga mengakses data pengguna tanpa mengungkap kredensial.
- **OpenID Connect**: Memperluas OAuth untuk menyediakan autentikasi, memungkinkan aplikasi memverifikasi identitas pengguna.
- **SAML**: Protokol berbasis XML yang digunakan untuk SSO, sering di lingkungan perusahaan.
- **WS-Federation**: Protokol khusus Microsoft untuk federasi identitas, digunakan dalam sistem lama.
- **LDAP**: Protokol untuk menanyakan layanan direktori guna mengautentikasi pengguna dan mengelola otorisasi.
- **Penyedia SSO Sosial**: Sistem berbasis OAuth (seperti Google, Facebook) yang memungkinkan aplikasi pihak ketiga mengautentikasi pengguna menggunakan kredensial media sosial mereka.

Setiap teknologi ini memiliki kekuatan dan kasus penggunaan tersendiri, dan dalam aplikasi modern, Anda mungkin melihat kombinasi di antaranya digunakan untuk aspek keamanan yang berbeda (misalnya, OAuth/OIDC untuk akses API, SAML untuk SSO perusahaan).
