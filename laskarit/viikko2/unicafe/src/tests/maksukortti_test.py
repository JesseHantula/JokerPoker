import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(2500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")
    
    def test_rahan_ottaminen_toimii(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_rahan_ottaminen_ei_vie_saldoa_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_ottaminen_palauttaa_true_jos_rahaa_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_rahan_ottaminen_palauttaa_false_jos_rahaa_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)

