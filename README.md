# Ohjelmistotekniikan harjoitustyö VisaBL 

### Pelin tarkoitus

Pelissä pelaajan on tarjoitus ohjata matoa, sekä syödä madolla esineitä. Madon pituus ja vauhti kasvavat pelin edetessä

### Dokumentaatio
[projektin vaatimuusmäärittely](https://github.com/VisaBL/ot-harjoitustyo/blob/master/laskarit/viikko2/Vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/VisaBL/ot-harjoitustyo/blob/master/projekti/tyoaikakirjanpito.md)

[Ensimmäinen relase](https://github.com/VisaBL/ot-harjoitustyo/releases/tag/Viikko5)

### Projektin suorittaminen 

projektin voi ajaa omalla tietokoneella ensin asentamalla riippuvuudet poetryn avulla 

	*$ poetry install*
	
Käynnistäminen 

	*$ poetry run invoke start*
	
testien suorittaminen

	*$ poetry run invoke test*
	
testikattavuusraportin hakeminen

	*$ poetry run invoke coverage-report*
	
pylint koodin analysointi

	*$ poetry run invoke run-pylint* 


