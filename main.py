import pandas
import os
import json
from dateutil import parser


def parse_date(date):
    try:
        return parser.parse(date, dayfirst=True).strftime("%d.%m.%Y")
    except:
        return date


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


def main():
    csv_to_json("MadaReports - MadaReports.csv", "mada_reports/madareports")


if __name__ == "__main__":
    main()
