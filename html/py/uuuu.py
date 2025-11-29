num = int(input('enter a number: '))
if num % 3 == 0 and num % 5 == 0:
    print('fizzbuzz')
elif num % 5 == 0:
    print('buzzz')
elif num % 3 == 0:
    print('fizz')
else:
    print('buzzzfizzz')