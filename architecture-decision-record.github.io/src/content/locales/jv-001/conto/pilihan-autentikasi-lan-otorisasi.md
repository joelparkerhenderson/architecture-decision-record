# Cathetan Keputusan Arsitektur: pilihan autentikasi lan otorisasi

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Autentikasi lan otorisasi aplikasi web yaiku rong konsep penting kanggo ngamanake akses menyang aplikasi lan layanan. Loro-lorone gegayutan karo identitas pangguna lan carane idin diwenehake, nanging fokus ing aspek sing beda:

- **Autentikasi** yaiku proses verifikasi identitas pangguna utawa sistem.
- **Otorisasi** yaiku proses nemtokake sumber daya utawa tindakan apa sing bisa diakses dening pangguna utawa sistem sing wis kauthentikasi.

Saiki, ayo kita nyemplung menyang protokol lan teknologi spesifik sing wis kok sebutake, sing lumrah digunakake ing aplikasi web modern kanggo ngatur autentikasi lan otorisasi.

### 1. **OAuth (Open Authorization)**

**OAuth** yaiku standar terbuka kanggo otorisasi. Iki ngidini pangguna menehi aplikasi pihak katelu akses winates menyang sumber dayane tanpa nuduhake kredensiale. Gagasan utamane yaiku **akses sing didelegasikake**. OAuth asring digunakake ing kahanan ing ngendi pangguna bisa mlebu menyang layanan pihak katelu (upamane mlebu nganggo Google) tanpa langsung menehi jeneng pangguna lan sandi marang pihak katelu.

- **Alur**: OAuth biasane nuruti alur adhedhasar **token**, ing ngendi server otorisasi nerbitake token akses marang aplikasi pihak katelu. Token iki makili idin pangguna, lan aplikasi nggunakake kanggo ngakses data utawa sumber daya pangguna saka API.
- **Conto**: Pangguna mlebu menyang aplikasi pihak katelu nganggo akun Google. Google verifikasi identitas pangguna lan banjur menehi token sing ngidini aplikasi pihak katelu ngakses sawetara data Google (upamane Google Calendar).

OAuth **ora** nangani autentikasi sacara langsung; iki babagan menehi akses. Kanggo autentikasi, OAuth asring dipasangake karo protokol liyane, kayata **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** yaiku lapisan identitas sing dibangun ing ndhuwur **OAuth 2.0** sing nambah autentikasi marang kemampuan otorisasi OAuth. Intine, OpenID Connect ngluwihi OAuth kanggo nangani **autentikasi pangguna** lan nyedhiyakake cara standar kanggo aplikasi verifikasi identitas pangguna.

- **Alur**: Nalika pangguna mlebu nganggo OpenID Connect, aplikasi pihak katelu njaluk token ID (saliyane token akses OAuth). Token ID ngemot informasi babagan pangguna (kayata jeneng pangguna, email, lan klaim liyane). Iki ngidini aplikasi ngerti sapa pangguna lan apa wis kauthentikasi.
- **Conto**: Mlebu menyang layanan kayata Slack nganggo akun Google (Google minangka panyedhia OpenID Connect) nglibatake autentikasi liwat OpenID Connect, dene OAuth ngatur akses menyang sumber daya Googlemu.

OIDC nggampangake aplikasi pihak katelu **ngauthentikasi pangguna** nalika isih ngidini kontrol rinci babagan sumber daya apa sing bisa diakses aplikasi kuwi.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** yaiku standar lawas adhedhasar XML sing digunakake kanggo tukar data autentikasi lan otorisasi antarane pihak-pihak, utamane ing skenario **Single Sign-On (SSO)**. Utamane digunakake ing lingkungan perusahaan supaya pangguna bisa autentikasi sepisan lan ngakses pirang-pirang aplikasi tanpa ngetik maneh kredensial.

- **Alur**: Pangguna dhisik autentikasi karo panyedhia identitas (IdP). IdP nggawe **pernyataan SAML** sing wis ditandatangani sing ngemot identitas pangguna lan atribut sing gegayutan. Pernyataan dikirim menyang panyedhia layanan (SP), sing nggunakake kanggo ngidini akses menyang aplikasi.
- **Conto**: Karyawan mlebu menyang portal perusahaan (IdP) lan otomatis mlebu menyang sistem liyane kayata email, CRM, lan sapanunggalane, tanpa ngetik maneh kredensial. Proses autentikasi adhedhasar pernyataan SAML sing dikirim dening IdP.

SAML lumrah digunakake ing **solusi SSO perusahaan** lan cocog kanggo aplikasi web ing lingkungan korporat, nanging kurang ramah seluler dibandhingake OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** yaiku protokol liyane sing digunakake kanggo **Single Sign-On (SSO)**, utamane ing lingkungan perusahaan adhedhasar Microsoft. Iki bagean saka kulawarga spesifikasi **WS-* (Web Services)** lan ngidini federasi identitas ing domain keamanan sing beda (kayata antarane organisasi sing beda utawa antarane layanan sing beda).

- **Alur**: WS-Federation ngidini **panyedhia identitas (IdP) sing dipercaya** ngauthentikasi pangguna lan nerbitake token sing bisa digunakake panyedhia layanan kanggo otorisasi. Padha karo SAML nanging asring digunakake ing skenario sing gumantung banget marang teknologi Microsoft.
- **Conto**: Pangguna mlebu menyang aplikasi perusahaan sing dihosting dening Microsoft Azure Active Directory (AD), lan identitase bisa digunakake kanggo ngakses layanan federasi liyane, kalebu aplikasi sing dihosting dening vendor pihak katelu.

Sanajan WS-Federation umume wis diganti protokol sing luwih anyar kayata OAuth2.0 lan OpenID Connect ing akeh lingkungan web modern, isih digunakake ing sistem warisan, utamane ing perusahaan sing berpusat ing Microsoft.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** yaiku protokol sing digunakake kanggo ngakses lan ngatur layanan direktori, lumrah digunakake kanggo **nyimpen kredensial pangguna** lan ngatur kontrol akses ing direktori terpusat (asring diarani **Directory Service**). LDAP ora khusus babagan autentikasi utawa otorisasi nanging digunakake kanggo nyimpen lan njupuk data identitas, sing banjur digunakake ing proses kuwi.

- **Autentikasi**: LDAP ngidini aplikasi ngauthentikasi pangguna kanthi nakokake layanan direktori kanggo kredensial (kayata sandi).
- **Otorisasi**: Iki uga ngatur peran lan idin pangguna, mbiyantu nemtokake apa pangguna nduwe akses menyang sumber daya tartamtu.
- **Conto**: Akeh perusahaan nggunakake direktori adhedhasar LDAP (upamane **Active Directory**) kanggo autentikasi lan otorisasi, utamane ing lingkungan Windows.

LDAP penting kanggo perusahaan ngatur akses pangguna ing sistem internal, nanging ing konteks web modern, LDAP asring diintegrasi karo protokol liyane kayata SAML utawa OAuth kanggo manajemen identitas sing luwih lengkap.

### 6. **Panyedhia SSO Sosial**

Panyedhia **Single Sign-On (SSO)** sosial kayata **Facebook**, **Google**, **Twitter**, **GitHub**, lan liya-liyane ngidini pangguna autentikasi menyang aplikasi pihak katelu nganggo kredensial media sosiale. Iki jinis **autentikasi adhedhasar OAuth** ing ngendi layanan pihak katelu (upamane Google) dadi panyedhia identitas.

- **Alur**: Pangguna ngeklik "Mlebu nganggo Google" (upamane). Aplikasi ngarahake menyang Google, ing ngendi pangguna mlebu (yen durung mlebu). Google banjur nyedhiyakake token akses utawa token ID marang aplikasi pihak katelu, sing bisa digunakake kanggo ngauthentikasi pangguna lan mbok menawa ngakses datane.
- **Conto**: Akeh aplikasi ngidini kowe mlebu nganggo kredensial Google utawa Facebook. Aplikasi bakal nggunakake OAuth utawa OpenID Connect ing mburi layar kanggo verifikasi identitasmu lan, ing sawetara kasus, ngakses data media sosial tartamtu.

SSO sosial yaiku cara autentikasi sing trep lan akeh diadopsi amarga nyuda alangan kanggo pangguna, sing mbok menawa ora pengin nggawe jeneng pangguna lan sandi liyane maneh.

---

### Ringkesan Bedane:

- **OAuth**: Digunakake kanggo otorisasi, ngidini aplikasi pihak katelu ngakses data pangguna tanpa mbukak kredensial.
- **OpenID Connect**: Ngluwihi OAuth kanggo nyedhiyakake autentikasi, ngidini aplikasi verifikasi identitas pangguna.
- **SAML**: Protokol adhedhasar XML sing digunakake kanggo SSO, asring ing lingkungan perusahaan.
- **WS-Federation**: Protokol khusus Microsoft kanggo federasi identitas, digunakake ing sistem warisan.
- **LDAP**: Protokol kanggo nakokake layanan direktori kanggo ngauthentikasi pangguna lan ngatur otorisasi.
- **Panyedhia SSO Sosial**: Sistem adhedhasar OAuth (kayata Google, Facebook) sing ngidini aplikasi pihak katelu ngauthentikasi pangguna nganggo kredensial media sosiale.

Saben teknologi iki nduwe kekuwatan lan kasus panggunaan dhewe-dhewe, lan ing aplikasi modern, kowe bisa ndeleng kombinasi sing digunakake kanggo aspek keamanan sing beda (upamane OAuth/OIDC kanggo akses API, SAML kanggo SSO perusahaan).
