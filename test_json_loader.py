from load.load_json_file import to_json
import unittest
import tempfile
import json
import os
from itertools import repeat


class TestConvertor(unittest.TestCase):
    def test_upload(self):
        data = [
            {
                "variable1": "value1",
                "variable2": 1,
                "variable3": "01.01.2001",
            }
        ]
        temporary_dir = tempfile.TemporaryDirectory().name
        base_filename = "testfile"

        to_json(data, temporary_dir, base_filename)

        with open(os.path.join(temporary_dir, base_filename + ".json")) as json_file:
            self.assertEqual(json.load(json_file), data)

    def test_large_data(self):
        data = list(repeat({"key1": "value1", "key2": "value2"}, 50001)) #TODO test more than just amount of files created, test files actually hold the expected values
        temporary_dir = tempfile.TemporaryDirectory().name
        base_filename = "testfile"
        to_json(data, temporary_dir, base_filename)

        self.assertEqual(len(os.listdir(temporary_dir)), 2)

    def test_non_existent_directory(self):
        data = [
            {
                "variable1": "value1",
                "variable2": 1,
                "variable3": "01.01.2001",
            }
        ]
        temporary_dir = tempfile.TemporaryDirectory().name + "/this/dir/does_not/exist"
        base_filename = "testfile"
        try:
            to_json(data, temporary_dir, base_filename)
            self.assertTrue(
                os.path.isfile(os.path.join(temporary_dir, base_filename + ".json"))
            )
        except:
            self.fail("function failed")


if __name__ == "__main__":
    unittest.main()
