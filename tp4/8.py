suma_pares = 0
contador_numeros = 0
while suma_pares <= 100:
    numero = int(input("Ingresa un número: "))
    contador_numeros += 1
    if numero % 2 == 0:
        suma_pares += numero
print("Se ingresaron en total", contador_numeros, "números.")
# crear variale solo de numeros para ya que los queremos sumar hasta que lleguen a 100
# y mostrar la cantidad de numeros que se ingresaron para llegar a 100