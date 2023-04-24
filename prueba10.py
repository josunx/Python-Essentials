try:
    var1,var2=0,10
    print(var2/var1)
    
except (ZeroDivisionError,TypeError,ModuleNotFoundError):
    print('Ocurre una excepcion de div (except)')

else: 
    print('Esta ejecutandose el bloque (else)') 
finally:
    print('Esta ejecutandose (finally)')
    