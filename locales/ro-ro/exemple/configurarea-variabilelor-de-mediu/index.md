# Configurarea variabilelor de mediu

Cuprins:

* [Rezumat](#rezumat)
  * [Problemă](#problemă)
  * [Decizie](#decizie)
  * [Stare](#stare)
* [Detalii](#detalii)
  * [Ipoteze](#ipoteze)
  * [Constrângeri](#constrângeri)
  * [Poziții](#poziții)
  * [Argument](#argument)
  * [Implicații ](#implicații)
* [Conexe](#conexe)
  * [Decizii conexe](#decizii-conexe)
  * [Cerințe conexe](#cerințe-conexe)
  * [Artefacte conexe](#artefacte-conexe)
  * [Principii conexe](#principii-conexe)
* [Note](#note)


## Rezumat


### Problemă

Vrem ca aplicațiile noastre să poată fi configurate dincolo de artefacte/binare/sursă, astfel încât un singur build să se comporte diferit în funcție de mediul de implementare.

  * Pentru a realiza aceasta, vrem să folosim configurarea prin variabile de mediu.

  * Vrem să gestionăm configurația folosind fișiere pe care le putem versiona.

  * Vrem să oferim o anumită ergonomie pentru dezvoltatori, de exemplu să se știe ce poate fi configurat și care sunt valorile implicite relevante.


### Decizie

S-au ales fișierele .env cu un fișier asociat de valori implicite și un fișier de schemă.


### Stare

Decis. Suntem deschiși să luăm în considerare capabilități noi pe măsură ce apar.


## Detalii


### Ipoteze

Preferăm separarea codului aplicației de codul mediului. Presupunem că aplicația trebuie să funcționeze diferit în medii diferite, precum mediul de dezvoltare, mediul de testare, mediul de demonstrație, mediul de producție etc.

Preferăm practica din industrie „12 factor app” și, mai mult, practica înrudită „15 factor app”.

Multe dintre proiectele noastre anterioare au folosit convenția unui fișier `.env` sau a unui director `.env` similar. Există practica tipică de a le ține în afara controlului versiunilor și de a folosi în schimb un alt mod de a le implementa, versiona și gestiona.


### Constrângeri

Vrem să ținem secretele în afara sistemului nostru de control al versiunilor (VCS) pentru gestionarea codului sursă (SCM).

Vrem să urmărim compatibilitatea cu framework-urile și bibliotecile software populare. De exemplu, Node are un modul „dotenv” pentru citirea configurației din variabile de mediu.


### Poziții

Am luat în considerare câteva abordări:

  * Stocarea configurației în aplicație, de exemplu într-un fișier `config.js`.

  * Stocarea configurației în mediu, de exemplu într-un fișier `.env`.

  * Preluarea configurației dintr-o locație cunoscută, precum un server de licențe.


### Argument

Am ales abordarea cu un fișier .env deoarece:

  * Este populară, inclusiv în rândul experților.

  * Urmează tiparul fișierelor `.env`, pe care echipele noastre le-au folosit cu succes de multe ori în multe proiecte.

  * Este simplă. În special, momentan acceptăm compromisurile semnificative pe care le vedem, precum lipsa capabilităților de audit în comparație cu o abordare cu server de licențe.


### Implicații 

Trebuie să găsim o modalitate de a separa configurația publică prin variabile de mediu de gestionarea secretelor.


## Conexe


### Decizii conexe

Ne așteptăm ca toate aplicațiile noastre să folosească această abordare.

Vom planifica modernizarea oricăror aplicații care folosesc o abordare mai puțin capabilă, precum codarea fixă într-un binar sau în codul sursă.

Vom păstra așa cum sunt oricare dintre aplicațiile noastre care folosesc o abordare mai capabilă, precum un server de licențe.


### Cerințe conexe

Vom adăuga capabilități devops pentru fișiere, inclusiv hook-uri, teste și integrare continuă.

Trebuie să instruim toți colegii dezvoltatori cu privire la această decizie.



### Artefacte conexe

Fiecare zonă în care facem implementări va avea nevoie de propriul fișier .env și de fișiere conexe.


### Principii conexe

Ușor reversibil.


## Note


Exemplu de fișier `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Exemplu de fișier `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Exemplu de fișier `.env.schema` doar cu cheile:

```env
NAME
EMAIL
```
