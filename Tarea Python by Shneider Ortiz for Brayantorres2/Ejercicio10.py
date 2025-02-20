#Ingresar cantidades al usuario
chelines = float(input("Ingrese la cantidad en chelines austríacos: "))
dracmas = float(input("Ingrese la cantidad en dracmas griegos: "))
pesetas = float(input("Ingrese la cantidad en pesetas: "))

#Se convierten de chelines austríacos a pesetas
pesetas_chelines = chelines * (956.871 / 100)

#Se convierten de dracmas griegos a pesetas y luego a francos franceses
pesetas_dracmas = dracmas * (88.607 / 100)
francos = pesetas_dracmas / 20.110

#Se convierten de pesetas a dólares y liras italianas
dolares = pesetas / 122.499
liras = pesetas / (9.289 / 100)

#Resultado final
print(f"{chelines} chelines austríacos equivalen a {pesetas_chelines:.2f} pesetas.")
print(f"{dracmas} dracmas griegos equivalen a {francos:.2f} francos franceses.")
print(f"{pesetas} pesetas equivalen a {dolares:.2f} dólares y {liras:.2f} liras italianas.")
