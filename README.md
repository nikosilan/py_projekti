# ✈️ Lentopeli

## 🚨 HUOM! Ohjelmisto 2 selain-pohjainen peli löytyy AINA KANSIOSTA "flask_game"!!!
## 🚨 HUOM! Sinun täytyy tehdä oikean yhteyden, jonka ohjausta löytyy "Ennen pelin käynnistämistä"

## Pelistä lyhyesti:
Lentopeli on tekstipohjainen lentopeli, jossa pelaaja pääsee matkustamaan ympäri maailmaa suurten lentokenttien välillä.  
Pelin tavoitteena on ansaita rahaa, hallita polttoainetta ja suorittaa lentoja edetäkseen pelissä ja avatakseen uusia mantereita.  

Peli alkaa päävalikosta, joka tervehtii ja antaa kolme vaihtoehtoa:
1. **Aloita peli**
2. **Luo uusi pelaaja**
3. **Katso tutoriaalli**

Jos olet uusi pelaaja, valitse ensin vaihtoehto **Luo hahmo** luodaksesi hahmon.
Sen jälkeen voit aloittaa pelin valitsemalla **Aloita**.
Jos tarvitset apua ymmärtääksesi miten peli toimii, paina **Info**.

---

## Pelin kulku
Pelin pääidea on lentää suurten lentokenttien välillä.  
Pelin alussa sinulle annetaan:
- **100 € rahaa**  
- **240 000 litraa polttoainetta**  
- **0 suoritettua lentoa**

Mitä enemmän lennät, sitä enemmän etenet pelissä.

Jokaisen lennon jälkeen voi tapahtua **satunnaisia tapahtumia**, kuten:
- Lentokoneen korjaus  
- Aarteiden löytäminen uudesta kohteesta  

Jos haluat ansaita lisää rahaa, voit pelata jotakin kahdesta minipelistä:
- **Noppa peli**  
- **Tietokilpailu**

Minipeleistä voi voittaa **1–100 €**.  
Jos polttoaineesi loppuu, voit tankata koneesi **100 €** maksua vastaan.

Peli jatkuu niin kauan, kunnes päätät lopettaa sen.

---

## Ennen pelin käynnistämistä

### 1. Tietokannan valmistelu
Lataa **flight_game** -tietokanta ja lisää seuraavat komennot **MariaDB**:hen tai **MySQL**:ään:

```sql
ALTER TABLE game ADD column bensa INT;
ALTER TABLE game ADD column raha INT;
ALTER TABLE game ADD column flights INT;
ALTER TABLE game ADD column sijainti VARCHAR(10);
```

Tämän jälkeen suorita nämä rivit:
```sql
ALTER TABLE game MODIFY bensa INT NOT NULL DEFAULT 0;
ALTER TABLE game MODIFY raha INT NOT NULL DEFAULT 0;
ALTER TABLE game MODIFY flights INT NOT NULL DEFAULT 0;
```

---

### 2 MySQL-yhteyden asetukset
Avaa tiedosto **flask_game/LOG_IN.PY** ja lisää sinne omat tietosi tietokantayhteyttä varten.

- Luo oma kirjautumistunnus kohtaan:
  ```python
  elif nimi.lower() == "oma_käyttäjätunnus"
  ```
- Lisää yhteysosoitteesi MySQL-tietokantaan kohtaan:
  ```python
  yhteys = mysql.connector.connect("tähän omat tietosi")
  ```
  
### 3. Tärkeää yhteyden toiminnasta

Jos olet lisännyt kaikki kirjautumistiedot **oikein** kohdan 2 mukaisesti, kaiken pitäisi toimia normaalisti.

Kun peli käynnistyy ja latausruudun jälkeen avautuu ponnahdusikkuna, joka pyytää nimeäsi, syötä täsmälleen **sama nimi**, jonka määrittelit MySQL–Python-yhteyttä varten kohdassa 2.

Tämän jälkeen peli etenee normaalisti.
Jos ilmenee virheitä tai peli ei etene, **OTA VÄLITTÖMÄSTI YHTEYTTÄ PELIN TEKIJÖIHIN**.

---

### 3. Pelin aloitus
Ajaa ensin **flask_game/APP.PY** tämä on tärkeä! Kirjaudu sisään PyCharm/komennon avulla kirjoittaen sinne oma nimesi.
Sitten avaa **flask_game/Menu.html** tämä avaa peli!
Kun peli on käynnissä, **luo ensin hahmo** ennen kuin alat pelata normaalisti.  
Muuten peli ei pysty seuraamaan raha-, polttoaine- tai lentotietoja.

**MUISTA AINA! päivittää kohteet klikkaamalla "Päivitä kohteet" painiketta kun aloitat pelaamaan, lennät seuraavaan kohteeseen tai jos sinun kohteesi päivittyy (minipelien jälkeen, tankauksen jälkeen yms.)**

---

## Nauti pelistä!
