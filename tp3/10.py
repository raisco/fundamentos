# Diseñar un programa que calcule y muestre el sueldo neto de un empleado en 
# base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa 
# el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es 
# casado se le incrementa el sueldo en 7% del bruto por cada año de antigüedad. 
# También se le realizan los siguientes descuentos: Jubilación: 11%, Obra Social: 
# 3%, Sindicato: 3%
# Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y 
# estado civil (1 si es soltero o 2 si es casado). Se debe informar: (reemplazar los 
# 9 por los valores que correspondan)
# Estado Civil: Soltero/Casado
# Sueldo básico Antigüedad Descuentos Importe
#  $ 999.99 99 años + 999.99
# Jubilación - 999,99
# Obra Social - 999,99
# Sindicato - 999,99
# ------------
# Sueldo Neto 999,99
sueldo=int(input('insertar sueldo: '))
anios=int(input('insertar anios de antiguedad'))
estado_civil=int(input('insetar 1 si estas soltero y si estas casado insertar 2'))
if estado_civil==1:
    porincrimento=0.05
elif estado_civil==2:
    porincrimento=0.07
else:
    print('error')
incre=sueldo*porincrimento*anios
sueldo_plus=sueldo*incre
jubil=sueldo_plus*0.11
sindic=sueldo_plus*0.02
obrasoc=sueldo_plus*0.03
sueldoneto=sueldo_plus-(jubil+sindic+obrasoc)
if estado_civil==2:
    print('casado')
else:
    print('soltero')
#hace los demas print