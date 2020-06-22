#input start and end years
start_year = int(input('Please enter the start year: '))
end_year = int(input('Please enter the end year: '))
print('\nHere is a list of leap years between {0} and {1}: '.format(start_year, end_year))

#creat an empty list
leapYearList = []

#algorithm to determine leap years, and add them to the list created
for exact_year in range(start_year, end_year + 1):
    if (exact_year % 4 == 0 and exact_year % 100 != 0) or (exact_year % 400 == 0):
        leapYearList.append(exact_year)

#counter for the leap year list
for couter in range(len(leapYearList)):
    #change to a new line after ten elements
    if couter % 10 == 0:
        print('\n')
    #add full stop the end
    if couter == len(leapYearList) - 1:
        print(leapYearList[couter], end='.')
    #add commas for other items
    else:
        print(leapYearList[couter], end=', ')
