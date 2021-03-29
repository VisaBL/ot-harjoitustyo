import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapääte(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    # TESTATAAN KASSAPAATTEEN LUONTI 

    def test_testaa_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kassassa_rahaa_kun_kassapaate_on_olemassa(self):  
        self.assertEqual(100000, self.kassapaate.kassassa_rahaa)

    # EDULLISET LOUNAAT KATEISELLA!!!! 

    def test_lounaan_ostaminen_kassa_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(100240, self.kassapaate.kassassa_rahaa)

    def test_lounaan_ostaminen_palauttaa_oikean_maaran_rahaa(self):
        self.assertEqual(60, self.kassapaate.syo_edullisesti_kateisella(300))
    
    def test_lounaan_ostaminen_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(1, self.kassapaate.edulliset)

    def test_lounaan_ostaminen_jos_ei_tarpeeksi_rahaa_ei_kasvata_myytyjen_lounasten_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(0, self.kassapaate.edulliset)

    def test_lounaan_ostaminen_jos_ei_tarpeeksi_rahaa_ei_kasvata_kassssa_olevaa_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(100000, self.kassapaate.kassassa_rahaa)

    def test_lounaan_ostaminen_jos_ei_tarpeeksi_rahaa_palautaaa_rahat(self):
        self.assertEqual(200, self.kassapaate.syo_edullisesti_kateisella(200))

    #MAUKKAAN LOUNAAN OSTAMINEN KATEISELLA 

    def test_lounaan_ostaminen_kassa_kasvaa_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(100400, self.kassapaate.kassassa_rahaa)

    def test_lounaan_ostaminen_palauttaa_oikean_maaran_rahaa_maukas(self):
        self.assertEqual(100, self.kassapaate.syo_maukkaasti_kateisella(500))
    
    def test_lounaan_ostaminen_maara_kasvaa_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(1, self.kassapaate.maukkaat)

    def test_lounaan_ostaminen_jos_ei_tarpeeksi_rahaa_ei_kasvata_myytyjen_lounasten_maaraa_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(0, self.kassapaate.maukkaat)

    def test_lounaan_ostaminen_jos_ei_tarpeeksi_rahaa_ei_kasvata_kassssa_olevaa_rahaa_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(100000, self.kassapaate.kassassa_rahaa)

    def test_lounaan_ostaminen_jos_ei_tarpeeksi_rahaa_palautaaa_rahat_maukas(self):
        self.assertEqual(300, self.kassapaate.syo_maukkaasti_kateisella(300))

#TESTATAAN SAMAT KORTILLA!!!! 
#EDULLISEN LOUNAAN OSTAMISET KORTILLA 

    def test_lounaan_ostaminen_kortilla_kassa_ei_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(100000, self.kassapaate.kassassa_rahaa)

    def test_lounaan_ostaminen_kortilla_palauttaa_true(self):
        self.assertEqual(True, self.kassapaate.syo_edullisesti_kortilla(self.kortti))
    
    def test_lounaan_ostaminen_kortilla_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(1, self.kassapaate.edulliset)

    def test_lounaan_ostaminen_kortilla_jos_ei_tarpeeksi_rahaa__kortilla_ei_kasvata_myytyjen_lounasten_maaraa(self):
        for i in range(5):
            self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(4, self.kassapaate.edulliset)  #Ei voi ottaa viidettä maksua 

    def test_lounaan_ostaminen_kortilla_jos_ei_tarpeeksi_rahaa_palautaaa_false(self):
        for i in range(5): #Ostetaan ensin neljä lounasta kortilla jossa 1000 snt 
            self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(False, self.kassapaate.syo_edullisesti_kortilla(self.kortti))

    # ja samat testit maukkaale lounaalle 

    def test_lounaan_ostaminen_kortilla_kassa_ei_kasvaa_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(100000, self.kassapaate.kassassa_rahaa)

    def test_lounaan_ostaminen_kortilla_palauttaa_true_maukas(self):
        self.assertEqual(True, self.kassapaate.syo_maukkaasti_kortilla(self.kortti))
    
    def test_lounaan_ostaminen_kortilla_maara_kasvaa_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(1, self.kassapaate.maukkaat)

    def test_lounaan_ostaminen_kortilla_jos_ei_tarpeeksi_rahaa__kortilla_ei_kasvata_myytyjen_lounasten_maaraa_maukas(self):
        for i in range(3):
            self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(2, self.kassapaate.maukkaat)  #Ei voi ottaa viidettä maksua 

    def test_lounaan_ostaminen_kortilla_jos_ei_tarpeeksi_rahaa_palautaaa_false_maukas(self):
        for i in range(2): #Ostetaan ensin neljä lounasta kortilla jossa 1000 snt 
            self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(False, self.kassapaate.syo_maukkaasti_kortilla(self.kortti))

#TESTATAAN VIELÄ RAHAN LATAAMINEN KORTILLE!!! 

    def test_rahan_lataaminen_kortille_kasvattaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual("saldo: 15.0", str(self.kortti))
    
    def test_rahan_lataaminen_kortille_kasvattaa_kassaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(100500, self.kassapaate.kassassa_rahaa)

    def test_rahan_lataaminen_negatiivinen_summa_ei_vahenna_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -200)
        self.assertEqual("saldo: 10.0", str(self.kortti))
