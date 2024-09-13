#  Una empresa factura a sus clientes el último día de cada mes. Si el cliente paga 
# su factura dentro de los primeros 10 días del mes siguiente, tiene un descuento 
# de $200 o del 2% de la factura, lo que resulte más conveniente para el cliente. 
# Si paga en los siguientes 10 días del mes deberá pagar el importe original de la 
# factura, mientras que si paga después del día 20 deberá abonar una multa de 
# $350 o del 10% de su factura, lo que resulte mayor. Escribir un programa que 
# lea el número del cliente y el total de la factura, y emita un informe donde conste el número del cliente y los tres importes que podría abonar
#  según la fecha de  pago
numero_cliente=int(input('ingresar numero del cliente: ''o -1 para finalizar: '))
while numero_cliente!=-1:
    total_de_factura=float(input('ingresar el valor de la factura: '))
    descuento=total_de_factura*0.98
    if total_de_factura-200<descuento:
        descuento_mayor=total_de_factura-200
        print(descuento_mayor)
    else:
        print(descuento)
    print('si pagas antes de los primeros 10 dias del mes tienes 200 de descuento o el 2%: ',total_de_factura-200,'y con el 2%: ',descuento)
    print('si pagas en la fecha de tiempo, tu factura es de: ',total_de_factura)
    print('si pagas atrasado se te multa con 350 o el 10%, el monto mas alto: ',total_de_factura+350,'y el 10%: ', (total_de_factura*0.10)+total_de_factura)
    numero_cliente=int(input('ingresar numero del cliente: ''o -1 para finalizar'))

   

