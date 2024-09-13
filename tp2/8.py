#  Leer una medida en metros e imprimir esta medida expresada en centímetros, 
# pulgadas, pies y yardas. Los factores de conversión son:
# · 1 pie = 12 pulgadas
# · 1 yarda = 3 pies
# · 1 pulgada = 2,54 cm.
# · 1 metro = 100 cm.
medidas=int(input('ingresar medidas en metros'))
centimetros=medidas*100
pulgadas=medidas*39.37
pies=medidas*3.37
yardas=medidas*1.094
print('la medida en centimentos es',centimetros)
print('la meida en pulgadas es',pulgadas)
print('la medida en pies es',pies)
print('la meida en yardas es',yardas)