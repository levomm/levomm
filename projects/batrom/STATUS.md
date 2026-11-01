# BATROM OY | Projekti tööde ülevaade

**Seisuga:** 01.11.2026  
**Veebileht:** https://batrom.fi  
**Fookus:** tehniline töökindlus, turvalisus, otsingunähtavus ja võimalik uusarendus

## Kulunud aeg ja töömaht

| Näitaja | Seis |
|---|---:|
| **Tegelikult kulunud aeg** | Mõõtmine seadistamisel; varasemat aega pole veel koondatud |
| **AI tokenid** | Mõõdetud andmed puuduvad |
| **Põhitööde järelejäänud maht** | **8–16 h** |
| **Võimalikud lisaarendused** | **114–232 h** |
| **Kõik etapid kokku** | **122–248 h** |

**Tundide tähendus:** tehtud tööde ajakulu ja tulevaste tööde hinnang on eri näitajad. Hinnangud kajastavad töötunde, mitte kalendriaega. AI tokenite arv on eraldi mõõdik, mitte töötundide asendaja.

## Projekti tööpuu

```text
BATROM/
├── 01_TEHTUD/
│   ├── [OK] Esmane turvaaudit ja korduskontroll
│   ├── [OK] WordPressi põhifailide ja andmebaasi kontroll
│   ├── [OK] Pluginate ja versioonide inventuur
│   ├── [OK] HTTPS-i ja suunamiste kontroll
│   ├── [OK] Serveripoolne varukoopia
│   ├── [OK] Krüpteeritud USB-varukoopia
│   ├── [OK] Zone+ taastetõmmis
│   ├── [OK] staging.batrom.fi loomine
│   ├── [OK] Testkeskkonna SSL ja PHP 8.3 seadistus
│   └── [OK] Testkeskkonna avalehe visuaalne kontroll
│
├── 02_POOLELI/
│   ├── [~] Testkeskkonna failide/andmebaasi eraldatus
│   ├── [~] Testkeskkonna pluginad ja teemad
│   ├── [~] Elementor + Elementor Pro ühilduvus
│   ├── [~] Failide kontrollsummade kõrvalekallete ülevaatus
│   └── [~] Brauserite kujunduserinevuse kontroll
│
├── 03_TEHNILINE_KORRASTAMINE/        [8–16 h]
│   ├── [ ] Testkeskkonna kaitse ja eraldatus
│   ├── [ ] Testkeskkonnast päris kirjade saatmise vältimine
│   ├── [ ] Pluginate turvaline uuendamine ja kontroll
│   ├── [ ] Kontaktvormi parandamine ja saatmistest
│   ├── [ ] Mobiili- ja funktsioonitestid
│   ├── [ ] Kontrollitud paranduste viimine põhisaidile
│   └── [ ] Kordusaudit ja taastamise proov
│
├── 04_LISA_MAKSIMAALNE_SEO/          [30–60 h]
├── 05_LISA_TURVAKAITSE_JA_SEIRE/     [10–22 h]
├── 06_LISA_AI_AGENT/                 [14–30 h]
│
└── 07_LISA_UUS_AGENTIC_VEEBILEHT/   [60–120 h]
```

## 03 · Olemasoleva veebilehe tehniline lõpetamine

| Töö | Hinnang |
|---|---:|
| Stagingu eraldatus, indekseerimise ja ligipääsu kaitse | 1–2 h |
| Pluginad, Elementor ja Elementor Pro | 3–6 h |
| Kontaktvormi parandamine ning kirjade kohaletoimetamise kontroll | 1–3 h |
| Funktsioonitestid, kinnitatud parandused ja kordusaudit | 3–5 h |
| **Kokku** | **8–16 h** |

**Valmimise tingimus:** uuendatud põhifunktsioonid töötavad, kontaktvormi päring jõuab kohale, testkeskkond on eraldi ning kontrollitud muudatused on põhisaidil kinnitatud.

## 04 · Maksimaalne SEO

**Eesmärk:** tugev tehniline ja sisuline nähtavus Soome otsingutes, eelkõige Batromi tegelike teenuste ja teeninduspiirkonna lõikes.

| Töö | Hinnang |
|---|---:|
| Tehniline SEO: indeks, sitemap, canonical, redirect, schema, Search Console | 5–10 h |
| Soome märksõnad, konkurendid ja otsingukavatsused | 5–10 h |
| Teenuselehed, usaldusväärne soomekeelne sisu, referentsid ja KKK | 8–18 h |
| Kohalik SEO: Tuusula/Uusimaa, Google Business Profile ja Maps | 4–8 h |
| Mobiili kiirus, Core Web Vitals ja piltide optimeerimine | 3–7 h |
| Päringute mõõtmine, SEO kontroll ja raport | 5–7 h |
| **Kokku** | **30–60 h** |

**Jooksev arendusaeg:** SEO seire ja täiustused ligikaudu **4–8 h kuus**. Otsingutulemuste kindlat positsiooni ei saa ette garanteerida.

## 05 · Täiendav turvakaitse ja seire

| Töö | Hinnang |
|---|---:|
| Kasutajarollid, ligipääsud, MFA | 2–4 h |
| WAF, sisselogimise piirangud ja botikaitse | 3–6 h |
| WordPressi ja veebiserveri turvaseadistused | 2–5 h |
| Seire, teavitused, varukoopiate ja taastamise kord | 3–7 h |
| **Kokku** | **10–22 h** |

**Jooksev jälgimine:** ligikaudu **1–3 h kuus**. See etapp täiendab tehnilist korrastamist, mitte ei korda samu uuendustöid.

## 06 · AI-agent olemasoleval veebilehel

| Töö | Hinnang |
|---|---:|
| Teenuste ja korduvate küsimuste teadmistebaas | 3–6 h |
| Soomekeelne veebivestlus ja kontekst | 3–6 h |
| Hinnapäringute kogumine ja suunamine | 4–8 h |
| Vastuste kontroll, turvalisus ja funktsioonitestid | 4–10 h |
| **Kokku** | **14–30 h** |

Agent aitab selgitada teenuseid, leida sobiva kontaktikanali ja esitada pakkumispäringu. Vastused peavad tuginema kinnitatud sisule; automaatselt ei lubata fikseerimata teenuseid, tähtaegu ega hindu.

## 07 · Uus agentic scroll-trigger veebileht

**Eraldi täismahus uusarendus.** Tänane veebileht jääb toimima seni, kuni uus versioon on testitud ja kasutuselevõtuks valmis.

| Töö | Hinnang |
|---|---:|
| Kontseptsioon, tehniline visuaalne suund ja UX | 8–16 h |
| Scroll-trigger stseenid, animatsioonid ja sujuvad üleminekud | 16–30 h |
| Mobiil, ligipääsetavus, laadimiskiirus ja SEO | 10–18 h |
| Agentic käitumine ja kontekstipõhised teenusesoovitused | 9–18 h |
| Külastusteekondade analüütika ja nõusolekuhaldus | 8–16 h |
| Sisu, testimine, ümbersuunamised ja avaldamine | 9–22 h |
| **Kokku** | **60–120 h** |

**Külastuskäitumise analüüs:** vaadatud teenused, kerimissügavus, CTA-nupud ja päringuteekond. Analüüs ja kohanduvad elemendid rakendatakse privaatsuspõhiselt ning vajaduse korral nõusoleku alusel. Võimalik tehniline suund: Next.js, GSAP/Motion, AI API ja privaatsust arvestav analüütika.

## Ajamahu koond

| Etapp | Järelejäänud töötunnid |
|---|---:|
| 03 · Tehniline korrastamine | **8–16 h** |
| 04 · Maksimaalne SEO | **30–60 h** |
| 05 · Täiendav turvakaitse ja seire | **10–22 h** |
| 06 · AI-agent | **14–30 h** |
| 07 · Uus agentic veebileht | **60–120 h** |
| **Kõik etapid kokku** | **122–248 h** |

Etapid 04–07 on **eraldi arendusvõimalused**. Nende vahel võib olla taaskasutatavaid osi, eelkõige AI-agentis ja uues veebilehes. Kui olemasolevale saidile eraldi AI-agentit ei tehta, on ülejäänud etappide summa **108–218 h**. Jooksvad igakuised tunnid ei sisaldu ühekordses kogusummas.

## Kinnitatud tehnilised tähelepanekud

- WordPressi põhifailide kontroll ja andmebaasi kontroll läbisid testi.
- Pluginate inventuuris oli 15 aktiivsel pluginal saadaval uuendusi; uuenduste testimine on veel pooleli.
- Kontaktvormi toimimist tuleb pärast parandusi uuesti kinnitada.
- Varukoopiad on loodud, kuid täiemahulist taastamist pole veel läbi katsetatud.
- Testkeskkond avaneb. Selle täielik eraldatus põhisaidist vajab enne uuendusteste kontrolli.
- Zone+ tõmmiseid säilitatakse 14 päeva.

---

**Staatuse tähendus:** `[OK]` kontrollitud, `[~]` pooleli, `[ ]` tegemata. Töömahud on hinnangud ja neid täpsustatakse töö käigus.
