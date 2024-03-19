from dateutil import parser
import copy


def parse_date(value):
    try:
        return parser.parse(value, dayfirst=True).strftime("%d.%m.%Y")
    except:
        raise TypeError("value is not a date")


def parse_dates_in_dictionary_list(dictionary_list, date_columns):
    parsed_list = copy.deepcopy(dictionary_list)
    for key in date_columns:
        for dictionary in parsed_list:
            dictionary[key] = parse_date(dictionary[key])

    return parsed_list
