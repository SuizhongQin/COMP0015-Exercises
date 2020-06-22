age = int(input('Enter your age: '))
while age < 0:
    age = int(input('Please enter your age: '))

price = 6
halfPrice = 6 / 2
thirdPrice = 6 / 3

if age < 16 and age >= 0:
    print('Your ticket costs {0:4.2f} pounds.'.format(halfPrice))
elif age >= 60:
    print('Your ticket costs {0:4.2f} pounds.'.format(thirdPrice))
else:
    print('Your ticket costs {0:4.2f} pounds.'.format(price))
