from extract import extract_files
from transform import parser
from load import upload_file
import os


def csv_to_json_convertor(source, destination):
    source_data = extract_files.extract_csv(source)
    transformed_data = parser.parse_dates_dict(source_data)
    destination_file_name = os.path.basename(source).split(".", 1)[0]

    upload_file.to_json(transformed_data, destination, destination_file_name)
