import unittest
from transform import parse_dates


class TestParser(unittest.TestCase):

    def test_regular_date(self):
        data = "20/5/2000"
        result = parse_dates.parse_date(data)
        self.assertEqual(result, "20.05.2000")

    def test_american_date(self):
        data = "7-25-2002"
        result = parse_dates.parse_date(data)
        self.assertEqual(result, "25.07.2002")

    def test_plaintext_date(self):
        data = "January 2nd 2003"
        result = parse_dates.parse_date(data)
        self.assertEqual(result, "02.01.2003")

    def test_not_a_date(self):
        data = "example"
        result = parse_dates.parse_date(data)
        self.assertEqual(result, "example")

    def test_numerical_value(self):
        data = 12345
        result = parse_dates.parse_date(data)
        self.assertEqual(result, 12345)

    def test_empty_value(self):
        data = None
        result = parse_dates.parse_date(data)
        self.assertEqual(result, None)
        
    
    def test_no_dates(self):
        data = [{"key1": "value1"}, {"key1": "value2"}]
        result = parse_dates.parse_dates_dict(data)
        self.assertEqual(result, data)
        
    def test_all_dates_converted(self):
        data = [{"key1": "1/2/2003"}, {"key1": "Feb 8 1999", "key2": "9.22.2024"}]
        result = parse_dates.parse_dates_dict(data)
        self.assertEqual(result, [{"key1": "01.02.2003"}, {"key1": "08.02.1999", "key2": "22.09.2024"}])

if __name__ == "__main__":
    unittest.main()
