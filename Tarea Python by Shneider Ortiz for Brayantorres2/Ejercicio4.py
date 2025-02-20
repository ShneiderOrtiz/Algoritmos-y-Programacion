#Ingresar valor total de la compra
compra1 = float(input("Ingrese el valor de la primera compra: "))
compra2 = float(input("Ingrese el valor de la segunda compra: "))
compra3 = float(input("Ingrese el valor de la tercera compra: "))
compra4 = float(input("Ingrese el valor de la cuarta compra: "))

#Calcular el total de las compras (15% de descuento)
descuento = (compra1 + compra2 + compra3 + compra4) * 0.15
total_a_pagar = (compra1 + compra2 + compra3 + compra4 - descuento)

#Mostrar resultado de la operacion
print(f"El descuento aplicado es: {descuento:.2f}")
print(f"El valor total a pagar luego del descuento es:{total_a_pagar:.2f} COP")
