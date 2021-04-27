## OHJELMISTOTUOTANTO-KURSSIN HARJOITUSTYÖN MÄÄRITTELYDOKUMENTTI

###Harjoitustyön konsepti
tarkoituksena jatkokehittää sekä uudelleenkirjoittaa ohjelmoinnin jatkokurssilla toteutettua matopeli-tyylistä peliä. 

###Työtlä halutut toiminnallisuudet
####Valikko
* Päävalikko // Not yet to be done 
	* Valikko käytettävissä hiirellä tai nuolinäppäimillä
	* Visuaalisesti suht. yksinkertainen
	* Valikos ta voi käynnistää uuden pelin, tai halutessaan tarkastella huippupisteitä
* Huippupisteet // Suurimanksi osaksi toteutettu.
	* Pelaajan pisteiden tallennus ainakin paikalliseen tiedostoon, mahdollisesti myös internet-palveluun omalla nimimerkillä. Huom! Nimimerkki ei ole uniikki // Toteuttamatta 
* Asetukset
	* Pelaaja pystyy säätämään resoluution sekä äänet. Asetukset tallennetaan paikalliseen tiedostoon 

####Pelin toiminnallisuudet
* Pelin haastavuustaso kasvaa pelaajan edetessä // toteutetuty
* Pelissä mato syö palkintoja, palkintojen syöminen kasvataa matoa // totetutettu 
* Madolle tarjoillaan erilaisia palkintoja joista jotkin kasvattavat pisteitä enemmän // pääosin toteutettu
* Mato kasvaa pidemmäksi pelin edetessä // toteutettu
* Erilaisia pelimoodeja, esimerkiksi, sokkelikko, tai seiniin törmäys pois tai päälle // toteuttamatta

###Kehitys 
####Alkuvaiheessa toteutettavat asiat
* Luodaan Mato-luokka, sprite-olio joka vastaa madon ominaisuuksista
* Palkinto-luokka, olio joka huolehtii madon palkintojen generoinnista 
* Tapahtumaloopun totetutus, madon sekä muiden olioiden piirtäminen pygame-kirjaston avustuksella 
####Myöhemmässä vaiheessa toetutettavat jatkokehitysideat
* Mahdolliset ääniefektit
* Pelivalikko
* Pelin asetukset
* Huippupisteiden tallentaminen ja tarkastelu // osittain toetuttu
* Pelin visuaalisen ilmeen viimeisteleminen (vasta kun kaikki muu haluttu toiminnallisuus on saavutetttu) // visuaalista ilmettä hiottu. mm. madon kääntyminen
