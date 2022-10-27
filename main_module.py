def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


if __name__ == "__main__":
    year = int(input("Type in what year you want to check if it is a leap year: "))
    if isLeapYear(year):
        print(f"\n the chosen year is: {year} which is a leap year!")
    else:
        print(f"\n the chosen year is: {year} which is not a leap year!")
