# Una editorial determina el precio de un libro según la cantidad de páginas que 
# contiene. El costo básico del libro es de $5000, más $32 por página con encuadernación rústica. Si el número de páginas supera las 300 la encuadernación 
# debe ser en tela, lo que incrementa el costo en $1200. Además, si el número de 
# páginas sobrepasa las 600 se hace necesario un procedimiento especial de encuadernación que incrementa el costo en otros $3360. Desarrollar un programa 
# que calcule el costo de un libro dado el número de páginas.
libro=int(input('ingresar numero de paginas'))
paginas_encuadernacion=int(input('ingresar paginas especiales'))
costo_libro_basico=5000
encuadernacion=32*paginas_encuadernacion
tela=1200
procedimiento_especial=3360
if libro<=299:
    costo_libro_basico=costo_libro_basico+encuadernacion
    print(costo_libro_basico)
elif libro<=600:
    costo_libro_basico=costo_libro_basico+encuadernacion+tela
    print('el valor del libro sera',costo_libro_basico)

elif  libro>=600:
    costo_libro_basico=costo_libro_basico+encuadernacion+tela+procedimiento_especial
    print('el valo del libro sera',costo_libro_basico)