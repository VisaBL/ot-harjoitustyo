import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)
    
    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual("saldo: 10.0", str(self.maksukortti))

    def test_kortin_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual("saldo: 15.0", str(self.maksukortti))

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual("saldo: 5.0", str(self.maksukortti))

    def test_saldo_ei_vahene_jos_ei_rahea(self):
        self.maksukortti.ota_rahaa(15000)
        self.assertEqual("saldo: 10.0", str(self.maksukortti))
    
    def test_metodi_palauttaa_true(self):
        self.assertEqual(True, self.maksukortti.ota_rahaa(500))
    
    def test_metodi_palauttaa_false(self):
        self.assertEqual(False, self.maksukortti.ota_rahaa(1500))

#Rahan ottaminen toimii
#   Saldo vähenee oikein, jos rahaa on tarpeeksi
#   Saldo ei muutu, jos rahaa ei ole tarpeeksi
#   Metodi palauttaa True, jos rahat riittivät ja muuten False
