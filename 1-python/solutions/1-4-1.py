from datetime import datetime

'''
# Get all attributes of the datetime module
attributes = dir(datetime)
for attribute in attributes:
    print(attribute)

'''

text = input("Enter date m/d/y: ")
now = datetime.strptime(text, "%m/%d/%Y")
nowstr = now.strftime("%Y-%m-%d")
print(nowstr)




import datetime
today = datetime.datetime.now()
print(today.day) 

----
        
from datetime import datetime
             
today = datetime.now()
print(today)

birthday = input("Enter your birthday")
test = datetime.strptime(birthday, '%m/%d/%Y')
print(test)
test_str = test.strftime('%A, %B %d %Y')
print(test_str)
---


from datetime import datetime, timedelta


birthday = input("Enter your birthday")

test = datetime.strptime(birthday, '%m/%d/%Y')
test = test + timedelta(days=1)
test_str = test.strftime('%A, %B %d %Y')
print(test_str)
