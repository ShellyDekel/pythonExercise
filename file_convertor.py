from extract.extract_csv_file import extract_csv
from transform.parse_dates import parse_dates_in_dictionary_list
from load.load_json_file import to_json
import os, logging

logger = logging.getLogger(__name__)


def csv_to_json_convertor(source, destination):
    source_data = extract_csv(source)
    date_columns = filter(lambda key: "date" in key.lower(), list(source_data[0]))
    
    if date_columns:
        logger.info("data requires date parsing")
        source_data = parse_dates_in_dictionary_list(source_data, date_columns)
    destination_file_name = os.path.basename(source).split(".", 1)[0]

    to_json(source_data, destination, destination_file_name, 50000)
