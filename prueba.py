libros = {
    'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019, 'AndesPress', False],
    'L002': ['Python en Ruta', 'M. Diaz', 'tecnología', 2023, 'CodeBooks', True],
    'L003': ['Mar y Viento', 'C. Silva', 'poesía', 2017, 'Litoral', False],
    'L004': ['Historia Breve', 'J. Pérez', 'historia', 2015, 'Cronos', False],
    'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficción', 2021, 'Orión', True],
    'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores', False]
}


prestamos = {
    'L001': [500, 4],
    'L002': [700, 0],
    'L003': [300, 10],
    'L004': [400, 2],
    'L005': [600, 1],
    'L006': [350, 6]
}


def leer_opcion():

    while True:

        try:

            opcion = int(input("Ingrese opción: "))

            if 1 <= opcion <= 6:

                return opcion

            else:

                print("Debe seleccionar una opción válida")


        except ValueError:

            print("Debe seleccionar una opción válida")



def copias_genero(genero, libros, prestamos):

    total = 0


    for codigo in libros:

        if libros[codigo][2].lower() == genero.lower():

            total += prestamos[codigo][1]


    print("El total de copias disponibles es:", total)



def busqueda_multa(multa_min, multa_max, libros, prestamos):

    encontrados = []


    for codigo in prestamos:

        multa = prestamos[codigo][0]

        copias = prestamos[codigo][1]


        if multa_min <= multa <= multa_max and copias != 0:

            titulo = libros[codigo][0]

            encontrados.append(titulo + "--" + codigo)


    encontrados.sort()


    if len(encontrados) == 0:

        print("No hay libros en ese rango de multa.")

    else:

        print("Los libros encontrados son:", encontrados)



def buscar_codigo(codigo, prestamos):

    codigo = codigo.upper()


    for cod in prestamos:

        if cod.upper() == codigo:

            return True


    return False



def actualizar_multa(codigo, nueva_multa, prestamos):

    codigo = codigo.upper()


    if buscar_codigo(codigo, prestamos) and nueva_multa > 0:

        prestamos[codigo][0] = nueva_multa

        return True


    return False



def validar_codigo(codigo, prestamos):

    if codigo.strip() == "":

        return False


    if buscar_codigo(codigo, prestamos):

        return False


    return True



def validar_texto(texto):

    return texto.strip() != ""



def validar_anio(anio):

    return anio > 0



def validar_novedad(novedad):

    return novedad.lower() == "s" or novedad.lower() == "n"



def validar_multa(multa):

    return multa > 0



def validar_copias(copias):

    return copias >= 0



def agregar_libro(codigo, titulo, autor, genero, anio, editorial, novedad, multa, copias, libros, prestamos):

    codigo = codigo.upper()


    if buscar_codigo(codigo, prestamos) or codigo in libros:

        return False


    libros[codigo] = [
        titulo,
        autor,
        genero,
        anio,
        editorial,
        novedad
    ]


    prestamos[codigo] = [
        multa,
        copias
    ]


    return True



def eliminar_libro(codigo, libros, prestamos):

    codigo = codigo.upper()


    if buscar_codigo(codigo, prestamos):

        del libros[codigo]

        del prestamos[codigo]

        return True


    return False

while True:

    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Copias por género")
    print("2. Búsqueda de libros por rango de multa")
    print("3. Actualizar multa de libro")
    print("4. Agregar libro")
    print("5. Eliminar libro")
    print("6. Salir")
    print("====================================")


    opcion = leer_opcion()



    if opcion == 1:

        genero = input("Ingrese género a consultar: ")

        copias_genero(
            genero,
            libros,
            prestamos
        )



    elif opcion == 2:

        while True:

            try:

                multa_min = int(input("Ingrese multa mínima: "))

                multa_max = int(input("Ingrese multa máxima: "))


                if multa_min >= 0 and multa_max >= 0 and multa_min <= multa_max:

                    break

                else:

                    print("Debe ingresar un rango válido")


            except ValueError:

                print("Debe ingresar valores enteros")


        busqueda_multa(
            multa_min,
            multa_max,
            libros,
            prestamos
        )



    elif opcion == 3:

        continuar = "s"


        while continuar.lower() == "s":

            codigo = input("Ingrese código del libro: ")


            try:

                nueva_multa = int(input("Ingrese nueva multa: "))


                resultado = actualizar_multa(
                    codigo,
                    nueva_multa,
                    prestamos
                )


                if resultado:

                    print("Multa actualizada")

                else:

                    print("El código no existe")


            except ValueError:

                print("Debe ingresar valores enteros")


            continuar = input("¿Desea actualizar otra multa (s/n)?: ")




    elif opcion == 4:


        codigo = input("Ingrese código: ")

        titulo = input("Ingrese título: ")

        autor = input("Ingrese autor: ")

        genero = input("Ingrese género: ")

        anio = 0

        multa = 0

        copias = 0

        editorial = input("Ingrese editorial: ")

        novedad = input("¿Es novedad? (s/n): ")



        try:

            anio = int(input("Ingrese año de publicación: "))

            multa = int(input("Ingrese precio de multa: "))

            copias = int(input("Ingrese copias disponibles: "))



            if (validar_codigo(codigo, prestamos)
                and validar_texto(titulo)
                and validar_texto(autor)
                and validar_texto(genero)
                and validar_anio(anio)
                and validar_texto(editorial)
                and validar_novedad(novedad)
                and validar_multa(multa)
                and validar_copias(copias)):



                if novedad.lower() == "s":

                    novedad = True

                else:

                    novedad = False



                agregado = agregar_libro(
                    codigo,
                    titulo,
                    autor,
                    genero,
                    anio,
                    editorial,
                    novedad,
                    multa,
                    copias,
                    libros,
                    prestamos
                )



                if agregado:

                    print("Libro agregado")

                else:

                    print("El código ya existe")



            else:

                print("Datos inválidos")



        except ValueError:

            print("Debe ingresar valores numéricos")




    elif opcion == 5:


        codigo = input("Ingrese código del libro: ")


        eliminado = eliminar_libro(
            codigo,
            libros,
            prestamos
        )



        if eliminado:

            print("Libro eliminado")

        else:

            print("El código no existe")




    elif opcion == 6:

        print("Programa finalizado.")

        break

# Sistema ReadCloud finalizado correctamente