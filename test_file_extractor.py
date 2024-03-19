import unittest
import tempfile
import csv
import os
from extract.extract_csv_file import extract_csv


def write_csv_file(path, data):
    with open(path, "w") as temp_csv_file:
        csv_writer = csv.writer(temp_csv_file)

        for row in data:
            csv_writer.writerow(row)


class TestConvertor(unittest.TestCase):

    def test_regularFile_expectedResult(self):
        data = [
            ["variable1", "variable2", "variable3"],
            ["value1", 1, "1/1/2001"],
            ["value2", 2, "2.4.2011"],
            ["value7", 5, "22-12-1998"],
        ]
        csv_file = tempfile.NamedTemporaryFile(suffix=".csv", mode="w").name
        write_csv_file(csv_file, data)
        result = extract_csv(csv_file)

        self.assertEqual(
            result,
            [
                {"variable1": "value1", "variable2": 1, "variable3": "1/1/2001"},
                {"variable1": "value2", "variable2": 2, "variable3": "2.4.2011"},
                {"variable1": "value7", "variable2": 5, "variable3": "22-12-1998"},
            ],
        )

    # TODO: add test for file with only titles, test with empty file


if __name__ == "__main__":
    unittest.main()
