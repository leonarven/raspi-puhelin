## Votukka === Ericsson Diavox + RaspberryPI + ??

**Projekti RaspberryPI:n käyttämiseksi Diavox-lankapuhelimella.**

Toistaiseksi on tärkeintä, että edes jotain tapahtuu.

![Ericsson Diavox](https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Ericsson_Diavox_006.jpg/640px-Ericsson_Diavox_006.jpg "By Unknown / Swedish National Museum of Science and Technology - http://digitaltmuseum.se/021026312152, CC BY 4.0, https://commons.wikimedia.org/w/index.php?curid=50890964")

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
- Luo abstrakti Feature-luokka, jonka kautta voi vakioida erilaisia reaktioita (lue. aliohjelmia) erilaisiin tapahtumiin
  - (esim. "kun näppäillään 1-2-3, soita lampaan määkäisy)
- Luo operaattori, joka orkestroi haluttuja Featureja

### Käyttö
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Konfigurointi
**lib/const.py** sisältää GPIO-pinnien määritykset

**lib/GPIO.py** säätää käytetäänkö MockGPIO-luokkaa RPi.GPIO:n sijaan

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
