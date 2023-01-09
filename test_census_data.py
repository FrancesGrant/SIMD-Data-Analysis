import unittest
import simd_age


class TestCensusData(unittest.TestCase):
    def test_regions(self):
        """ Function to test that the regions function generates a list of available 
        regions in the dataset"""
        regions = len(census_data.regions())
        #  Expected value
        expected_value = 358
        self.assertEqual(regions, expected_value)

    
    def test_total_population(self):
        pass
        """ Function to test that the total_population returns the total population in
         a specific region for people an age less than or equal to an input age"""
        lower_deeside_under_15 = (census_data.total_population("Lower Deeside", 15))
        #  Expected value
        expected_value = 2962
        self.assertEqual(lower_deeside_under_15, expected_value)

census_data = simd_age.CensusData("DC1117SC.csv")
census_data.load()
census_data.regions()

if __name__ == "__main__":
    unittest.main()




