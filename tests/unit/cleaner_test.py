import unittest

import numpy as np
from numpy import dtype

from helpers.Cleaner import resample_gas, fill_cpi_na


class MyTestCase(unittest.TestCase):

    def test_resample(self):
        df = resample_gas()
        # Test case: Resamples data
        self.assertNotEqual(any(df.columns),
                            'Percentage of Residential Sector Consumption for Which Price Data Are Available',
                            "Should not contain column of percentage consumption")
        # Test case: Datetime index present
        self.assertEqual(df.index.dtype,
                         dtype('<M8[ns]'),  # Numpy datetime dtype
                         "Data frame index should be date time")

    # Test case: Cleans and fills NaN
    def test_fill_na(self):
        df = fill_cpi_na()
        self.assertNotEqual(df.values.any(),
                            np.nan,
                            "No values should be NaN")


if __name__ == '__main__':
    unittest.main()
