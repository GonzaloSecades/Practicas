
def suma(x, y):
    return x + y


def resta(x, y):
    return x - y


def multiplicacion(x, y):
    return x * y


def division(x, y):
    return x / y


print("Seleccionar operacion")
print("1.Suma")
print("2.Resta")
print("3.Multiplicacion")
print("4.Division")

while True:
    
    choice = input("Ingrese una opcion(1/2/3/4): ")

    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))

        if choice == '1':
            print(num1, "+", num2, "=", suma(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", resta(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplicacion(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", division(num1, num2))
        break
    else:
        print("Entrada Invalida")