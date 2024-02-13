## Votukka === Ericsson Diavox + RaspberryPI + ??

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

### Testiskriptit

#### tests/play_audio.py, toista audiotidosto
```
python3 tests/play_audio.py
```

#### script_keypad_pinger.py, lue näppäimistöä ja toista näppäimen merkki
```
python3 script_keypad_pinger.py
```
