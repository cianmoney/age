driving = input('have u ever drive a car')
if driving != 'yes' and driving != 'no':
    print('you can only type yes or no')
    raise SystemExit

age = input('your age?')
age = int(age)
if driving == 'yes':
    if age >= 18:
        print('you pass test')
    else:
        print('why?')
elif driving == 'no':
	if age >= 18:
		print('為什麼不考？')
	else:
		print('just wait a moment')
