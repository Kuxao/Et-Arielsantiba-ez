peliculas = {
    "P101": ["La Casa de Oro", "drama", 116, "B", "Español", False],
    "P102": ["Noche Neon", "acción", 125, "C", "Inglés", True],
    "P103": ["Planeta Azul", "documental", 90, "A", "Español", False],
    "P104": ["Pista Total", "comedia", 105, "A", "Español", True],
    "P105": ["Código Zero", "thriller", 118, "C", "Inglés", True],
    "P106": ["Viaje Lunar", "ciencia ficción", 140, "B", "Inglés", False]
}

cartelera = {
    "P101": [5990, 40],
    "P102": [7990, 0],
    "P103": [4990, 25],
    "P104": [6990, 12],
    "P105": [8990, 0],
    "P106": [7490, 8]
}


while True:

    print("\n====================================")
    print("          MENÚ PRINCIPAL")
    print("====================================")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("====================================")

    opcion = leer_opcion()

    if opcion == 1:

        genero = input("Ingrese el género: ")

        if validar_texto(genero):

            cupos_genero(
                genero,
                peliculas,
                cartelera
            )

        else:

            print("El género no puede estar vacío.")

    elif opcion == 2:

        while True:

            try:

                p_min = int(input("Ingrese precio mínimo: "))

                p_max = int(input("Ingrese precio máximo: "))

                if p_min >= 0 and p_max >= 0 and p_min <= p_max:

                    break

                else:

                    print(
                        "Debe ingresar valores válidos."
                    )

            except ValueError:

                print(
                    "Debe ingresar valores enteros."
                )


        busqueda_precio(
            p_min,
            p_max,
            peliculas,
            cartelera
        )

    elif opcion == 3:

        codigo = input(
            "Ingrese el código de la película: "
        )


        while not validar_texto(codigo):

            print("El código no puede estar vacío.")

            codigo = input(
                "Ingrese el código de la película: "
            )


        while True:

            try:

                nuevo_precio = int(
                    input("Ingrese el nuevo precio: ")
                )

                if validar_precio(nuevo_precio):

                    break

                else:

                    print(
                        "El precio debe ser mayor que cero."
                    )

            except ValueError:

                print(
                    "Debe ingresar un número entero."
                )


        resultado = actualizar_precio(
            codigo,
            nuevo_precio,
            peliculas,
            cartelera
        )


        if resultado:

            print("Precio actualizado.")

        else:

            print("El código no existe.")

    elif opcion == 4:

        codigo = input(
            "Ingrese el código de la película: "
        )


        while not validar_texto(codigo):

            print("El código no puede estar vacío.")

            codigo = input(
                "Ingrese el código de la película: "
            )


        titulo = input("Ingrese el título: ")


        while not validar_texto(titulo):

            print("El título no puede estar vacío.")

            titulo = input("Ingrese el título: ")


        genero = input("Ingrese el género: ")


        while not validar_texto(genero):

            print("El género no puede estar vacío.")

            genero = input("Ingrese el género: ")


        while True:

            try:

                duracion = int(
                    input("Ingrese la duración en minutos: ")
                )

                if validar_duracion(duracion):

                    break

                else:

                    print(
                        "La duración debe ser mayor que cero."
                    )

            except ValueError:

                print(
                    "Debe ingresar un número entero."
                )


        clasificacion = input(
            "Ingrese la clasificación (A, B o C): "
        )


        while not validar_clasificacion(clasificacion):

            print(
                "La clasificación debe ser A, B o C."
            )

            clasificacion = input(
                "Ingrese la clasificación (A, B o C): "
            )


        idioma = input("Ingrese el idioma: ")


        while not validar_texto(idioma):

            print("El idioma no puede estar vacío.")

            idioma = input("Ingrese el idioma: ")


        es_3d = input("¿Es 3D? (s/n): ")


        while not validar_es_3d(es_3d):

            print("Debe ingresar s o n.")

            es_3d = input("¿Es 3D? (s/n): ")


        if es_3d == "s":

            es_3d = True

        else:

            es_3d = False


        while True:

            try:

                precio = int(
                    input("Ingrese el precio: ")
                )

                if validar_precio(precio):

                    break

                else:

                    print(
                        "El precio debe ser mayor que cero."
                    )

            except ValueError:

                print(
                    "Debe ingresar un número entero."
                )


        while True:

            try:

                cupos = int(
                    input("Ingrese la cantidad de cupos: ")
                )

                if validar_cupos(cupos):

                    break

                else:

                    print(
                        "Los cupos deben ser mayores o iguales a cero."
                    )

            except ValueError:

                print(
                    "Debe ingresar un número entero."
                )


        resultado = agregar_pelicula(
            codigo,
            titulo,
            genero,
            duracion,
            clasificacion,
            idioma,
            es_3d,
            precio,
            cupos,
            peliculas,
            cartelera
        )


        if resultado:

            print("Película agregada.")

        else:

            print("El código ya existe.")

    elif opcion == 5:

        codigo = input(
            "Ingrese el código de la película: "
        )


        while not validar_texto(codigo):

            print("El código no puede estar vacío.")

            codigo = input(
                "Ingrese el código de la película: "
            )


        resultado = eliminar_pelicula(
            codigo,
            peliculas,
            cartelera
        )


        if resultado:

            print("Película eliminada correctamente.")

        else:

            print("El código no existe.")

    elif opcion == 6:
        print("Programa finalizado.")
        break