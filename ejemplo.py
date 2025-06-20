import json
import os

ARCHIVO_TAREAS = 'tareas.json'

def cargar_tareas():
    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, 'r') as archivo:
            return json.load(archivo)
    return []

def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, 'w') as archivo:
        json.dump(tareas, archivo, indent=4)

def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("\nTareas pendientes:")
        for i, tarea in enumerate(tareas, 1):
            estado = "✔" if tarea['completada'] else "✗"
            print(f"{i}. [{estado}] {tarea['descripcion']}")

def agregar_tarea(tareas):
    descripcion = input("Ingresa la descripción de la nueva tarea: ")
    tareas.append({"descripcion": descripcion, "completada": False})
    print("Tarea agregada.")

def completar_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        num = int(input("Número de tarea completada: ")) - 1
        if 0 <= num < len(tareas):
            tareas[num]['completada'] = True
            print("Tarea marcada como completada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada no válida.")

def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        num = int(input("Número de tarea a eliminar: ")) - 1
        if 0 <= num < len(tareas):
            tarea = tareas.pop(num)
            print(f"Tarea '{tarea['descripcion']}' eliminada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada no válida.")

def menu():
    tareas = cargar_tareas()
    while True:
        print("\n--- Lista de Tareas ---")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            mostrar_tareas(tareas)
        elif opcion == '2':
            agregar_tarea(tareas)
            guardar_tareas(tareas)
        elif opcion == '3':
            completar_tarea(tareas)
            guardar_tareas(tareas)
        elif opcion == '4':
            eliminar_tarea(tareas)
            guardar_tareas(tareas)
        elif opcion == '5':
            guardar_tareas(tareas)
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    menu()