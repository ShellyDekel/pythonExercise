import pandas, logging, os

logger = logging.getLogger(__name__)

def extract_csv(filepath):
    logger.info("extracting csv file: " + filepath)
    
    if not os.path.isfile(filepath):
        logger.error("csv file " + filepath + " cannot be extracted: file doesn't exist")
        raise FileNotFoundError("given file doesn't exit")
    else:
        try:
            file_data = pandas.read_csv(filepath).to_dict(orient="records")
        except:
            logger.error("csv file " + filepath + " cannot be extracted: wrong file format")
            raise FileNotFoundError("wrong file format, function requires csv file")
        
        if file_data:
            logger.info("successfully extracted csv file " + filepath)
            return file_data
        else:
            logger.error("csv file " + filepath + " cannot be extracted: file does not contain any data")
            raise FileNotFoundError("file does not contain any data")
