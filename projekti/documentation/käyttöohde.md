
### Projektin suorittaminen
projektin voi ajaa omalla tietokoneella ensin asentamalla riippuvuudet poetryn avulla

*$ poetry install*
Käynnistäminen

*$ poetry run invoke start*
testien suorittaminen

*$ poetry run invoke test*
testikattavuusraportin hakeminen

*$ poetry run invoke coverage-report*
testikattavuuden saa tulostettua myös suoraan terminaaliin komennolla

*$ poetry run invoke coverege-terminal*
pylint koodin analysointi

*$ poetry run invoke lint* 

### Pelaaminen ja Toiminnallisuudet

* Valitse valikosta "start game*

![alt_text](https://github.com/VisaBL/ot-harjoitustyo/blob/master/projekti/documentation/Pictures/Screenshot%20from%202021-05-16%2022-15-22.png?raw=true)

* Pelaaja voi vaihtaa madon kulkusuuntaa nuolinäppäimillä 

![alt_text](https://github.com/VisaBL/ot-harjoitustyo/blob/master/projekti/documentation/Pictures/game.png?raw=true)

* Pelin lopuksi oman nimen voi halutessaan kirjoittaa testikenttään, painamalla return painiketta

* Huippupisteitä voi selata valikon load higscores-kohdasta
