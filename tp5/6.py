#  Leer un número entero y mostrar un mensaje informando cuántos dígitos contie
# ne. Tener en cuenta que el número puede ser negativo. Ejemplo: Si se ingresa 
# 12345 se debe imprimir 5.
num=int(input('ingresar un numero: '))
i=0
while num >0:
    i+=1
    num = num//10
print(i)