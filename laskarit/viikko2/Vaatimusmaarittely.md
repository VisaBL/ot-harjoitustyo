## OHJELMISTOTUOTANTO-KURSSIN HARJOITUSTYÖN MÄÄRITTELYDOKUMENTTI

###Harjoitustyön konsepti
tarkoituksena jatkokehittää sekä uudelleenkirjoittaa ohjelmoinnin jatkokurssilla toteutettua matopeli-tyylistä peliä. 

###Työtlä halutut toiminnallisuudet
####Valikko
* Päävalikko
	* Valikko käytettävissä hiirellä tai nuolinäppäimillä
	* Visuaalisesti suht. yksinkertainen
	* Valikosta voi käynnistää uuden pelin, tai halutessaan tarkastella huippupisteitä
* Huippupisteet
	* Pelaajan pisteiden tallennus ainakin paikalliseen tiedostoon, mahdollisesti myös internet-palveluun omalla nimimerkillä. Huom! Nimimerkki ei ole uniikki 
* Asetukset
	* Pelaaja pystyy säätämään resoluution sekä äänet. Asetukset tallennetaan paikalliseen tiedostoon 

####Pelin toiminnallisuudet
* Pelin haastavuustaso kasvaa pelaajan edetessä
* Pelissä mato syö palkintoja, palkintojen syöminen kasvataa matoa
* Madolle tarjoillaan erilaisia palkintoja joista jotkin kasvattavat pisteitä enemmän
* Mato kasvaa pidemmäksi pelin edetessä 
* Erilaisia pelimoodeja, esimerkiksi, sokkelikko, tai seiniin törmäys pois tai päälle

###Kehitys 
####Alkuvaiheessa toteutettavat asiat
* Luodaan Mato-luokka, sprite-olio joka vastaa madon ominaisuuksista
* Palkinto-luokka, olio joka huolehtii madon palkintojen generoinnista 
* Tapahtumaloopun totetutus, madon sekä muiden olioiden piirtäminen pygame-kirjaston avustuksella 
####Myöhemmässä vaiheessa toetutettavat jatkokehitysideat
* Mahdolliset ääniefektit
* Pelivalikko
* Pelin asetukset
* Huippupisteiden tallentaminen ja tarkastelu 
* Pelin visuaalisen ilmeen viimeisteleminen (vasta kun kaikki muu haluttu toiminnallisuus on saavutetttu)
