import dateutils
date_str = '1/15/2025'
parsed_date = dateutils.parsedate_mdy(date_str)
formatted_date = dateutils.formatdate_ymd(parsed_date)
print(formatted_date)