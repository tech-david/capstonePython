import unittest

from model.dataset.TrainTestData import train_test_split_business_cycle
from model.features.Preparation import complete_df


class MyTestCase(unittest.TestCase):
    def test_split(self):
        x_train, x_test, y_train, y_test = train_test_split_business_cycle()
        df = complete_df()
        train_size = len(x_train)
        test_size = len(x_test)
        total_size = len(df)
        self.assertEqual(test_size,
                         36,
                         "Test size should be 36 periods")
        self.assertEqual(total_size,
                         train_size + 36,
                         "Adding 36 to training should equal total data")


if __name__ == '__main__':
    unittest.main()
