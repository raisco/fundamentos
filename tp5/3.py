# Una empresa aplica el siguiente procedimiento en la comercialización de sus productos
#  Aplica el precio base a la primera docena de unidades.
#  Aplica un 10% de descuento a todas las unidades entre 13 y 100.
#  Aplica un 25% de descuento a todas las unidades por encima de las 100.
#  Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio 
# base es 100. El cálculo resultante sería:
#  100 * 12 + 90 * 88 + 75 * 130 = 18870
#  y el precio promedio es de 18870/230 = 82.04
#  Escribir un programa que lea la cantidad solicitada de un producto y su precio 
# base, y muestre el valor total de la venta y el precio promedio por unidad. El fin 
# de carga se determina ingresando -1 como cantidad solicitada. Al finalizar informar
#  Cantidad de ventas realizadas total.
#  Cantidad de ventas en las que se aplicó un 10% de descuento.
#  Cantidad de ventas en las que SOLO se aplicó el precio base, es decir 
# que no se le realizaron descuentos
cant_producto=int(input('ingresar la cantidad de producto deseado: '))
total_de_ventas=0
total_con_precio_base=0
total_con_descuento_10=0
while cant_producto!=-1:
    precio_base=int(input('ingresar el precio base: '))
    if cant_producto <= 12:  
        total_venta_ = precio_base * +cant_producto
        total_con_precio_base += cant_producto  
    elif 13 <= cant_producto and cant_producto<= 100:  
        total_venta_ = (precio_base * 12) + (precio_base * 0.9 * (cant_producto - 12))  
        total_con_precio_base +=  12
        total_con_descuento_10 += cant_producto-12  
    else:  
        total_venta_ = (precio_base * 12) + (precio_base * 0.9 * 88) + (precio_base * 0.75 * (cant_producto - 100)) 
        total_con_precio_base +=  12
        total_con_descuento_10 += 88
    print("total venta: ",total_venta_,"promedio x unidad: ", total_venta_/cant_producto)

    cant_producto=int(input('ingresar la cantidad de producto deseado: '))
    total_de_ventas += total_venta_ 

print("Cantidad de ventas realizadas total", total_de_ventas,"Cantidad de ventas en las que se aplicó un 10 de descuento", 
      total_con_descuento_10,"Cantidad de ventas en las que SOLO se aplicó el precio base",total_con_precio_base)

