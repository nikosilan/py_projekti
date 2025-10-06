# ✈️ Lentopeli

## Pelistä lyhyesti:
Lentopeli on tekstipohjainen lentopeli, jossa pelaaja pääsee matkustamaan ympäri maailmaa suurten lentokenttien välillä.  
Pelin tavoitteena on ansaita rahaa, hallita polttoainetta ja suorittaa lentoja edetäkseen pelissä ja avatakseen uusia mantereita.  

Peli alkaa päävalikosta, joka tervehtii ja antaa neljä vaihtoehtoa:
1. **Aloita peli**  
2. **Luo uusi pelaaja**  
3. **Katso pelaajan tilastot**  
4. **Poistu pelistä**

Jos olet uusi pelaaja, valitse ensin vaihtoehto **2** luodaksesi hahmon.  
Sen jälkeen voit aloittaa pelin valitsemalla **1**.  
Jos sinulla on jo tallennettu peli, voit tarkastella etenemistäsi valinnalla **3**.  
Pelistä poistutaan valinnalla **4**.

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
Avaa tiedosto **LOG_IN.PY** ja lisää sinne omat tietosi tietokantayhteyttä varten.

- Luo oma kirjautumistunnus kohtaan:
  ```python
  elif nimi.lower() == "oma_käyttäjätunnus"
  ```
- Lisää yhteysosoitteesi MySQL-tietokantaan kohtaan:
  ```python
  yhteys = mysql.connector.connect("tähän omat tietosi")
  ```

---

### 3. Pelin aloitus
Ajaa ensin **AIRCRAFT_MAIN.PY** tämä on tärkeä!
Kun peli on käynnissä, **luo ensin hahmo** ennen kuin alat pelata normaalisti.  
Muuten peli ei pysty seuraamaan raha-, polttoaine- tai lentotietoja.

---

## Nauti pelistä!
