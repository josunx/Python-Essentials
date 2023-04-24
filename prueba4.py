edad1 = int(input('Ingresa tu edad: '))

if edad1>=18:
    print('Usted es mayor de edad')
    tit1=input('Tiene titulo de bachiller: ').lower()
    if tit1=='si':
        print('Si puede sacar la licencia')
    else:
        print('No tiene titulo de bachiller')
else:
    print('usted es menor de edad')
    if edad1>=16 and edad1<18:
        print('Existe la posibilidad de un permiso de aprendizaje')
    else:
        print('No es posible sacar una licencia')