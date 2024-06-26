LIBROS = ['Ficción', 'No Ficción', 'Ciencia','Autos']
libro = []

def registrar_libro():
    titulo = input("Ingrese el título del libro: ").lower()
    autor = input("Ingrese el autor del libro: ").lower()
    genero = input("Ingrese el género del libro: ").lower()
    while libro not in LIBROS:
        print("Este libro no exixte. Prueba otro.")
        genero = input("Ingrese el género del libro: ").lower()
    precio = float(input("Ingrese el precio del libro: "))
    stock = int(input("Ingrese la cantidad en stock del libro: "))
    
    libro.append({
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "precio": precio,
        "stock": stock
    })
    print("Libro registrado exitosamente.")


def listar_libros():
    print("Listas de Libros.")
    for libro in LIBROS:
        print(libro)