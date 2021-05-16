# Ohjelmistotekniikan harjoitustyö VisaBL 

### Pelin tarkoitus

Pelissä pelaajan on tarjoitus ohjata matoa, sekä syödä madolla esineitä. Madon pituus ja vauhti kasvavat pelin edetessä

### Dokumentaatio
[ohjelman vaatimuusmäärittely](https://github.com/VisaBL/ot-harjoitustyo/blob/master/projekti/documentation/Vaatimusmaarittely.md)

[käyttöohje](https://github.com/VisaBL/ot-harjoitustyo/blob/master/projekti/documentation/k%C3%A4ytt%C3%B6ohde.md)

[arkkitehtuurikuvaus](https://github.com/VisaBL/ot-harjoitustyo/blob/master/projekti/documentation/arkkitehtuuridokumentaatio.md)

[testausdokumentti](https://github.com/VisaBL/ot-harjoitustyo/blob/master/projekti/documentation/Testausdokumentti.md)

[työaikakirjanpito](https://github.com/VisaBL/ot-harjoitustyo/blob/master/projekti/documentation/tyoaikakirjanpito.md)

[Ensimmäinen relase](https://github.com/VisaBL/ot-harjoitustyo/releases/tag/Viikko5)

[Final relase(loppupalautus)](https://github.com/VisaBL/ot-harjoitustyo/releases/tag/Loppupalautus)



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
	
### Käyttöohje 


