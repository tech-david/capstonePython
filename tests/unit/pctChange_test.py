import unittest

from model.features.Aggregator import get_all_features
from model.features.PctChange import percent_change


class MyTestCase(unittest.TestCase):
    def test_extract_features(self):
        # Get features before and after extraction
        df_not_extracted = get_all_features()
        df_extracted = percent_change()
        # Get standard deviations of bread column to test
        std_n_e = df_not_extracted[['Bread']].std()
        std_e = df_extracted[['Bread']].std()
        # Values should change
        self.assertNotEqual(std_e.values,
                            std_n_e.values,
                            "Values should not be equal")


if __name__ == '__main__':
    unittest.main()
