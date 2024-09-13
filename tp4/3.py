# Realizar un programa para ingresar desde el teclado un conjunto de números y 
# mostrar por pantalla el menor y el mayor de ellos. Finalizar la lectura de datos 
# con un valor -1.
num=int(input('ingrese numero o terminar con un -1 '))
carga=False
while num!=-1:
    if carga==False: 
        num_mayor=num
        num_menor=num
        carga=True
    else:
        if num<num_menor:
            num_menor=num
        if num>num_mayor:
            num_mayor=num

    num=int(input('ingrese un numero o terminar con un -1 '))
print('el numero mayor es ', num_mayor,'y el numero menor es ',num_menor)