while True:
    print("\n--- Calculadora ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Ingrese una opción (1-5): ")

    if opcion == "5":
        print("¡Hasta luego!")
        break  # Rompe el bucle y termina el programa

    if opcion in ["1", "2", "3", "4"]:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            resultado = numero1 + numero2
            print("Resultado:", resultado)
        elif opcion == "2":
            resultado = numero1 - numero2
            print("Resultado:", resultado)
        elif opcion == "3":
            resultado = numero1 * numero2
            print("Resultado:", resultado)
        elif opcion == "4":
            if numero2 != 0:
                resultado = numero1 / numero2
                print("Resultado:", resultado)
            else:
                print("Error: No se puede dividir por cero")
    else:
        print("Opción no válida. Intente de nuevo.")