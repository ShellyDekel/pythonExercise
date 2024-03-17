import unittest
import tempfile
import csv
import os
import json
from main import csv_to_json


def create_temp_csv_file(data):
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
        ]

        csv_file_path = create_temp_csv_file(data)

        temp_json_directory = tempfile.TemporaryDirectory().name
        temp_json_filename = os.path.join(temp_json_directory, "test.json")

        try:
            csv_to_json(csv_file_path, temp_json_filename)

            with open(temp_json_filename) as json_file:
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

    def test_non_existant_csv_path(self):
        temp_json_directory = tempfile.TemporaryDirectory().name
        temp_json_filename = os.path.join(temp_json_directory, "test.json")

        try:
            csv_to_json("fakecsvfile.csv", temp_json_filename)
            self.assertTrue(False, "FileNotFoundError was not raised")
        except FileNotFoundError:
            self.assertTrue(True)

    def test_wrong_file_type(self):
        temp_file = tempfile.TemporaryFile().name
        temp_json_directory = tempfile.TemporaryDirectory().name
        temp_json_filename = os.path.join(temp_json_directory, "test.json")

        try:
            csv_to_json(temp_file, temp_json_filename)
            self.assertTrue(False, "FileNotFoundError was not raised")
        except FileNotFoundError:
            self.assertTrue(True)

    def test_json_directory_doesnt_exist(self):
        data = [
            ["variable1", "variable2", "variable3"],
            ["value1", 1, "1/1/2001"],
        ]
        csv_file_path = create_temp_csv_file(data)
        temp_json_directory = tempfile.TemporaryDirectory().name
        temp_json_filename = os.path.join(
            temp_json_directory, "dir/doesn't/exist/test.json"
        )
        try:
            csv_to_json(csv_file_path, temp_json_filename)
            self.assertTrue(os.path.isfile(temp_json_filename))
        except:
            self.assertTrue(False, "unexpected error")

    def test_json_filename_doenst_includes_suffix(self):
        data = [
            ["variable1", "variable2", "variable3"],
            ["value1", 1, "1/1/2001"],
        ]
        csv_file_path = create_temp_csv_file(data)
        temp_json_directory = tempfile.TemporaryDirectory().name
        temp_json_filename = os.path.join(temp_json_directory, "test")
        try:
            csv_to_json(csv_file_path, temp_json_filename)
            self.assertTrue(os.listdir(temp_json_directory)[0].endswith(".json"))
        except:
            self.assertTrue(False, "unexpected error")

    def test_empty_cvs_file(self):
        empty_cvs_file = tempfile.NamedTemporaryFile(
            suffix=".csv", delete=False, mode="w"
        )
        temp_json_directory = tempfile.TemporaryDirectory().name
        temp_json_filename = os.path.join(temp_json_directory, "test.json")

        csv_to_json(empty_cvs_file.name, temp_json_filename)

        self.assertTrue(
            os.path.isfile(temp_json_filename)
            and os.path.getsize(temp_json_filename) == 0
        )


if __name__ == "__main__":
    unittest.main()
