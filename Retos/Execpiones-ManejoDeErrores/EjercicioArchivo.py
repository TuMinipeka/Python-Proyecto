def division():
    while True:
        try:
            num1 = int(input("Ingrese numero 1: "))
            num2 = int(input("Ingrese numero 2: "))

            resultado = num1/num2

            print("Resultado: ", resultado)
            break
        except ZeroDivisionError:
            print("El divisor no puede ser cero.")
            continue
        except ValueError:
            print("Los Valores Debe Ser Numericos.")
            continue
        finally:
            print("Proceso Terminado")
division()