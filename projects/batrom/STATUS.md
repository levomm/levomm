# BATROM OY | Tööde tegevusjärjekord

**Seisuga:** 01.11.2026  
**Veebileht:** batrom.fi  
**Tähised:** `[OK]` tehtud ja kontrollitud · `[~]` pooleli · `[ ]` teha · `[?]` valik / otsus

## Tööde puu

```text
BATROM/
│
├── 00_TEHTUD/
│   ├── [OK] Esmane turvaaudit ja korduskontroll
│   ├── [OK] WordPressi põhifailide ja andmebaasi kontroll
│   ├── [OK] Aegunud pistikprogrammide inventuur
│   ├── [OK] Serveri ja HTTPS-i kontroll
│   ├── [OK] Krüpteeritud USB-varukoopia
│   ├── [OK] Zone+ taastetõmmis
│   ├── [OK] staging.batrom.fi loodud
│   ├── [OK] Stagingu SSL ja PHP 8.3
│   └── [OK] Testkeskkonna avaleht avaneb
│
├── 01_KÕIGEPEALT_SAIT_KORDA/                 8–16 h
│   ├── [~] Stagingu andmebaasi ja failide eraldatus
│   ├── [ ] Stagingu kaitse ja otsingust peitmine
│   ├── [ ] Testkeskkonna päris e-kirjade blokeerimine
│   ├── [ ] Oluliste pluginate turvaline uuendamine
│   ├── [ ] Elementor + Elementor Pro ühilduvustest
│   ├── [ ] Kontaktvormi parandamine ja päringukatse
│   ├── [ ] Menüü, teenuste ja mobiilivaate testid
│   ├── [ ] Varukoopia taastamise kontroll
│   ├── [ ] Kontrollitud muudatused päris veebilehel
│   └── [ ] Kordusaudit
│
├── 02_SEO_EELTÖÖ_JA_SUUNA_VALIK/             8–15 h*
│   ├── [ ] Soome märksõnade ja konkurentide analüüs
│   ├── [ ] Olemasolevate teenuste ning sisu kaardistus
│   ├── [ ] Google Search Console / Maps / indekseerimine
│   ├── [ ] SEO tehnilised kitsaskohad ja sisukava
│   └── [?] OTSUS: kas jätkata WordPressiga või teha uus sait?
│       │
│       ├── A) JÄTKAME WORDPRESSIGA
│       │   ├── [?] Tugevam turvakaitse ja seire       10–22 h
│       │   ├── [ ] SEO rakendamine olemasoleval saidil 22–45 h*
│       │   ├── [?] AI-abimees veebilehele             14–30 h
│       │   ├── [?] AI-agentide päringute vastuvõtt    12–24 h
│       │   └── [ ] Kontrollitud kasutuselevõtt
│       │
│       └── B) EHITAME UUE AGENTIC SAIDI
│           ├── [?] Uue saidi kinnitamine ja lähteülesanne
│           ├── [ ] Uus tehniline scroll-trigger sait 60–120 h
│           │   ├── Disain, kerimisanimeeringud, videod
│           │   ├── Mobiil, kiirus, ligipääsetavus
│           │   ├── Teenuste sisu, vormid ja haldus
│           │   ├── Turvalisus ja varukoopiad
│           │   └── Nõusolekupõhine külastusanalüütika
│           ├── [ ] SEO sisuloome ja migratsioon      22–45 h*
│           ├── [?] AI-abimees (eraldi täisfunktsioonid) 14–30 h
│           ├── [?] AI-agentide päringute vastuvõtt   12–24 h
│           └── [ ] Testimine, ümbersuunamised ja avaldamine
│
└── 03_PÄRAST_AVALDAMIST/
    ├── [ ] Päringute ja veateadete jälgimine
    ├── [?] SEO pidev arendus               4–8 h/kuus
    └── [?] Turvaseire ja hooldus           1–3 h/kuus
```

* SEO eeltöö **8–15 h** ning SEO rakendamine **22–45 h** moodustavad kokku **30–60 h**, mitte kaks eri SEO-projekti. Uue saidi arenduse ja SEO rakenduse töödes võib olla kattuvust.

## Mida tuleb otsustada ja millal?

### 1. Kas jääda WordPressi juurde või ehitada uus veebileht?

**Otsuse koht:** pärast esmase saidi turvaprobleemide parandamist ja SEO eeltööd, **enne suuremahulist SEO sisutööd, uut kujundust või AI-integratsiooni**.

- **WordPressi jätkamine:** vana sait tehakse tugevamaks ja nähtavamaks; vähem ümbertegemist.
- **Uue veebilehe ehitamine:** eraldi agentic/scroll-trigger arendus. Praegune sait jääb toimima kuni uue kasutuselevõtuni.

### 2. Kas lisada täiendav kaitse?

**Otsuse koht:** kohe, kui on selge, kas põhisait jääb WordPressile või liigub uuele platvormile. Turvaline ligipääs, uuendused, vormide kaitse ja põhiseire on niikuinii vajalikud. **Täiendav kaitse (10–22 h)** tähendab näiteks tugevamat liiklusfiltrit, täiendavat seiret ja rangemat õiguste haldust. Uue saidi puhul tuleb ulatus ümber hinnata, sest osa kaitsest kuulub juba uusarendusse.

### 3. Kas veebilehele on vaja AI-abimeest?

**Otsuse koht:** siis, kui teenused ja pakkumispäringu teekond on paigas, aga **enne lõpliku kasutajaliidese ehitamist**. Uue saidi korral tuleks vältida esmalt vanale WordPressile ja hiljem uuele saidile eraldi sama agendi arendamist.

### 4. Kas süsteem võtab vastu teiste AI-agentide päringuid?

**Otsuse koht:** pärast ettevõtte teenuste ja päringu väljade kokkuleppimist. **Valikuline arendus 12–24 h**: masinloetav teenuseinfo, turvaline päringuliides, päringute kontroll ja automaatne edastamine. Ettevõtte nimel lõplikku pakkumist ei saadeta ilma kontrollita. See on ettevalmistus võimaluseks, et edaspidi saadab osa kliente päringuid oma AI-assistendi kaudu.

### 5. Kas teha külastaja teekonna põhjal kohanduv veebileht?

**Otsuse koht:** uue saidi disaini ja analüütika kavandamisel. Uue saidi 60–120 tunni vahemikku kuulub scroll-trigger kujundus ning nõusolekupõhised ja privaatsust arvestavad kasutusmõõdikud. Külastajate varjatud isikutuvastamine ei ole eesmärk.

## Ajahinnangud

| Etapp | Hinnang |
|---|---:|
| Olemasoleva saidi tehniline korrastamine | **8–16 h** |
| Maksimaalne SEO, mõlemas valikus kokku | **30–60 h** |
| Täiendav turvakaitse, valikuline | **10–22 h** |
| AI-abimees, valikuline | **14–30 h** |
| Agentidelt päringute vastuvõtt, valikuline | **12–24 h** |
| Täiesti uus agentic scroll-trigger veebileht, valikuline | **60–120 h** |

**Kindel tööjada (tehniline korrastamine + täismahus SEO): 38–76 töötundi.** Ülejäänud mahud lisanduvad ainult vastava valiku korral. Mõned ülesanded võivad kattuda, seetõttu ei liideta kõiki valikulisi variante ühte üldsummasse.

## Tehtud kontrollide seis

- WordPressi põhifailide kontroll ja andmebaasi tervisekontroll läbisid testi.
- Kontrolli ajal vajas uuendamist 15 aktiivset pluginat; oluline on Elementor ja Pro koos üle testida.
- Kontaktvormi rike pole veel parandatuks kinnitatud.
- Krüpteeritud USB-varukoopia arhiivikontroll läbis testi. Täielik taastamise proov on veel tegemata.
- Zone+ tõmmis on loodud; Zone+ tõmmised säilivad 14 päeva.
- Testkeskkonna avaleht avaneb, kuid selle täielik eraldatus põhisaidist vajab kontrollimist.

**Kulunud aeg:** varasemate tööde tegelikke tunde ei ole veel usaldusväärselt koondatud. **AI tokenid:** mõõdetud koondandmed puuduvad. Kõik dokumendis olevad tunnid on **tulevaste tööde hinnangud**, mitte juba kulunud aeg.
