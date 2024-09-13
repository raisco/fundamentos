#  Una inmobiliaria paga a sus vendedores un salario de $250000, más una comisión de $50000 por cada venta realizada, más el 5% del valor de las ventas. 
# Realizar un programa que imprima el número del vendedor y el salario que le 
# corresponde en un determinado mes. Se leen el número del vendedor, la cantidad de ventas que realizó y el valor total de las mismas. 
vendedor=int(input('ingresar numero del vendedor'))
salario=500000
comision=5000
xventa=0.05
ventas=5
tventas=10000
print('el vendendedor', vendedor,'gano',salario+comision*ventas+tventas*xventa)