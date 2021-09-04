weight=float(input('weight(kg): '))
height=float(input('height(meter): '))
bmi=weight/height**2
if bmi<18.5:
    print('under weight')
elif bmi<25:
    print('normal')
elif bmi<30:
    print('over weight')
elif bmi<35:
    print('obese')
else:
    print('extremly obese')
