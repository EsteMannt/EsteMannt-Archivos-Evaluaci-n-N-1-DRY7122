# Script: Clasificar número de VLAN

# Solicitar número de VLAN al usuario
vlan = int(input("Ingrese el número de VLAN: "))

# Verificar y mostrar el tipo de rango
if 1 <= vlan <= 1005:
    print(f"La VLAN {vlan} corresponde al rango NORMAL (1–1005).")
elif 1006 <= vlan <= 4094:
    print(f"La VLAN {vlan} corresponde al rango EXTENDIDO (1006–4094).")
else:
    print("El número de VLAN ingresado está fuera del rango válido (1–4094).")
