import Funciones as fn

libros = []

ventas = []

while True:
        print("\nMenú:")
        print("1. Registrar libro")
        print("2. Listar todos los libros")
        print("3. Registrar venta")
        print("4. Imprimir reporte de ventas")
        print("5. Generar txt")
        print("6. Salir del Programa")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            fn.registrar_libro()
        elif opcion == 2:
            fn.listar_libros()
        elif opcion == 3:
            fn.registrar_venta()
        elif opcion == 4:
            fn.imprimir_reporte_ventas()
        elif opcion == 5:
            fn.generar_txt()
        elif opcion == 6:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
