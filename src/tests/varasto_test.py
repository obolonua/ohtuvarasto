import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_with_negative_value(self):
    # Trying to add a negative amount should not change saldo
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_negatiivinen_tilavuus_nollataan(self):
        v = Varasto(-5)
        self.assertAlmostEqual(v.tilavuus, 0)

    def test_konstruktori_negatiivinen_alkusaldo_nollataan(self):
        v = Varasto(10, -7)
        self.assertAlmostEqual(v.saldo, 0)

    def test_konstruktori_alkusaldo_yli_tilavuuden_taytetaan(self):
        v = Varasto(10, 15)
        self.assertAlmostEqual(v.saldo, 10)


    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisataan_liikaa(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_negatiivinen_avro(self):
        self.varasto.ota_varastosta(-20)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_liikaa(self):
        self.varasto.lisaa_varastoon(10)
        x = self.varasto.ota_varastosta(15)
        self.assertAlmostEqual(x, 10)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    # def test_str_returns_correct_format(self):
    #     self.varasto.lisaa_varastoon(7)
    #     self.assertEqual(str(self.varasto), "saldo = 7, vielä tilaa 3")