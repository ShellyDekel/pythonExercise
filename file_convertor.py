from extract.extract_csv_file import extract_csv
from transform.parse_dates import parse_dates_in_dictionary_list
from load.load_json_file import to_json
import os


def csv_to_json_convertor(source, destination):
    source_data = extract_csv(source)
    date_collums = filter(lambda key: "date" in key.lower(), list(source_data[0]))
    transformed_data = parse_dates_in_dictionary_list(source_data, date_collums)
    destination_file_name = os.path.basename(source).split(".", 1)[0]

    to_json(transformed_data, destination, destination_file_name)
