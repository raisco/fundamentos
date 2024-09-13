#Realizar un programa para ingresar desde el teclado un conjunto de números. Al finalizar mostrar por pantalla el primer y último valor ingresado. Finalizar la lectura con -1
num=int(input('ingrese un numero '))
boton=True
while num!=-1:
     if boton==True:
         primer_numero=num
         boton=False        
     ultimo_num=num
     num=int(input('ingresar un numero o un -1 para terminar '))
print('el primer numero es ', primer_numero, 'el ultimo numero es ', ultimo_num)


