# ਆਰਕੀਟੈਕਚਰ ਫੈਸਲਾ ਰਿਕਾਰਡ (ADR)

ਆਰਕੀਟੈਕਚਰ ਫੈਸਲਾ ਰਿਕਾਰਡ (ADR) ਇੱਕ ਅਜਿਹਾ ਦਸਤਾਵੇਜ਼ ਹੈ ਜੋ ਕਿਸੇ ਮਹੱਤਵਪੂਰਨ ਆਰਕੀਟੈਕਚਰ ਫੈਸਲੇ ਨੂੰ ਉਸ ਦੇ ਪ੍ਰਸੰਗ ਅਤੇ ਨਤੀਜਿਆਂ ਸਮੇਤ ਦਰਜ ਕਰਦਾ ਹੈ।

> [!IMPORTANT]
> ਇਨ੍ਹਾਂ ਸਰੋਤਾਂ ਨੂੰ ਕਿਸੇ ਵੀ ਨਾਜ਼ੁਕ ਸਿਸਟਮ ਵਿੱਚ ਵਰਤਣ ਤੋਂ ਪਹਿਲਾਂ ਆਪਣੀ ਖੁਦ ਦੀ ਪੂਰੀ ਪੜਤਾਲ ਕਰੋ।

ਸਮੱਗਰੀ:

- [ਆਰਕੀਟੈਕਚਰ ਫੈਸਲਾ ਰਿਕਾਰਡ ਕੀ ਹੈ?](#ਆਰਕੀਟੈਕਚਰ-ਫੈਸਲਾ-ਰਿਕਾਰਡ-ਕੀ-ਹੈ)
- [ADR ਵਰਤਣਾ ਕਿਵੇਂ ਸ਼ੁਰੂ ਕਰੀਏ](#adr-ਵਰਤਣਾ-ਕਿਵੇਂ-ਸ਼ੁਰੂ-ਕਰੀਏ)
- [ਟੂਲਾਂ ਨਾਲ ADR ਵਰਤਣਾ ਕਿਵੇਂ ਸ਼ੁਰੂ ਕਰੀਏ](#ਟੂਲਾਂ-ਨਾਲ-adr-ਵਰਤਣਾ-ਕਿਵੇਂ-ਸ਼ੁਰੂ-ਕਰੀਏ)
- [git ਨਾਲ ADR ਵਰਤਣਾ ਕਿਵੇਂ ਸ਼ੁਰੂ ਕਰੀਏ](#git-ਨਾਲ-adr-ਵਰਤਣਾ-ਕਿਵੇਂ-ਸ਼ੁਰੂ-ਕਰੀਏ)
- [ADR ਲਈ Claude Code ਸਕਿੱਲ](#adr-ਲਈ-claude-code-ਸਕਿੱਲ)
- [ADR ਲਈ ਫਾਈਲ ਨਾਮ ਪਰੰਪਰਾਵਾਂ](#adr-ਲਈ-ਫਾਈਲ-ਨਾਮ-ਪਰੰਪਰਾਵਾਂ)
- [ਚੰਗੇ ADR ਲਿਖਣ ਲਈ ਸੁਝਾਅ](#ਚੰਗੇ-adr-ਲਿਖਣ-ਲਈ-ਸੁਝਾਅ)
- [ADR ਉਦਾਹਰਨ ਟੈਂਪਲੇਟ](#adr-ਉਦਾਹਰਨ-ਟੈਂਪਲੇਟ)
- [ADR ਲਈ ਟੀਮ ਵਰਕ ਸਲਾਹ](#adr-ਲਈ-ਟੀਮ-ਵਰਕ-ਸਲਾਹ)
- [ADR ਲਈ ਟੀਮ ਵਰਕ ਸਵਾਲ](#adr-ਲਈ-ਟੀਮ-ਵਰਕ-ਸਵਾਲ)
- [ADR ਲਈ ਅਗਲੇ ਕਦਮ ਦੇ ਸੰਕਲਪ](#adr-ਲਈ-ਅਗਲੇ-ਕਦਮ-ਦੇ-ਸੰਕਲਪ)
- [ਆਰਕੀਟੈਕਚਰ ਚਿੱਤਰ, ਦ੍ਰਿਸ਼ ਅਤੇ ਦ੍ਰਿਸ਼ਟੀਕੋਣ](#ਆਰਕੀਟੈਕਚਰ-ਚਿੱਤਰ-ਦ੍ਰਿਸ਼-ਅਤੇ-ਦ੍ਰਿਸ਼ਟੀਕੋਣ)
- [ਕੋਡ ਵਜੋਂ ਫੈਸਲਿਆਂ ਲਈ ਫਿਟਨੈਸ ਫੰਕਸ਼ਨ](#ਕੋਡ-ਵਜੋਂ-ਫੈਸਲਿਆਂ-ਲਈ-ਫਿਟਨੈਸ-ਫੰਕਸ਼ਨ)
- [ਪੁੱਲ ਰਿਕੁਐਸਟਾਂ ਲਈ ਫੈਸਲੇ ਦੇ ਗਾਰਡਰੇਲ](#ਪੁੱਲ-ਰਿਕੁਐਸਟਾਂ-ਲਈ-ਫੈਸਲੇ-ਦੇ-ਗਾਰਡਰੇਲ)
- [ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ](#ਹੋਰ-ਜਾਣਕਾਰੀ-ਲਈ)

ਟੈਂਪਲੇਟ:

- [Jeff Tyree ਅਤੇ Art Akerman ਦਾ ਫੈਸਲਾ ਰਿਕਾਰਡ ਟੈਂਪਲੇਟ](ਟੈਂਪਲੇਟ/ਜੈਫ-ਟਾਇਰੀ-ਅਤੇ-ਆਰਟ-ਅਕਰਮੈਨ-ਦਾ-ਫੈਸਲਾ-ਰਿਕਾਰਡ-ਟੈਂਪਲੇਟ/)
- [Michael Nygard ਦਾ ਫੈਸਲਾ ਰਿਕਾਰਡ ਟੈਂਪਲੇਟ](ਟੈਂਪਲੇਟ/ਮਾਈਕਲ-ਨਾਈਗਾਰਡ-ਦਾ-ਫੈਸਲਾ-ਰਿਕਾਰਡ-ਟੈਂਪਲੇਟ/)
- [EdgeX ਦਾ ਫੈਸਲਾ ਰਿਕਾਰਡ ਟੈਂਪਲੇਟ](ਟੈਂਪਲੇਟ/edgex-ਦਾ-ਫੈਸਲਾ-ਰਿਕਾਰਡ-ਟੈਂਪਲੇਟ/)
- [arc42 ਦਾ ਫੈਸਲਾ ਰਿਕਾਰਡ ਟੈਂਪਲੇਟ](ਟੈਂਪਲੇਟ/arc42-ਦਾ-ਫੈਸਲਾ-ਰਿਕਾਰਡ-ਟੈਂਪਲੇਟ/)
- [ਅਲੈਗਜ਼ੈਂਡਰੀਅਨ ਪੈਟਰਨ ਲਈ ਫੈਸਲਾ ਰਿਕਾਰਡ ਟੈਂਪਲੇਟ](ਟੈਂਪਲੇਟ/ਅਲੈਗਜ਼ੈਂਡਰੀਅਨ-ਪੈਟਰਨ-ਲਈ-ਫੈਸਲਾ-ਰਿਕਾਰਡ-ਟੈਂਪਲੇਟ/)
- [ਕਾਰੋਬਾਰੀ ਕੇਸ ਲਈ ਫੈਸਲਾ ਰਿਕਾਰਡ ਟੈਂਪਲੇਟ](ਟੈਂਪਲੇਟ/ਕਾਰੋਬਾਰੀ-ਕੇਸ-ਲਈ-ਫੈਸਲਾ-ਰਿਕਾਰਡ-ਟੈਂਪਲੇਟ/)
- [MADR ਪ੍ਰੋਜੈਕਟ ਦਾ ਫੈਸਲਾ ਰਿਕਾਰਡ ਟੈਂਪਲੇਟ](ਟੈਂਪਲੇਟ/madr-ਪ੍ਰੋਜੈਕਟ-ਦਾ-ਫੈਸਲਾ-ਰਿਕਾਰਡ-ਟੈਂਪਲੇਟ/)
- [Planguage ਵਰਤਦਾ ਫੈਸਲਾ ਰਿਕਾਰਡ ਟੈਂਪਲੇਟ](ਟੈਂਪਲੇਟ/planguage-ਵਰਤਦਾ-ਫੈਸਲਾ-ਰਿਕਾਰਡ-ਟੈਂਪਲੇਟ/)
- [Paulo Merson ਦਾ ਫੈਸਲਾ ਰਿਕਾਰਡ ਟੈਂਪਲੇਟ](https://github.com/pmerson/ADR-template)
- [Olaf Zimmermann ਦਾ ਫੈਸਲਾ ਰਿਕਾਰਡ ਟੈਂਪਲੇਟ](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Gareth Morgan ਦਾ ਫੈਸਲਾ ਰਿਕਾਰਡ ਟੈਂਪਲੇਟ](ਟੈਂਪਲੇਟ/ਗੈਰੇਥ-ਮੋਰਗਨ-ਦਾ-ਫੈਸਲਾ-ਰਿਕਾਰਡ-ਟੈਂਪਲੇਟ/)
- [GIG Cymru NHS Wales ਦਾ ਫੈਸਲਾ ਰਿਕਾਰਡ ਟੈਂਪਲੇਟ](ਟੈਂਪਲੇਟ/gig-cymru-nhs-wales-ਦਾ-ਫੈਸਲਾ-ਰਿਕਾਰਡ-ਟੈਂਪਲੇਟ/)
- [Ignacio Larrañaga ਦਾ ਮਹੱਤਵਪੂਰਨ ਤਕਨੀਕੀ ਫੈਸਲਿਆਂ (ITD) ਲਈ ਫੈਸਲਾ ਰਿਕਾਰਡ ਟੈਂਪਲੇਟ](ਟੈਂਪਲੇਟ/ਮਹੱਤਵਪੂਰਨ-ਤਕਨੀਕੀ-ਫੈਸਲਿਆਂ-ਲਈ-ਫੈਸਲਾ-ਰਿਕਾਰਡ-ਟੈਂਪਲੇਟ/)

ਉਦਾਹਰਨਾਂ:

- [CSS ਫਰੇਮਵਰਕ](ਉਦਾਹਰਨਾਂ/css-ਫਰੇਮਵਰਕ/)
- [ਵਾਤਾਵਰਣ ਵੇਰੀਏਬਲ ਸੰਰਚਨਾ](ਉਦਾਹਰਨਾਂ/ਵਾਤਾਵਰਣ-ਵੇਰੀਏਬਲ-ਸੰਰਚਨਾ/)
- [ਮੈਟ੍ਰਿਕਸ, ਮਾਨੀਟਰ, ਅਲਰਟ](ਉਦਾਹਰਨਾਂ/ਮੈਟ੍ਰਿਕਸ-ਮਾਨੀਟਰ-ਅਲਰਟ/)
- [Microsoft Azure DevOps](ਉਦਾਹਰਨਾਂ/microsoft-azure-devops/)
- [ਮੋਨੋਰੈਪੋ ਬਨਾਮ ਮਲਟੀਰੈਪੋ](ਉਦਾਹਰਨਾਂ/ਮੋਨੋਰੈਪੋ-ਬਨਾਮ-ਮਲਟੀਰੈਪੋ/)
- [ਪ੍ਰੋਗਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ](ਉਦਾਹਰਨਾਂ/ਪ੍ਰੋਗਰਾਮਿੰਗ-ਭਾਸ਼ਾਵਾਂ/)
- [ਗੁਪਤ ਜਾਣਕਾਰੀ ਦੀ ਸਟੋਰੇਜ](ਉਦਾਹਰਨਾਂ/ਗੁਪਤ-ਜਾਣਕਾਰੀ-ਦੀ-ਸਟੋਰੇਜ/)
- [ਟਾਈਮਸਟੈਂਪ ਫਾਰਮੈਟ](ਉਦਾਹਰਨਾਂ/ਟਾਈਮਸਟੈਂਪ-ਫਾਰਮੈਟ/)
- [ਹੋਰ ਬਹੁਤ ਕੁਝ...](ਉਦਾਹਰਨਾਂ/)

## ਆਰਕੀਟੈਕਚਰ ਫੈਸਲਾ ਰਿਕਾਰਡ ਕੀ ਹੈ?

**ਆਰਕੀਟੈਕਚਰ ਫੈਸਲਾ ਰਿਕਾਰਡ** (ADR) ਇੱਕ ਅਜਿਹਾ ਦਸਤਾਵੇਜ਼ ਹੈ ਜੋ ਕਿਸੇ ਮਹੱਤਵਪੂਰਨ ਆਰਕੀਟੈਕਚਰ ਫੈਸਲੇ ਨੂੰ ਉਸ ਦੇ ਪ੍ਰਸੰਗ ਅਤੇ ਨਤੀਜਿਆਂ ਸਮੇਤ ਦਰਜ ਕਰਦਾ ਹੈ।

**ਆਰਕੀਟੈਕਚਰ ਫੈਸਲਾ** (AD) ਸਾਫਟਵੇਅਰ ਡਿਜ਼ਾਈਨ ਦੀ ਇੱਕ ਅਜਿਹੀ ਚੋਣ ਹੈ ਜੋ ਕਿਸੇ ਮਹੱਤਵਪੂਰਨ ਲੋੜ ਨੂੰ ਪੂਰਾ ਕਰਦੀ ਹੈ।

**ਆਰਕੀਟੈਕਚਰ ਫੈਸਲਾ ਲੌਗ** (ADL) ਕਿਸੇ ਖਾਸ ਪ੍ਰੋਜੈਕਟ (ਜਾਂ ਸੰਸਥਾ) ਲਈ ਬਣਾਏ ਅਤੇ ਸੰਭਾਲੇ ਗਏ ਸਾਰੇ ADR ਦਾ ਸੰਗ੍ਰਹਿ ਹੈ।

**ਆਰਕੀਟੈਕਚਰ ਪੱਖੋਂ ਮਹੱਤਵਪੂਰਨ ਲੋੜ** (ASR) ਉਹ ਲੋੜ ਹੈ ਜਿਸ ਦਾ ਸਾਫਟਵੇਅਰ ਸਿਸਟਮ ਦੇ ਆਰਕੀਟੈਕਚਰ ਉੱਤੇ ਮਾਪਣਯੋਗ ਪ੍ਰਭਾਵ ਪੈਂਦਾ ਹੈ।

ਇਹ ਸਭ **ਆਰਕੀਟੈਕਚਰ ਗਿਆਨ ਪ੍ਰਬੰਧਨ** (AKM) ਦੇ ਵਿਸ਼ੇ ਅਧੀਨ ਆਉਂਦੇ ਹਨ।

ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਉਦੇਸ਼ ADR ਦੀ ਤੇਜ਼ ਜਾਣ-ਪਛਾਣ ਦੇਣਾ ਹੈ: ਇਨ੍ਹਾਂ ਨੂੰ ਕਿਵੇਂ ਬਣਾਇਆ ਜਾਵੇ ਅਤੇ ਹੋਰ ਜਾਣਕਾਰੀ ਕਿੱਥੇ ਮਿਲੇਗੀ।

ਸੰਖੇਪ ਰੂਪ:

  * **AD**: ਆਰਕੀਟੈਕਚਰ ਫੈਸਲਾ

  * **ADL**: ਆਰਕੀਟੈਕਚਰ ਫੈਸਲਾ ਲੌਗ

  * **ADR**: ਆਰਕੀਟੈਕਚਰ ਫੈਸਲਾ ਰਿਕਾਰਡ

  * **AKM**: ਆਰਕੀਟੈਕਚਰ ਗਿਆਨ ਪ੍ਰਬੰਧਨ

  * **ASR**: ਆਰਕੀਟੈਕਚਰ ਪੱਖੋਂ ਮਹੱਤਵਪੂਰਨ ਲੋੜ

## ADR ਵਰਤਣਾ ਕਿਵੇਂ ਸ਼ੁਰੂ ਕਰੀਏ

ADR ਵਰਤਣਾ ਸ਼ੁਰੂ ਕਰਨ ਲਈ, ਆਪਣੇ ਸਾਥੀਆਂ ਨਾਲ ਇਨ੍ਹਾਂ ਖੇਤਰਾਂ ਬਾਰੇ ਗੱਲ ਕਰੋ।

ਫੈਸਲੇ ਦੀ ਪਛਾਣ:

  * AD ਕਿੰਨਾ ਜ਼ਰੂਰੀ ਅਤੇ ਕਿੰਨਾ ਮਹੱਤਵਪੂਰਨ ਹੈ?

  * ਕੀ ਇਹ ਹੁਣੇ ਲੈਣਾ ਪਵੇਗਾ, ਜਾਂ ਹੋਰ ਜਾਣਕਾਰੀ ਮਿਲਣ ਤੱਕ ਉਡੀਕ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ?

  * ਨਿੱਜੀ ਅਤੇ ਸਾਂਝਾ ਤਜਰਬਾ, ਅਤੇ ਨਾਲ ਹੀ ਮੰਨੇ-ਪ੍ਰਮੰਨੇ ਡਿਜ਼ਾਈਨ ਤਰੀਕੇ ਅਤੇ ਅਭਿਆਸ, ਫੈਸਲੇ ਦੀ ਪਛਾਣ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦੇ ਹਨ।

  * ਆਦਰਸ਼ ਤੌਰ ਉੱਤੇ ਇੱਕ ਫੈਸਲਿਆਂ ਦੀ ਕਰਨਯੋਗ ਸੂਚੀ ਰੱਖੋ ਜੋ ਉਤਪਾਦ ਦੀ ਕਰਨਯੋਗ ਸੂਚੀ ਦੀ ਪੂਰਕ ਹੋਵੇ।

ਫੈਸਲਾ ਲੈਣਾ:

  * ਫੈਸਲੇ ਲੈਣ ਦੀਆਂ ਕਈ ਤਕਨੀਕਾਂ ਮੌਜੂਦ ਹਨ, ਆਮ ਵੀ ਅਤੇ ਸਾਫਟਵੇਅਰ ਆਰਕੀਟੈਕਚਰ ਲਈ ਖਾਸ ਵੀ, ਜਿਵੇਂ ਕਿ ਡਾਇਲਾਗ ਮੈਪਿੰਗ।

  * ਸਮੂਹਕ ਫੈਸਲਾ ਲੈਣਾ ਖੋਜ ਦਾ ਇੱਕ ਸਰਗਰਮ ਵਿਸ਼ਾ ਹੈ।

ਫੈਸਲੇ ਨੂੰ ਲਾਗੂ ਕਰਨਾ ਅਤੇ ਪਾਲਣਾ ਕਰਵਾਉਣਾ:

  * AD ਸਾਫਟਵੇਅਰ ਡਿਜ਼ਾਈਨ ਵਿੱਚ ਵਰਤੇ ਜਾਂਦੇ ਹਨ; ਇਸ ਲਈ ਇਨ੍ਹਾਂ ਨੂੰ ਸਿਸਟਮ ਦੇ ਉਨ੍ਹਾਂ ਹਿੱਸੇਦਾਰਾਂ ਤੱਕ ਪਹੁੰਚਾਉਣਾ ਅਤੇ ਉਨ੍ਹਾਂ ਤੋਂ ਮਨਜ਼ੂਰ ਕਰਵਾਉਣਾ ਜ਼ਰੂਰੀ ਹੈ ਜੋ ਇਸ ਲਈ ਫੰਡ ਦਿੰਦੇ ਹਨ, ਇਸ ਨੂੰ ਵਿਕਸਿਤ ਕਰਦੇ ਹਨ ਅਤੇ ਚਲਾਉਂਦੇ ਹਨ।

  * ਆਰਕੀਟੈਕਚਰ ਪੱਖੋਂ ਸਪੱਸ਼ਟ ਕੋਡਿੰਗ ਸ਼ੈਲੀਆਂ ਅਤੇ ਕੋਡ ਸਮੀਖਿਆਵਾਂ, ਜੋ ਆਰਕੀਟੈਕਚਰ ਸੰਬੰਧੀ ਚਿੰਤਾਵਾਂ ਅਤੇ ਫੈਸਲਿਆਂ ਉੱਤੇ ਧਿਆਨ ਦਿੰਦੀਆਂ ਹਨ, ਦੋ ਸੰਬੰਧਿਤ ਅਭਿਆਸ ਹਨ।

  * ਸਾਫਟਵੇਅਰ ਦੇ ਵਿਕਾਸ ਦੌਰਾਨ ਕਿਸੇ ਸਾਫਟਵੇਅਰ ਸਿਸਟਮ ਦਾ ਆਧੁਨਿਕੀਕਰਨ ਕਰਦੇ ਸਮੇਂ ਵੀ AD ਉੱਤੇ (ਦੁਬਾਰਾ) ਵਿਚਾਰ ਕਰਨਾ ਪੈਂਦਾ ਹੈ।

ਫੈਸਲੇ ਸਾਂਝੇ ਕਰਨਾ (ਵਿਕਲਪਿਕ):

  * ਬਹੁਤ ਸਾਰੇ AD ਕਈ ਪ੍ਰੋਜੈਕਟਾਂ ਵਿੱਚ ਦੁਹਰਾਏ ਜਾਂਦੇ ਹਨ।

  * ਇਸ ਲਈ, ਜਦੋਂ ਸਪੱਸ਼ਟ ਗਿਆਨ ਪ੍ਰਬੰਧਨ ਰਣਨੀਤੀ ਅਪਣਾਈ ਜਾਂਦੀ ਹੈ, ਤਾਂ ਪਿਛਲੇ ਫੈਸਲਿਆਂ ਦੇ ਚੰਗੇ ਅਤੇ ਮਾੜੇ ਦੋਵੇਂ ਤਜਰਬੇ ਮੁੜ ਵਰਤੋਂ ਯੋਗ ਕੀਮਤੀ ਸਰੋਤ ਬਣ ਸਕਦੇ ਹਨ।

ਫੈਸਲੇ ਦਾ ਦਸਤਾਵੇਜ਼ੀਕਰਨ:

  * ਫੈਸਲੇ ਦਰਜ ਕਰਨ ਲਈ ਬਹੁਤ ਸਾਰੇ ਟੈਂਪਲੇਟ ਅਤੇ ਟੂਲ ਮੌਜੂਦ ਹਨ।

  * ਐਜਾਇਲ ਭਾਈਚਾਰਿਆਂ ਨੂੰ ਵੇਖੋ, ਜਿਵੇਂ ਕਿ M. Nygard ਦੇ ADR।

  * ਰਵਾਇਤੀ ਸਾਫਟਵੇਅਰ ਇੰਜੀਨੀਅਰਿੰਗ ਅਤੇ ਆਰਕੀਟੈਕਚਰ ਡਿਜ਼ਾਈਨ ਪ੍ਰਕਿਰਿਆਵਾਂ ਨੂੰ ਵੇਖੋ, ਜਿਵੇਂ ਕਿ IBM UMF ਅਤੇ CapitalOne ਦੇ Tyree ਅਤੇ Akerman ਵੱਲੋਂ ਸੁਝਾਏ ਗਏ ਸਾਰਣੀ ਖਾਕੇ।

ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ:

  * ਉੱਪਰ ਦਿੱਤੇ ਕਦਮ Wikipedia ਦੀ [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision) ਐਂਟਰੀ ਤੋਂ ਲਏ ਗਏ ਹਨ

## ਟੂਲਾਂ ਨਾਲ ADR ਵਰਤਣਾ ਕਿਵੇਂ ਸ਼ੁਰੂ ਕਰੀਏ

- [MySpec](https://myspec.dev) — ਸਵੈਚਾਲਿਤ ਨਿਰਧਾਰਨ ਅਤੇ ਆਰਕੀਟੈਕਚਰ ਫੈਸਲਾ ਪਲੇਟਫਾਰਮ, ਜੋ ਪ੍ਰੋਜੈਕਟ ਸੰਵਿਧਾਨ, ਤਕਨੀਕੀ ਆਰਕੀਟੈਕਚਰ ਅਤੇ ADR ਨੂੰ ਸਾਫ਼-ਸੁਥਰੇ Markdown ਵਿੱਚ ਢਾਲ ਕੇ MCP ਰਾਹੀਂ ਪੇਸ਼ ਕਰਦਾ ਹੈ।

ਤੁਸੀਂ ਟੂਲਾਂ ਨਾਲ ADR ਵਰਤਣਾ ਜਿਵੇਂ ਚਾਹੋ ਸ਼ੁਰੂ ਕਰ ਸਕਦੇ ਹੋ।

ਉਦਾਹਰਨ ਲਈ:

  * ਜੇ ਤੁਹਾਨੂੰ Google Drive ਅਤੇ ਔਨਲਾਈਨ ਸੰਪਾਦਨ ਪਸੰਦ ਹੈ, ਤਾਂ ਤੁਸੀਂ ਇੱਕ Google Doc ਜਾਂ Google Sheet ਬਣਾ ਸਕਦੇ ਹੋ।

  * ਜੇ ਤੁਹਾਨੂੰ ਸੋਰਸ ਕੋਡ ਵਰਜਨ ਕੰਟਰੋਲ, ਜਿਵੇਂ ਕਿ git, ਪਸੰਦ ਹੈ, ਤਾਂ ਤੁਸੀਂ ਹਰ ADR ਲਈ ਇੱਕ ਫਾਈਲ ਬਣਾ ਸਕਦੇ ਹੋ।

  * ਜੇ ਤੁਹਾਨੂੰ ਪ੍ਰੋਜੈਕਟ ਯੋਜਨਾਬੰਦੀ ਦੇ ਟੂਲ, ਜਿਵੇਂ ਕਿ Atlassian Jira, ਪਸੰਦ ਹਨ, ਤਾਂ ਤੁਸੀਂ ਉਸ ਟੂਲ ਦਾ ਯੋਜਨਾ ਟਰੈਕਰ ਵਰਤ ਸਕਦੇ ਹੋ।

  * ਜੇ ਤੁਹਾਨੂੰ ਵਿਕੀ, ਜਿਵੇਂ ਕਿ MediaWiki, ਪਸੰਦ ਹਨ, ਤਾਂ ਤੁਸੀਂ ਇੱਕ ADR ਵਿਕੀ ਬਣਾ ਸਕਦੇ ਹੋ।

## git ਨਾਲ ADR ਵਰਤਣਾ ਕਿਵੇਂ ਸ਼ੁਰੂ ਕਰੀਏ

ਜੇ ਤੁਹਾਨੂੰ git ਵਰਜਨ ਕੰਟਰੋਲ ਪਸੰਦ ਹੈ, ਤਾਂ ਸੋਰਸ ਕੋਡ ਵਾਲੇ ਇੱਕ ਆਮ ਸਾਫਟਵੇਅਰ ਪ੍ਰੋਜੈਕਟ ਲਈ ਅਸੀਂ git ਨਾਲ ADR ਵਰਤਣਾ ਇਸ ਤਰ੍ਹਾਂ ਸ਼ੁਰੂ ਕਰਨਾ ਪਸੰਦ ਕਰਦੇ ਹਾਂ।

ADR ਫਾਈਲਾਂ ਲਈ ਇੱਕ ਡਾਇਰੈਕਟਰੀ ਬਣਾਓ:

```sh
$ mkdir adr
```

ਹਰ ADR ਲਈ ਇੱਕ ਟੈਕਸਟ ਫਾਈਲ ਬਣਾਓ, ਜਿਵੇਂ ਕਿ `choose-database.md`:

```sh
$ vi choose-database.md
```

ADR ਵਿੱਚ ਜੋ ਚਾਹੋ ਲਿਖੋ। ਵਿਚਾਰਾਂ ਲਈ ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਦੇ ਟੈਂਪਲੇਟ ਵੇਖੋ।

ADR ਨੂੰ ਆਪਣੇ git ਰਿਪੋ ਵਿੱਚ ਕਮਿਟ ਕਰੋ।

## ADR ਲਈ Claude Code ਸਕਿੱਲ

ਇਹ ਰਿਪੋਜ਼ਟਰੀ [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/) ਹੇਠ ਦੋ [Claude Code](https://claude.com/claude-code) ਸਕਿੱਲ ਦਿੰਦੀ ਹੈ, ਤਾਂ ਜੋ ਇੱਕ AI ਕੋਡਿੰਗ ਏਜੰਟ ADR ਉਸ ਤਰ੍ਹਾਂ ਲਿਖ ਅਤੇ ਸੰਭਾਲ ਸਕੇ ਜਿਵੇਂ ਇਹ ਪ੍ਰੋਜੈਕਟ ਸਿਫ਼ਾਰਸ਼ ਕਰਦਾ ਹੈ:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — ਆਮ ਵਰਤੋਂ ਲਈ, ਕਿਸੇ ਵੀ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ADR ਲਿਖਣ ਵਾਲੇ ਹਰ ਕਿਸੇ ਲਈ। ਇਹ ਤੈਅ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ ਕਿ ਕੀ ਕਿਸੇ ਫੈਸਲੇ ਨੂੰ ADR ਦੀ ਲੋੜ ਹੈ, `adr/` ਜਾਂ `decisions/` ਡਾਇਰੈਕਟਰੀ ਸਥਾਪਿਤ ਕਰਦਾ ਹੈ, ਫਾਈਲ ਦਾ ਨਾਮ ਰੱਖਦਾ ਹੈ, ਗਿਆਰਾਂ ਨਾਲ ਦਿੱਤੇ ਢਾਂਚਿਆਂ ਵਿੱਚੋਂ ਇੱਕ ਟੈਂਪਲੇਟ ਚੁਣਦਾ ਹੈ, ਅਤੇ ਪ੍ਰਸੰਗ/ਫੈਸਲਾ/ਨਤੀਜੇ ਭਾਗ ਚੰਗੀ ਤਰ੍ਹਾਂ ਲਿਖਦਾ ਹੈ।

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — ਖਾਸ ਤੌਰ ਉੱਤੇ ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਦੇ ਸੰਭਾਲਕਰਤਾਵਾਂ ਲਈ। ਇਹ ਰਿਪੋਜ਼ਟਰੀ ਦੀ ਬਣਤਰ, README/ਲੋਕੇਲ ਮਿਰਰਿੰਗ ਪਰੰਪਰਾ, ਅਤੇ ਨਵਾਂ ਟੈਂਪਲੇਟ, ਉਦਾਹਰਨ ਜਾਂ ਟੂਲ ਲਿੰਕ ਜੋੜਨ ਦੇ ਠੀਕ-ਠੀਕ ਕਦਮ ਦਸਤਾਵੇਜ਼ੀ ਰੂਪ ਵਿੱਚ ਦਿੰਦਾ ਹੈ।

ਕਿਸੇ ਸਕਿੱਲ ਨੂੰ ਵਰਤਣ ਲਈ, ਉਸ ਦੇ ਫੋਲਡਰ ਦੀ ਨਕਲ ਉਸ ਰਿਪੋਜ਼ਟਰੀ ਦੀ ਜੜ੍ਹ ਵਿੱਚ `.claude/skills/` ਵਿੱਚ ਕਰੋ ਜਿਸ ਵਿੱਚ ਤੁਸੀਂ ਕੰਮ ਕਰ ਰਹੇ ਹੋ (ਜਾਂ ਇਸ ਨੂੰ ਹਰ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਉਪਲਬਧ ਕਰਾਉਣ ਲਈ `~/.claude/skills/` ਵਿੱਚ), ਫਿਰ Claude Code ਨੂੰ ADR ਲਿਖਣ ਜਾਂ ਸਮੀਖਿਆ ਕਰਨ ਲਈ ਕਹੋ।

## ADR ਲਈ ਫਾਈਲ ਨਾਮ ਪਰੰਪਰਾਵਾਂ

ਜੇ ਤੁਸੀਂ ਆਪਣੇ ADR ਆਮ ਟੈਕਸਟ ਫਾਈਲਾਂ ਵਿੱਚ ਬਣਾਉਣ ਦੀ ਚੋਣ ਕਰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ADR ਫਾਈਲ ਨਾਮ ਲਈ ਆਪਣੀ ਪਰੰਪਰਾ ਬਣਾਉਣਾ ਚਾਹੋਗੇ।

ਅਸੀਂ ਇੱਕ ਖਾਸ ਫਾਰਮੈਟ ਵਾਲੀ ਫਾਈਲ ਨਾਮ ਪਰੰਪਰਾ ਵਰਤਣਾ ਪਸੰਦ ਕਰਦੇ ਹਾਂ।

ਉਦਾਹਰਨਾਂ:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

ਸਾਡੀ ਫਾਈਲ ਨਾਮ ਪਰੰਪਰਾ:

  * ਨਾਮ ਵਿੱਚ ਵਰਤਮਾਨ ਕਾਲ ਦੀ ਹੁਕਮੀ ਕਿਰਿਆ ਵਾਕੰਸ਼ ਹੁੰਦਾ ਹੈ। ਇਹ ਪੜ੍ਹਨਯੋਗਤਾ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ ਅਤੇ ਸਾਡੇ ਕਮਿਟ ਸੁਨੇਹੇ ਦੇ ਫਾਰਮੈਟ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ।

  * ਨਾਮ ਵਿੱਚ ਛੋਟੇ ਅੱਖਰ ਅਤੇ ਡੈਸ਼ ਵਰਤੇ ਜਾਂਦੇ ਹਨ (ਇਸ ਰਿਪੋ ਵਾਂਗ)। ਇਹ ਪੜ੍ਹਨਯੋਗਤਾ ਅਤੇ ਸਿਸਟਮ ਦੀ ਵਰਤੋਂਯੋਗਤਾ ਵਿਚਕਾਰ ਸੰਤੁਲਨ ਹੈ।

  * ਐਕਸਟੈਂਸ਼ਨ markdown ਹੈ। ਇਹ ਆਸਾਨ ਫਾਰਮੈਟਿੰਗ ਲਈ ਲਾਭਦਾਇਕ ਹੋ ਸਕਦਾ ਹੈ।

## ਚੰਗੇ ADR ਲਿਖਣ ਲਈ ਸੁਝਾਅ

ਚੰਗੇ ADR ਦੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ:

* ਤਰਕ-ਆਧਾਰ: ਕਿਸੇ ਖਾਸ AD ਨੂੰ ਅਪਣਾਉਣ ਦੇ ਕਾਰਨ ਦੱਸੋ। ਇਸ ਵਿੱਚ ਪ੍ਰਸੰਗ (ਹੇਠਾਂ ਵੇਖੋ), ਵੱਖ-ਵੱਖ ਸੰਭਾਵੀ ਚੋਣਾਂ ਦੇ ਫਾਇਦੇ ਅਤੇ ਨੁਕਸਾਨ, ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦੀ ਤੁਲਨਾ, ਲਾਗਤ/ਲਾਭ ਦੀ ਚਰਚਾ ਅਤੇ ਹੋਰ ਬਹੁਤ ਕੁਝ ਸ਼ਾਮਲ ਹੋ ਸਕਦਾ ਹੈ।

* ਖਾਸ: ਹਰ ADR ਇੱਕ AD ਬਾਰੇ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ, ਕਈ AD ਬਾਰੇ ਨਹੀਂ।

* ਟਾਈਮਸਟੈਂਪ: ਪਛਾਣ ਕਰੋ ਕਿ ADR ਦੀ ਹਰ ਗੱਲ ਕਦੋਂ ਲਿਖੀ ਗਈ। ਇਹ ਖਾਸ ਤੌਰ ਉੱਤੇ ਉਨ੍ਹਾਂ ਪਹਿਲੂਆਂ ਲਈ ਮਹੱਤਵਪੂਰਨ ਹੈ ਜੋ ਸਮੇਂ ਨਾਲ ਬਦਲ ਸਕਦੇ ਹਨ, ਜਿਵੇਂ ਕਿ ਲਾਗਤਾਂ, ਸਮਾਂ-ਸਾਰਣੀਆਂ, ਸਕੇਲਿੰਗ ਅਤੇ ਇਸ ਤਰ੍ਹਾਂ ਦੀਆਂ ਹੋਰ ਚੀਜ਼ਾਂ।

* ਅਟੱਲ: ADR ਵਿੱਚ ਮੌਜੂਦਾ ਜਾਣਕਾਰੀ ਨੂੰ ਨਾ ਬਦਲੋ। ਇਸ ਦੀ ਬਜਾਏ, ਨਵੀਂ ਜਾਣਕਾਰੀ ਜੋੜ ਕੇ ADR ਵਿੱਚ ਸੋਧ ਕਰੋ, ਜਾਂ ਨਵਾਂ ADR ਬਣਾ ਕੇ ਪੁਰਾਣੇ ਨੂੰ ਬਦਲ ਦਿਓ।

ADR ਵਿੱਚ ਚੰਗੇ "ਪ੍ਰਸੰਗ" ਭਾਗ ਦੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ:

* ਆਪਣੀ ਸੰਸਥਾ ਦੀ ਸਥਿਤੀ ਅਤੇ ਕਾਰੋਬਾਰੀ ਤਰਜੀਹਾਂ ਦੱਸੋ।

* ਆਪਣੀਆਂ ਟੀਮਾਂ ਦੀ ਸਮਾਜਿਕ ਬਣਤਰ ਅਤੇ ਹੁਨਰਾਂ ਦੀ ਬਣਤਰ ਉੱਤੇ ਆਧਾਰਿਤ ਤਰਕ ਅਤੇ ਵਿਚਾਰ ਸ਼ਾਮਲ ਕਰੋ।

* ਸੰਬੰਧਿਤ ਫਾਇਦੇ ਅਤੇ ਨੁਕਸਾਨ ਸ਼ਾਮਲ ਕਰੋ, ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਬਿਆਨ ਕਰੋ ਕਿ ਉਹ ਤੁਹਾਡੀਆਂ ਲੋੜਾਂ ਅਤੇ ਟੀਚਿਆਂ ਨਾਲ ਮੇਲ ਖਾਣ।

ADR ਵਿੱਚ ਚੰਗੇ "ਨਤੀਜੇ" ਭਾਗ ਦੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ:

* ਦੱਸੋ ਕਿ ਫੈਸਲਾ ਲੈਣ ਤੋਂ ਬਾਅਦ ਕੀ ਹੁੰਦਾ ਹੈ। ਇਸ ਵਿੱਚ ਪ੍ਰਭਾਵ, ਨਤੀਜੇ, ਆਉਟਪੁੱਟ, ਅਗਲੇਰੀ ਕਾਰਵਾਈ ਅਤੇ ਹੋਰ ਬਹੁਤ ਕੁਝ ਸ਼ਾਮਲ ਹੋ ਸਕਦਾ ਹੈ।

* ਬਾਅਦ ਦੇ ਕਿਸੇ ਵੀ ADR ਬਾਰੇ ਜਾਣਕਾਰੀ ਸ਼ਾਮਲ ਕਰੋ। ਇਹ ਕਾਫ਼ੀ ਆਮ ਹੈ ਕਿ ਇੱਕ ADR ਹੋਰ ADR ਦੀ ਲੋੜ ਪੈਦਾ ਕਰ ਦਿੰਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਜਦੋਂ ਇੱਕ ADR ਕੋਈ ਵੱਡੀ ਸਮੁੱਚੀ ਚੋਣ ਕਰਦਾ ਹੈ, ਜੋ ਅੱਗੇ ਹੋਰ ਛੋਟੇ ਫੈਸਲਿਆਂ ਦੀ ਲੋੜ ਪੈਦਾ ਕਰਦੀ ਹੈ।

* ਕੋਈ ਵੀ ਕਾਰਵਾਈ ਤੋਂ ਬਾਅਦ ਦੀ ਸਮੀਖਿਆ ਪ੍ਰਕਿਰਿਆ ਸ਼ਾਮਲ ਕਰੋ। ਟੀਮਾਂ ਲਈ ਹਰ ADR ਦੀ ਇੱਕ ਮਹੀਨੇ ਬਾਅਦ ਸਮੀਖਿਆ ਕਰਨਾ ਆਮ ਗੱਲ ਹੈ, ਤਾਂ ਜੋ ADR ਦੀ ਜਾਣਕਾਰੀ ਦੀ ਅਸਲ ਅਭਿਆਸ ਵਿੱਚ ਜੋ ਹੋਇਆ ਉਸ ਨਾਲ ਤੁਲਨਾ ਕਰਕੇ ਸਿੱਖਿਆ ਅਤੇ ਤਰੱਕੀ ਕੀਤੀ ਜਾ ਸਕੇ।

ਨਵਾਂ ADR ਪਿਛਲੇ ADR ਦੀ ਥਾਂ ਲੈ ਸਕਦਾ ਹੈ:

* ਜਦੋਂ ਕੋਈ AD ਲਿਆ ਜਾਂਦਾ ਹੈ ਜੋ ਪਿਛਲੇ ADR ਨੂੰ ਬਦਲਦਾ ਜਾਂ ਅਯੋਗ ਕਰਦਾ ਹੈ, ਤਾਂ ਇੱਕ ਨਵਾਂ ADR ਬਣਾਇਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ

## ADR ਉਦਾਹਰਨ ਟੈਂਪਲੇਟ

ADR ਉਦਾਹਰਨ ਟੈਂਪਲੇਟ ਜੋ ਅਸੀਂ ਨੈੱਟ ਤੋਂ ਇਕੱਠੇ ਕੀਤੇ ਹਨ:

- [Michael Nygard ਦਾ ADR ਟੈਂਪਲੇਟ](ਟੈਂਪਲੇਟ/ਮਾਈਕਲ-ਨਾਈਗਾਰਡ-ਦਾ-ਫੈਸਲਾ-ਰਿਕਾਰਡ-ਟੈਂਪਲੇਟ/) (ਸਾਦਾ ਅਤੇ ਪ੍ਰਸਿੱਧ)

- [Jeff Tyree ਅਤੇ Art Akerman ਦਾ ADR ਟੈਂਪਲੇਟ](ਟੈਂਪਲੇਟ/ਜੈਫ-ਟਾਇਰੀ-ਅਤੇ-ਆਰਟ-ਅਕਰਮੈਨ-ਦਾ-ਫੈਸਲਾ-ਰਿਕਾਰਡ-ਟੈਂਪਲੇਟ/) (ਵਧੇਰੇ ਗੁੰਝਲਦਾਰ)

- [ਅਲੈਗਜ਼ੈਂਡਰੀਅਨ ਪੈਟਰਨ ਲਈ ADR ਟੈਂਪਲੇਟ](ਟੈਂਪਲੇਟ/ਅਲੈਗਜ਼ੈਂਡਰੀਅਨ-ਪੈਟਰਨ-ਲਈ-ਫੈਸਲਾ-ਰਿਕਾਰਡ-ਟੈਂਪਲੇਟ/) (ਪ੍ਰਸੰਗ ਦੇ ਵੇਰਵਿਆਂ ਸਮੇਤ ਸਾਦਾ)

- [ਕਾਰੋਬਾਰੀ ਕੇਸ ਲਈ ADR ਟੈਂਪਲੇਟ](ਟੈਂਪਲੇਟ/ਕਾਰੋਬਾਰੀ-ਕੇਸ-ਲਈ-ਫੈਸਲਾ-ਰਿਕਾਰਡ-ਟੈਂਪਲੇਟ/) (ਵਧੇਰੇ MBA-ਮੁਖੀ, ਲਾਗਤਾਂ, SWOT ਅਤੇ ਹੋਰ ਰਾਵਾਂ ਸਮੇਤ)

- [Markdown Any Decision Records (MADR) ਪ੍ਰੋਜੈਕਟ ਦਾ ADR ਟੈਂਪਲੇਟ](ਟੈਂਪਲੇਟ/madr-ਪ੍ਰੋਜੈਕਟ-ਦਾ-ਫੈਸਲਾ-ਰਿਕਾਰਡ-ਟੈਂਪਲੇਟ/) (ਸਾਦਾ ਅਤੇ ਵਿਸਤ੍ਰਿਤ ਦੋਵੇਂ ਸੰਸਕਰਨ; ਬਾਅਦ ਵਾਲਾ ਵਿਕਲਪਾਂ ਅਤੇ ਉਨ੍ਹਾਂ ਦੇ ਫਾਇਦਿਆਂ ਤੇ ਨੁਕਸਾਨਾਂ ਉੱਤੇ ਜ਼ੋਰ ਦਿੰਦਾ ਹੈ)

- [Planguage ਵਰਤਦਾ ADR ਟੈਂਪਲੇਟ](ਟੈਂਪਲੇਟ/planguage-ਵਰਤਦਾ-ਫੈਸਲਾ-ਰਿਕਾਰਡ-ਟੈਂਪਲੇਟ/) (ਵਧੇਰੇ ਗੁਣਵੱਤਾ ਭਰੋਸਾ-ਮੁਖੀ)

- [Ignacio Larrañaga ਦਾ ਮਹੱਤਵਪੂਰਨ ਤਕਨੀਕੀ ਫੈਸਲਿਆਂ (ITD) ਲਈ ਟੈਂਪਲੇਟ](ਟੈਂਪਲੇਟ/ਮਹੱਤਵਪੂਰਨ-ਤਕਨੀਕੀ-ਫੈਸਲਿਆਂ-ਲਈ-ਫੈਸਲਾ-ਰਿਕਾਰਡ-ਟੈਂਪਲੇਟ/) (ਲੀਨ ਅਤੇ ਫੈਸਲਾ-ਪਹਿਲਾਂ, ਕਾਰਜਕਾਰੀ ਪੱਧਰ ਦੀ ਤੇਜ਼ ਸਮੀਖਿਆ ਲਈ ਅਨੁਕੂਲਿਤ)

## ADR ਲਈ ਟੀਮ ਵਰਕ ਸਲਾਹ

ਜੇ ਤੁਸੀਂ ਆਪਣੀ ਟੀਮ ਨਾਲ ਫੈਸਲਾ ਰਿਕਾਰਡ ਵਰਤਣ ਬਾਰੇ ਸੋਚ ਰਹੇ ਹੋ, ਤਾਂ ਇੱਥੇ ਉਹ ਸਲਾਹ ਹੈ ਜੋ ਅਸੀਂ ਕਈ ਟੀਮਾਂ ਨਾਲ ਕੰਮ ਕਰਕੇ ਸਿੱਖੀ ਹੈ।

ਤੁਹਾਡੇ ਕੋਲ ਆਪਣੇ ਸਾਥੀਆਂ ਦੀ ਅਗਵਾਈ ਕਰਨ ਦਾ ਮੌਕਾ ਹੈ: "ਕੀ" ਥੋਪਣ ਦੀ ਬਜਾਏ "ਕਿਉਂ" ਬਾਰੇ ਮਿਲ ਕੇ ਗੱਲ ਕਰੋ। ਉਦਾਹਰਨ ਲਈ, ਫੈਸਲਾ ਰਿਕਾਰਡ ਟੀਮਾਂ ਲਈ ਵਧੇਰੇ ਸਮਝਦਾਰੀ ਨਾਲ ਸੋਚਣ ਅਤੇ ਬਿਹਤਰ ਸੰਚਾਰ ਕਰਨ ਦਾ ਤਰੀਕਾ ਹਨ; ਜੇ ਇਹ ਸਿਰਫ਼ ਕੰਮ ਤੋਂ ਬਾਅਦ ਜਬਰੀ ਕਰਵਾਈ ਜਾਂਦੀ ਕਾਗਜ਼ੀ ਕਾਰਵਾਈ ਦੀ ਲੋੜ ਬਣ ਜਾਣ, ਤਾਂ ਫੈਸਲਾ ਰਿਕਾਰਡ ਕੀਮਤੀ ਨਹੀਂ ਰਹਿੰਦੇ।

ਕੁਝ ਟੀਮਾਂ "ADR" ਸੰਖੇਪ ਰੂਪ ਦੀ ਬਜਾਏ "decisions" (ਫੈਸਲੇ) ਨਾਮ ਨੂੰ ਬਹੁਤ ਜ਼ਿਆਦਾ ਪਸੰਦ ਕਰਦੀਆਂ ਹਨ। ਜਦੋਂ ਕੁਝ ਟੀਮਾਂ "decisions" ਡਾਇਰੈਕਟਰੀ ਨਾਮ ਵਰਤਦੀਆਂ ਹਨ, ਤਾਂ ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਹੁੰਦਾ ਹੈ ਜਿਵੇਂ ਬੱਤੀ ਜਗ ਪਈ ਹੋਵੇ, ਅਤੇ ਟੀਮ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਵਧੇਰੇ ਜਾਣਕਾਰੀ ਪਾਉਣ ਲੱਗ ਪੈਂਦੀ ਹੈ, ਜਿਵੇਂ ਕਿ ਵਿਕਰੇਤਾ ਦੇ ਫੈਸਲੇ, ਯੋਜਨਾਬੰਦੀ ਦੇ ਫੈਸਲੇ, ਸਮਾਂ-ਸਾਰਣੀ ਦੇ ਫੈਸਲੇ ਆਦਿ। ਇਸ ਤਰ੍ਹਾਂ ਦੀ ਸਾਰੀ ਜਾਣਕਾਰੀ ਇੱਕੋ ਟੈਂਪਲੇਟ ਵਰਤ ਸਕਦੀ ਹੈ। ਸਾਡਾ ਅਨੁਮਾਨ ਹੈ ਕਿ ਲੋਕ ਸੰਖੇਪ ਰੂਪਾਂ ("ADR") ਦੀ ਬਜਾਏ ਸ਼ਬਦਾਂ ("decisions") ਨਾਲ ਤੇਜ਼ੀ ਨਾਲ ਸਿੱਖਦੇ ਹਨ, ਲੋਕ "ਰਿਕਾਰਡ" ਸ਼ਬਦ ਹਟਾਏ ਜਾਣ ਉੱਤੇ ਚੱਲ ਰਹੇ ਕੰਮ ਦੇ ਦਸਤਾਵੇਜ਼ ਲਿਖਣ ਲਈ ਵਧੇਰੇ ਪ੍ਰੇਰਿਤ ਹੁੰਦੇ ਹਨ, ਅਤੇ ਕੁਝ ਡਿਵੈਲਪਰਾਂ ਅਤੇ ਕੁਝ ਮੈਨੇਜਰਾਂ ਨੂੰ "ਆਰਕੀਟੈਕਚਰ" ਸ਼ਬਦ ਪਸੰਦ ਨਹੀਂ ਹੁੰਦਾ।

ਸਿਧਾਂਤ ਵਿੱਚ, ਅਟੱਲਤਾ ਆਦਰਸ਼ ਹੈ। ਅਭਿਆਸ ਵਿੱਚ, ਸਾਡੀਆਂ ਟੀਮਾਂ ਲਈ ਬਦਲਣਯੋਗਤਾ ਵਧੇਰੇ ਕਾਰਗਰ ਰਹੀ ਹੈ। ਅਸੀਂ ਨਵੀਂ ਜਾਣਕਾਰੀ ਮੌਜੂਦਾ ADR ਵਿੱਚ ਮਿਤੀ ਦੀ ਮੋਹਰ ਅਤੇ ਇਸ ਨੋਟ ਨਾਲ ਪਾਉਂਦੇ ਹਾਂ ਕਿ ਇਹ ਜਾਣਕਾਰੀ ਫੈਸਲੇ ਤੋਂ ਬਾਅਦ ਮਿਲੀ। ਇਸ ਤਰ੍ਹਾਂ ਦੀ ਪਹੁੰਚ ਇੱਕ "ਜਿਉਂਦੇ ਦਸਤਾਵੇਜ਼" ਵੱਲ ਲੈ ਜਾਂਦੀ ਹੈ ਜਿਸ ਨੂੰ ਅਸੀਂ ਸਾਰੇ ਅੱਪਡੇਟ ਕਰ ਸਕਦੇ ਹਾਂ। ਆਮ ਅੱਪਡੇਟ ਉਦੋਂ ਹੁੰਦੇ ਹਨ ਜਦੋਂ ਸਾਨੂੰ ਨਵੇਂ ਸਾਥੀਆਂ, ਨਵੀਆਂ ਪੇਸ਼ਕਸ਼ਾਂ, ਸਾਡੀ ਵਰਤੋਂ ਦੇ ਅਸਲ ਨਤੀਜਿਆਂ ਰਾਹੀਂ ਜਾਣਕਾਰੀ ਮਿਲਦੀ ਹੈ, ਜਾਂ ਫੈਸਲੇ ਤੋਂ ਬਾਅਦ ਤੀਜੀ ਧਿਰ ਦੀਆਂ ਤਬਦੀਲੀਆਂ ਹੁੰਦੀਆਂ ਹਨ, ਜਿਵੇਂ ਕਿ ਵਿਕਰੇਤਾ ਦੀਆਂ ਸਮਰੱਥਾਵਾਂ, ਕੀਮਤ ਯੋਜਨਾਵਾਂ, ਲਾਇਸੰਸ ਸਮਝੌਤੇ ਆਦਿ।

## ADR ਲਈ ਟੀਮ ਵਰਕ ਸਵਾਲ

### ADR ਕੌਣ ਬਣਾ ਸਕਦਾ ਹੈ?

ਖਾਸ ਵਿਅਕਤੀਆਂ, ਖਾਸ ਭੂਮਿਕਾਵਾਂ, ਖਾਸ ਟੀਮਾਂ ਜਾਂ ਖਾਸ ਵਿਭਾਗਾਂ ਵਰਗੇ ਖੇਤਰਾਂ ਬਾਰੇ ਵਿਚਾਰ ਕਰੋ; ਇਹ ਵੀ ਵਿਚਾਰ ਕਰੋ ਕਿ ਕੀ ਅਜਿਹੇ ਵਿਅਕਤੀ, ਭੂਮਿਕਾਵਾਂ, ਟੀਮਾਂ ਜਾਂ ਵਿਭਾਗ ਹਨ ਜੋ ADR ਦੀ ਫਰਮਾਇਸ਼ ਦੇ ਸਕਦੇ ਹਨ, ਯਾਨੀ ਉਹ ਇੱਕ ਅਜਿਹਾ ADR ਮੰਗਦੇ ਹਨ ਜੋ ਕੋਈ ਹੋਰ ਲਿਖੇਗਾ।

ਉਦਾਹਰਨ ਜਵਾਬ: ਸਾਡੀ ਸੰਸਥਾ ਦਾ ਕੋਈ ਵੀ ਵਿਅਕਤੀ ਜਿਸ ਨੇ ਆਰਕੀਟੈਕਚਰ ਫੈਸਲਾ ਰਿਕਾਰਡ ਦਾ README ਪੰਨਾ ਪੜ੍ਹਿਆ ਹੈ, ADR ਦਾ ਪ੍ਰਸਤਾਵ ਰੱਖ ਸਕਦਾ ਹੈ, ਯਾਨੀ ਉਹ ਵਿਅਕਤੀ ਇਸ ਨੂੰ ਲਿਖਣਾ ਸ਼ੁਰੂ ਕਰ ਸਕਦਾ ਹੈ ਅਤੇ ਟੀਮ ਨਾਲ ਸਾਂਝਾ ਕਰ ਸਕਦਾ ਹੈ।

### ADR ਸ਼ੁਰੂ ਕਰਨ ਨੂੰ ਕੀ ਜਾਇਜ਼ ਠਹਿਰਾਉਂਦਾ ਹੈ?

ਆਪਣੀ ਸੰਸਥਾ ਦੀਆਂ ਟੀਮਾਂ ਦੇ ਕੰਮ ਕਰਨ ਦੇ ਤਰੀਕੇ, ਤੁਹਾਡੇ ਸਾਫਟਵੇਅਰ ਸਿਸਟਮ ਦੀ ਬਣਤਰ, ਟੀਮਾਂ ਵਿਚਕਾਰ ਤਾਲਮੇਲ, ਲੰਬੇ ਸਮੇਂ ਦੀ ਸਾਂਭ-ਸੰਭਾਲ ਯੋਗਤਾ, ਬਾਹਰੀ ਇੰਟਰਫੇਸ, ਤੁਸੀਂ ਕਿਸ ਨੂੰ ਲਾਭ ਪਹੁੰਚਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਅਤੇ ਇਸ ਤਰ੍ਹਾਂ ਦੇ ਹੋਰ ਖੇਤਰਾਂ ਬਾਰੇ ਵਿਚਾਰ ਕਰੋ।

ਉਦਾਹਰਨ ਜਵਾਬ: ਅਸੀਂ ADR ਉਦੋਂ ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹਾਂ ਜਦੋਂ ਅਸੀਂ ਚਾਹੁੰਦੇ ਹਾਂ ਕਿ ਭਵਿੱਖ ਦੇ ਡਿਵੈਲਪਰ ਸਮਝਣ ਕਿ ਅਸੀਂ ਜੋ ਕਰ ਰਹੇ ਹਾਂ ਉਹ "ਕਿਉਂ" ਕਰ ਰਹੇ ਹਾਂ।

### ADR ਸ਼ੁਰੂ ਨਾ ਕਰਨ ਨੂੰ ਕੀ ਜਾਇਜ਼ ਠਹਿਰਾਉਂਦਾ ਹੈ?

ਉਨ੍ਹਾਂ ਫੈਸਲਿਆਂ ਵਰਗੇ ਖੇਤਰਾਂ ਬਾਰੇ ਵਿਚਾਰ ਕਰੋ ਜੋ ਆਰਕੀਟੈਕਚਰ ਬਾਰੇ ਨਹੀਂ ਹਨ, ਜਾਂ ਬਹੁਤ ਛੋਟੇ ਹਨ ਜਿਵੇਂ ਕਿ ਘੱਟੋ-ਘੱਟ ਜੋਖਮ ਵਾਲੇ, ਆਪਣੇ-ਆਪ ਵਿੱਚ ਪੂਰੇ ਜਾਂ ਇੱਕ ਡਿਵੈਲਪਰ ਦੇ ਫੈਸਲੇ, ਜਾਂ ਜੋ ਪਹਿਲਾਂ ਹੀ ਕਿਸੇ ਹੋਰ ਥਾਂ ਪੂਰੀ ਤਰ੍ਹਾਂ ਕਵਰ ਹਨ ਜਿਵੇਂ ਕਿ ਮਿਆਰਾਂ, ਨੀਤੀਆਂ ਜਾਂ ਦਸਤਾਵੇਜ਼ਾਂ ਵਿੱਚ, ਜਾਂ ਜੋ ਅਸਥਾਈ ਹਨ ਜਿਵੇਂ ਕਿ ਵਰਕਅਰਾਊਂਡ, ਸੰਕਲਪ ਦੇ ਸਬੂਤ ਜਾਂ ਪ੍ਰਯੋਗ।

ਉਦਾਹਰਨ ਜਵਾਬ: ਅਸੀਂ ADR ਛੱਡਣਾ ਚਾਹੁੰਦੇ ਹਾਂ ਜਦੋਂ ਕੋਈ ਫੈਸਲਾ ਦਾਇਰੇ, ਸਮੇਂ, ਜੋਖਮ ਅਤੇ ਲਾਗਤ ਵਿੱਚ ਸੀਮਤ ਹੋਵੇ, ਜਾਂ ਪਹਿਲਾਂ ਹੀ ਕਿਸੇ ਹੋਰ ਥਾਂ ਕਵਰ ਹੋਵੇ।

### ADR ਦਾ ਜੀਵਨ-ਚੱਕਰ ਕੀ ਹੈ?

ਸ਼ੁਰੂਆਤ ਦੀ ਪ੍ਰਕਿਰਿਆ, ਖੋਜ ਦੀ ਪ੍ਰਕਿਰਿਆ, ਫੈਸਲਾ ਲੈਣ ਦੀ ਪ੍ਰਕਿਰਿਆ, ਲਾਗੂ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਅਤੇ ਸਮਾਪਤੀ ਦੀ ਪ੍ਰਕਿਰਿਆ ਵਰਗੇ ਖੇਤਰਾਂ ਬਾਰੇ ਵਿਚਾਰ ਕਰੋ। ਇਸ ਬਾਰੇ ਵਿਚਾਰ ਕਰੋ ਕਿ ਸਮੇਂ ਦੇ ਨਾਲ ADR ਦੇ ਜੀਵਨ-ਚੱਕਰ ਨੂੰ ਕਿਵੇਂ ਟਰੈਕ ਕਰਨਾ ਹੈ, ਜਿਵੇਂ ਕਿ ADR ਨੂੰ ਇੱਕ ਅਵਸਥਾ ਤੋਂ ਅਗਲੀ ਅਵਸਥਾ ਵਿੱਚ ਕਿਵੇਂ ਲਿਜਾਣਾ ਹੈ, ਅਤੇ ਇਹ ਹਿੱਸੇਦਾਰਾਂ ਨੂੰ ਕਿਵੇਂ ਦੱਸਣਾ ਹੈ।

ਉਦਾਹਰਨ ਜਵਾਬ: ਅਸੀਂ ਚਾਹੁੰਦੇ ਹਾਂ ਕਿ ADR ਦੇ ਪੰਜ ਜੀਵਨ-ਚੱਕਰ ਪੜਾਅ ਹੋਣ: ਸ਼ੁਰੂਆਤ → ਖੋਜ → ਮੁਲਾਂਕਣ → ਲਾਗੂ ਕਰਨਾ → ਸਾਂਭ-ਸੰਭਾਲ → ਸਮਾਪਤੀ।

### ADR ਦੇ ਜੀਵਨ-ਚੱਕਰ ਦੇ ਕਦਮਾਂ ਲਈ ਮਾਪਦੰਡ ਕੀ ਹਨ?

ADR ਲਈ ਪ੍ਰਵਾਨਗੀ ਦੇ ਮਾਪਦੰਡ ਵਰਗੇ ਖੇਤਰਾਂ ਬਾਰੇ ਵਿਚਾਰ ਕਰੋ, ਯਾਨੀ ਤੁਹਾਨੂੰ ਕਿਵੇਂ ਪਤਾ ਲੱਗੇਗਾ ਕਿ ਇਹ ਇੱਕ ਜੀਵਨ-ਚੱਕਰ ਕਦਮ ਤੋਂ ਅਗਲੇ ਕਦਮ ਵਿੱਚ ਜਾਣ ਲਈ ਕਾਫ਼ੀ ਚੰਗਾ ਹੈ? ਕੀ ਸਮੱਸਿਆ ਸਪੱਸ਼ਟ ਤੌਰ ਉੱਤੇ ਬਿਆਨ ਕੀਤੀ ਗਈ ਹੈ? ਕੀ ਵਿਕਲਪਾਂ ਬਾਰੇ ਵਿਚਾਰ ਕੀਤਾ ਗਿਆ ਹੈ? ਕੀ ਸਮਝੌਤਿਆਂ ਨੂੰ ਚੰਗੀ ਤਰ੍ਹਾਂ ਸਮਝਿਆ ਅਤੇ ਦਰਜ ਕੀਤਾ ਗਿਆ ਹੈ?
ਕੀ ਸਾਰਾ ਸੰਬੰਧਿਤ ਪ੍ਰਸੰਗ ਮੌਜੂਦ ਹੈ? ਕੀ ਸਾਰੇ ਸੰਬੰਧਿਤ ਹਿੱਸੇਦਾਰ ਸ਼ਾਮਲ ਹਨ? ਕੀ ਸਾਰੀ ਪ੍ਰਤੀਕਿਰਿਆ ਸ਼ਾਮਲ ਕਰ ਲਈ ਗਈ ਹੈ?

ਉਦਾਹਰਨ ਜਵਾਬ: ਅਸੀਂ ਚਾਹੁੰਦੇ ਹਾਂ ਕਿ ADR ਉੱਤੇ ਹਿੱਸੇਦਾਰ ਵੋਟ ਪਾਉਣ ਜਦੋਂ ਸਰਗਰਮ ਟੀਮ ਨੇ 1) ਆਪਣੀ ਖੋਜ ਪੂਰੀ ਕਰ ਲਈ ਹੋਵੇ, 2) ਆਪਣਾ ਮੁਲਾਂਕਣ ਪੂਰਾ ਕਰ ਲਿਆ ਹੋਵੇ, 3) ADR ਪ੍ਰਸਤਾਵ ਨੂੰ ਟਿੱਪਣੀਆਂ ਦੀ ਬੇਨਤੀ ਅਤੇ ਇੱਕ ਹਫ਼ਤੇ ਦੀ ਸਮਾਂ-ਸੀਮਾ ਨਾਲ ਹਿੱਸੇਦਾਰਾਂ ਨੂੰ ਪ੍ਰਕਾਸ਼ਿਤ ਕਰ ਦਿੱਤਾ ਹੋਵੇ, 4) ਹਿੱਸੇਦਾਰਾਂ ਦੀਆਂ ਸਾਰੀਆਂ ਟਿੱਪਣੀਆਂ ਸ਼ਾਮਲ ਅਤੇ ਹੱਲ ਕਰ ਲਈਆਂ ਗਈਆਂ ਹੋਣ।

### ADR ਨਾਲ ਕਿਹੜੀਆਂ ਭੂਮਿਕਾਵਾਂ ਅਤੇ ਜ਼ਿੰਮੇਵਾਰੀਆਂ ਜੁੜੀਆਂ ਹਨ?

ਪ੍ਰਸਤਾਵਕ, ਖੋਜਕਰਤਾ, ਮੁਲਾਂਕਣਕਰਤਾ, ਸਮੀਖਿਅਕ, ਮਨਜ਼ੂਰੀ ਦੇਣ ਵਾਲਾ, ਸਾਂਭ-ਸੰਭਾਲ ਕਰਨ ਵਾਲਾ ਅਤੇ ਇਸ ਤਰ੍ਹਾਂ ਦੀਆਂ ਭੂਮਿਕਾਵਾਂ ਬਾਰੇ ਵਿਚਾਰ ਕਰੋ। ਹਿੱਸੇਦਾਰਾਂ ਨਾਲ ਸੰਚਾਰ, ਉਮੀਦਾਂ ਪੂਰੀਆਂ ਹੋਣ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਣਾ, ਵੈੱਬਸਾਈਟ ਜਾਂ ਇੰਟਰਾਨੈੱਟ ਉੱਤੇ ਸਾਂਝਾ ਕਰਨਾ, ਅਤੇ ਕੰਮ ਦੀ ਸਮੇਂ-ਸਮੇਂ ਉੱਤੇ ਸਮੀਖਿਆ ਕਰਨਾ, ਖਾਸ ਕਰਕੇ ਜਦੋਂ ਸੰਬੰਧਿਤ ਤਬਦੀਲੀਆਂ ਹੋਣ, ਵਰਗੀਆਂ ਜ਼ਿੰਮੇਵਾਰੀਆਂ ਬਾਰੇ ਵਿਚਾਰ ਕਰੋ।

ਉਦਾਹਰਨ ਜਵਾਬ: ਅਸੀਂ ਚਾਹੁੰਦੇ ਹਾਂ ਕਿ ਹਰ ADR ਦਾ ਹਮੇਸ਼ਾ ਇੱਕ ਪ੍ਰਾਇਮਰੀ ਸੰਪਰਕ ਵਿਅਕਤੀ, ਇੱਕ ਸੈਕੰਡਰੀ ਸੰਪਰਕ ਵਿਅਕਤੀ ਅਤੇ ਇੱਕ ਜਵਾਬਦੇਹ ਟੀਮ ਹੋਵੇ; ਇਹ ਸੰਚਾਰ, ਪ੍ਰਕਾਸ਼ਨ, ਸਾਂਭ-ਸੰਭਾਲ, ਘੱਟੋ-ਘੱਟ ਸਾਲ ਵਿੱਚ ਇੱਕ ਵਾਰ ਸਮੇਂ-ਸਮੇਂ ਉੱਤੇ ਸਮੀਖਿਆ, ਅਤੇ ਲੋੜ ਪੈਣ ਉੱਤੇ ਅੰਤ ਵਿੱਚ ਸਮਾਪਤੀ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਹਨ।

### ਸ਼ਾਸਨ-ਪ੍ਰਬੰਧ ADR ਨਾਲ ਕਿਵੇਂ ਜੁੜਿਆ ਹੈ?

ਆਪਣੀ ਸੰਸਥਾ ਦੇ ਕੰਮ ਕਰਨ ਦੇ ਤਰੀਕਿਆਂ, ਕਾਨੂੰਨੀ ਪੱਖਾਂ ਜਾਂ ਮਨੁੱਖੀ ਸਰੋਤ ਪੱਖਾਂ ਵਰਗੀਆਂ ਕਿਸੇ ਵੀ ਖਾਸ ਪਾਲਣਾ ਲੋੜਾਂ, ਅਤੇ ਸਹਿਮਤੀ ਬਨਾਮ ਟਕਰਾਅ ਬਨਾਮ ਉੱਚ-ਪੱਧਰ ਉੱਤੇ ਭੇਜਣ ਨੂੰ ਤੁਸੀਂ ਕਿਵੇਂ ਸੰਭਾਲਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਇਨ੍ਹਾਂ ਬਾਰੇ ਵਿਚਾਰ ਕਰੋ। ਕੀ ਅਜਿਹੇ ਖੇਤਰ, ਵਿਅਕਤੀ ਜਾਂ ਟੀਮਾਂ ਹਨ ਜਿਨ੍ਹਾਂ ਦਾ ADR ਬਾਰੇ ਦੂਜਿਆਂ ਨਾਲੋਂ ਵੱਧ ਪ੍ਰਭਾਵ ਹੋ ਸਕਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਉਸ ਨੂੰ ਮਨਜ਼ੂਰ ਕਰ ਸਕਣਾ, ਉਸ ਉੱਤੇ ਵੋਟ ਪਾ ਸਕਣਾ, ਜਾਂ ਉਸ ਨੂੰ ਵੀਟੋ ਕਰ ਸਕਣਾ?

ਉਦਾਹਰਨ ਜਵਾਬ: ADR ਦਾ ਸ਼ਾਸਨ-ਪ੍ਰਬੰਧ ਇਸ ਤਰਜੀਹੀ ਕ੍ਰਮ ਵਿੱਚ ਹੈ: CEO, CTO, CLO, ਉਹ ਟੀਮ ਜੋ ADR ਨੂੰ ਲਾਗੂ ਕਰਦੀ ਹੈ, ਅਤੇ ਟੀਮ ਦੇ ਉਹ ਮਾਹਰ ਜਿਨ੍ਹਾਂ ਨੂੰ AD ਬਾਰੇ ਸਭ ਤੋਂ ਵੱਧ ਜਾਣਕਾਰੀ ਹੈ। ਜਦੋਂ ਤੱਕ ADR ਵਿੱਚ ਵਰਣਨ ਨਾ ਕੀਤਾ ਗਿਆ ਹੋਵੇ, ਕਿਸੇ ਹੋਰ ਕੋਲ ਸ਼ਾਸਨ-ਪ੍ਰਬੰਧ ਦਾ ਅਧਿਕਾਰ ਨਹੀਂ ਹੈ।

### ADR ਨਾਲ ਕਿਹੜੇ ਸਿਧਾਂਤ ਜੁੜੇ ਹਨ?

ਆਪਣੀ ਸੰਸਥਾ ਦੇ ਕੰਮ ਕਰਨ ਦੇ ਉਨ੍ਹਾਂ ਤਰੀਕਿਆਂ ਬਾਰੇ ਵਿਚਾਰ ਕਰੋ ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਤੇਜ਼ੀ ਨਾਲ ਚੱਲਣਾ ਬਨਾਮ ਹੌਲੀ ਚੱਲਣਾ, ਫੈਸਲੇ ਵਿੱਚ ਸਹਿਮਤੀ ਬਨਾਮ ਫੈਸਲੇ ਵਿੱਚ ਟਕਰਾਅ, ਜੋਖਮ ਪਸੰਦ ਬਨਾਮ ਸੁਰੱਖਿਆ ਪਸੰਦ, ਜਨਤਕ ਚਰਚਾ ਬਨਾਮ ਨਿੱਜੀ ਚਰਚਾ, ਅਤੇ ਇਸ ਤਰ੍ਹਾਂ ਦੀਆਂ ਗੱਲਾਂ ਸ਼ਾਮਲ ਹਨ।

ਉਦਾਹਰਨ ਜਵਾਬ: ਅਸੀਂ ਇਹ ਅਗਵਾਈ ਸਿਧਾਂਤ ਵਰਤਦੇ ਹਾਂ: ਕਾਰਵਾਈ ਨੂੰ ਤਰਜੀਹ, ਅਸਹਿਮਤ ਹੋਵੋ ਪਰ ਵਚਨਬੱਧ ਰਹੋ, ਆਸਾਨੀ ਨਾਲ ਪਲਟਾਏ ਜਾ ਸਕਣ ਵਾਲੇ ਅਤੇ ਆਸਾਨੀ ਨਾਲ ਅਲੱਗ ਕੀਤੇ ਜਾ ਸਕਣ ਵਾਲੇ ਫੈਸਲਿਆਂ ਲਈ 70% ਅਨੁਮਾਨ ਕਾਫ਼ੀ ਚੰਗੇ ਹਨ, ਅਤੇ ਕੰਮ ਕਰਨ ਦੇ ਜਨਤਕ ਤਰੀਕੇ, ਸਿਵਾਏ ਗੁਪਤ ਜਾਣਕਾਰੀ ਦੇ, ਜਿਵੇਂ ਸਾਡੀ ਸੰਸਥਾ ਦੇ ਗੁਪਤਤਾ ਸਮਝੌਤੇ ਵਿੱਚ ਦੱਸਿਆ ਗਿਆ ਹੈ।

## ADR ਲਈ ਅਗਲੇ ਕਦਮ ਦੇ ਸੰਕਲਪ

[Arc42](https://arc42.org/) ਦੋ ਸਵਾਲਾਂ ਦਾ ਵਿਹਾਰਕ ਢੰਗ ਨਾਲ ਜਵਾਬ ਦਿੰਦਾ ਹੈ ਅਤੇ ਇਸ ਨੂੰ ਤੁਹਾਡੀਆਂ ਖਾਸ ਲੋੜਾਂ ਮੁਤਾਬਕ ਢਾਲਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਤੁਹਾਨੂੰ ਆਪਣੇ ਆਰਕੀਟੈਕਚਰ ਬਾਰੇ ਕੀ ਦਸਤਾਵੇਜ਼ੀ ਰੂਪ ਦੇਣਾ/ਸੰਚਾਰ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ? ਕਿਵੇਂ ਦਸਤਾਵੇਜ਼ੀ ਰੂਪ ਦੇਣਾ/ਸੰਚਾਰ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ? Arc42 ਵਿੱਚ ਆਰਕੀਟੈਕਚਰ ਫੈਸਲਾ ਰਿਕਾਰਡ ਦੇ ਨਾਲ-ਨਾਲ ਟੀਚਿਆਂ, ਬੰਦਸ਼ਾਂ, ਪ੍ਰਸੰਗਾਂ, ਗੁਣਵੱਤਾ, ਜੋਖਮਾਂ ਅਤੇ ਹੋਰ ਬਾਰੇ ਮਾਰਗਦਰਸ਼ਨ ਸ਼ਾਮਲ ਹੈ।

[C4 ਮਾਡਲ](https://c4model.com/) ਸਾਫਟਵੇਅਰ ਆਰਕੀਟੈਕਚਰ ਚਿੱਤਰਕਾਰੀ ਦੀ ਸਿੱਖਣ ਵਿੱਚ ਆਸਾਨ, ਡਿਵੈਲਪਰ-ਮਿੱਤਰ ਪਹੁੰਚ ਹੈ। C4 ਪ੍ਰਸੰਗ, ਕੰਟੇਨਰ, ਕੰਪੋਨੈਂਟ, ਕੋਡ ਲਈ ਲੜੀਵਾਰ ਚਿੱਤਰਾਂ ਦਾ ਸਮੂਹ ਹੈ, ਨਾਲ ਹੀ ਸਿਸਟਮ ਦ੍ਰਿਸ਼-ਭੂਮੀ, ਗਤੀਸ਼ੀਲ ਅਤੇ ਡਿਪਲਾਇਮੈਂਟ ਲਈ ਸਹਾਇਕ ਚਿੱਤਰ।

## ਆਰਕੀਟੈਕਚਰ ਚਿੱਤਰ, ਦ੍ਰਿਸ਼ ਅਤੇ ਦ੍ਰਿਸ਼ਟੀਕੋਣ

ਆਰਕੀਟੈਕਚਰ ਚਿੱਤਰ ਨੂੰ "ਆਰਕੀਟੈਕਚਰ ਦ੍ਰਿਸ਼" ਕਿਹਾ ਜਾਂਦਾ ਹੈ।

"ਆਰਕੀਟੈਕਚਰ ਦ੍ਰਿਸ਼" ਇੱਕ "ਆਰਕੀਟੈਕਚਰ ਦ੍ਰਿਸ਼ਟੀਕੋਣ" ਦਾ ਇੱਕ ਨਮੂਨਾ ਹੁੰਦਾ ਹੈ।

"ਆਰਕੀਟੈਕਚਰ ਦ੍ਰਿਸ਼ਟੀਕੋਣ" ਦਾ ਇੱਕ ਖਾਸ ਦਰਸ਼ਕ ਹੁੰਦਾ ਹੈ ਜਿਸ ਦੀਆਂ ਖਾਸ ਚਿੰਤਾਵਾਂ ਧਿਆਨ ਵਿੱਚ ਹੁੰਦੀਆਂ ਹਨ।

ਆਰਕੀਟੈਕਚਰ ਦ੍ਰਿਸ਼ਟੀਕੋਣ ਦੀਆਂ ਉਦਾਹਰਨਾਂ, ਦ੍ਰਿਸ਼ ਦੀਆਂ ਉਦਾਹਰਨਾਂ, ਅਤੇ ਚਿੱਤਰ ਦੀਆਂ ਉਦਾਹਰਨਾਂ:

- ਕਾਰੋਬਾਰੀ ਸਮਰੱਥਾਵਾਂ (Business Capabilities)

- ਉੱਚ-ਪੱਧਰੀ ਕਾਰੋਬਾਰੀ ਪ੍ਰਕਿਰਿਆਵਾਂ

- [ਮੁੱਲ ਧਾਰਾਵਾਂ (Value Streams)](https://en.wikipedia.org/wiki/Value_stream)

- ਐਪਲੀਕੇਸ਼ਨ ਕੰਪੋਨੈਂਟਾਂ ਨਾਲ ਜੋੜੇ ਗਏ ਸਾਫਟਵੇਅਰ ਫੰਕਸ਼ਨ

- [C4 ਮਾਡਲ](https://en.wikipedia.org/wiki/C4_model) ਪ੍ਰਸੰਗ ਚਿੱਤਰ (TO-BE / AS-IS)

- [C4 ਮਾਡਲ](https://en.wikipedia.org/wiki/C4_model) ਕੰਟੇਨਰ ਚਿੱਤਰ (TO-BE / AS-IS)

- ਡਾਟਾ ਇਕਾਈਆਂ ਨੂੰ ਐਪਲੀਕੇਸ਼ਨ ਕੰਪੋਨੈਂਟਾਂ ਨਾਲ ਜੋੜਨ ਲਈ [ਇਕਾਈ-ਸੰਬੰਧ ਚਿੱਤਰ (Entity-relationship Diagram)](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD)

- ਸਿਸਟਮਾਂ ਦੇ ਅੰਦਰ ਅਤੇ ਏਕੀਕਰਨਾਂ ਲਈ ਕਾਰਜਾਤਮਕ ਪ੍ਰਵਾਹਾਂ ਦਾ ਵਰਣਨ ਕਰਨ ਲਈ [ਕ੍ਰਮ ਚਿੱਤਰ (Sequence Diagrams)](https://en.wikipedia.org/wiki/Sequence_diagram)

- ਐਪਲੀਕੇਸ਼ਨ ਕੰਪੋਨੈਂਟਾਂ ਵਿੱਚ ਡਾਟਾ ਪ੍ਰਵਾਹਾਂ ਦਾ ਵਰਣਨ ਕਰਨ ਲਈ [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) ਚਿੱਤਰ

- ਕਾਰੋਬਾਰੀ ਪ੍ਰਕਿਰਿਆਵਾਂ / ਵਰਤੋਂਕਾਰ ਦ੍ਰਿਸ਼ਾਂ ਦਾ ਵਰਣਨ ਕਰਨ ਲਈ [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) ਚਿੱਤਰ

- [ਪਛਾਣ ਅਤੇ ਪਹੁੰਚ ਪ੍ਰਬੰਧਨ (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) ਚਿੱਤਰ

- ਹਰ ਐਪਲੀਕੇਸ਼ਨ ਕੰਪੋਨੈਂਟ ਲਈ ਭੂਮਿਕਾਵਾਂ ਵਾਲੇ [ਭੂਮਿਕਾ-ਆਧਾਰਿਤ ਪਹੁੰਚ ਨਿਯੰਤਰਣ (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) ਚਿੱਤਰ

- ਹਰ ਐਪਲੀਕੇਸ਼ਨ ਕੰਪੋਨੈਂਟ ਲਈ ਗੁਣਾਂ ਵਾਲੇ [ਗੁਣ-ਆਧਾਰਿਤ ਪਹੁੰਚ ਨਿਯੰਤਰਣ (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) ਚਿੱਤਰ

- ਗੋਪਨੀਯਤਾ ਚਿੱਤਰ

ਸੰਬੰਧਿਤ ਚਿੱਤਰ:

- ਵਰਤੋਂ-ਕੇਸ ਚਿੱਤਰ (Use Case Diagram) ਪ੍ਰਬੰਧਨ/ਗਾਹਕਾਂ ਨੂੰ ਵਰਤੋਂ ਦੇ ਕੇਸ ਦਿਖਾਉਂਦਾ ਹੈ, ਜੋ ਲੋੜਾਂ ਤੋਂ ਪਹਿਲਾਂ ਆਉਂਦੇ ਹਨ, ਜੋ ਸਾਫਟਵੇਅਰ ਆਰਕੀਟੈਕਚਰ ਤੋਂ ਪਹਿਲਾਂ ਆਉਂਦੀਆਂ ਹਨ।

- ਡਿਪਲਾਇਮੈਂਟ ਚਿੱਤਰ (Deployment Diagram) ਉਹ ਭੌਤਿਕ ਹਾਰਡਵੇਅਰ/ਕੰਪਿਊਟਰ ਦਿਖਾਉਂਦਾ ਹੈ ਜਿਨ੍ਹਾਂ ਉੱਤੇ ਸਾਫਟਵੇਅਰ ਕੰਪੋਨੈਂਟ ਡਿਪਲਾਇ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।
- ਡਾਟਾ ਪ੍ਰਵਾਹ ਚਿੱਤਰ (Data Flow Diagram) ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਡਾਟਾ ਸਿਸਟਮ ਵਿੱਚੋਂ ਕਿਵੇਂ ਲੰਘਦਾ ਅਤੇ ਬਦਲਦਾ ਹੈ।
- ਕ੍ਰਮ ਚਿੱਤਰ (Sequence Diagram) ਇਹ ਦਿਖਾਉਣ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ ਕਿ HTTP ਵਰਗੇ ਪ੍ਰੋਟੋਕੋਲ ਸਮਾਂ ਧੁਰੇ ਉੱਤੇ ਕਿਵੇਂ ਕੰਮ ਕਰਦੇ ਹਨ।

- ਗਤੀਵਿਧੀ ਚਿੱਤਰ (Activity Diagram) ਗਤੀਵਿਧੀਆਂ ਦਾ ਉਹ ਵਰਕਫਲੋ ਦਰਸਾਉਂਦਾ ਹੈ ਜੋ ਸਾਫਟਵੇਅਰ ਸਿਸਟਮ ਚਲਾਉਂਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ NPC AI।

## ਕੋਡ ਵਜੋਂ ਫੈਸਲਿਆਂ ਲਈ ਫਿਟਨੈਸ ਫੰਕਸ਼ਨ

ਫਿਟਨੈਸ ਫੰਕਸ਼ਨ ਪ੍ਰੋਗਰਾਮਿੰਗ ਕੋਡ ਨਾਲ ਲਿਖੀਆਂ ਗਈਆਂ ਨਿਰਪੱਖ ਸਵੈਚਾਲਿਤ ਜਾਂਚਾਂ ਹਨ, ਜੋ ਪੁਸ਼ਟੀ ਕਰਦੀਆਂ ਹਨ ਕਿ ਫੈਸਲੇ ਕਾਇਮ ਰੱਖੇ ਜਾ ਰਹੇ ਹਨ।

- ਫਿਟਨੈਸ ਫੰਕਸ਼ਨ ਫੈਸਲਿਆਂ ਨੂੰ ਪਰਖਣਯੋਗ ਅਤੇ ਭਰੋਸੇਯੋਗ ਬਣਾਉਂਦੇ ਹਨ।

- ਫੈਸਲਿਆਂ ਲਈ ਫਿਟਨੈਸ ਫੰਕਸ਼ਨ ਗੁਣਵੱਤਾ ਭਰੋਸੇ, ਰੈਗੂਲੇਟਰੀ ਪ੍ਰਕਿਰਿਆਵਾਂ ਅਤੇ ਸ਼ਾਸਨ-ਪ੍ਰਬੰਧ ਦੇ ਟੀਚਿਆਂ ਵਿੱਚ ਬਹੁਤ ਮਦਦ ਕਰ ਸਕਦੇ ਹਨ।

### ਫਿਟਨੈਸ ਫੰਕਸ਼ਨ ਫੈਸਲਿਆਂ ਨਾਲ ਕਿਵੇਂ ਜੁੜਦੇ ਹਨ

ਫੈਸਲਾ ਰਿਕਾਰਡ ਫੈਸਲੇ ਨੂੰ ਦਰਜ ਕਰਦਾ ਹੈ, ਜਦਕਿ ਫਿਟਨੈਸ ਫੰਕਸ਼ਨ ਫੈਸਲੇ ਦੀ ਪੱਕੀ ਪੁਸ਼ਟੀ ਕਰਦਾ ਹੈ।

- ਉਦਾਹਰਨ ਫੈਸਲਾ: ਅਸੀਂ ਆਡਿਟ ਲੋੜਾਂ ਲਈ ਇਵੈਂਟ ਸੋਰਸਿੰਗ ਵਰਤਦੇ ਹਾਂ।

- ਉਦਾਹਰਨ ਫਿਟਨੈਸ ਫੰਕਸ਼ਨ: ਅਸੀਂ ਨਿਰੰਤਰ ਏਕੀਕਰਨ ਸਰਵਰ ਨਾਲ ਜਾਂਚ ਕਰਦੇ ਹਾਂ ਕਿ ਸਾਰੀਆਂ ਅਵਸਥਾ ਤਬਦੀਲੀਆਂ ਲਈ ਇਵੈਂਟ ਬਣਾਉਣੇ ਲਾਜ਼ਮੀ ਹਨ।

### ਫਿਟਨੈਸ ਫੰਕਸ਼ਨ ਫੈਸਲਿਆਂ ਦੀ ਮਦਦ ਕਿਉਂ ਕਰਦੇ ਹਨ

ਨਿਰਪੱਖ ਮਾਪ: ਫਿਟਨੈਸ ਫੰਕਸ਼ਨ ਪਾਸ ਜਾਂ ਫੇਲ੍ਹ ਹੁੰਦੇ ਹਨ, ਇਸ ਲਈ ਕੰਮ ਦਿਸਦਾ ਅਤੇ ਸਪੱਸ਼ਟ ਹੁੰਦਾ ਹੈ।

ਨਿਰੰਤਰ ਵਰਤੋਂ: ਫਿਟਨੈਸ ਫੰਕਸ਼ਨ ਤੁਹਾਡੇ ਜਿਉਂਦੇ ਨਿਯਮ ਹਨ, ਜੋ ਹਰ ਕਮਿਟ ਅਤੇ ਬਿਲਡ ਉੱਤੇ ਚੱਲਦੇ ਹਨ।

ਰੀਫੈਕਟਰ ਕਰਨ ਦਾ ਭਰੋਸਾ: ਫਿਟਨੈਸ ਫੰਕਸ਼ਨ ਫੈਸਲੇ ਦੇ ਨਿਯਮਾਂ ਦੀਆਂ ਗਲਤੀਆਂ ਆਪਣੇ-ਆਪ ਫੜ ਲੈਂਦੇ ਹਨ।

ਵਧਣਯੋਗ ਸ਼ਾਸਨ-ਪ੍ਰਬੰਧ: ਫਿਟਨੈਸ ਫੰਕਸ਼ਨ ਰੁਕਾਵਟਾਂ ਪੈਦਾ ਕੀਤੇ ਬਿਨਾਂ ਮਿਆਰਾਂ ਦੀ ਪੱਕੀ ਪੁਸ਼ਟੀ ਕਰਦੇ ਹਨ।

### ਕੀ ਫਿਟਨੈਸ ਫੰਕਸ਼ਨ AI ਵਰਤ ਸਕਦੇ ਹਨ?

ਫਿਟਨੈਸ ਫੰਕਸ਼ਨ ਆਪਣੇ ਕੰਮ, ਜਿਵੇਂ ਕਿ ਤੁਹਾਡੀਆਂ ਯੋਜਨਾਵਾਂ, ਕੋਡ, ਸਕੀਮਾਂ, API ਅਤੇ ਹੋਰ ਬਹੁਤ ਕੁਝ, ਬਾਰੇ ਸਵਾਲ ਪੁੱਛ ਕੇ ਫੈਸਲਿਆਂ ਲਈ AI LLM ਦਾ ਲਾਭ ਲੈ ਸਕਦੇ ਹਨ:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### ਆਰਕੀਟੈਕਚਰ ਯੂਨਿਟ ਟੈਸਟਿੰਗ

[ArchUnit](https://www.archunit.org/): ਕਿਸੇ ਵੀ ਸਾਦੇ Java ਯੂਨਿਟ ਟੈਸਟ ਫਰੇਮਵਰਕ ਨਾਲ Java ਕੋਡ ਦੇ ਆਰਕੀਟੈਕਚਰ ਨਿਯਮਾਂ ਦੀ ਜਾਂਚ ਕਰੋ।

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): Jest, Vitest, Jasmine ਆਦਿ ਨਾਲ TypeScript ਕੋਡ ਅਤੇ JavaScript ਕੋਡ ਦੇ ਆਰਕੀਟੈਕਚਰ ਨਿਯਮਾਂ ਦੀ ਜਾਂਚ ਕਰੋ।

## ਪੁੱਲ ਰਿਕੁਐਸਟਾਂ ਲਈ ਫੈਸਲੇ ਦੇ ਗਾਰਡਰੇਲ

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
ਸਹੀ ਫੈਸਲਾ ਰਿਕਾਰਡਾਂ ਨੂੰ ਸਹੀ ਸਮੇਂ ਉੱਤੇ ਆਪਣੇ-ਆਪ ਸਾਹਮਣੇ ਲਿਆਉਂਦਾ ਹੈ — ਜਦੋਂ
ਕੋਈ ਡਿਵੈਲਪਰ ਸਰਗਰਮੀ ਨਾਲ ਉਹ ਕੋਡ ਬਦਲ ਰਿਹਾ ਹੋਵੇ ਜਿਸ ਨੂੰ ਉਹ ਫੈਸਲੇ ਕਵਰ ਕਰਦੇ ਹਨ। ਇਸ ਉਮੀਦ ਵਿੱਚ ਰਹਿਣ ਦੀ ਬਜਾਏ ਕਿ ਡਿਵੈਲਪਰ ਮਿਲਾਉਣ (merge) ਤੋਂ
ਪਹਿਲਾਂ ਦਸਤਾਵੇਜ਼ਾਂ ਦਾ ਫੋਲਡਰ ਪੜ੍ਹਨਗੇ, ਸੰਬੰਧਿਤ ਪ੍ਰਸੰਗ ਸਿੱਧਾ ਪੁੱਲ ਰਿਕੁਐਸਟ ਉੱਤੇ ਦਿਸ ਪੈਂਦਾ ਹੈ।

ਇਹ ਹਰ ਕਿਸਮ ਦੇ ਫੈਸਲਾ ਰਿਕਾਰਡ ਲਈ ਕੰਮ ਕਰਦਾ ਹੈ: ਆਰਕੀਟੈਕਚਰ ਫੈਸਲੇ, ਡਾਟਾ
ਫੈਸਲੇ, ਪਾਲਣਾ ਫੈਸਲੇ, ਕਲੀਨਿਕਲ ਅਤੇ ਡਾਕਟਰੀ ਫੈਸਲੇ, ਸੁਰੱਖਿਆ ਫੈਸਲੇ ਅਤੇ ਹੋਰ।

ਕਿਸੇ ਵੀ CI ਸਿਸਟਮ (GitLab, Jenkins, CircleCI) ਨਾਲ ਅਤੇ ਪ੍ਰੀ-ਕਮਿਟ ਹੁੱਕ ਵਜੋਂ ਕੰਮ ਕਰਦਾ ਹੈ।
ਓਪਨ ਸੋਰਸ। MIT ਲਾਇਸੰਸ।

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) ਇੱਕ GitHub
Action ਹੈ ਜੋ ਪੁੱਲ ਰਿਕੁਐਸਟ ਨੂੰ ਫੇਲ੍ਹ ਕਰ ਦਿੰਦੀ ਹੈ ਜਦੋਂ ਨਿਗਰਾਨੀ ਅਧੀਨ ਕੋਡ ਮਾਰਗ ਬਦਲਦੇ ਹਨ ਅਤੇ
ਆਰਕੀਟੈਕਚਰ ਫੈਸਲਾ ਰਿਕਾਰਡ ਜੋੜਿਆ ਜਾਂ ਅੱਪਡੇਟ ਨਹੀਂ ਕੀਤਾ ਜਾਂਦਾ। ਛੋਟਾਂ ਸਪੱਸ਼ਟ ਹਨ: ਕਾਰਨ ਸਮੇਤ
`ADR-Exempt:` ਲਾਈਨ ਗੇਟ ਨੂੰ ਪਾਸ ਕਰ ਦਿੰਦੀ ਹੈ ਅਤੇ ਜੌਬ ਸਾਰ ਵਿੱਚ ਲਿਖੀ ਜਾਂਦੀ ਹੈ।
ਟੈਂਪਲੇਟ-ਨਿਰਪੱਖ, ਕੋਈ ਨਿਰਭਰਤਾਵਾਂ ਨਹੀਂ। ਓਪਨ ਸੋਰਸ। MIT ਲਾਇਸੰਸ।

## ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ

ਜਾਣ-ਪਛਾਣ:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

ਟੈਂਪਲੇਟ:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

ਡੂੰਘਾਈ ਨਾਲ:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - ਮੁਫ਼ਤ ਮਾਸਿਕ ਸਾਫਟਵੇਅਰ ਆਰਕੀਟੈਕਚਰ ਪਾਠ

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

ਟੂਲ:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

ਕੰਪਨੀ-ਵਿਸ਼ੇਸ਼ ਮਾਰਗਦਰਸ਼ਨ:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

ਉਦਾਹਰਨਾਂ:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

ਵੀਡੀਓ:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

ਪੌਡਕਾਸਟ:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

ਕਿਤਾਬਾਂ:

- [Software Architecture Metrics: Case Studies to Improve the Quality of Your Architecture - by Christian Ciceri, Dave Farley, Neal Ford, Andrew Harmel-Law, Michael Keeling and Carola Lilienthal](https://www.amazon.com/Software-Architecture-Metrics-Christian-Ciceri-ebook/dp/B0B1NZ8Z5V)

- [Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives - by Nick Rozanski and Eoin Woods](https://www.amazon.com/Software-Systems-Architecture-Stakeholders-Perspectives/dp/032171833X)

- [Software Architecture in Practice (SEI Series in Software Engineering)](https://www.amazon.com/Software-Architecture-Practice-SEI-Engineering-ebook/dp/B094CPJ96B)

- [Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering)](https://www.amazon.com/Documenting-Software-Architectures-Beyond-Engineering-ebook/dp/B0046XS3RO)

- [The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)

- [Fundamentals of Software Architecture: An Engineering Approach - by Mark Richards and Neal Ford](https://www.amazon.com/Fundamentals-Software-Architecture-Engineering-Approach-ebook/dp/B0849MPK73)

- [Building Evolutionary Architectures - by Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage](https://www.amazon.com/Building-Evolutionary-Architectures-Neal-Ford-ebook/dp/B0BN4T1P27?crid=37FA31IFLAS0Z)

- [Foundations of Decision Analysis by Ronald Howard and Ali Abbas](https://www.amazon.com/Foundations-Decision-Analysis-Ronald-Howard-ebook/dp/B00SZECJTI?crid=14BK5SDP76UN6)

- [Head First Software Architecture - by Raju Gandhi, Neal Ford and Mark Richards](https://www.amazon.com/Head-First-Software-Architecture-Architectural-ebook/dp/B0CW1JMNF2)

- [Communication Patterns: A Guide for Developers and Architects - by Jacqui Read](https://www.amazon.com/Communication-Patterns-Guide-Developers-Architects/dp/1098140540)

ਇਹ ਵੀ ਵੇਖੋ:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - ਫੈਸਲਿਆਂ ਨੂੰ ਸਪੱਸ਼ਟ ਤਰਕ, ਧਾਰਨਾਵਾਂ, ਗਿਆਨਾਤਮਕ ਅਵਸਥਾ ਅਤੇ ਸਮਝੌਤਿਆਂ ਸਮੇਤ ਦਰਸਾਉਣ ਲਈ ਵਿਕਰੇਤਾ-ਨਿਰਪੱਖ, ਮਸ਼ੀਨ ਵੱਲੋਂ ਪੜ੍ਹਨਯੋਗ YAML/JSON ਫਾਰਮੈਟ। ਇਹ ਫੈਸਲੇ ਦੇ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਿੱਚ ਬਣਤਰ ਵਾਲਾ, ਪਰਖਣਯੋਗ ਤਰਕ ਜੋੜ ਕੇ ADR ਦਾ ਪੂਰਕ ਬਣਦਾ ਹੈ।
