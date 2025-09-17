
'''
import datetime 

today = datetime.datetime.now()
print(today)
print(today.day)

from datetime import datetime
today = datetime.now
print(today)


bday = input("Enter your birthday")

test = datetime.strptime(bday, "%m/%d/%Y")
print(test)

"Wednesday, June 22, 1990"

test_str = test.strftime("%A, %B %d %Y")
print(test_str)

from datetime import datetime, timedelta

from datetime import datetime, timedelta

bday = input("Enter your birthday")

test = datetime.strptime(bday, "%m/%d/%Y")
# print(test)
test = test + timedelta(days=1)
print(test)
test_str = test.strftime("%A, %B %d %Y")
print(test_str)
                 


'''


from datetime import datetime

def parsedate_mdy(text: str):
    """
    Parses a date in the format mm/dd/yyyy and returns a datetime object.
    """
    return datetime.strptime(text, '%m/%d/%Y')

def formatdate_ymd(date: datetime):
    """
    Takes a datetime object and returns a string in the format yyyy-mm-dd.
    """
    return date.strftime("%Y-%m-%d")

# Calling the functions
text = input('Enter date m/d/y: ')
date = parsedate_mdy(text)
date_str = formatdate_ymd(date)
print(date_str)
