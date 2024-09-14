def metros_a_millas(metros_a):
   millas_b = metros_a / 1609
   return millas_b

metros_a = float(input("ingrese los metros que desea convertir a millas:"))

millas_b = metros_a_millas(metros_a) / 1609

print(f"{metros_a} metros son {millas_b} millas ")
