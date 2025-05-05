from operaciones.aprendiz_a import suma, resta, multiplicacion
from operaciones.aprendiz_b import division, modulo, potencia

def mostrar_menu():
    print("""
    Calculadora Modular:
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Módulo
    6. Potencia
    7. Salir
    """)

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    
    if opcion == '7':
        print("Saliendo...")
        break

    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        print("Resultado:", suma(a, b))
    elif opcion == '2':
        print("Resultado:", resta(a, b))
    elif opcion == '3':
        print("Resultado:", multiplicacion(a, b))
    elif opcion == '4':
        print("Resultado:", division(a, b))
    elif opcion == '5':
        print("Resultado:", modulo(a, b))
    elif opcion == '6':
        print("Resultado:", potencia(a, b))
    else:
        print("Opción no válida.")
