age = int(input('Enter your age: '))
while age < 0:
    age = int(input('Please enter a correct age: '))

record = str(input('Do you have a criminal record (y/n): '))
#while record != 'y' or 'n':
#    record = str(input('Please enter a correct record: '))

if age >= 18 and age <= 65:
    if record == 'n':
        print('You are required to do jury service.')
    else:
        print('You are excluded from jury service.')
else:
    print('You are excluded from jury service.')
