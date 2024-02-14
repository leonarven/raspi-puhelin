## Votukka === Ericsson Diavox + RaspberryPI + ??

[![Ericsson Diavox](https://github.com/leonarven/raspi-puhelin/blob/main/media/diavox.jpg?raw=true "Photo: Okänd / Tekniska museet - https://digitaltmuseum.se/021026312683/telefonapparat, CC BY 4.0")](https://digitaltmuseum.se/021026312683/telefonapparat)

**Projekti RaspberryPI:n käyttämiseksi Diavox-lankapuhelimella.**

Toistaiseksi on tärkeintä, että edes jotain tapahtuu.

### Tavoitteet

1. Kuulokkeesta voidaan toistaa ääntä
2. Kuulokkeen sijainti (nostettu/paikoillaan) voidaan tunnistaa
3. Näppäimistön syötettä voidaan lukea

Optiona

4. Hälytysääntä voidaan soittaa
5. Ulkoista kaiutinelementtiä voidaan käyttää
6. Mikrofonia voidaan käyttää
7. Mystinen R-painike tekee jotain mystistä

### TODO
- Kytke konfiguroitavuus env-muuttujiin / vipuihin / alustaan (onko RPi.GPIO käytettävissä vai ei)
- Muuta MockGPIO -luokka lukemaan jotain ulkoista tiedostoa tmv., jolla voi etänä säätää INPUT-pinnejä
  - Esim. MockGPIO.csv, jolla asettaa inputteja "ylös" ja jota seurataan iteroinnin rinnalla
```
Kommentti,Pinni,Arvo
C3,11,1
R2,5,1
```

### Käyttö
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```
### Konfigurointi
- **lib/const.py** sisältää GPIO-pinnien määritykset
- **lib/GPIO.py** säätää käytetäänkö MockGPIO-luokkaa RPi.GPIO:n sijaan
### Testiskriptit
#### tests/play_audio.py, toista audiotidosto
```
python3 tests/play_audio.py
```
#### tests/button_pull_detection.py, toista ääntä kuulokekytkimen statuksen muuttuessa
```
python3 tests/button_pull_detection.py
```
#### script_keypad_pinger.py, lue näppäimistöä ja toista näppäimen merkki
```
python3 script_keypad_pinger.py
```
