#  Una empresa cuenta con N empleados, divididos en tres categorías (1, 2 y 3). 
# Por cada empleado se lee su legajo, categoría y salario. Se solicita elaborar un 
# informe que contenga:
#  Importe total de salarios pagados por la empresa.
#  Cantidad de empleados que ganan más de $200000.
#  Cantidad de empleados que ganan menos de $50000, cuya categoría sea 3.
#  Legajo del empleado que más gana.
#  Sueldo más bajo.
#  Importe total de sueldos por cada categoría.
#  Salario promedio
total_salarios = 0  
cant_empleados_mas_200k = 0  
cant_empleados_menos_50k_cat3 = 0  
legajo_max_sueldo = 0 
max_sueldo = 0  
min_sueldo = float('inf')  
total_salarios_cat1 = 0  
total_salarios_cat2 = 0  
total_salarios_cat3 = 0  
n = int(input("Ingrese la cantidad de empleados: "))  
contador = 0   
while contador < n:  
    legajo = input("Ingrese el legajo del empleado: ")  
    categoria = int(input("Ingrese la categoría (1, 2 o 3): "))  
    salario = float(input("Ingrese el salario del empleado: "))  
    total_salarios += salario  
    if salario > 200000:  
        cant_empleados_mas_200k += 1   
    if salario < 50000 and categoria == 3:  
        cant_empleados_menos_50k_cat3 += 1   
    if salario > max_sueldo:  
        max_sueldo = salario  
        legajo_max_sueldo = legajo      
    if salario < min_sueldo:  
        min_sueldo = salario  
    if categoria == 1:  
        total_salarios_cat1 += salario  
    elif categoria == 2:  
        total_salarios_cat2 += salario  
    elif categoria == 3:  
        total_salarios_cat3 += salario  
    contador += 1   
if n > 0:  
    salario_promedio = total_salarios / n  
else:  
    salario_promedio = 0  
print("Informe:")  
print("Importe total de salarios pagados: $", total_salarios)  
print("Cantidad de empleados que ganan más de $200000:", cant_empleados_mas_200k)  
print("Cantidad de empleados que ganan menos de $50000 y son de categoría 3:", cant_empleados_menos_50k_cat3)  
print("Legajo del empleado que más gana:", legajo_max_sueldo)  
print("Sueldo más bajo: $", min_sueldo)  
print("Importe total de sueldos por categoría 1: $", total_salarios_cat1)  
print("Importe total de sueldos por categoría 2: $", total_salarios_cat2)  
print("Importe total de sueldos por categoría 3: $", total_salarios_cat3)  
print("Salario promedio: $", salario_promedio)  