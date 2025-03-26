num = int(input("Ingrese un número: "))
suma = sum(i for i in range(1, num) if num % i == 0)
print(f"{num} es un número perfecto" if suma == num else f"{num} no es un número perfecto")
