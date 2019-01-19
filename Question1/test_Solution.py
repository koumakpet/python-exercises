import unittest
import Solution


class TestSolution(unittest.TestCase):
    """Test for Solution"""

    def test_main(self):
        result = Solution.main()
        self.assertEqual(result, """105,140,175,210,245,280,315,350,385,420,455,490,525,560,595,630,665,700,735,770,805,840,875,910,945,980,1015,1050,1085,1120,1155,1190,1225,1260,1295,1330,1365,1400,1435,1470,1505,1540,1575,1610,1645,1680,1715,1750,1785,1820,1855,1890,1925,1960,1995,2030,2065,2100,2135,2170,2205,2240,2275,2310,2345,2380,2415,2450,2485,2520,2555,2590,2625,2660,2695,2730,2765,2800,2835,2870,2905,2940,2975,3010,3045,3080,3115,3150,3185,3220,3255,3290,3325,3360,3395,3430,3465,3500,3535,3570,3605,3640,3675,3710,3745,3780,3815,3850,3885,3920,3955,3990,4025,4060,4095,4130,4165,4200,4235,4270,4305,4340,4375,4410,4445,4480,4515,4550,4585,4620,4655,4690,4725,4760,4795,4830,4865,4900,4935,4970,5005,5040,5075,5110,5145,5180,5215,5250,5285,5320,5355,5390,5425,5460,5495,5530,5565,5600,5635,5670,5705,5740,5775,5810,5845,5880,5915,5950,5985,6020,6055,6090,6125,6160,6195,6230,6265,6300,6335,6370,6405,6440,6475,6510,6545,6580,6615,6650,6685,6720,6755,6790,6825,6860,6895,6930,6965,7000,7035,7070,7105,7140,7175,7210,7245,7280,7315,7350,7385,7420,7455,7490,7525,7560,7595,7630,7665,7700,7735,7770,7805,7840,7875,7910,7945,7980""")


if __name__ == '__main__':
    unittest.main()
