# Un fletero requiere un programa que calcule el precio de sus viajes a partir de la 
# cantidad de kilómetros que recorre. Para eso cuenta con la siguiente tarifa:
# · Viaje mínimo $2700. Sólo se cobra cuando el importe por kilómetro no 
# alcanza este mínimo.
# · Si recorre entre 0 y 10 km: $400 por km
# · Si recorre 10 km o más: $200 por km
kilometros_recorridos=float(input('ingresar km recorridos: '))
viaje_minimo=2700
if kilometros_recorridos>=1 and kilometros_recorridos<=10:
    print('el precio del viaje es: ',kilometros_recorridos*400)
elif kilometros_recorridos>10:
    print('el valor del viaje es: ',kilometros_recorridos*200)

else:
    print('el viaje minimo es: ',viaje_minimo)