# input the year
year = int(input("Please Enter a Year: "))
# determine whether the input year is valid
while year < 0:
    year = int(input('Error! Please Enter the Correct Year:'))
# algorithm to determine the leap year
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year.".format(year))
        else:
            print("{0} is a common leap year.".format(year))
    else:
        print("{0} is a leap year.".format(year))
else:
    print("{0} is a common year.".format(year))
