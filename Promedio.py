def obtener_calificacion(examen_numero):
    while True:
        try:
            calificacion = float(input(f"Introduce la calificación del examen {examen_numero}: "))
            if 0 <= calificacion <= 10:
                return calificacion
            else:
                print("La calificación debe estar entre 0 y 10. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

examen1 = obtener_calificacion(1)
examen2 = obtener_calificacion(2)
examen3 = obtener_calificacion(3)

promedio = (examen1 + examen2 + examen3) / 3

print(f"El promedio de tus tres exámenes parciales es: {promedio:.2f}")

input("Presiona Enter para salir...")