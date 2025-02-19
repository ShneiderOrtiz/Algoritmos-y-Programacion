#Ingresar cantidad en dracmas
dracmas = float(input("Ingrese la cantidad en dracmas griegos: "))

#Se convierten los dracmas a pesetas
pesetas = dracmas * (88.607 / 100)

#Se convierten las pesetas a francos franceses
francos = pesetas / 20.110

#Resultado obtenido
print(f"{dracmas} dracmas equivalen a {francos:.2f} francos franceses.")
