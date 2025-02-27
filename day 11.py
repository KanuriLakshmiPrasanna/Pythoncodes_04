#Return no.of days in a month, If it is leap year Feb should return 29, Non-leap year should return 28

def leap_year(yr):
    if yr%4==0:
        if yr%100==0:
            if yr%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def no_of_days(y,m):
    month_lst=[1,3,5,7,8,10,12]
    if month in month_lst:
        return (f"No.of days are 31")
    elif month==2:
        if is_leap_year:
            return (f"No.of days are 29")
        else:
            return (f"No.of days are 28")
    else:
        return (f"No.of days are 30")
year=int(input("Enter year:"))
month=int(input("Enter month number[eg Jan-1,Feb-2..]:"))
is_leap_year=leap_year(year)
print(no_of_days(year,month))
