estudiantes = []
while True:
  print("\n---SISTEMA DE ESTUDIANTES---")
  print("1. REGISTRAR ESTUDIANTE") 
  print("2. VER ESTUDIANTES")
  print("3. BUSCAR ESTUDIANTES")
  print("4. SALIR")
        opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))

        # Aquí debes guardar el estudiante

    elif opcion == "2":
        # Aquí debes mostrar los estudiantes

    elif opcion == "3":
        nombre_buscar = input("Ingrese el nombre a buscar: ")

        # Aquí debes buscar el estudiante

    elif opcion == "4":
        print("Programa terminado")
        break

    else:
        print("Opción no válida")
