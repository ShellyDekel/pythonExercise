import pandas


def extract_csv(filepath):
    file_data = pandas.read_csv(filepath).to_dict(orient="records")
    
    if not file_data == []:
        return file_data
    else:
        raise FileNotFoundError("file does not contain any values")
