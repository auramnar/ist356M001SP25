from datetime import datetime
def parsedate_mdy(text):
    return datetime.strptime(text, '%m/%d/%Y')
def formatdate_ymd(date):
    return date.strftime('%Y-%m-%d')
def test_parsedate_mdy():
    assert parsedate_mdy('12/31/2020') == datetime(2020, 12, 31)
    assert parsedate_mdy('03/06/2020') == datetime(2020, 3, 6)
def test_formatdate_ymd():
    assert formatdate_ymd(datetime(2020, 12, 31)) == '2020-12-31'
    assert formatdate_ymd(datetime(2020, 3, 6)) == '2020-03-06'