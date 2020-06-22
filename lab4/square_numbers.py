def squareString(min, max):
    for i in range(min, max + 1):
        for j in range(i, i + (max - min)+1):
            ans = j
            if j > max:
                ans = j - (max - min) - 1
            print(ans, end='')
        print('')


squareString(0, 9)
