# Calculadora básica en Python

def sumar(a, b):
    """Devuelve la suma de a y b."""
    return a + b


def restar(a, b):
    """Devuelve la resta de a menos b."""
    return a - b


def multiplicar(a, b):
    """Devuelve el producto de a y b."""
    return a * b


def dividir(a, b):
    """Devuelve la división de a entre b."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def main():
    print("Calculadora básica")
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Ingrese el número de la operación: ")

    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Por favor ingrese números válidos")
        return

    try:
        if opcion == '1':
            resultado = sumar(num1, num2)
        elif opcion == '2':
            resultado = restar(num1, num2)
        elif opcion == '3':
            resultado = multiplicar(num1, num2)
        elif opcion == '4':
            resultado = dividir(num1, num2)
        else:
            print("Opción no válida")
            return
        print(f"El resultado es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
