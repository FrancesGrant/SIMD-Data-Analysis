import unittest
import simd_age

class TestSIMD_Data(unittest.TestCase):
    def test_regions(self):
        """ Function to test that the regions function generates a list of available 
        regions in the dataset"""
        regions = len(simd_data.regions())
        #  Expected value
        expected_value = 352
        self.assertEqual(regions, expected_value)

    def test_lowest_simd(self):
        """ Function to test that the lowest_simd function returns the name 
        of the region that has the lowest average SIMD rank"""
        lowest_simd = (simd_data.lowest_simd())
        #  Expected string
        expected_string = 'Mossend and Holytown'
        self.assertEqual(lowest_simd, expected_string)

simd_data = simd_age.SIMD_Data("SIMD_2020v2.csv")
simd_data.load()
simd_data.regions()

if __name__ == "__main__":
    unittest.main()



    