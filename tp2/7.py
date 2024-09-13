# Una persona invierte su capital en un banco y desea saber cuánto dinero ganará 
# en un mes, teniendo en cuenta que el banco paga 2% mensual. ¿Cuánto ganará 
# en seis meses si deja su dinero invertido
capital_inicial = 1000         
tasa_interes = 0.02      
meses = 6               
monto_total = capital_inicial * (1 + tasa_interes) ** meses 
interes_ganado = monto_total - capital_inicial  
print('interes ganado en ', meses, ' meses es de: ',interes_ganado)  