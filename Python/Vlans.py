# Script 3: Clasificar VLAN
vlan = int(input("Ingrese el número de VLAN: "))

if 1 <= vlan <= 1005:
    print("La VLAN ingresada corresponde al rango normal.")
elif 1006 <= vlan <= 4094:
    print("La VLAN ingresada corresponde al rango extendido.")
else:
    print("Número de VLAN fuera de rango válido (1-4094).")
