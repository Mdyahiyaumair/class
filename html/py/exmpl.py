nat = input('enter nationality: ')
age = int(input('enter age: '))
if nat == 'indian':
    if age >= 18 :
        print('eligible to vote')
    else:
        print('not eligible - age less than 18')
else:
    print('not eligible - not an Indian national')