from dateutil import parser
import copy, logging

logger = logging.getLogger(__name__)


def parse_date(value):
    try:
        logger.debug("parsing value: " + value)

        return parser.parse(value, dayfirst=True).strftime("%d.%m.%Y")
    except:
        logger.error("value " + value + " is not a valid date")

        raise TypeError("value is not a date")


def parse_dates_in_dictionary_list(dictionary_list, date_columns):
    logger.info(
        "parsing dictionary list according to values: [" + ", ".join(date_columns) + "]"
    )

    if not date_columns:
        logger.error("no columns were given")

        raise ValueError("no date columns given")
    else:
        parsed_list = copy.deepcopy(dictionary_list)

        for key in date_columns:
            for dictionary in parsed_list:

                try:
                    logger.debug(list(dictionary))
                    dictionary[key] = parse_date(dictionary[key])
                except KeyError:
                    logger.error(
                        "key: "
                        + key
                        + " does not exist in the given dictionary list"
                    )
                    raise KeyError(key + "does not exist in given dictionary")

        logger.info("dictionary list parsed successfully")

        return parsed_list
