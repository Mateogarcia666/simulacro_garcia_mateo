inventario = []

def menu():
    print('''1.Cargar producto/s.
2. Buscar producto.
3. Ordenar inventario.
4. Mostrar producto más caro y más barato.
5. Mostrar productos con precio mayor a 15000.
6. Salir''')
    
def cargar_inventario():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto ")) 
    producto = [nombre, precio, cantidad]
    inventario.append(producto)
    print(inventario)
    return producto

def buscar_producto():
    if len(inventario) == 0:
        print("El almacen se encuentra vacio")
    else:
        nombre_busqueda = input ("Ingrese el nombre del producto que desea buscar: ")
        for producto in inventario:
            if nombre_busqueda == producto:
                nombre_busqueda = producto
            
        if nombre_busqueda == None:
            print("El producto seleccionado no se encuentra")
        else: 
            print(producto)

def ordenar_inventario():
    if not inventario:
        print("No hay productos en el inventario.")
        return
    n = len(inventario)
    for i in range(n):
        for j in range(0, n-i-1):
            if inventario[j][1] > inventario[j+1][1]:
                inventario[j], inventario[j+1] = inventario[j+1], inventario[j]
    print(f"Inventario ordenado por precio de manera ascendente: {inventario}")
    
def producto_mas_caro():
    if len(inventario) == 0:
        print("El almacen esta vacio")
    else:
        producto_caro = float('-inf')
        for producto in range(1):
            if producto_caro < producto[1]:
                producto_caro = producto
        print(f"El producto mas caro es: {producto_caro}")

def producto_mas_barato():
    if len(inventario) == 0:
        print("El almacen esta vacio")
    else:
        producto_barato = float('+inf')
        for producto in inventario:
            if producto_barato > producto[1]:
                producto_caro = producto
        print(f"El producto mas caro es: {producto_caro}")

def producto_superior_15000():
    productos_mayores = [producto[1] > 15000]
    if productos_mayores:
        print("Productos con precio mayor a 15000:")
        for producto in productos_mayores:
            print(f"Nombre: {producto[0]}, Precio: {producto[1]}")
