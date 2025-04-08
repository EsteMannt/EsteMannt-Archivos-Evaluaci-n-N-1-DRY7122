# Script: Solicitar y mostrar datos del estudiante

# Solicitar información al usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
codigo_seccion = input("Ingrese su código-sección: ")
sede = input("Ingrese su sede: ")

# Mostrar la información ingresada
print("\nInformación ingresada:")
print(f"Nombre completo     : {nombre} {apellido}")
print(f"Código-sección      : {codigo_seccion}")
print(f"Sede                : {sede}")
