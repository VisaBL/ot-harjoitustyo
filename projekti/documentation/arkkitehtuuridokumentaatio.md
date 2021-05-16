## Arkkitehtuuridokumentaatio 

### Rakenne
![alt text](https://github.com/VisaBL/ot-harjoitustyo/blob/master/projekti/documentation/Pictures/rakenne.png?raw=true)
Ohjelma (peli) Koostuu seuvaanlaisista osista
* UI - Sisältää valikon, sekä Draw_windows luokatat
	* Valikko toteutettu pygamw_gui kirjastolla 
* Pelin Komponentit
	* Snake-luokka
	* Rewards-luokka
	* Pelisilmukka (game_loop)
* Palvelut
	* Tiedoston lajaaja (file_loader) 
		* Lataa Sprite-tekstuurit
		* Avaa sekä tallentaa paikalliset tiedostot tulosten tallentamista varten
	* Tulosten tallentamisesta sekä hakemisesta vastaava luokka (Leaderboard_uploader)
		* Hakee sekä tulostaa huippupisteet paikallisesta tiedostosta  
		

### Sekvenssikaavio pelin toiminta
![alt text](https://github.com/VisaBL/ot-harjoitustyo/blob/master/projekti/documentation/Pictures/sekvenssikaavio.png?raw=true)


### Tiedon pysyväistallennus 
* Ohjelma tallentaa tulokset paikallisesti csv tiedostoon file_loader luokan toimesta, 
* Tulokset tallenetaan sekä haetaaan myös google-drive taulukosta. Tästä vastaa leaderboard_uploader-luokka 
