print('====Calculator====\nPlease input two numbers!\n(input "q" to quit!)')

while True:
    number_1 = input('number 1: ')
    if number_1 == 'q':
        break
    number_2 = input('number 2: ')
    try:
        answer = float(number_2) + float(number_1)
    except ValueError:
        print('Please input numbers!')
    else:
        print(str(answer))
