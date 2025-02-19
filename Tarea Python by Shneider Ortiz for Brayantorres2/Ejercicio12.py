#Ingresar cantidad en pesetas
pesetas = float(input("Ingrese la cantidad en pesetas: "))

#Se convierten a dólares
dolares = pesetas / 122.499

#Ahora se convierten a liras italianas
liras = pesetas / (9.289 / 100)

#Resultado final
print(f"{pesetas} pesetas equivalen a {dolares:.2f} dólares y {liras:.2f} liras italianas.")
