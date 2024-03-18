import unittest
from transform import parser


class TestParser(unittest.TestCase):

    def test_regular_date(self):
        data = "20/5/2000"
        result = parser.parse_date(data)
        self.assertEqual(result, "20.05.2000")

    def test_american_date(self):
        data = "7-25-2002"
        result = parser.parse_date(data)
        self.assertEqual(result, "25.07.2002")

    def test_plaintext_date(self):
        data = "January 2nd 2003"
        result = parser.parse_date(data)
        self.assertEqual(result, "02.01.2003")

    def test_not_a_date(self):
        data = "example"
        result = parser.parse_date(data)
        self.assertEqual(result, "example")

    def test_numerical_value(self):
        data = 12345
        result = parser.parse_date(data)
        self.assertEqual(result, 12345)

    def test_empty_value(self):
        data = None
        result = parser.parse_date(data)
        self.assertEqual(result, None)


if __name__ == "__main__":
    unittest.main()
