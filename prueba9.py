def suma12():
    """
    funicon que no recibe argumentos y
    no devuleve datos solo genera 
    un mensaje

    """
    print('Mensaje generado en una funcion',5/0)
    
    return

def rest(num1,num2,num3):
    """
    Funcion que recibe parametros,
    pero no devuelve datos
    
    """
    resta = num1-num2-num3
    print(f"El resultado de restar num1 num2 y num3 es: {resta}")
    return

def data():
    """
    Funcion que no recibe datos, pero
    si devuelve algo
    
    """
    var1 = {'A':78,56:1982,'Key3':'Valores'}
    
    return var1 

def fun1(var1=5,var2=5):
    """
    Funcion que recibe datos y 
    devuelve datos
    
    """
    if var1<=var2:
        print('Multiplicacion')
        return var1*var2
    else:
        print('Division')
        return var1/var2
    
print('La funcion es: ',fun1())

def fun2(*var10):
    print(var10)
    return

def prom1(*val2):
    return round(sum(val2)+len(val2),1)

