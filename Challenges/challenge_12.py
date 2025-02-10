from datetime import datetime
def parsedate_mdy(text):
    return datetime.strptime(text, '%m/%d/%Y')
def formatdate_ymd(date):
    return date.strftime('%Y-%m-%d')
date_str = '1/15/2025'
parsed_date = parsedate_mdy(date_str)
formatted_date = formatdate_ymd(parsed_date)
print(formatted_date)