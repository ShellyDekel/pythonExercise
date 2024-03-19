import unittest
from transform import parse_dates


class TestParser(unittest.TestCase):

    def test_regularDMYDate_parsedDate(self):
        data = "20/5/2000"
        result = parse_dates.parse_date(data)
        self.assertEqual(result, "20.05.2000")

    def test_MDYDate_ParsedDMYDate(self):
        data = "7-25-2002"
        result = parse_dates.parse_date(data)
        self.assertEqual(result, "25.07.2002")

    def test_plaintextDate_ParsedDMYDate(self):
        data = "January 2nd 2003"
        result = parse_dates.parse_date(data)
        self.assertEqual(result, "02.01.2003")

    def test_notADate_trowError(self):
        data = "example"
        with self.assertRaises(TypeError):
            parse_dates.parse_date(data)

    def test_datelikeNumericalValue_throwError(self):
        data = 12032022
        with self.assertRaises(TypeError):
            parse_dates.parse_date(data)

    def test_emptyVariable_throwError(self):
        data = None
        with self.assertRaises(TypeError):
            parse_dates.parse_date(data)

    def test_averageInput_successfullyParsedAllDates(self):
        data = [
            {"key1": "value1", "date": "1/2/2003", "another": "jan 5 2019", "last": 78},
            {"key1": "value2", "date": "8/8/1994", "another": "oct 18 1984","last": 555},
            {"key1": "string", "date": "6/12/2021", "another": "feb 22 1807","last": 12}
        ]
        expected = [
            {"key1": "value1", "date": "01.02.2003", "another": "05.01.2019","last": 78},
            {"key1": "value2", "date": "08.08.1994", "another": "18.10.1984","last": 555},
            {"key1": "string", "date": "06.12.2021", "another": "22.02.1807","last": 12}
        ]
        result = parse_dates.parse_dates_in_dictionary_list(data, ["date", "another"])
        self.assertEqual(result, expected)

    def test_averageInput_originalDataUnchangedAfterCallingFunction(self):
        data = [
            {"key1": "value1", "date": "1/2/2003", "another": "jan 5 2019", "last": 78},
            {"key1": "value2", "date": "8/8/1994", "another": "oct 18 1984","last": 555},
            {"key1": "string", "date": "6/12/2021", "another": "feb 22 1807","last": 12}
        ]
        result = parse_dates.parse_dates_in_dictionary_list(data, ["date", "another"])
        self.assertNotEqual(result, data)


if __name__ == "__main__":
    unittest.main()
