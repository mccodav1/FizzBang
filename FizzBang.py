for num in range(1,101):
    if num % 3 != 0 and num % 5 != 0:
        print(num)
    else:
        if num % 3 == 0:
            print('fizz', end='')
        if num % 5 == 0:
            print('bang', end='')
        print('')
