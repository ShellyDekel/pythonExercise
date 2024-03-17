import unittest
import tempfile
import csv
import os
import json
from main import csv_to_json


def create_temp_csv_file(data):
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False, mode="w") as temp_csv_file:
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
        ]

        csv_file_path = create_temp_csv_file(data)

        temp_json_directory = tempfile.TemporaryDirectory().name
        temp_json_filename = "test.json"

        try:
            csv_to_json(csv_file_path, temp_json_directory, temp_json_filename)

            with open(
                os.path.join(temp_json_directory, temp_json_filename)
            ) as json_file:
                self.assertEqual(
                    json.load(json_file),
                    [
                        {
                            "variable1": "value1",
                            "variable2": 1,
                            "variable3": "01.01.2001",
                        }
                    ],
                )
        finally:
            os.remove(csv_file_path)


if __name__ == "__main__":
    unittest.main()
