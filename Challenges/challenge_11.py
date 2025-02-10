from datetime import datetime
date='1/15/2025'
date=datetime.strptime(date, '%m/%d/%Y')
date = str(date.date())
print(date)