###################################################
# Working with Dates
# Student: Sindhu
###################################################

def is_leap_year(year):
    """
    Returns True if year is a leap year, False otherwise.
    """
    if (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    elif (year % 4 == 0):
        return True
    else:
        return False


def days_in_month(year, month):
    """
    Returns the number of days in the given month and year.
    """
    if month < 1 or month > 12:
        return 0

    # Days in each month
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_leap_year(year):
        return 29
    else:
        return month_days[month - 1]


def is_valid_date(year, month, day):
    """
    Returns True if year-month-day is a valid date.
    """
    if year < 1 or month < 1 or month > 12:
        return False
    if day < 1 or day > days_in_month(year, month):
        return False
    return True


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Returns the number of days between two dates.
    If either date is invalid or the second date is before the first date, returns 0.
    """
    import datetime

    if not (is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2)):
        return 0

    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)

    delta = date2 - date1
    if delta.days < 0:
        return 0
    return delta.days


def age_in_days(year, month, day):
    """
    Returns person's age in days as of today.
    If date is invalid or in the future, returns 0.
    """
    import datetime

    if not is_valid_date(year, month, day):
        return 0

    birth_date = datetime.date(year, month, day)
    today = datetime.date.today()

    if birth_date > today:
        return 0

    delta = today - birth_date
    return delta.days


###################################################
# Test code
###################################################
# You can test here manually before submitting
print(days_in_month(2024, 2))     # 29 (leap year)
print(is_valid_date(2024, 2, 29)) # True
print(days_between(2024, 2, 1, 2024, 3, 1)) # 29
print(age_in_days(2000, 1, 1))    # Depends on current date
