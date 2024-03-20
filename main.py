from file_convertor import csv_to_json_convertor
import logging

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=logging.INFO, datefmt='%d.%m.%Y %I:%M:%S %p')
    logger.info("started converting files")
    csv_to_json_convertor("MadaReports - MadaReports.csv", "mada_reports")
    logger.info("converted successfully, exiting program")


if __name__ == "__main__":
    main()
