#nombre,apellido,edad = 'Jossue','Navarro','22'

nombre = input('ingrese su nombre:')
apellido = input('ingrese su apellido:')
edad = input('ingrese su edad:')

print('Hola me llamo ',nombre,' ',apellido,' y mi edad es ',edad,'a~nos')

str1 = '1- Hola me llamo {} {} y mi edad es {} a~nos'.format(nombre,apellido,edad)

print (str1)