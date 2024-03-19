import unittest
import tempfile
import csv
import os
from extract import extract_csv_file


def create_temp_csv_file(data): # noo need for tempfile
    with tempfile.NamedTemporaryFile(
        suffix=".csv", delete=False, mode="w"
    ) as temp_csv_file:
        csv_writer = csv.writer(temp_csv_file)

        for row in data:
            csv_writer.writerow(row)

        temp_file_path = temp_csv_file.name

    return temp_file_path


class TestConvertor(unittest.TestCase):

    def test_regualr_function(self):
        data = [
            ["variable1", "variable2", "variable3"],
            ["value1", 1, "1/1/2001"],
            ["value2", 2, "2.4.2011"],
            ["value7", 5, "22-12-1998"],
        ]

        csv_file_path = create_temp_csv_file(data)

        try:
            result = extract_csv_file.extract_csv(csv_file_path)

            self.assertEqual(
                    result,
                    [
                        {
                            "variable1": "value1",
                            "variable2": 1,
                            "variable3": "1/1/2001",
                        },
                        {
                            "variable1": "value2",
                            "variable2": 2,
                            "variable3": "2.4.2011",
                        },
                        {
                            "variable1": "value7",
                            "variable2": 5,
                            "variable3": "22-12-1998",
                        }
                    ],
                )
        finally:
            os.remove(csv_file_path)
            
    #TODO: add test for file with only titles, test with empty file


if __name__ == "__main__":
    unittest.main()
