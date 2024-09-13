#  Devolver True si el número entero recibido como primer parámetro es múltiplo 
# del segundo, o False en caso contrario. Ejemplo: esmultiplo(40, 8) devuelve True 
# y esmultiplo(50, 3) devuelve False.
def esmultiplo(a,b):
    if a%b==0:
        a=True
    else:
        a%b!=0
        a=False
    return a
a=int(input('ingresar numero: '))
b=int(input('ingresar segundo numero: '))
print(esmultiplo(a,b))