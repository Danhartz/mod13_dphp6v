import re
import unittest
from datetime import datetime

#validating functions

def is_valid_symbol(symbol: str) -> bool:
    """
    symbol: must be 1–7 uppercase alphabetical characters (A – Z)
    """
    if not isinstance(symbol, str):
        return False
    return bool(re.fullmatch(r"[A-Z]{1,7}", symbol))


def is_valid_chart_type(choice: str) -> bool:
    """
    chart type: 1 numeric character, must be 1 or 2
    (1=line, 2=bar)
    """
    if not isinstance(choice, str):
        return False
    return bool(re.fullmatch(r"[12]", choice))


def is_valid_time_series(choice: str) -> bool:
    """
    time series function: 1 numeric character, must be 1–4
    (1=daily, 2=weekly, 3=monthly, 4=other)
    """
    if not isinstance(choice, str):
        return False
    return bool(re.fullmatch(r"[1-4]", choice))

def is_valid_date(date_str: str) -> bool:
    """
    date type: must match YYYY-MM-DD
    """
    if not isinstance(date_str, str):
        return False
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_valid_date_range(start: str, end: str) -> bool:
    """
    Ensures:
    - Both are valid dates
    - End date >= start date
    """
    if not (is_valid_date(start) and is_valid_date(end)):
        return False

    start_dt = datetime.strptime(start, "%Y-%m-%d")
    end_dt = datetime.strptime(end, "%Y-%m-%d")
    return end_dt >= start_dt

#unit tests

class TestProject3Inputs(unittest.TestCase):

    #symbols
    def test_symbol_valid(self):
        self.assertTrue(is_valid_symbol("A"))
        self.assertTrue(is_valid_symbol("AAPL"))
        self.assertTrue(is_valid_symbol("ABCDEFG"))  

    def test_symbol_invalid(self):
        self.assertFalse(is_valid_symbol("aapl"))     
        self.assertFalse(is_valid_symbol("AaPL"))     
        self.assertFalse(is_valid_symbol("AAPL1"))    
        self.assertFalse(is_valid_symbol("ABCDEFGH")) 

    #chart type
    def test_chart_type_valid(self):
        self.assertTrue(is_valid_chart_type("1"))
        self.assertTrue(is_valid_chart_type("2"))

    def test_chart_type_invalid(self):
        self.assertFalse(is_valid_chart_type("0"))
        self.assertFalse(is_valid_chart_type("3"))
        self.assertFalse(is_valid_chart_type("line"))
        self.assertFalse(is_valid_chart_type(""))

    #time series
    def test_time_series_valid(self):
        self.assertTrue(is_valid_time_series("1"))
        self.assertTrue(is_valid_time_series("2"))
        self.assertTrue(is_valid_time_series("3"))
        self.assertTrue(is_valid_time_series("4"))

    def test_time_series_invalid(self):
        self.assertFalse(is_valid_time_series("0"))
        self.assertFalse(is_valid_time_series("5"))
        self.assertFalse(is_valid_time_series("daily"))
        self.assertFalse(is_valid_time_series(""))

    #dates
    def test_date_valid(self):
        self.assertTrue(is_valid_date("2024-01-01"))
        self.assertTrue(is_valid_date("1999-12-31"))

    def test_date_invalid_format(self):
        self.assertFalse(is_valid_date("01-01-2024"))
        self.assertFalse(is_valid_date("2024/01/01"))
        self.assertFalse(is_valid_date("2024-1-1"))
        self.assertFalse(is_valid_date(""))

    def test_date_invalid_values(self):
        self.assertFalse(is_valid_date("2024-13-01"))
        self.assertFalse(is_valid_date("2024-02-30"))

    #date range
    def test_date_range_valid(self):
        self.assertTrue(is_valid_date_range("2024-01-01", "2024-01-10"))
        self.assertTrue(is_valid_date_range("2024-01-01", "2024-01-01"))

    def test_date_range_invalid(self):
        self.assertFalse(is_valid_date_range("2024-01-10", "2024-01-01"))
        self.assertFalse(is_valid_date_range("bad-date", "2024-01-10"))
        self.assertFalse(is_valid_date_range("2024-01-01", "nope"))

#run unit tests

if __name__ == "__main__":
    unittest.main()
