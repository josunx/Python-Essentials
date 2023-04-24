edad2 = int(input('Ingresa tu edad: '))

if edad2<12:
    print('Usted es un nino')
elif edad2>=12 and edad2<18:
    print('Usted es un joven')
elif edad2>=18 and edad2<30:
    print('Usted es un adulto joven')
else:
    print('Usted es un adulto mayor')