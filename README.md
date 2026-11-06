# Claude

## Climate tech ochtendsamenvatting

Elke ochtend om 06:58 (Amsterdamse tijd) maakt een geplande Claude-taak een
samenvatting van de climate tech-nieuwsbrieven van de afgelopen 24 uur en mailt
die naar mijn eigen Gmail-adres.

### Nieuwsbrieven

| Nieuwsbrief | Afzender in Gmail | Status |
|---|---|---|
| CTVC (Climate Tech VC) | `ctvc.co` | Aanmelding nog bevestigen via de mail "Complete your sign up" |
| Sifted | `sifted.eu` | Nog aanmelden op sifted.eu |
| Bloomberg Green (Green Daily) | `noreply@news.bloomberg.com` | Aangemeld. Alleen Green-edities tellen mee, andere Bloomberg-mails niet |

### Hoe het werkt

1. Een geplande taak in claude.ai ("Climate tech ochtendsamenvatting") start
   elke ochtend een nieuwe sessie met de Gmail-connector.
2. Claude zoekt de nieuwsbrieven hierboven met `newer_than:1d` en leest ze volledig.
3. Claude schrijft een Nederlandse samenvatting: eerst de belangrijkste punten,
   daarna per nieuwsbrief financieringsrondes, beleid, trends en links.
4. De samenvatting gaat als mail naar mijzelf met het onderwerp
   "🌱 Climate tech ochtendsamenvatting – <datum>".

### Nieuwsbrief toevoegen

Pas de prompt van de geplande taak aan in claude.ai en voeg de afzender toe
aan STAP 1. Werk daarna de tabel hierboven bij.

### Vereist

De geplande taak heeft de **Gmail-connector** nodig. Zonder die connector kan
de taak je mail niet lezen of versturen.
