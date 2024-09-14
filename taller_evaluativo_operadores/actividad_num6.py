def pesos_a_dolares(pesos, tasa_cambio):
  dolares = pesos / tasa_cambio
  return dolares


if __name__ == "_main_":
 tasa_cambio = 4000

pesos = float(input("Ingrese la cantidad de pesos colombianos a convertir a dólares: "))
dolares = pesos_a_dolares(pesos, tasa_cambio)

print(f"{pesos} pesos colombianos son {dolares:.2f} dólares.")
