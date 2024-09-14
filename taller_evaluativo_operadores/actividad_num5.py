def nuevo_salario_minimo(salario_actual):
    incremento = 0.042
    nuevo_salario = salario_actual * (1 + incremento)
    return nuevo_salario

salario_actual = float(input("Ingrese el salario mínimo actual: "))
nuevo_salario = nuevo_salario_minimo(salario_actual)
print(f"El nuevo salario mínimo para el próximo año es: {nuevo_salario:.2f}")
