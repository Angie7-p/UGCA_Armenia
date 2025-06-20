import random
import time

def mostrar_bienvenida():
    print("🎲 Bienvenido al juego de Adivina el Número 🎲")
    print("Estoy pensando en un número entre 1 y 100.")
    print("Tú debes adivinarlo en la menor cantidad de intentos posible.")
    print("¡Buena suerte!\n")

def seleccionar_dificultad():
    print("Selecciona la dificultad:")
    print("1 - Fácil (15 intentos)")
    print("2 - Media (10 intentos)")
    print("3 - Difícil (5 intentos)")
    while True:
        opcion = input("Opción (1/2/3): ")
        if opcion == '1':
            return 15
        elif opcion == '2':
            return 10
        elif opcion == '3':
            return 5
        else:
            print("Opción inválida. Intenta de nuevo.")

def jugar():
    mostrar_bienvenida()
    intentos_maximos = seleccionar_dificultad()
    numero_secreto = random.randint(1, 100)
    intentos = 0
    puntos = 100

    while intentos < intentos_maximos:
        try:
            intento = int(input(f"\nIntento #{intentos + 1}: Adivina el número: "))
            if intento < 1 or intento > 100:
                print("Por favor ingresa un número entre 1 y 100.")
                continue
        except ValueError:
            print("Eso no es un número válido.")
            continue

        intentos += 1
        if intento == numero_secreto:
            print(f"\n🎉 ¡Felicidades! Adivinaste el número en {intentos} intentos.")
            print(f"Tu puntuación final es: {puntos}")
            break
        elif intento < numero_secreto:
            print("Demasiado bajo.")
        else:
            print("Demasiado alto.")

        puntos -= int(100 / intentos_maximos)

    else:
        print(f"\n💀 ¡Has perdido! El número era {numero_secreto}.")
        print("Mejor suerte la próxima vez.")

def main():
    while True:
        jugar()
        jugar_de_nuevo = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if jugar_de_nuevo != 's':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        print("\nReiniciando...\n")
        time.sleep(1)

if __name__ == "__main__":
    main()