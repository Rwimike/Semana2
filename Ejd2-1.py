def validar_calificacion(calificacion, materia):
    """Valida que la calificación esté entre 0 y 100."""
    try:
        cal = float(calificacion)
        if 0 <= cal <= 100:
            return cal
        else:
            raise ValueError(f"La calificación para {materia} debe estar entre 0 y 100.")
    except ValueError as e:
        print(f"Error: {e}")
        return None

def calcular_promedio(calificaciones, materia):
    """Calcula el promedio de una lista de calificaciones."""
    if not calificaciones:
        print(f"No se ingresaron calificaciones válidas para {materia}.")
        return None
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"El promedio de las calificaciones en {materia} es: {promedio:.2f}")
    if promedio >= 60:
        print(f"Estado en {materia}: ¡Aprobado!")
    else:
        print(f"Estado en {materia}: Reprobado.")
    return promedio

def contar_mayores(calificaciones, valor, materia):
    """Cuenta cuántas calificaciones son mayores que un valor dado."""
    if not calificaciones:
        print(f"No hay calificaciones para comparar en {materia}.")
        return
    conteo = 0
    i = 0
    while i < len(calificaciones):
        if calificaciones[i] > valor:
            conteo += 1
        i += 1
    print(f"En {materia}, hay {conteo} calificaciones mayores que {valor}.")

def verificar_calificacion(calificaciones, cal_especifica, materia):
    """Verifica si una calificación está en la lista y cuenta su frecuencia."""
    if not calificaciones:
        print(f"No hay calificaciones para verificar en {materia}.")
        return
    conteo = 0
    encontrada = False
    for cal in calificaciones:
        if cal != cal_especifica:
            continue
        encontrada = True
        conteo += 1
        if conteo > 1:
            break
    if encontrada:
        print(f"En {materia}, la calificación {cal_especifica} aparece {conteo} vez/veces.")
    else:
        print(f"En {materia}, la calificación {cal_especifica} no está en la lista.")

def seleccionar_materia(materias_notas):
    """Permite al usuario seleccionar una materia válida."""
    print("\nMaterias disponibles:", ", ".join(materias_notas.keys()))
    materia = input("Ingrese la materia que desea evaluar: ").capitalize()
    if materia in materias_notas:
        return materia
    else:
        print(f"Error: La materia '{materia}' no está en la lista.")
        return None

def ingresar_notas_materia(materia, num_notas):
    """Solicita un número fijo de notas para la materia."""
    calificaciones = []
    print(f"\nIngrese {num_notas} calificaciones para {materia} (0-100):")
    for i in range(num_notas):
        while True:
            print(f"Calificación {i+1}:")
            cal = validar_calificacion(input(), materia)
            if cal is not None:
                calificaciones.append(cal)
                break
            print("Por favor, ingrese una calificación válida.")
    return calificaciones

def calcular_promedio_general(notas_por_materia):
    """Calcula el promedio general de un estudiante basado en todas las notas."""
    todas_notas = []
    for materia, notas in notas_por_materia.items():
        todas_notas.extend(notas)
    if not todas_notas:
        return None
    promedio_general = sum(todas_notas) / len(todas_notas)
    return promedio_general

def mostrar_promedios_por_materia(notas_por_materia, nombre_estudiante):
    """Muestra los promedios de todas las materias de un estudiante."""
    if not notas_por_materia:
        print(f"\n{nombre_estudiante} no tiene notas registradas.")
        return
    print(f"\nPromedios por materia de {nombre_estudiante}:")
    for materia, notas in notas_por_materia.items():
        promedio = sum(notas) / len(notas) if notas else None
        if promedio is not None:
            print(f"{materia}: {promedio:.2f}")
        else:
            print(f"{materia}: No hay notas registradas.")

def mostrar_promedios_todos_estudiantes(estudiantes, materias_notas):
    """Muestra los promedios por materia y general de todos los estudiantes."""
    if not estudiantes:
        print("\nNo hay estudiantes registrados.")
        return
    print("\n--- Promedios de todos los estudiantes ---")
    for estudiante, datos in estudiantes.items():
        print(f"\nEstudiante: {estudiante}")
        notas_por_materia = datos["notas_por_materia"]
        for materia in materias_notas.keys():
            notas = notas_por_materia.get(materia, [])
            promedio = sum(notas) / len(notas) if notas else None
            if promedio is not None:
                print(f"{materia}: {promedio:.2f}")
            else:
                print(f"{materia}: No registrado")
        promedio_general = datos["promedio_general"]
        if promedio_general is not None:
            print(f"Promedio general: {promedio_general:.2f}")
        else:
            print("Promedio general: No registrado")

def clasificar_promedios(estudiantes):
    """Clasifica los promedios de los estudiantes en categorías."""
    categorias = {
        "Bajo (0-59)": 0,
        "Medio (60-79)": 0,
        "Alto (80-89)": 0,
        "Superior (90-100)": 0
    }
    for estudiante, datos in estudiantes.items():
        promedio = datos["promedio_general"]
        if promedio is None:
            continue
        if 0 <= promedio <= 59:
            categorias["Bajo (0-59)"] += 1
        elif 60 <= promedio <= 79:
            categorias["Medio (60-79)"] += 1
        elif 80 <= promedio <= 89:
            categorias["Alto (80-89)"] += 1
        elif 90 <= promedio <= 100:
            categorias["Superior (90-100)"] += 1
    
    print("\nDistribución de promedios de los estudiantes:")
    for categoria, conteo in categorias.items():
        print(f"{categoria}: {conteo} estudiantes")

def gestionar_estudiante(nombre_estudiante, estudiantes, materias_notas):
    """Submenú para gestionar las acciones de un estudiante."""
    while True:
        print(f"\n--- Gestionando a {nombre_estudiante} ---")
        print("1. Ingresar notas para una materia")
        print("2. Ingresar notas para todas las materias")
        print("3. Ver promedios por materia")
        print("4. Ver promedio general")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            materia = seleccionar_materia(materias_notas)
            if materia is None:
                continue

            num_notas = materias_notas[materia]
            calificaciones = ingresar_notas_materia(materia, num_notas)
            estudiantes[nombre_estudiante]["notas_por_materia"][materia] = calificaciones

            calcular_promedio(calificaciones, materia)

            print(f"Ingrese un valor para contar calificaciones mayores en {materia}:")
            valor = validar_calificacion(input(), materia)
            if valor is not None:
                contar_mayores(calificaciones, valor, materia)

            print(f"Ingrese una calificación específica para buscar en {materia}:")
            cal_especifica = validar_calificacion(input(), materia)
            if cal_especifica is not None:
                verificar_calificacion(calificaciones, cal_especifica, materia)

            promedio_general = calcular_promedio_general(estudiantes[nombre_estudiante]["notas_por_materia"])
            estudiantes[nombre_estudiante]["promedio_general"] = promedio_general

        elif opcion == "2":
            for materia, num_notas in materias_notas.items():
                if materia in estudiantes[nombre_estudiante]["notas_por_materia"]:
                    print(f"\nYa existen notas para {materia}. Saltando...")
                    continue
                print(f"\nProcesando {materia}...")
                calificaciones = ingresar_notas_materia(materia, num_notas)
                estudiantes[nombre_estudiante]["notas_por_materia"][materia] = calificaciones

                calcular_promedio(calificaciones, materia)

                print(f"Ingrese un valor para contar calificaciones mayores en {materia}:")
                valor = validar_calificacion(input(), materia)
                if valor is not None:
                    contar_mayores(calificaciones, valor, materia)

                print(f"Ingrese una calificación específica para buscar en {materia}:")
                cal_especifica = validar_calificacion(input(), materia)
                if cal_especifica is not None:
                    verificar_calificacion(calificaciones, cal_especifica, materia)

            promedio_general = calcular_promedio_general(estudiantes[nombre_estudiante]["notas_por_materia"])
            estudiantes[nombre_estudiante]["promedio_general"] = promedio_general
            if promedio_general is not None:
                print(f"\nPromedio general de {nombre_estudiante}: {promedio_general:.2f}")

        elif opcion == "3":
            mostrar_promedios_por_materia(estudiantes[nombre_estudiante]["notas_por_materia"], nombre_estudiante)

        elif opcion == "4":
            promedio_general = estudiantes[nombre_estudiante]["promedio_general"]
            if promedio_general is None:
                print(f"\n{nombre_estudiante} no tiene notas registradas.")
            else:
                print(f"\nPromedio general de {nombre_estudiante}: {promedio_general:.2f}")

        elif opcion == "5":
            print(f"\nVolviendo al menú principal...")
            break

        else:
            print("\nOpción inválida. Por favor, seleccione 1, 2, 3, 4 o 5.")

def main():
    # Diccionario con materias y número de notas
    materias_notas = {
        "Matematicas": 6,
        "Fisica": 4,
        "Quimica": 5,
        "Historia": 3
    }

    # Almacenar datos de estudiantes
    estudiantes = {}

    while True:
        print("\n--- Gestión de Calificaciones ---")
        print("1. Gestionar estudiante")
        print("2. Ver promedios de todos los estudiantes")
        print("3. Ver distribución de promedios")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            nombre_estudiante = input("\nIngrese el nombre del estudiante: ").strip()
            if not nombre_estudiante:
                print("Error: El nombre no puede estar vacío.")
                continue

            # Inicializar datos del estudiante si no existe
            if nombre_estudiante not in estudiantes:
                estudiantes[nombre_estudiante] = {"notas_por_materia": {}, "promedio_general": None}

            # Entrar al submenú del estudiante
            gestionar_estudiante(nombre_estudiante, estudiantes, materias_notas)

        elif opcion == "2":
            mostrar_promedios_todos_estudiantes(estudiantes, materias_notas)

        elif opcion == "3":
            if not estudiantes:
                print("\nNo hay datos de estudiantes para analizar.")
            else:
                clasificar_promedios(estudiantes)

        elif opcion == "4":
            print("\n¡Programa finalizado!")
            break

        else:
            print("\nOpción inválida. Por favor, seleccione 1, 2, 3 o 4.")

main()