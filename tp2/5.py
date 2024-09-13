# Calcular el descuento y el importe a pagar por un medicamento adquirido en una 
# farmacia. El precio del mismo se ingresa por teclado. La farmacia realiza un descuento del 35% a todos los medicamentos. Se solicita mostrar el precio original, 
# el monto del descuento y el importe final a paga
producto=float(input('ingresar precio del producto: '))
descuento_de_35=producto*0.35
monto_final=producto-descuento_de_35
print('el monto original es: ', producto, 'se le descontara: ',descuento_de_35,'el monto final pagar es de: ',monto_final)
