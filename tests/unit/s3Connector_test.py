import unittest

from helpers.S3Connector import connect


class MyTestCase(unittest.TestCase):
    def test_connection(self):
        # Test case: Connects to S3 bucket
        s3 = connect()
        bucket = s3.Bucket('capstoneds2022data')
        self.assertEqual(bucket.creation_date.year,
                         2022,
                         "S3 should connect using key")


if __name__ == '__main__':
    unittest.main()
