#  Imprimir una columna de asteriscos, donde su altura se recibe como parámetro
def columa_astericos(A):
    for _ in range (A):
        print('*')
        
A=int(input('Ingresar altura: '))
print(columa_astericos(A))