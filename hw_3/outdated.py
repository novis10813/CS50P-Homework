l = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

small_month = [4, 6, 9, 11]


def isleapyear(year:int):
    assert year > 0
    # judge leap year or not
    # the year mod 4 == 0, and mod 100 != 0
    # the year mod 400 == 0
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


while True:
    try:
        '''
        There are several  condition for this problem:
        1. there are different days in different month
        2. leap year leads to 29 days in February
        '''
        dates = input("Date: ")
        
        # month sanity check
        if dates[0].isdigit():
            month, day, year = dates.split("/")
            assert (int(month) >= 1) and (int(month) <= 12)
            month = int(month)
        else:
            month, day, year = dates.replace(",", "").split(" ")
            assert month.title() in l
            month = l.index(month.title()) + 1
        
        day = int(day)
        year = int(year)
        
        # day sanity check
        if isleapyear(int(year)):
            if month == 2:
                assert (day >= 1) and (day <= 29)
            
            elif month in small_month:
                assert (day >= 1) and (day <= 30)
                
            else:
                assert (day >= 1) and (day <= 31)
        
        print(f"{year}-{month:02d}-{day:02d}")
        
    except AssertionError:
        pass
    
    else:
        break