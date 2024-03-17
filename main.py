import pandas
import os
import json
from dateutil import parser


def parse_date(date):
    try:
        return parser.parse(date, dayfirst=True).strftime("%d.%m.%Y")
    except:
        return date


def csv_to_json(csv_path: str, json_directory: str, json_file_name: str):
    if not os.path.isfile(csv_path) or not csv_path.endswith(".csv"):
        raise Exception("CSV file not found")

    if not os.path.isdir(json_directory):
        os.makedirs(json_directory)

    if not json_file_name.endswith(".json"):
        json_file_name += ".json"

    csv_file = pandas.read_csv(csv_path)

    csv_file = csv_file.map(lambda x: parse_date(x))

    json_file_path = os.path.join(json_directory, json_file_name)

    with open(json_file_path, "w") as json_file:
        json.dump(csv_file.to_dict(orient="records"), json_file, indent=2)


def main():
    csv_to_json("MadaReports - MadaReports.csv", "./mada_reports", "madareports")


if __name__ == "__main__":
    main()
