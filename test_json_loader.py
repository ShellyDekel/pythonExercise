from load.load_json_file import to_json
import unittest, tempfile, json, os, random, string
from itertools import repeat


def random_word(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


class TestConvertor(unittest.TestCase):
    def test_loadRegularData_loadedSuccessfully(self):
        data = [
            {"variable1": "value1", "variable2": 1, "variable3": "01.01.2001"},
            {"variable1": "asdfg", "variable2": 9, "variable3": "01.12.2020"},
            {"variable1": "qwerty", "variable2": 14, "variable3": "15.10.1998"},
        ]

        temporary_dir = tempfile.TemporaryDirectory().name
        base_filename = "testfile"

        to_json(data, temporary_dir, base_filename, 10)

        with open(os.path.join(temporary_dir, base_filename + ".json")) as json_file:
            self.assertEqual(json.load(json_file), data)

    def test_dataPassesFileLimit_loadedMultipleFilesSuccessfully(self):
        data = list(repeat({"key1": random_word(5), "key2": random_word(10)}, 21))
        temporary_dir = tempfile.TemporaryDirectory().name
        base_filename = "testfile"
        to_json(data, temporary_dir, base_filename, 10)
        expected_first = data[0:10]
        expected_second = data[10:20]
        expected_third = data[20:21]

        with open(
            os.path.join(temporary_dir, base_filename + "1.json")
        ) as first_json, open(
            os.path.join(temporary_dir, base_filename + "2.json")
        ) as second_json, open(
            os.path.join(temporary_dir, base_filename + "3.json")
        ) as third_json:
            self.assertTrue(
                len(os.listdir(temporary_dir)) == 3
                and json.load(first_json) == expected_first
                and json.load(second_json) == expected_second
                and json.load(third_json) == expected_third
            )

    def test_directoryDoesntExist_loadedSuccessfullyInNewlyCreatedDirectory(self):
        data = [{"variable1": "value1", "variable2": 1, "variable3": "01.01.2001"}]
        temporary_dir = tempfile.TemporaryDirectory().name + "/this/dir/does_not/exist"
        base_filename = "testfile"
        try:
            to_json(data, temporary_dir, base_filename, 10)
            self.assertTrue(
                os.path.isfile(os.path.join(temporary_dir, base_filename + ".json"))
            )
        except:
            self.fail("function failed")        
            
    def test_noData_raiseErrorAndDontCreateFile(self):
        data = []
        temporary_dir = tempfile.TemporaryDirectory().name
        base_filename = "testfile"
        
        with self.assertRaises(ValueError):
            to_json(data, temporary_dir, base_filename, 10)
        self.assertFalse(os.path.isfile(os.path.join(temporary_dir, base_filename + ".json")))
        


if __name__ == "__main__":
    unittest.main()
