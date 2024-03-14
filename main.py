import pandas

def csv_to_json(csv_path: str, json_directory_path: str, json_file_name: str):
    csv_file = pandas.read_csv(csv_path)
    json_file = open(json_directory_path + "/" + json_file_name + ".json", "w")
    json_file.write(csv_file.to_json(orient='records', indent=2))

def main():
    csv_to_json("MadaReports - MadaReports.csv", "./mada_reports", "madareports")

if __name__ == "__main__":
    main()