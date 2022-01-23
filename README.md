# Kupujem-prodajem cms

Ovo je demo projekat - vježba. Rađen je kao jedan od domaćih za Developer's lab Django kurs. Predstavlja mali vebsajt koji se bazira na dijeljenju oglasa.

## Sadržaj

Stranica sadrži:
- početnu stranicu - */*
- stranicu sa kategorijama - */kategorije/*
- stranicu sa oglasima, svim ili samo iz odabrane kategorije - */oglasi/*
- stranicu za dodavanje novog oglasa - */oglasi/novi/*
- stranicu sa detaljima za odabrani oglas - */oglasi/[id]/*
- login stranicu - */login/*

## Forme

Za dodavanje novih komentara i oglasa korišćene su modelForms, i submitovani podaci su automatski povezani sa korisnikom koji je ih je submitovao i dodati u bazu podataka

## Login sistem

Za ulogovanje i izlogovanje korišćen je ugrađeni django sistem, tako što je u glavni urls fajl uključen django.contrib.auth.urls, i dodat novi templejt `templates/registrations/login.html`