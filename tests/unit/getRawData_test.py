import unittest

from helpers.GetRawData import get_gas_data


class MyTestCase(unittest.TestCase):
    def test_ingestion(self):
        df = get_gas_data()
        # Test case: Ingests data and applies test split
        self.assertTrue(df.columns.any(),
                        df[['Year', 'Month']],
                        "Both year and month columns should exist")  # Asserting both columns exist


if __name__ == '__main__':
    unittest.main()
