from dateutil import parser


def parse_date(value):
    try:
        return parser.parse(value, dayfirst=True).strftime("%d.%m.%Y")
    except:
        TypeError("value is not a date")


def parse_dates_in_dictionary_list(dictionary_list, date_columns):
    for key in date_columns:
        for dictionary in dictionary_list:
            dictionary[key] = parse_date(dictionary[key])

    return dictionary_list
