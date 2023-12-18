#Sign up

import csv

def nickname(nombre_usuario):
    long = len(nombre_usuario)
    y = nombre_usuario.isalnum()

    if y == False:
        print("El nombre de usuario puede contener solo letras y números")

    if long < 6:
        print("El nombre de usuario debe contener al menos 6 caracteres")

    if long > 12:
        print("El nombre de usuario no puede contener más de 12 caracteres")

    if long > 5 and long < 13 and y == True:
        return True

def clave(password):
    validar = False
    long = len(password)
    espacio = False
    mayuscula = False
    minuscula = False
    numeros = False
    y = password.isalnum()
    correcto = True

    for carac in password:
        if carac.isspace() == True:
            espacio = True

        if carac.isupper() == True:
            mayuscula = True

        if carac.islower() == True:
            minuscula = True

        if carac.isdigit() == True:
            numeros = True

    if espacio == True:
        print("La contraseña no puede contener espacios")
    else:
        validar = True

    if long < 8 and validar == True:
        print("Mínimo 8 caracteres")
        validar = False

    if mayuscula == True and minuscula == True and numeros == True and y == False and validar == True:
        validar = True
    else:
        correcto = False

    if validar == True and correcto == False:
        print("La contraseña elegida no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")

    if validar == True and correcto == True:
        return True

def guardar_datos(nombre_usuario, password):
    # Guardar los datos en un archivo CSV con separador ";"
    with open('usuarios.csv', mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([nombre_usuario, password])
    print("Se ha creado exitosamente el archivo 'usuarios.csv' con la información.")

correcto = False
while not correcto:
    nombre = input("Ingrese nombre de usuario: ")
    if nickname(nombre):
        print("Usuario creado exitosamente")
        correcto = True

while correcto:
    contrasenia = input("Ingrese su Password: ")
    if clave(contrasenia):
        print("Contraseña creada exitosamente")
        guardar_datos(nombre, contrasenia)
        correcto = False

def leer_archivo(nombre_archivo):
    '''
    Esta función lee archivos.
    Pre: Recibe el nombre del archivo csv (str)
    Post: retorna una variable en la que se almacena una “matriz” con los datos del archivo csv

    '''
    try:
        with open(nombre_archivo, "rt", encoding='utf-8-sig') as archivo:
            lineas = archivo.readlines()
            return lineas
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Error: Ocurrió un problema al leer el archivo '{nombre_archivo}': {e}")


def mostrar_datos(lineas):
    '''
    Esta función muestra los datos de un archivo
    Pre: Recibe una matriz
    Post: Imprime por pantalla lo que se guardo en la variable. No retorna nada.
    '''
    
    if lineas:
        # Itera sobre las líneas omitiendo el encabezado
        for i, linea in enumerate(lineas[1:], start=1):
            datos = linea.strip().split(";")
            titulo = datos[1]
            sinopsis = datos[2]

            # Imprime el título en una línea y la sinopsis en líneas separadas
            print(f"{i}. {titulo}")
            print(f"   Sinopsis: {sinopsis.strip()}")

            # Línea separadora más larga
            print("=" * 80)
    else:
        print("No hay datos para mostrar.")


def mostrar_cartelera():
    '''
    Esta función muestra los datos almacenados en la variable cartelera
    pre: nombre del archivo (“cartelera.csv”)
    post: Imprime el indice, titulo, fecha y resumen de las películas de la semana.
    '''
    nombre_archivo = "cartelera.csv"
    datos_cartelera = leer_archivo(nombre_archivo)
    mostrar_datos(datos_cartelera)
    
    
def buscar_pelicula(indice_pelicula):
    '''
    Esta función muestra los datos almacenados en la variable película
    Pre: Recibe el índice (int) de la película.
    Post: Imprime por pantalla los datos de la película. (Titulo, Genero, Duracion, Sala, Idioma)
    '''
    try:
        # Leer y mostrar la información de la película seleccionada desde "descripcion.csv"
        nombre_archivo_descripcion = "descripcion.csv"
        datos_descripcion = leer_archivo(nombre_archivo_descripcion)

        if datos_descripcion:
            pelicula_seleccionada = datos_descripcion[indice_pelicula].strip().split(";")
            print("\nInformación de la película seleccionada:")
            print(f"Título: {pelicula_seleccionada[1]}")
            print(f"Género: {pelicula_seleccionada[2]}")
            print(f"Duración: {pelicula_seleccionada[3]} minutos")
            print(f"Sala: {pelicula_seleccionada[4]} ")
            print(f"Idioma: {pelicula_seleccionada[5]}")
        else:
            print("No hay datos para mostrar.")
    except IndexError:
        print("El índice de la película seleccionada no es válido.")
    except Exception as e:
        print(f"Ocurrió un problema al buscar la película: {e}")


def mostrar_horarios(indice_pelicula):
    '''
    Esta funcion muestra por pantalla los horarios de la pelicula seleccionada.
    Pre: Recibe el indice (int) de la pelicula seleecionada.
    Post: Imprime por pantalla que dias se proyecta la película seleccionada ( indice, fecha, hora).
    '''
    try:
        # Leer fechas y horarios desde "horarios.csv"
        nombre_archivo_horarios = "horarios.csv"
        datos_horarios = leer_archivo(nombre_archivo_horarios)

        if datos_horarios:
            print("\nFechas y horarios disponibles para la película:")
            
            opciones_disponibles = []  # Almacenar opciones con el mismo índice
            for i, linea in enumerate(datos_horarios[1:], start=1):  # Saltar la primera línea (encabezados)
                datos = linea.strip().split(";")
                if datos and len(datos) >= 4 and datos[0].isdigit() and datos[0] == str(indice_pelicula):
                    sub_indice_letra = datos[1]
                    fecha_hora = datos[1] + " " + datos[2] 
                    opciones_disponibles.append((sub_indice_letra, fecha_hora))  # Almacenar letra y fecha_hora
            
            # Mostrar las opciones disponibles
            if opciones_disponibles:
                for i, opcion in enumerate(opciones_disponibles, start=1):
                    print(f"{i}. {opcion[1]} ")

                # Solicitar al usuario que elija una opción por número
                sub_indice_numero = int(input("Seleccione una fecha y hora (número): "))

                # Verificar que la opción seleccionada esté en el rango correcto
                if 1 <= sub_indice_numero <= len(opciones_disponibles):
                    opcion_seleccionada = opciones_disponibles[sub_indice_numero - 1]
                    print(f"Ha seleccionado: {opcion_seleccionada[1]}")
                    return opcion_seleccionada[0]
                else:
                    print("Opción no válida.")
            else:
                print(f"No hay fechas y horarios disponibles para la película con índice {indice_pelicula}.")
        else:
            print("No hay datos para mostrar.")
    except Exception as e:
        print(f"Ocurrió un problema al mostrar los horarios: {e}")
        
        
def obtener_sala(indice_pelicula):
    '''
    Esta funcion busca en que sala se proyecta la pelicula seleccionada.
    Pre: Recibe el indice (int) de la pelicula seleccionada
    Post: Retorna el nombre de la sala (str)
    '''
    try:
        # Leer información de las salas desde "descripcion.csv"
        nombre_archivo_descripcion = "descripcion.csv"
        datos_descripcion = leer_archivo(nombre_archivo_descripcion)

        if datos_descripcion:
            for i, linea in enumerate(datos_descripcion[1:], start=1):  # Saltar la primera línea (encabezados)
                datos = linea.strip().split(";")
                if datos and len(datos) >= 6 and datos[0].isdigit() and datos[0] == str(indice_pelicula):
                    return datos[4].strip()
            
            # Si no se encuentra información para el índice de la película
            print(f"No se encontró información de la sala para la película con índice {indice_pelicula}.")
            return None
        else:
            print("No hay datos de salas para mostrar.")
            return None
    except Exception as e:
        print(f"Ocurrió un problema al obtener la sala: {e}")
        return None


def obtener_precio_sala(sala):
    '''
    Esta función según la sala retorna el precio de los boletos.
    Pre: Recibe el nombre de la sala (str)
    Post: Retorna el precio de los boletos (int)
    '''
    if sala.lower() == "2d":
        return 2500
    elif sala.lower() == "3d":
        return 3200
    else:
        print(f"No se reconoce el tipo de sala: {sala}")
        return None


def calcular_precio(cantidad, precio):
    '''
    Esta función calcula el precio a pagar segun la cantidad de boletos seleccionada.
    Pre: Recubre la cantidad de boletos a comprar (int) y recibe el precio de cada boleto (int)
    '''
    return cantidad * precio


def comprar_boleto(indice_pelicula):
    '''
    Esta funcion realiza la funcion de ejecutar la compra, recibe el indice de la pelicula seleccionada para tener los datos necesarios para realizar el resumen de compra cuando el usuario esta por aceptar realizar el pago.
    pre: recibe el indice de la pelicula seleccionada (int)
    post: retorna un mensaje de compra exitosa.
    '''
    try:

        titulo, genero, duracion, sala, idioma = buscar_pelicula(indice_pelicula)

        # Pregunta si desea continuar la compra
        opcion = int(input("¿Desea continuar la compra? (0 para cancelar, 1 para comprar): "))
        if opcion == 0:
            print("Compra cancelada. Volviendo al home.")
            return
        elif opcion == 1:
            # Preguntar cuantos boletos va a comprar
            cantidad_boletos = int(input("Ingrese la cantidad de boletos que desea comprar: "))

            # Obtener el precio del boleto
            precio_boleto = obtener_precio_sala(sala)

            if precio_boleto is not None:
                # Calcular el precio total
                total_pagar = calcular_precio(cantidad_boletos, precio_boleto)

                # Mostrar información de la compra
                print("\nDetalles de la compra:")
                print(f"Título de la película: {titulo}")
                print(f"Género: {genero}")
                print(f"Duración: {duracion} minutos")
                print(f"Sala: {sala}")
                print(f"Idioma: {idioma}")
                print(f"Precio por boleto: {precio_boleto}")
                print(f"Cantidad de boletos: {cantidad_boletos}")
                print(f"Total a pagar: {total_pagar}")

                # Preguntar si quiere pagar o cancelar la compra
                confirmar_pago = int(input("¿Desea pagar la compra? (0 para cancelar, 1 para pagar): "))
                if confirmar_pago == 0:
                    print("Compra cancelada. Volviendo al home.")
                elif confirmar_pago == 1:
                    print("Compra exitosa. Gracias por su compra.")
                    # Aquí puedes agregar la lógica para procesar el pago (si es necesario)
                else:
                    print("Opción no válida. Compra cancelada.")
            else:
                print("No se pudo obtener el precio de la sala. Compra cancelada.")
        else:
            print("Opción no válida. Compra cancelada.")
    except ValueError:
        print("Error: Ingrese un número válido para la opción.")
    except Exception as e:
        print(f"Ocurrió un problema al realizar la compra: {e}")



def futuros_estrenos():
    '''
    Esta funcion muestra las peliculas que próximamente se van a proyectar en el cine.
    Pre: Recibe el nombre del archivo (“Estrenos.csv”)
    Post: Imprime por pantalla el indice, titulo, fecha y resumen de las películas de las peliculas
    '''
    try:
        # Leer y mostrar los datos de futuros estrenos desde "estrenos_futuros.csv"
        nombre_archivo_estrenos = "estrenos_futuros.csv"
        datos_estrenos = leer_archivo(nombre_archivo_estrenos)

        if datos_estrenos:
            print("\nFuturos estrenos:")
            mostrar_datos(datos_estrenos)
        else:
            print("No hay datos de futuros estrenos para mostrar.")
    except Exception as e:
        print(f"Ocurrió un problema al mostrar los futuros estrenos: {e}")
        

def mostrar_precio():
    '''
    Esta funcion muestra los precios de las peliculas por sala.
    Pre: Recibe el nombre del archivo (“Precio.csv”)
    Post: Imprime por pantalla el precio de la sala
    '''
    try:
        nombre_archivo_salas = "salas.csv"
        datos_salas = leer_archivo(nombre_archivo_salas)

        if datos_salas:
            print("\nPrecios de las salas:")
            mostrar_datos(datos_salas)
        else:
            print("No hay datos de precios de salas para mostrar.")
    except Exception as e:
        print(f"Ocurrió un problema al mostrar los precios de salas: {e}")




# Menu de opciones
if __name__ == "__main__":
    while True:
        print("\nBienvenido al sistema de venta de boletos de cine online")
        print("1. Cartelera")
        print("2. Futuros estrenos")
        print("3. Precios")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            mostrar_cartelera()
            # Lógica para seleccionar una película e ingresar el índice
            try:
                indice_seleccionado = int(input("Ingrese el número de la película que desea ver: "))
                buscar_pelicula(indice_seleccionado)
                mostrar_horarios(indice_seleccionado)
                sala = obtener_sala(indice_seleccionado)
                precio = obtener_precio_sala(sala)
                print(f"El precio para la sala {sala} es: {precio} por unidad.")
                comprar_boleto(indice_seleccionado)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == '2':
            futuros_estrenos()
        elif opcion == '3':
            mostrar_precio()
        elif opcion == '4':
            print("Gracias por usar nuestro sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")