import pandas

def excel_to_json(excel_path: str, json_directory_path: str, json_file_name: str):
    excelFile = pandas.read_csv(excel_path)
    json_file = open(json_directory_path + "/" + json_file_name + ".json", "w")
    json_file.write(excelFile.to_json(orient='records', indent=2))

def main():
    excel_to_json("MadaReports - MadaReports.csv", "./mada_reports", "madareports")

if __name__ == "__main__":
    main()