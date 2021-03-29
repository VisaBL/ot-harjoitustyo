import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    #luodaan kolme korttia 
    def setUp(self):
        self.kortti = Maksukortti(10)
        self.kortti_2_5 = Maksukortti(2.5)
        self.kortti_4 = Maksukortti(4)
    #testi 3
    def test_syo_edullisesti_onnistuu_kun_saldoa_2_5(self):
        self.kortti_2_5.syo_edullisesti()
        self.assertEqual(str(self.kortti_2_5), "Kortilla on rahaa 0.0 euroa")
    #testi 4
    def test_syo_maukkaasti_onnistuu_kun_saldoa_4(self):
        self.kortti_4.syo_maukkaasti()
        self.assertEqual(str(self.kortti_4), "Kortilla on rahaa 0 euroa")

    #testi1
    def test_syo_jokapäivä_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        for i in range(5):
            self.kortti.syo_maukkaasti()
        self.assertEqual("Kortilla on rahaa 2 euroa", str(self.kortti))
    #test2
    def test_kortille_voi_ladata_negatiivista_rahaa(self):
        self.kortti.lataa_rahaa(-25)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

