def main():
    time = input("What time is it? ")
    time = convert(time)
    
    if time >= 7 and time <= 8:
        print("breakfast time")
    
    elif time >= 12 and time <= 13:
        print("lunch time")
    
    elif time >= 18 and time <= 19:
        print("dinner time")
    
    else:
        pass


def convert(time):
    am_pm = None
    
    try:
        time, am_pm = time.split(" ")
    except ValueError:
        pass
    
    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute)/60
    
    foo = hour + minute
    
    if am_pm:
        if am_pm == "p.m.":
            foo += 12
    
    return foo


if __name__ == "__main__":
    main()