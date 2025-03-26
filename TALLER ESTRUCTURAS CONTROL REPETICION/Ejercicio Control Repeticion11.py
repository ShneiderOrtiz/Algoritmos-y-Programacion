saldo = 1000  # Saldo inicial
while True:
    print("\n1. Depositar\n2. Retirar\n3. Consultar saldo\n4. Salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        monto = float(input("Ingrese la cantidad a depositar: "))
        saldo += monto
    elif opcion == 2:
        monto = float(input("Ingrese la cantidad a retirar: "))
        if monto <= saldo:
            saldo -= monto
        else:
            print("Saldo insuficiente.")
    elif opcion == 3:
        print(f"Saldo actual: {saldo}")
    elif opcion == 4:
        print("Saliendo del cajero...")
        break
    else:
        print("Opción inválida.")
