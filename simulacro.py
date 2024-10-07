from simulacrofunc import *

inventario = []
while True:
    menu()
    opcion = input("Ingrese una opcion: (1,2,3,4,5,6):")

    if opcion == '1':
        cargar_inventario()
    elif opcion == '2':
        buscar_producto()
    elif opcion == '3':
        ordenar_inventario(inventario)
    elif opcion == '4':
        producto_mas_caro()
        producto_mas_barato()
    elif opcion == '5':
        producto_superior_15000()
    elif opcion == '6':
        break
    else: 
        print("Opcion incorrecta seleccione 1,2,3,4,5,6: ")