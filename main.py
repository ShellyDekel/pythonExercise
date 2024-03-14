import pandas

def excelToJson(excelPath: str, jsonDirectoryPath: str, jsonFileName: str):
    excelFile = pandas.read_csv(excelPath)
    jsonFile = open(jsonDirectoryPath + "/" + jsonFileName + ".json", "w")
    jsonFile.write(excelFile.to_json(orient='records'))

def main():
    excelToJson("MadaReports - MadaReports.csv", "./mada_reports", "madareports")

if __name__ == "__main__":
    main()