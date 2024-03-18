from extract import extract_files
from transform import parser
from load import upload_file
import os

def csv_to_json(csv_path: str, json_file_name: str):

    # load
    os.makedirs(os.path.dirname(json_file_name), exist_ok=True)

    try:
        # extract
        csv_file = pandas.read_csv(csv_path)
        # transform
        csv_file = csv_file.map(lambda x: parse_date(x))

        # load
        with open(json_file_name, "w") as json_file:
            json.dump(csv_file.to_dict(orient="records"), json_file, indent=2)
    except:
        with open(json_file_name, "w") as json_file:
            pass
        
def csv_to_json_convertor(source, destination):
    source_data = extract_files.extract_csv(source)
    transformed_data = parser.parse_dates_dict(source_data)
    destination_file_name = os.path.basename(source).split(".", 1)[0]
    
    upload_file.to_json(transformed_data, destination, destination_file_name)