#Ingresar cantidad en metros
metros = float(input("Ingrese la cantidad en metros: "))

#Se convierten a pulgadas
pulgadas = metros * 39.27

#Se convierten  a pies
pies = pulgadas / 12

#Resultados
print(f"{metros} metros equivalen a {pies:.2f} pies y {pulgadas:.2f} pulgadas.")
