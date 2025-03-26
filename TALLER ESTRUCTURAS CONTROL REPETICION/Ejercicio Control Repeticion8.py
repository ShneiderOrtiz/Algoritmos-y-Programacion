total_consumidores = 0
mujeres_menores = 0
hombres_sin_aguardiente = 0
suma_edades_cerveza = 0
contador_cerveza = 0
consumo_whisky = 0
total_encuestados = 0

while True:
    consume = input("¿Consume licor? (Sí/No): ").strip().lower()
    if consume == "sí":
        total_consumidores += 1
        licor = int(input("Licor preferido (1-6): "))
        edad = int(input("Edad: "))
        sexo = input("Sexo (M/F): ").strip().lower()
        
        if sexo == "f" and edad < 18:
            mujeres_menores += 1
        if sexo == "m" and licor != 1 and 20 <= edad <= 25:
            hombres_sin_aguardiente += 1
        if licor == 3:
            suma_edades_cerveza += edad
            contador_cerveza += 1
        if licor == 5:
            consumo_whisky += 1

    total_encuestados += 1
    continuar = input("¿Desea continuar la encuesta? (Sí/No): ").strip().lower()
    if continuar != "sí":
        break

print(f"Total consumidores: {total_consumidores}")
print(f"Mujeres menores de edad: {mujeres_menores}")
print(f"Hombres sin aguardiente (20-25 años): {hombres_sin_aguardiente}")
print(f"Promedio edad consumidores de cerveza: {suma_edades_cerveza / contador_cerveza if contador_cerveza > 0 else 0}")
print(f"Porcentaje de consumidores de whisky: {consumo_whisky / total_encuestados * 100:.2f}%")
