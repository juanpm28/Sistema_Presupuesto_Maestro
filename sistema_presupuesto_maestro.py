opciones_activo = { 1 : 'Efectivo', 2 : 'Clientes', 3 : 'Deudores Diversos', 4 : 'Funcionarios y Empleados',
                    5 : 'Inventario de materiales', 6 : 'Inventario de Producto Terminado',
                    7 : 'Terreno', 8 : 'Planta y Equipo', 9 : 'Depreciación Acumulada'}

opciones_pasivo = { 10 : 'Proveedores', 11 : 'Documentos por Pagar', 12 : 'ISR Por Pagar', 
                    13 : 'Préstamos Bancarios'}

opciones_capital = {14 : 'Capital Contribuido', 15 : 'Capital Ganado'}

activos = {}

pasivos = {}

capital = {}

# [{'Producto 1': [2323, 43, 12, 15]}, {'Producto 2': [32, 12, 5, 23]}, {'Producto 3': [12, 32, 43, 32]}, ]
productos = []

# [{Materia A: 4000, Materia B: 2111, Materia C: 2000, Producto 1: 10000, Producto 2: 45454, Producto 3: }]
inventario_inicial_semestre_1 = [{}]
inventario_final_semestre_2 = {}

def registrar_cuentas():
    print("\n| Las cuentas de Activo |\n")
    for k in opciones_activo.items():
        print(k)
    print("\n| Las cuentas de Pasivo |\n")
    for k in opciones_pasivo.items():
        print(k)
    print("\n| Las cuentas de Capital |\n")
    for k in opciones_capital.items():
        print(k)
    try:
        while True:
            str_cuenta = (input("\nElige la opción de la cuenta (o 'salir' para finalizar): \n"))
            if str_cuenta.lower() == 'salir':
                print("Finalizando proceso...\n")
                break
            cuenta = int(str_cuenta)
            print(f"\nCuenta: {opciones_activo[cuenta]}\n")
            
            if cuenta in opciones_activo:
                monto = int(input('Ingresa el monto de la cuenta\n'))
                activos.update({opciones_activo[cuenta]:monto})
            if cuenta in opciones_pasivo:
                monto = int(input('Ingresa el monto de la cuenta\n'))
                pasivos.update({opciones_pasivo[cuenta]:monto})
            if cuenta in opciones_capital:
                monto = int(input('Ingresa el monto de la cuenta\n'))
                capital.update({opciones_capital[cuenta]:monto})
            print("\nRegistro de cuenta exitoso\n")
            break
    except Exception:
        print("Error. La Cuenta no fue encontrada")

def imprimir_balance():
    print("\n| Las cuentas de Activo |\n")
    for k in activos.items():
        print(k)
    print("\n| Las cuentas de Pasivo |\n")
    for k in pasivos.items():
        print(k)
    print("\n| Las cuentas de Capital |\n")
    for k in capital.items():
        print(k)

def imprimir_productos_materiales():
    for k in productos.items():
        print(k)

def requerimiento_materiales():
    while True:
        # {'CL':[matA, matB, matC, mano_obra]}
        producto = {}
        nombre_producto = input("\nIngresa el nombre del producto (o 'salir' para finalizar): \n")
        if nombre_producto.lower() == 'salir':
            return productos
        
        while True:       
            # Material A
            _cantidad_material_A = input(f"\nIngrese la cantidad de material A \n")
            # 1
            try:
                cantidad_material_A = float(_cantidad_material_A)
            except:
                print('Error, se te ponchó una llanta')
                continue
                
            # 2
            if cantidad_material_A < 0:
                print('Error. La cantidad no puede ser menor o igual a 0')
                continue
            
            while True:
                # Material B
                _cantidad_material_B = input(f"\nIngrese la cantidad de material B\n")
                # 1
                try:
                    cantidad_material_B = float(_cantidad_material_B)
                except:
                    print('Error, se te ponchó una llanta')
                    continue
                # 2
                if cantidad_material_B < 0:
                    print('Error. La cantidad no puede ser menor o igual a 0')
                    continue
                    
                break
                
            while True:
                # Material C
                _cantidad_material_C = input(f"\nIngrese la cantidad de material C (o 'salir' para volver a preguntar el producto): \n")
                # 1
                try:
                    cantidad_material_C = float(_cantidad_material_C)
                except:
                    print('Error, se te ponchó una llanta')
                    continue
                # 2
                if cantidad_material_C < 0:
                    print('Error. La cantidad no puede ser menor o igual a 0')
                    continue
                break
                
            while True:
                # Horas de mano de obra
                _mano_obra = input(f"\nIngrese las horas de mano de obra (o 'salir' para volver a preguntar el producto): \n")
                # 1
                try:
                    mano_obra = float(_mano_obra)
                except:
                    print('Error, se te ponchó una llanta')
                    continue
                # 2
                if mano_obra < 0:
                    print('Error. La cantidad no puede ser menor o igual a 0')
                    continue
                
                break
                
                
            # Ingreso de datos a diccionario de producto
            producto[nombre_producto] = [cantidad_material_A, cantidad_material_B, cantidad_material_C, mano_obra]
            
            # Ingreso del producto a productos
            productos.append(producto)
            
            break
    # print("\nProductos y sus materiales:")
            
            
            
            
def redaccion():
  pass
def informacion_inventarios():
    pass
def menu():
    print("\n---Sistema de Presupuesto Maestro---\n")
    print('Elementos de la redacción -------------------------------')
    print("[1] Registrar cuentas")
    print("[2] Imprimir Balance General") # Considerar
    print("[3] Requerimientos de materiales")
    print("[4] Imprimir Productos y materiales")
    print("[5] Información de inventarios")
    print("[6] Productos")
    print("[7] Gastos de administración y ventas")
    print("[8] Gastos de fabricación indirectos")
    print('Elementos de la redacción -------------------------------')
    
    print("[X] Salir")

while True:
    menu()
    opcion = input("Ingresa una opción: ")
    if opcion == "1":
        registrar_cuentas()
        continue
    if opcion == "2":
        imprimir_balance()
        continue
    if opcion == "3":
        lista_productos = requerimiento_materiales()
        for i in lista_productos:
            print(i)

    if opcion == "4":
        imprimir_productos_materiales()
        continue
    if opcion == "5":
        imprimir_productos_materiales()
        continue
    if opcion == "6":
        imprimir_productos_materiales()
        continue
    if opcion == "7":
        imprimir_productos_materiales()
        continue
    if opcion == "8":
        imprimir_productos_materiales()
        continue
    if opcion.lower() == "x":
        print("Saliendo del programa...")
        break


# Programa


# while True
print("\n---Sistema de Presupuesto Maestro---\n")
print('Elementos de la redacción -------------------------------')
print("[1] Registrar cuentas")
print("[2] Imprimir Balance General") 
print("[3] Requerimientos de materiales")
print("[4] Imprimir Productos y materiales")
print("[5] Información de inventarios")
print("[6] Productos")
print("[7] Gastos de administración y ventas")
print("[8] Gastos de fabricación indirectos")


