import unittest

from model.dataset.FullDataset import min_max_data


class MyTestCase(unittest.TestCase):
    def test_scaled_data(self):
        df = min_max_data()
        # Test case: Scales data
        self.assertEqual(all(df.min(axis=0)),
                         0,
                         "All columns have minimum value of 0")
        self.assertEqual(all(df.max(axis=0)),
                         1,
                         "All columns have maximum value of 1")


if __name__ == '__main__':
    unittest.main()
