import unittest
import tempfile
import csv
import os
from main import csv_to_json


def create_temp_csv_file(data):
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as temp_csv_file:
        with csv.writer(temp_csv_file) as csv_writer:
            for row in data:
                csv_writer.writerow(row)
        temp_file_path = temp_csv_file.name

    return temp_file_path


class TestConvertor(unittest.TestCase):

    def test_regualr_function(self):
        data = [
            ["variable1", "variable2", "variable3"],
            ["value1", 1, "1/1/2001"],
            ["value2", 2, "2,2,2002"],
            ["value3", 3, "3.3.2003"],
        ]
        
        csv_file_path = create_temp_csv_file(data)

        temp_json_directory = tempfile.TemporaryDirectory().name
        temp_json_filename = "test.json"
        
        try:
            csv_to_json(csv_file_path, temp_json_directory, temp_json_filename)
            
            with open(os.path.join(temp_json_directory, temp_json_filename)) as json_file:
                self.assertEqual()
        finally:
            os.remove(csv_file_path)


if __name__ == "__main__":
    unittest.main()
