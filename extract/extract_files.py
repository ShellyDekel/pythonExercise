import pandas

def extract_csv(filepath):
    return pandas.read_csv(filepath).to_dict(orient="records")