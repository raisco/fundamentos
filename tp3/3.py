# Desarrollar un programa que solicite un número de mes (por ejemplo 4) y 
# escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido y 
# mostrar un mensaje de error en caso de que no lo sea.
mes=int(input('ingresar numero del mes'))
if mes==1:
    print('enero')

elif mes==2:
    print('febrero')
elif mes==3:
    print('marzo')
elif mes==4:
    print('abril')
elif mes==5:
    print('mayo')
elif mes==6:
    print('junio')
elif mes==7:
    print('julio')
elif mes==8:
    print('agosto')
elif mes==9:
    print('septiembre')
elif mes==10:
    print('octubre')
elif mes==11:
    print('noviembre')
elif mes==12:
    print('diciembre')
else: print('error')