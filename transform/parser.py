from dateutil import parser

def parse_date(value):
    try:
        return parser.parse(value, dayfirst=True).strftime("%d.%m.%Y")
    except:
        return value
    
def parse_dates_dict(dictionary_list):
    for index in dictionary_list:
        for key, value in dictionary_list[index]:
            dictionary_list[index][key] = parse_date(value)
    
    return dictionary_list