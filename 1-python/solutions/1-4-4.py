from datetime import datetime

# Define the functions that you want to test
def parsedate_mdy(text: str) -> datetime:
    """
    Parses a date in the format mm/dd/yyyy and returns a datetime object.
    """
    return datetime.strptime(text, "%m/%d/%Y")

def formatdate_ymd(date: datetime) -> str:
    """
    Takes a datetime object and returns a string in the format yyyy-mm-dd.
    """
    return date.strftime("%Y-%m-%d")

# Test functions to assert expected results

def test_parsedate_mdy():
    # Test Case 1: Valid input
    date = parsedate_mdy("02/05/2025")
    assert date == datetime(2025, 2, 5), f"Test failed: expected '2025-02-05', got {date}"

    # Test Case 2: Another valid input
    date = parsedate_mdy("12/25/2023")
    assert date == datetime(2023, 12, 25), f"Test failed: expected '2023-12-25', got {date}"

def test_formatdate_ymd():
    # Test Case 1: Valid datetime object
    date_str = formatdate_ymd(datetime(2025, 2, 5))
    assert date_str == "2025-02-05", f"Test failed: expected '2025-02-05', got {date_str}"

    # Test Case 2: Another valid datetime object
    date_str = formatdate_ymd(datetime(2023, 12, 25))
    assert date_str == "2023-12-25", f"Test failed: expected '2023-12-25', got {date_str}"

# Run the test functions
if __name__ == "__main__":
    test_parsedate_mdy()
    test_formatdate_ymd()
    print("All tests passed!")


# testing demo
date = '12/30/2000'
date_dt_expect = datetime(2000, 12, 30)
date_dt_actual = parsedate_mdy(date)
assert date_dt_expect == date_dt_actual, f"Test failed: expected {date_dt_expect}, got {date_dt_actual}"
