import nota
def calcular_nota_final(taller1, taller2, cuestionario1, cuestionario2, proyecto_final):


    peso_taller1 = 0.20
    peso_taller2 = 0.15
    peso_cuestionario1 = 0.22
    peso_cuestionario2 = 0.10
    peso_proyecto_final = 0.33

    nota_final = (taller1 * peso_taller1 +
                  taller2 * peso_taller2 +
                  cuestionario1 * peso_cuestionario1 +
                  cuestionario2 * peso_cuestionario2 +
                  proyecto_final * peso_proyecto_final)

    return round(nota_final, 2)


if nota == "_main_":
 taller1: float = float(input("Ingrese la nota del Taller 1: "))
taller2 = float(input("Ingrese la nota del Taller 2 (1.0 - 5.0): "))
cuestionario1 = float(input("Ingrese la nota del Cuestionario 1: "))
cuestionario2 = float(input("Ingrese la nota del Cuestionario 2: "))
proyecto_final = float(input("Ingrese la nota del Proyecto Final: "))

nota_final = calcular_nota_final(taller1, taller2, cuestionario1, cuestionario2, proyecto_final)

print(f"La nota final calculada es: {nota_final}")
