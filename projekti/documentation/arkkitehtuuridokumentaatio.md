## Arkkitehtuuridokumentaatio 

### Rakenne
Ohjelma (peli) Koostuu seuvaanlaisista osista
* UI - Sisältää valikon, sekä Draw_windows luokat
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
		

