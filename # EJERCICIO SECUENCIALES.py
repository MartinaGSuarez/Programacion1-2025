# EJERCICIO SECUENCIALES
# CALCULADORA DE PROPINAS EN UN RESTAURANTE

# LE PEDIMOS AL USUARIO QUE INGRESE EL MONTO TOTAL DE LA CUENTA
monto = float(input(f"Ingrese el monto de la cuenta: "))

# CALCULAR LA PROPINA AL 10% Y AL 15%
propina_10 = monto * 0.10
propina_15 = monto * 0.15

# CALCULAR EL TOTAL A PAGAR 
total_10 = monto + propina_10
total_15 = monto + propina_15

# SE IMPRIME POR PANTALLA EL TOTAL A PAGAR
print(f"\nPropina sugerida (10%): {propina_10}")
print(f"Total a pagar (10%): {total_10}")

print(f"\nPropina sugerida (15%): {propina_15}")
print(f"Total a pagar (15%): {total_15}")



