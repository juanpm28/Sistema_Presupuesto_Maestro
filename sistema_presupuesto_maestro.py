from tabulate import tabulate


def cantidad(prompt):
  _cantidad = input(prompt)
  if not _cantidad:
    return 0
  try:
    cantidad = float(_cantidad)
    return cantidad
  except ValueError:
    print("Error. Ingresa una cantidad válida.")
    return cantidad(prompt)
prod1_material_a_total = 0

# Cuentas del Activo Circulante
efectivo = cantidad("Ingresa el monto de la cuenta de Efectivo: ")
clientes =cantidad("Ingresa el monto de la cuenta de Clientes: ")
deudores_diversos =cantidad("Ingresa el monto de la cuenta de Deudores Diversos: ")
funcionarios_empleados =cantidad("Ingresa el monto de la cuenta de Funcionarios y Empleados: ")
inventario_materiales =cantidad("Ingresa el monto de la cuenta de Inventario de materiales: ")
inventario_producto_terminado =cantidad("Ingresa el monto de la cuenta de Inventario de Producto Terminado: ")

# Total de Activo Circulante
total_activo_circulante = efectivo + clientes + deudores_diversos + funcionarios_empleados + inventario_materiales + inventario_producto_terminado

# Cuentas del Activo No Circulante
terreno = cantidad("Ingresa el monto de la cuenta de Terreno: ")
planta_equipo =  cantidad("Ingresa el monto de la cuenta de Planta y Equipo: ")
depreciacion_acumulada = cantidad("Ingresa el monto de la cuenta de Depreciación Acumulada: ")

# Total de Activo No Circulante
total_activo_no_circulante = terreno + planta_equipo - depreciacion_acumulada

# Total de Activo Total
activo_total = total_activo_circulante + total_activo_no_circulante

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Cuentas del Pasivo a Corto Plazo
proveedores = cantidad("Ingresa el monto de la cuenta de Proveedores: ")
documentos_por_pagar = cantidad("Ingresa el monto de la cuenta de Documentos por Pagar: ")
isr_por_pagar = cantidad("Ingresa el monto de la cuenta de ISR Por Pagar: ")

# Total de Pasivo a Corto Plazo
total_pasivo_corto_plazo = proveedores + documentos_por_pagar + isr_por_pagar

# Cuentas del Pasivo a Largo Plazo
prestamos_bancarios = cantidad("Ingresa el monto de la cuenta de Préstamos Bancarios: ")

# Total de Pasivo a Largo Plazo
total_pasivo_largo_plazo = prestamos_bancarios

# Total del Pasivo
pasivo_total = total_pasivo_corto_plazo + total_pasivo_largo_plazo

# Cuentas del Capital Contable
capital_contribuido =  cantidad("Ingresa el monto de la cuenta de Capital Contribuido: ")
capital_ganado = cantidad("Ingresa el monto de la cuenta de Capital Ganado: ")

# Total del Capital Contable
capital_contable_total = capital_contribuido + capital_ganado

# Suma del Pasivo y Capital
suma_pasivo_capital = pasivo_total + capital_contable_total




# Requerimiento de materiales
print('\nRequerimiento de materiales')
# Solicitar los datos de materia prima A en metros para cada producto
print("Ingrese los datos de Materia Prima A en metros para cada producto:")
prod1_material_a = cantidad("Prod 1: ")
prod2_material_a = cantidad("Prod 2: ")
prod3_material_a = cantidad("Prod 3: ")

# Solicitar los datos de materia prima B en metros para cada producto
print("\nIngrese los datos de Materia Prima B en metros para cada producto:")
prod1_material_b = cantidad("Prod 1: ")
prod2_material_b = cantidad("Prod 2: ")
prod3_material_b = cantidad("Prod 3: ")

# Solicitar los datos de materia prima C en piezas para cada producto
print("\nIngrese los datos de Materia Prima C en piezas para cada producto:")
prod1_material_c = cantidad("Prod 1: ")
prod2_material_c = cantidad("Prod 2: ")
prod3_material_c = cantidad("Prod 3: ")

# Solicitar los datos de horas de mano de obra para cada producto
print("\nIngrese los datos de Horas de Mano de Obra para cada producto:")
prod1_horas_mano_obra = cantidad("Prod 1: ")
prod2_horas_mano_obra = cantidad("Prod 2: ")
prod3_horas_mano_obra = cantidad("Prod 3: ")

mano_obra_directa_1 = cantidad('Ingresa el costo de mano de obra directa el primer semestre: ')
mano_obra_directa_2 = cantidad('Ingresa el costo de mano de obra directa el segundo semestre: ')

# INFORMACIÓN DE INVENTARIOS
print('\nInformación de inventarios')
# Solicitar los datos de inventario inicial del primer semestre
print("Ingrese los datos de Inventario Inicial del Primer Semestre:")
inventario_inicial_a_1 = cantidad("Materia Prima A metros: ")
inventario_inicial_b_1 = cantidad("Materia Prima B metros: ")
inventario_inicial_c_1 = cantidad("Materia Prima C piezas: ")
inventario_inicial_prod1_1 = cantidad("Producto 1: ")
inventario_inicial_prod2_1 = cantidad("Producto 2: ")
inventario_inicial_prod3_1 = cantidad("Producto 3: ")

# Solicitar los datos de inventario final del segundo semestre
print("\nIngrese los datos de Inventario Final del Segundo Semestre:")
inventario_final_a_2 = cantidad("Materia Prima A metros: ")
inventario_final_b_2 = cantidad("Materia Prima B metros: ")
inventario_final_c_2 = cantidad("Materia Prima C piezas: ")
inventario_final_prod1_2 = cantidad("Producto 1: ")
inventario_final_prod2_2 = cantidad("Producto 2: ")
inventario_final_prod3_2 = cantidad("Producto 3: ")

# Solicitar los datos de costo del primer y segundo semestre
print("\nIngrese los datos de Costo del Primer Semestre:")
costo_a_1 =  cantidad("Materia Prima A metros: $")
costo_b_1 =  cantidad("Materia Prima B metros: $")
costo_c_1 = cantidad("Materia Prima C piezas: $")

print("\nIngrese los datos de Costo del Segundo Semestre:")
costo_a_2 = cantidad("Materia Prima A metros: $")
costo_b_2 = cantidad("Materia Prima B metros: $")
costo_c_2 = cantidad("Materia Prima C piezas: $")


# PRODUCTOS
print('\nProductos')
# Solicitar los montos para cada campo numérico
precio_venta_prod1_1 = cantidad("Ingrese el precio de venta para el Prod1 en el Primer Semestre: ")
precio_venta_prod1_2 = cantidad("Ingrese el precio de venta para el Prod1 en el Segundo Semestre: ")

precio_venta_prod2_1 = cantidad("Ingrese el precio de venta para el Prod2 en el Primer Semestre: ")
precio_venta_prod2_2 = cantidad("Ingrese el precio de venta para el Prod2 en el Segundo Semestre: ")

precio_venta_prod3_1 = cantidad("Ingrese el precio de venta para el Prod3 en el Primer Semestre: ")
precio_venta_prod3_2 = cantidad("Ingrese el precio de venta para el Prod3 en el Segundo Semestre: ")

ventas_planeadas_prod1_1 = cantidad("Ingrese las ventas planeadas para el Prod1 en el Primer Semestre: ")
ventas_planeadas_prod1_2 = cantidad("Ingrese las ventas planeadas para el Prod1 en el Segundo Semestre: ")

ventas_planeadas_prod2_1 = cantidad("Ingrese las ventas planeadas para el Prod2 en el Primer Semestre: ")
ventas_planeadas_prod2_2 = cantidad("Ingrese las ventas planeadas para el Prod2 en el Segundo Semestre: ")

ventas_planeadas_prod3_1 = cantidad("Ingrese las ventas planeadas para el Prod3 en el Primer Semestre: ")
ventas_planeadas_prod3_2 = cantidad("Ingrese las ventas planeadas para el Prod3 en el Segundo Semestre: ")


# Solicitar los montos para Gastos de Administración y Ventas
print('\nGastos de Administración y Ventas')
depreciacion_gav = cantidad("Depreciación Anual: ")
sueldos_gav = cantidad("Sueldos y Salarios Anuales: ")
comisiones_gav = cantidad("Comisiones '%' de las ventas proyectadas: ")
varios_gav_1 = cantidad("Varios Primer Semestre: ")
varios_gav_2 = cantidad("Varios Segundo Semestre: ")
intereses_gav = cantidad("Intereses por Préstamo anuales: ")

# Solicitar los montos para Gastos de Fabricación Indirectos
print('\nGastos de Fabricación Indirectos')
depreciacion_gif = cantidad("Depreciación Anual: ")
seguros_gif = cantidad("Seguros Anuales: ")
mantenimiento_gif_1 = cantidad("Mantenimiento Primer Semestre: ")
mantenimiento_gif_2 = cantidad("Mantenimiento Segundo Semestre: ")
energeticos_gif_1 = cantidad("Energéticos Primer Semestre: ")
energeticos_gif_2 = cantidad("Energéticos Segundo Semestre: ")
varios_gif = cantidad("Varios Anuales: ")

############################################################################################################################################################################################
############################################################################################################################################################################################
####################################################################    PRESUPUESTO MAESTRO    #############################################################################################
############################################################################################################################################################################################
############################################################################################################################################################################################

print('1. Presupuesto de Ventas')
unidades_vender_producto1_1 = ventas_planeadas_prod1_1
unidades_vender_producto1_2 = ventas_planeadas_prod1_2
unidades_vender_producto2_1 = ventas_planeadas_prod2_1
unidades_vender_producto2_2 = ventas_planeadas_prod2_2
unidades_vender_producto3_1 = ventas_planeadas_prod3_1
unidades_vender_producto3_2 = ventas_planeadas_prod3_2


precio_venta_producto1_1 = precio_venta_prod1_1
precio_venta_producto1_2 = precio_venta_prod1_2
precio_venta_producto2_1 = precio_venta_prod2_1
precio_venta_producto2_2 = precio_venta_prod2_2
precio_venta_producto3_1 = precio_venta_prod3_1
precio_venta_producto3_2 = precio_venta_prod3_2


importe_venta_producto1_1 = unidades_vender_producto1_1 * precio_venta_producto1_1
importe_venta_producto1_2 = unidades_vender_producto1_2 * precio_venta_producto1_2
importe_venta_producto1_anual = importe_venta_producto1_1 + importe_venta_producto1_2

importe_venta_producto2_1 = unidades_vender_producto2_1 * precio_venta_producto2_1
importe_venta_producto2_2 = unidades_vender_producto2_2 * precio_venta_producto2_2
importe_venta_producto2_anual = importe_venta_producto2_1 + importe_venta_producto2_2

importe_venta_producto3_1 = unidades_vender_producto3_1 * precio_venta_producto3_1
importe_venta_producto3_2 = unidades_vender_producto3_2 * precio_venta_producto3_2
importe_venta_producto3_anual = importe_venta_producto3_1 + importe_venta_producto3_2


total_ventas_semestre1 = importe_venta_producto1_1 + importe_venta_producto2_1 + importe_venta_producto3_1
total_ventas_semestre2 = importe_venta_producto1_2 + importe_venta_producto2_2 + importe_venta_producto3_2
total_ventas_anual = total_ventas_semestre1 + total_ventas_semestre2

# Datos de las ventas por producto y semestre
data = [
    ["PRODUCTO 1", "", "", ""],
    ["Unidades a vender", unidades_vender_producto1_1, unidades_vender_producto1_2, ""],
    ["Precio de Venta", precio_venta_producto1_1, precio_venta_producto1_2, ""],
    ["Importe de Venta", importe_venta_producto1_1, importe_venta_producto1_2, importe_venta_producto1_anual],
    ["PRODUCTO 2", "", "", ""],
    ["Unidades a vender", unidades_vender_producto2_1, unidades_vender_producto2_2, ""],
    ["Precio de Venta", precio_venta_producto2_1, precio_venta_producto2_2, ""],
    ["Importe de Venta", importe_venta_producto2_1, importe_venta_producto2_2, importe_venta_producto2_anual],
    ["PRODUCTO 3", "", "", ""],
    ["Unidades a vender", unidades_vender_producto3_1, unidades_vender_producto3_2, ""],
    ["Precio de Venta", precio_venta_producto3_1, precio_venta_producto3_2, ""],
    ["Importe de Venta", importe_venta_producto3_1, importe_venta_producto3_2, importe_venta_producto3_anual],
    ["Total de Ventas por Semestre", total_ventas_semestre1, total_ventas_semestre2, total_ventas_anual]
]


# Imprimir la tabla
print(tabulate(data, headers=["1er. Semestre", "2do. Semestre", "2016"], tablefmt="rounded_grid"))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("\n2. Determinación del saldo de Clientes y Flujo de Entradas")

saldo_clientes_31_dic_2015 = clientes

ventas_2016 = total_ventas_anual
total_clientes_2016 = ventas_2016 + saldo_clientes_31_dic_2015
por_cobranza_2015 = saldo_clientes_31_dic_2015
por_cobranza_2016 = ventas_2016 * .8   
cobranza_total = por_cobranza_2015 + por_cobranza_2016
saldo_clientes_2016 = total_clientes_2016 - cobranza_total



data = [
    ["Saldo de clientes 31-Dic-2015", "", saldo_clientes_31_dic_2015],
    ["Ventas 2016", "", ventas_2016],
    ["Total de Clientes 2016", "", total_clientes_2016],
    [""],
    ["Entradas de Efectivo:", "", ""],
    ["Por Cobranza del 2015", por_cobranza_2015, ""],
    ["Por Cobranza del 2016", por_cobranza_2016, ""],
    ["", "" , por_cobranza_2015 + por_cobranza_2016],
    ["Saldo de Clientes del 2016", "", total_clientes_2016 - (por_cobranza_2015 + por_cobranza_2016)]
]

# Imprimir tabla
print(tabulate(data, headers=["Descripción", "Importe", "Total"], tablefmt="rounded_grid"))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print('3. Presupuesto de producción')
# Inicializar variables para el producto PRODUCTO 1 ---------------------------------
# Unidades a vender
prod1_unidades_vender_1 = unidades_vender_producto1_1
prod1_unidades_vender_2 = unidades_vender_producto1_2
prod1_unidades_vender_total = prod1_unidades_vender_1 + prod1_unidades_vender_2

# (+) Inventario Final
prod1_inventario_final_1 = inventario_inicial_prod1_1
prod1_inventario_final_2 = inventario_final_prod1_2
prod1_inventario_final_total = prod1_inventario_final_2

# (=) Total de Unidades
prod1_total_unidades_1 = prod1_unidades_vender_1 + prod1_inventario_final_1
prod1_total_unidades_2 = prod1_unidades_vender_2 + prod1_inventario_final_2
prod1_total_unidades_total = prod1_unidades_vender_total + prod1_inventario_final_total

# (-) Inventario Inicial
prod1_inventario_inicial = prod1_inventario_final_1

# (=) Unidades a Producir
prod1_unidades_producir_1 = prod1_unidades_vender_1 + prod1_inventario_final_1 - prod1_inventario_inicial
prod1_unidades_producir_2 = prod1_unidades_vender_2 + prod1_inventario_final_2 - prod1_inventario_inicial
prod1_unidades_producir_total = prod1_unidades_producir_1 + prod1_unidades_producir_2

# Inicializar variables para el producto PRODUCTO 2 ---------------------------------
# Unidades a vender
prod2_unidades_vender_1 = unidades_vender_producto2_1
prod2_unidades_vender_2 = unidades_vender_producto2_2
prod2_unidades_vender_total = prod2_unidades_vender_1 + prod2_unidades_vender_2

# (+) Inventario Final
prod2_inventario_final_1 = inventario_inicial_prod2_1
prod2_inventario_final_2 = inventario_final_prod2_2
prod2_inventario_final_total = prod2_inventario_final_2

# (=) Total de Unidades
prod2_total_unidades_1 = prod2_unidades_vender_1 + prod2_inventario_final_1
prod2_total_unidades_2 = prod2_unidades_vender_2 + prod2_inventario_final_2
prod2_total_unidades_total = prod2_unidades_vender_total + prod2_inventario_final_total


# (-) Inventario Inicial
prod2_inventario_inicial = prod2_inventario_final_1

# (=) Unidades a Producir
prod2_unidades_producir_1 = prod2_unidades_vender_1 + prod2_inventario_final_1 - prod2_inventario_inicial
prod2_unidades_producir_2 = prod2_unidades_vender_2 + prod2_inventario_final_2 - prod2_inventario_inicial
prod2_unidades_producir_total = prod2_unidades_producir_1 + prod2_unidades_producir_2

# Inicializar variables para el producto PRODUCTO 3 ---------------------------------
# Unidades a vender
prod3_unidades_vender_1 = unidades_vender_producto3_1
prod3_unidades_vender_2 = unidades_vender_producto3_2
prod3_unidades_vender_total = prod3_unidades_vender_1 + prod3_unidades_vender_2

# (+) Inventario Final
prod3_inventario_final_1 = inventario_inicial_prod3_1
prod3_inventario_final_2 = inventario_final_prod3_2
prod3_inventario_final_total = prod3_inventario_final_2

# (=) Total de Unidades
prod3_total_unidades_1 = prod3_unidades_vender_1 + prod3_inventario_final_1
prod3_total_unidades_2 = prod3_unidades_vender_2 + prod3_inventario_final_2
prod3_total_unidades_total = prod3_unidades_vender_total + prod3_inventario_final_total

# (-) Inventario Inicial
prod3_inventario_inicial = prod3_inventario_final_1

# (=) Unidades a Producir
prod3_unidades_producir_1 = prod3_unidades_vender_1 + prod3_inventario_final_1 - prod3_inventario_inicial
prod3_unidades_producir_2 = prod3_unidades_vender_2 + prod3_inventario_final_2 - prod3_inventario_inicial
prod3_unidades_producir_total = prod3_unidades_producir_1 + prod3_unidades_producir_2

# Imprimir tabla
print(tabulate([
    ["Producto 1", "", "", ""],
    ["Unidades a vender", prod1_unidades_vender_1, prod1_unidades_vender_2, prod1_unidades_vender_total],
    ["(+) Inventario Final", prod1_inventario_final_1, prod1_inventario_final_2, prod1_inventario_final_total],
    ["(=) Total de Unidades", prod1_total_unidades_1, prod1_total_unidades_2, prod1_total_unidades_total],
    ["(-) Inventario Inicial", prod1_inventario_inicial, prod1_inventario_inicial, prod1_inventario_inicial],
    ["(=) Unidades a Producir", prod1_unidades_producir_1, prod1_unidades_producir_2, prod1_unidades_producir_total],
    
    ["Producto 2", "", "", ""],
    ["Unidades a vender", prod2_unidades_vender_1, prod2_unidades_vender_2, prod2_unidades_vender_total],
    ["(+) Inventario Final", prod2_inventario_final_1, prod2_inventario_final_2, prod2_inventario_final_total],
    ["(=) Total de Unidades", prod2_total_unidades_1, prod2_total_unidades_2, prod2_total_unidades_total],
    ["(-) Inventario Inicial", prod2_inventario_inicial, prod2_inventario_inicial, prod2_inventario_inicial],
    ["(=) Unidades a Producir", prod2_unidades_producir_1, prod2_unidades_producir_2, prod2_unidades_producir_total],
    
    ["Producto 3", "", "", ""],
    ["Unidades a vender", prod3_unidades_vender_1, prod3_unidades_vender_2, prod3_unidades_vender_total],
    ["(+) Inventario Final", prod3_inventario_final_1, prod3_inventario_final_2, prod3_inventario_final_total],
    ["(=) Total de Unidades", prod3_total_unidades_1, prod3_total_unidades_2, prod3_total_unidades_total],
    ["(-) Inventario Inicial", prod3_inventario_inicial, prod3_inventario_inicial, prod3_inventario_inicial],
    ["(=) Unidades a Producir", prod3_unidades_producir_1, prod3_unidades_producir_2, prod3_unidades_producir_total]
    
], headers=["", "1er. Semestre", "2do. Semestre", "Total"], tablefmt="rounded_grid"))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print('4. Presupuesto de Requerimiento de Materiales')
# Variables para el producto prod1
prod1_material_a_1 = prod1_material_a
prod1_material_b_1 = prod1_material_b
prod1_material_c_1 = prod1_material_c

prod1_material_a_2 = prod1_material_a_1
prod1_material_b_2 = prod1_material_b_1
prod1_material_c_2 = prod1_material_c_1

prod1_material_a_total = prod1_material_a_1 + prod1_material_a_2
prod1_material_b_total = prod1_material_b_1 + prod1_material_b_2
prod1_material_c_total = prod1_material_c_1 + prod1_material_c_2

# Variables para el producto prod2
prod2_material_a_1 = prod2_material_a
prod2_material_b_1 = prod2_material_b
prod2_material_c_1 = prod2_material_c

prod2_material_a_2 = prod2_material_a_1
prod2_material_b_2 = prod2_material_b_1
prod2_material_c_2 = prod2_material_c_1

prod2_material_a_total = prod2_material_a_1
prod2_material_b_total = prod2_material_b_1
prod2_material_c_total = prod2_material_c_1

# Variables para el producto prod3
prod3_material_a_1 = prod3_material_a
prod3_material_b_1 = prod3_material_b
prod3_material_c_1 = prod3_material_c

prod3_material_a_2 = prod3_material_a_1
prod3_material_b_2 = prod3_material_b_1
prod3_material_c_2 = prod3_material_c_1

prod3_material_a_total = prod3_material_a_1
prod3_material_b_total = prod3_material_b_1
prod3_material_c_total = prod3_material_c_1

# Total de requerimientos de materiales
total_material_a_1 = prod1_material_a_1 * prod1_unidades_producir_1 + prod2_material_a_1 * prod2_unidades_producir_1 + prod3_material_a_1 * prod3_unidades_producir_1
total_material_b_1 = prod1_material_b_1 * prod1_unidades_producir_1 + prod2_material_b_1 * prod2_unidades_producir_1 + prod3_material_b_1 * prod3_unidades_producir_1
total_material_c_1 = prod1_material_c_1 * prod1_unidades_producir_1 + prod2_material_c_1 * prod2_unidades_producir_1 + prod3_material_c_1 * prod3_unidades_producir_1

total_material_a_2 = prod1_material_a_2 * prod1_unidades_producir_2 + prod2_material_a_2 * prod2_unidades_producir_2 + prod3_material_a_2 * prod3_unidades_producir_2
total_material_b_2 = prod1_material_b_2 * prod1_unidades_producir_2 + prod2_material_b_2 * prod2_unidades_producir_2 + prod3_material_b_2 * prod3_unidades_producir_2
total_material_c_2 = prod1_material_c_2 * prod1_unidades_producir_2 + prod2_material_c_2 * prod2_unidades_producir_2 + prod3_material_c_2 * prod3_unidades_producir_2

total_material_a_total = total_material_a_1 + total_material_a_2
total_material_b_total = total_material_b_1 + total_material_b_2
total_material_c_total = total_material_c_1 + total_material_c_2


# Imprimir tabla
print(tabulate([
    ["PRODUCTO 1", "", "", ""],
    ["Unidades a producir", prod1_unidades_producir_1, prod1_unidades_producir_2, prod1_unidades_producir_1 + prod1_unidades_producir_2],
    ["", "", "", ""],
    ["Material A", "", "", ""],
    ["Requerimiento de material", prod1_material_a_1, prod1_material_a_2, prod1_material_a_total],
    ["Total de Material A requerido", prod1_material_a_1 * prod1_unidades_producir_1, prod1_material_a_2 * prod1_unidades_producir_2, prod1_material_a_1 * prod1_unidades_producir_1 + prod1_material_a_2 * prod1_unidades_producir_2],
    ["Material B", "", "", ""],
    ["Requerimiento de material", prod1_material_b_1, prod1_material_b_2, prod1_material_b_total],
    ["Total de Material B requerido", prod1_material_b_1 * prod1_unidades_producir_1, prod1_material_b_2 * prod1_unidades_producir_2, prod1_material_b_1 * prod1_unidades_producir_1 + prod1_material_b_2 * prod1_unidades_producir_2],
    ["Material C", "", "", ""],
    ["Requerimiento de material", prod1_material_c_1, prod1_material_c_2, prod1_material_c_total],
    ["Total de Material C requerido", prod1_material_c_1 * prod1_unidades_producir_1, prod1_material_c_2 * prod1_unidades_producir_2, prod1_material_c_1 * prod1_unidades_producir_1 + prod1_material_c_2 * prod1_unidades_producir_2],
    ["", "", "", ""],
    ["PRODUCTO 2", "", "", ""],
    ["Unidades a producir", prod2_unidades_producir_1, prod2_unidades_producir_2, prod2_unidades_producir_2],
    ["", "", "", ""],
    ["Material A", "", "", ""],
    ["Requerimiento de material", prod2_material_a_1, prod2_material_a_2, prod2_material_a_total],
    ["Total de Material A requerido", prod2_material_a_1 * prod2_unidades_producir_1, prod2_material_a_2 * prod2_unidades_producir_2, prod2_material_a_1 * prod2_unidades_producir_1 + prod2_material_a_2 * prod2_unidades_producir_2],
    ["Material B", "", "", ""],
    ["Requerimiento de material", prod2_material_b_1, prod2_material_b_2, prod2_material_b_total],
    ["Total de Material B requerido", prod2_material_b_1 * prod2_unidades_producir_1, prod2_material_b_2 * prod2_unidades_producir_2, prod2_material_b_1 * prod2_unidades_producir_1 + prod2_material_b_2 * prod2_unidades_producir_2],
    ["Material C", "", "", ""],
    ["Requerimiento de material", prod2_material_c_1, prod2_material_c_2, prod2_material_c_total],
    ["Total de Material C requerido", prod2_material_c_1 * prod2_unidades_producir_1, prod2_material_c_2 * prod2_unidades_producir_2, prod2_material_c_1 * prod2_unidades_producir_1 + prod2_material_c_2 * prod2_unidades_producir_2],
    ["", "", "", ""],
    ["PRODUCTO 3", "", "", ""],
    ["Unidades a producir", prod3_unidades_producir_1, prod3_unidades_producir_2, prod3_unidades_producir_2],
    ["", "", "", ""],
    ["Material A", "", "", ""],
    ["Requerimiento de material", prod3_material_a_1, prod3_material_a_2, prod3_material_a_total],
    ["Total de Material A requerido", prod3_material_a_1 * prod3_unidades_producir_1, prod3_material_a_2 * prod3_unidades_producir_2, prod3_material_a_1 * prod3_unidades_producir_1 + prod3_material_a_2 * prod3_unidades_producir_2],
    ["Material B", "", "", ""],
    ["Requerimiento de material", prod3_material_b_1, prod3_material_b_2, prod3_material_b_total],
    ["Total de Material B requerido", prod3_material_b_1 * prod3_unidades_producir_1, prod3_material_b_2 * prod3_unidades_producir_2, prod3_material_b_1 * prod3_unidades_producir_1 + prod3_material_b_2 * prod3_unidades_producir_2],
    ["Material C", "", "", ""],
    ["Requerimiento de material", prod3_material_c_1, prod3_material_c_2, prod3_material_c_total],
    ["Total de Material C requerido", prod3_material_c_1 * prod3_unidades_producir_1, prod3_material_c_2 * prod3_unidades_producir_2, prod3_material_c_1 * prod3_unidades_producir_1 + prod3_material_c_2 * prod3_unidades_producir_2],
    ["", "", "", ""],
    ["Total de Requerimientos", "", "", ""],
    ["Material A", total_material_a_1, total_material_a_2, total_material_a_total],
    ["Material B", total_material_b_1, total_material_b_2, total_material_b_total],
    ["Material C", total_material_c_1, total_material_c_2, total_material_c_total]
], headers=["", "1er. Semestre", "2do. Semestre", "Total 2016"], tablefmt="rounded_grid"))



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print('5. Presupuesto de Compra de Materiales')
# Variables para el Material A--------------------------------------
# Requerimiento de materiales
material_a_requerido_1 = total_material_a_1
material_a_requerido_2 = total_material_a_2
material_a_requerido_total = material_a_requerido_1 + material_a_requerido_2

# ( + ) Inventario Final
inventario_final_a_1 = inventario_inicial_a_1
inventario_final_a_2 = inventario_final_a_2
inventario_final_a_total = inventario_final_a_2

# Total de Materiales
total_material_a_1 = material_a_requerido_1 + inventario_final_a_1
total_material_a_2 = material_a_requerido_2 + inventario_final_a_2
total_material_a_total = material_a_requerido_total + inventario_final_a_total

# ( - ) Inventario Inicial
inventario_inicial_a_1 = inventario_final_a_1
inventario_inicial_a_2 = inventario_final_a_1
inventario_inicial_a_total = inventario_final_a_1

# Material a comprar
material_a_comprar_1 = material_a_requerido_1 + inventario_final_a_1 - inventario_inicial_a_1
material_a_comprar_2 = material_a_requerido_2 + inventario_final_a_2 - inventario_inicial_a_2
material_a_comprar_total = material_a_requerido_total + inventario_final_a_total - inventario_inicial_a_total

# Precio de Compra
precio_compra_material_a_1 = costo_a_1
precio_compra_material_a_2 = costo_a_2

# Total de Material A en $:
total_precio_material_a_1 = material_a_comprar_1 * precio_compra_material_a_1
total_precio_material_a_2 = material_a_comprar_2 * precio_compra_material_a_2
total_precio_material_a_total = total_precio_material_a_1 + total_precio_material_a_2

# Variables para el Material B-----------------------------
# Requerimiento de materiales
material_b_requerido_1 = total_material_b_1
material_b_requerido_2 = total_material_b_2
material_b_requerido_total = material_b_requerido_1 + material_b_requerido_2

# ( + ) Inventario Final
inventario_final_b_1 = inventario_inicial_b_1
inventario_final_b_2 = inventario_final_b_2
inventario_final_b_total = inventario_final_b_2

# Total de Materiales
total_material_b_1 = material_b_requerido_1 + inventario_final_b_1
total_material_b_2 = material_b_requerido_2 + inventario_final_b_2
total_material_b_total = material_b_requerido_total + inventario_final_b_total

# ( - ) Inventario Inicial
inventario_inicial_b_1 = inventario_final_b_1
inventario_inicial_b_2 = inventario_final_b_1
inventario_inicial_b_total = inventario_final_b_1

# Material a comprar
material_b_comprar_1 = material_b_requerido_1 + inventario_final_b_1 - inventario_inicial_b_1
material_b_comprar_2 = material_b_requerido_2 + inventario_final_b_2 - inventario_inicial_b_2
material_b_comprar_total = material_b_requerido_total + inventario_final_b_total - inventario_inicial_b_total

# Precio de Compra
precio_compra_material_b_1 = costo_b_1
precio_compra_material_b_2 = costo_b_2

# Total de Material B en $:
total_precio_material_b_1 = material_b_comprar_1 * precio_compra_material_b_1
total_precio_material_b_2 = material_b_comprar_2 * precio_compra_material_b_2
total_precio_material_b_total = total_precio_material_b_1 + total_precio_material_b_2

# Variables para el Material C--------------------------------------
# Requerimiento de materiales
material_c_requerido_1 = total_material_c_1
material_c_requerido_2 = total_material_c_2
material_c_requerido_total = material_c_requerido_2

# ( + ) Inventario Final
inventario_final_c_1 = inventario_inicial_c_1
inventario_final_c_2 = inventario_final_c_2
inventario_final_c_total = inventario_final_c_2

# Total de Materiales
total_material_c_1 = material_c_requerido_1 + inventario_final_c_1
total_material_c_2 = material_c_requerido_2 + inventario_final_c_2
total_material_c_total = material_c_requerido_total + inventario_final_c_total

# ( - ) Inventario Inicial
inventario_inicial_c_1 = inventario_final_c_1
inventario_inicial_c_2 = inventario_final_c_1
inventario_inicial_c_total = inventario_final_c_1

# Material a comprar
material_c_comprar_1 = material_c_requerido_1 + inventario_final_c_1 - inventario_inicial_c_1
material_c_comprar_2 = material_c_requerido_2 + inventario_final_c_2 - inventario_inicial_c_2
material_c_comprar_total = material_c_requerido_total + inventario_final_c_total - inventario_inicial_c_total

# Precio de Compra
precio_compra_material_c_1 = costo_c_1
precio_compra_material_c_2 = costo_c_2

# Total de Material C en $:
total_precio_material_c_1 = material_c_comprar_1 * precio_compra_material_c_1
total_precio_material_c_2 = material_c_comprar_2 * precio_compra_material_c_2
total_precio_material_c_total = total_precio_material_c_1 + total_precio_material_c_2

# Total de compras
total_compras_1 = total_precio_material_a_1 + total_precio_material_b_1 + total_precio_material_c_1
total_compras_2 = total_precio_material_a_2 + total_precio_material_b_2 + total_precio_material_c_2
total_compras_total = total_precio_material_a_total + total_precio_material_b_total + total_precio_material_c_total

# Preparar datos para tabulate
data = [
    ["Material A", "", "", ""],
    ["Requerimiento de materiales", material_a_requerido_1, material_a_requerido_2, material_a_requerido_total],
    ["( + ) Inventario Final", inventario_final_a_1, inventario_final_a_2, inventario_final_a_total],
    ["Total de Materiales", total_material_a_1, total_material_a_2, total_material_a_total],
    ["( - ) Inventario Inicial", inventario_inicial_a_1, inventario_inicial_a_2, inventario_inicial_a_total],
    ["Material a comprar", material_a_comprar_1, material_a_comprar_2, material_a_comprar_total],
    ["Precio de Compra", precio_compra_material_a_1, precio_compra_material_a_2, ""],
    ["Total de Material A en $:", total_precio_material_a_1, total_precio_material_a_2, total_precio_material_a_total],
    ["", "", "", ""],
    ["Material B", "", "", ""],
    ["Requerimiento de materiales", material_b_requerido_1, material_b_requerido_2, material_b_requerido_total],
    ["( + ) Inventario Final", inventario_final_b_1, inventario_final_b_2, inventario_final_b_total],
    ["Total de Materiales", total_material_b_1, total_material_b_2, total_material_b_total],
    ["( - ) Inventario Inicial", inventario_inicial_b_1, inventario_inicial_b_2, inventario_inicial_b_total],
    ["Material a comprar", material_b_comprar_1, material_b_comprar_2, material_b_comprar_total],
    ["Precio de Compra", precio_compra_material_b_1, precio_compra_material_b_2, ""],
    ["Total de Material B en $:", total_precio_material_b_1, total_precio_material_b_2, total_precio_material_b_total],
    ["", "", "", ""],
    ["Material C", "", "", ""],
    ["Requerimiento de materiales", material_c_requerido_1, material_c_requerido_2, material_c_requerido_total],
    ["( + ) Inventario Final", inventario_final_c_1, inventario_final_c_2, inventario_final_c_total],
    ["Total de Materiales", total_material_c_1, total_material_c_2, total_material_c_total],
    ["( - ) Inventario Inicial", inventario_inicial_c_1, inventario_inicial_c_2, inventario_inicial_c_total],
    ["Material a comprar", material_c_comprar_1, material_c_comprar_2, material_c_comprar_total],
    ["Precio de Compra", precio_compra_material_c_1, precio_compra_material_c_2, ""],
    ["Total de Material C en $:", total_precio_material_c_1, total_precio_material_c_2, total_precio_material_c_total],
    ["", "", "", ""],
    ["Compras totales:", total_compras_1, total_compras_2, total_compras_total],
]

# Imprimir la tabla
print(tabulate(data, headers=["", "1er. Semestre", "2do. Semestre", "Total 2016"], tablefmt="rounded_grid"))


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print('6. Determinación del saldo de Proveedores y Flujo de Salidas')
saldo_proveedores_31_dic_2015 = proveedores
compras_2016 = total_compras_total
total_proveedores_2016 = saldo_proveedores_31_dic_2015 + compras_2016
por_proveedores_2015 = saldo_proveedores_31_dic_2015 # en la redaccion de la profe se cobra el 100%
por_proveedores_2016 = compras_2016 * 0.5 # en la redaccion de la profe se cobra el 50%
total_salidas_2016 = por_proveedores_2015 + por_proveedores_2016
saldo_proveedores_2016 = total_proveedores_2016 - total_salidas_2016

data = [
    ["Saldo de Proveedores 31-Dic-2015","" , saldo_proveedores_31_dic_2015],
    ["Compras 2016","" , compras_2016],
    ["Total de Proveedores 2016", "", total_proveedores_2016],
    ["", "", ""],
    ["Salidas de Efectivo:", "", ""],
    ["Por Proveedores del 2015", por_proveedores_2015, ""],
    ["Por Proveedores del 2016", por_proveedores_2016, ""],
    ["Total de Salidas 2016:", "",total_salidas_2016 ],
    ["", "", ""],
    ["Saldo de Proveedores del 2016", "", f"{saldo_proveedores_2016:.2f}"]
]

headers = ["Descripción", "Importe", "Total"]

print(tabulate(data, headers=headers, tablefmt="rounded_grid"))



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


print('7. Presupuesto de Mano de Obra Directa')
# Variables para el PRODUCTO 1----------------------------------------
# Unidades a producir
prod1_unidades_1 = prod1_unidades_producir_1
prod1_unidades_2 = prod1_unidades_producir_2
prod1_unidades_total = prod1_unidades_1 + prod1_unidades_2

# Horas requeridas por unidad
prod1_horas_por_unidad = prod1_horas_mano_obra

# Total de horas requeridas
prod1_horas_total_1 = prod1_unidades_1 * prod1_horas_por_unidad
prod1_horas_total_2 = prod1_unidades_2 * prod1_horas_por_unidad
prod1_horas_total_total = prod1_unidades_total * prod1_horas_por_unidad

# Cuota por hora
prod1_cuota_por_hora_1 = mano_obra_directa_1
prod1_cuota_por_hora_2 = mano_obra_directa_2

# Importe de M.O.D.
prod1_importe_mod_1 = prod1_horas_total_1 * prod1_cuota_por_hora_1
prod1_importe_mod_2 = prod1_horas_total_2 * prod1_cuota_por_hora_2
prod1_importe_mod_total = prod1_importe_mod_1 + prod1_importe_mod_2

# Variables para el PRODUCTO 2--------------------------------------------------
# Unidades a producir
prod2_unidades_1 = prod2_unidades_producir_1
prod2_unidades_2 = prod2_unidades_producir_2
prod2_unidades_total = prod2_unidades_1 + prod2_unidades_2

# Horas requeridas por unidad
prod2_horas_por_unidad = prod2_horas_mano_obra

# Total de horas requeridas
prod2_horas_total_1 = prod2_unidades_1 * prod2_horas_por_unidad
prod2_horas_total_2 = prod2_unidades_2 * prod2_horas_por_unidad
prod2_horas_total_total = prod2_unidades_total * prod2_horas_por_unidad

# Cuota por hora
prod2_cuota_por_hora_1 = mano_obra_directa_1
prod2_cuota_por_hora_2 = mano_obra_directa_2

# Importe de M.O.D.
prod2_importe_mod_1 = prod2_horas_total_1 * prod2_cuota_por_hora_1
prod2_importe_mod_2 = prod2_horas_total_2 * prod2_cuota_por_hora_2
prod2_importe_mod_total = prod2_importe_mod_1 + prod2_importe_mod_2

# Variables para el PRODUCTO 3----------------------------------------
# Unidades a producir
prod3_unidades_1 = prod3_unidades_producir_1
prod3_unidades_2 = prod3_unidades_producir_2
prod3_unidades_total = prod3_unidades_1 + prod3_unidades_2

# Horas requeridas por unidad
prod3_horas_por_unidad = prod3_horas_mano_obra

# Total de horas requeridas
prod3_horas_total_1 = prod3_unidades_1 * prod3_horas_por_unidad
prod3_horas_total_2 = prod3_unidades_2 * prod3_horas_por_unidad
prod3_horas_total_total = prod3_unidades_total * prod3_horas_por_unidad

# Cuota por hora
prod3_cuota_por_hora_1 = mano_obra_directa_1
prod3_cuota_por_hora_2 = mano_obra_directa_2

# Importe de M.O.D.
prod3_importe_mod_1 = prod3_horas_total_1 * prod3_cuota_por_hora_1
prod3_importe_mod_2 = prod3_horas_total_2 * prod3_cuota_por_hora_2
prod3_importe_mod_total = prod3_importe_mod_1 + prod3_importe_mod_2



# Total de horas requeridas por semestre
total_horas_1 = prod1_horas_total_1 + prod2_horas_total_1 + prod3_horas_total_1
total_horas_2 = prod1_horas_total_2 + prod2_horas_total_2 + prod3_horas_total_2
total_horas_total = prod1_horas_total_total + prod2_horas_total_total + prod3_horas_total_total

# Total de MOD por semestre
total_mod_1 = prod1_importe_mod_1 + prod2_importe_mod_1 + prod3_importe_mod_1
total_mod_2 = prod1_importe_mod_2 + prod2_importe_mod_2 + prod3_importe_mod_2
total_mod_total = prod1_importe_mod_total + prod2_importe_mod_total + prod3_importe_mod_total

# Crear tabla de datos para tabulate
data = [
    ["PRODUCTO 1", "", "", ""],
    ["Unidades a producir", prod1_unidades_1, prod1_unidades_2, prod1_unidades_total],
    ["Horas requeridas por unidad", prod1_horas_por_unidad, prod1_horas_por_unidad, prod1_horas_por_unidad],
    ["Total de horas requeridas", prod1_horas_total_1, prod1_horas_total_2, prod1_horas_total_total],
    ["Cuota por hora", prod1_cuota_por_hora_1, prod1_cuota_por_hora_2, ""],
    ["Importe de M.O.D.", prod1_importe_mod_1, prod1_importe_mod_2, prod1_importe_mod_total],
    ["", "", "", ""],
    ["PRODUCTO 2", "", "", ""],
    ["Unidades a producir", prod2_unidades_1, prod2_unidades_2, prod2_unidades_total],
    ["Horas requeridas por unidad", prod2_horas_por_unidad, prod2_horas_por_unidad, prod2_horas_por_unidad],
    ["Total de horas requeridas",  prod2_horas_total_1, prod2_horas_total_2, prod2_horas_total_total],
    ["Cuota por hora", prod2_cuota_por_hora_1, prod2_cuota_por_hora_2, ""],
    ["Importe de M.O.D.", prod2_importe_mod_1, prod2_importe_mod_2, prod2_importe_mod_total],
    ["", "", "", ""],
    ["PRODUCTO 3", "", "", ""],
    ["Unidades a producir", prod3_unidades_1, prod3_unidades_2, prod3_unidades_total],
    ["Horas requeridas por unidad", prod3_horas_por_unidad, prod3_horas_por_unidad, prod3_horas_por_unidad],
    ["Total de horas requeridas", prod3_horas_total_1, prod3_horas_total_2, prod3_horas_total_total],
    ["Cuota por hora", prod3_cuota_por_hora_1, prod3_cuota_por_hora_2, ""],
    ["Importe de M.O.D.", prod3_importe_mod_1, prod3_importe_mod_2, prod3_importe_mod_total],
    ["", "", "", ""],
    ["Total de horas requeridas por semestre", total_horas_1, total_horas_2, total_horas_total],
    ["Total de M.O.D. por semestre", total_mod_1, total_mod_2, total_mod_total]
]

# Imprimir la tabla
print(tabulate(data, headers=["1er. Semestre", "2do. Semestre", "Total 2009"], tablefmt="rounded_grid"))


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("8. Presupuesto de Gastos Indirectos de Fabricación")
# Depreciación
depreciacion_gif_1 = depreciacion_gif/2
depreciacion_gif_2 = depreciacion_gif_1
depreciacion_gif_total = depreciacion_gif_1 + depreciacion_gif_2

# Seguros
seguros_gif_1 = seguros_gif/2
seguros_gif_2 = seguros_gif_1
seguros_gif_total = seguros_gif_1 + seguros_gif_2

# Mantenimiento
mantenimiento_gif_1 = mantenimiento_gif_1
mantenimiento_gif_2 = mantenimiento_gif_2
mantenimiento_gif_total = mantenimiento_gif_1 + mantenimiento_gif_2

# Energéticos
energeticos_gif_1 = energeticos_gif_1
energeticos_gif_2 = energeticos_gif_2
energeticos_gif_total = energeticos_gif_1 + energeticos_gif_2

# Varios
varios_gif_1 = varios_gif/2
varios_gif_2 = varios_gif_1
varios_gif_total = varios_gif_1 + varios_gif_2

# Total G.I.F. por semestre
total_gif_1 = depreciacion_gif_1 + seguros_gif_1 + mantenimiento_gif_1 + energeticos_gif_1 + varios_gif_1
total_gif_2 = depreciacion_gif_2 + seguros_gif_2 + mantenimiento_gif_2 + energeticos_gif_2 + varios_gif_2
total_gif_total = depreciacion_gif_total + seguros_gif_total + mantenimiento_gif_total + energeticos_gif_total + varios_gif_total
costo_hora_gif = total_gif_total/total_horas_total

data = [
    ["Depreciación", depreciacion_gif_1, depreciacion_gif_2, depreciacion_gif_total],
    ["Seguros", seguros_gif_1, seguros_gif_2, seguros_gif_total],
    ["Mantenimiento", mantenimiento_gif_1, mantenimiento_gif_2, mantenimiento_gif_total],
    ["Energéticos", energeticos_gif_1, energeticos_gif_2, energeticos_gif_total],
    ["Varios", varios_gif_1, varios_gif_2, varios_gif_total],
    ["Total G.I.F. por semestre", total_gif_1, total_gif_2, total_gif_total],
    ["Coeficiente para determinar el costo por hora de Gastos Indirectos de Fabricación", "", "", ""],
    ["Total de G.I.F.", "", "", total_gif_total],
    ["(/) Total horas M.O.D. Anual", "", "", total_horas_total],
    ["(=) Costo por Hora de G.I.F.", "", "", f"{costo_hora_gif:.2f}"]
]

headers = ["", "1er. Semestre", "2do. Semestre", "Total 2016"]

print(tabulate(data, headers=headers, tablefmt="rounded_grid"))


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("9. Presupuesto de Gastos de Operación")

# Depreciación
depreciacion_gav_1 = depreciacion_gav/2
depreciacion_gav_2 = depreciacion_gav_1
depreciacion_gav_total = depreciacion_gav_1 + depreciacion_gav_2

# Sueldos y salarios
sueldos_gav_1 = sueldos_gav/2
sueldos_gav_2 = sueldos_gav_1
sueldos_gav_total = sueldos_gav_1 + sueldos_gav_2

# Comisiones
comisiones_gav_1 = comisiones_gav * total_ventas_semestre1
comisiones_gav_2 = comisiones_gav * total_ventas_semestre2
comisiones_gav_total = comisiones_gav_1 + comisiones_gav_2

# Varios
varios_gav_1 = varios_gav_1
varios_gav_2 = varios_gav_2
varios_gav_total = varios_gav_1 + varios_gav_2

# Intereses del Prestamo
intereses_gav_1 = intereses_gav/2
intereses_gav_2 = intereses_gav_1
intereses_gav_total = intereses_gav_1 + intereses_gav_2

# Total de Gastos de Operación
total_gav_1 = depreciacion_gav_1 + sueldos_gav_1 + comisiones_gav_1 + varios_gav_1 + intereses_gav_1
total_gav_2 = depreciacion_gav_2 + sueldos_gav_2 + comisiones_gav_2 + varios_gav_2 + intereses_gav_2
total_gav_total = depreciacion_gav_total + sueldos_gav_total + comisiones_gav_total + varios_gav_total + intereses_gav_total


data = [
    ["Depreciación", depreciacion_gav_1, depreciacion_gav_2, depreciacion_gav_total],
    ["Sueldos y Salarios", sueldos_gav_1, sueldos_gav_2, sueldos_gav_total],
    ["Comisiones", f"{comisiones_gav_1:.2f}", f"{comisiones_gav_2:.2f}", f"{comisiones_gav_total:.2f}"],
    ["Varios", varios_gav_1, varios_gav_2, varios_gav_total],
    ["Intereses del Prestamo", intereses_gav_1, intereses_gav_2, intereses_gav_total],
    ["Total Total de Gastos de Operación", f"{total_gav_1:.2f}", f"{total_gav_2:.2f}", f"{total_gav_total:.2f}"],
]

headers = ["", "1er. Semestre", "2do. Semestre", "Total 2016"]

print(tabulate(data, headers=headers, tablefmt="rounded_grid"))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("10. Determinación del Costo Unitario de Productos Terminados")
# Variables para el Producto 1
prod1_material_a_precio = precio_compra_material_a_2
prod1_material_a_cantidad = prod1_material_a_2
prod1_material_a_costo = prod1_material_a_precio * prod1_material_a_cantidad

prod1_material_b_precio = precio_compra_material_b_2
prod1_material_b_cantidad = prod1_material_b_2
prod1_material_b_costo = prod1_material_b_precio * prod1_material_b_cantidad

prod1_material_c_precio = precio_compra_material_c_2
prod1_material_c_cantidad = prod1_material_c_2
prod1_material_c_costo = prod1_material_c_precio * prod1_material_c_cantidad

prod1_mano_obra_precio = prod1_cuota_por_hora_2
prod1_mano_obra_cantidad = prod1_horas_por_unidad
prod1_mano_obra_costo = prod1_mano_obra_precio * prod1_mano_obra_cantidad

prod1_gif_precio = costo_hora_gif
prod1_gif_cantidad = prod1_mano_obra_cantidad
prod1_gif_costo = prod1_gif_precio * prod1_gif_cantidad

prod1_costo_unitario = prod1_material_a_costo + prod1_material_b_costo + prod1_material_c_costo + prod1_mano_obra_costo + prod1_gif_costo

# Variables para el Producto 2
prod2_material_a_precio = prod1_material_a_precio
prod2_material_a_cantidad = prod2_material_a_2
prod2_material_a_costo = prod2_material_a_precio * prod2_material_a_cantidad

prod2_material_b_precio = prod1_material_b_precio
prod2_material_b_cantidad = prod2_material_b_2
prod2_material_b_costo = prod2_material_b_precio * prod2_material_b_cantidad

prod2_material_c_precio = prod1_material_c_precio
prod2_material_c_cantidad = prod2_material_c_2
prod2_material_c_costo = prod2_material_c_precio * prod2_material_c_cantidad

prod2_mano_obra_precio = prod1_mano_obra_precio
prod2_mano_obra_cantidad = prod2_horas_por_unidad
prod2_mano_obra_costo = prod2_mano_obra_precio * prod2_mano_obra_cantidad

prod2_gif_precio = prod1_gif_precio
prod2_gif_cantidad = prod2_mano_obra_cantidad
prod2_gif_costo = prod2_gif_precio * prod2_gif_cantidad

prod2_costo_unitario = prod2_material_a_costo + prod2_material_b_costo + prod2_material_c_costo + prod2_mano_obra_costo + prod2_gif_costo

# Variables para el Producto 3
prod3_material_a_precio = prod1_material_a_precio
prod3_material_a_cantidad = prod3_material_a_2
prod3_material_a_costo = prod3_material_a_precio * prod3_material_a_cantidad

prod3_material_b_precio = prod1_material_b_precio
prod3_material_b_cantidad = prod3_material_b_2
prod3_material_b_costo = prod3_material_b_precio * prod3_material_b_cantidad

prod3_material_c_precio = prod1_material_c_precio
prod3_material_c_cantidad = prod3_material_c_2
prod3_material_c_costo = prod3_material_c_precio * prod3_material_c_cantidad

prod3_mano_obra_precio = prod1_mano_obra_precio
prod3_mano_obra_cantidad = prod3_horas_por_unidad
prod3_mano_obra_costo = prod3_mano_obra_precio * prod3_mano_obra_cantidad

prod3_gif_precio = prod1_gif_precio
prod3_gif_cantidad = prod3_mano_obra_cantidad
prod3_gif_costo = prod3_gif_precio * prod3_gif_cantidad

prod3_costo_unitario = prod3_material_a_costo + prod3_material_b_costo + prod3_material_c_costo + prod3_mano_obra_costo + prod3_gif_costo

# Creación de la tabla
data = [
    ["", "", "PRODUCTO 1", ""],
    ["Descripción", "Costo", "Cantidad", "Costo Unitario"],
    ["Material A", prod1_material_a_precio, prod1_material_a_cantidad, prod1_material_a_costo],
    ["Material B", prod1_material_b_precio, prod1_material_b_cantidad, prod1_material_b_costo],
    ["Material C", prod1_material_c_precio, prod1_material_c_cantidad, prod1_material_c_costo],
    ["Mano de Obra", prod1_mano_obra_precio, prod1_mano_obra_cantidad, prod1_mano_obra_costo],
    ["Gastos Indirectos de Fabricación", prod1_gif_precio, prod1_gif_cantidad, prod1_gif_costo],
    ["Costo Unitario", "", "", prod1_costo_unitario],
    ["", "", "", ""],
    ["", "", "PRODUCTO 2", ""],
    ["Descripción", "Costo", "Cantidad", "Costo Unitario"],
    ["Material A", prod2_material_a_precio, prod2_material_a_cantidad, prod2_material_a_costo],
    ["Material B", prod2_material_b_precio, prod2_material_b_cantidad, prod2_material_b_costo],
    ["Material C", prod2_material_c_precio, prod2_material_c_cantidad, prod2_material_c_costo],
    ["Mano de Obra", prod2_mano_obra_precio, prod2_mano_obra_cantidad, prod2_mano_obra_costo],
    ["Gastos Indirectos de Fabricación", prod2_gif_precio, prod2_gif_cantidad, prod2_gif_costo],
    ["Costo Unitario", "", "", prod2_costo_unitario],
    ["", "", "", ""],
    ["", "", "PRODUCTO 3", ""],
    ["Descripción", "Costo", "Cantidad", "Costo Unitario"],
    ["Material A", prod3_material_a_precio, prod3_material_a_cantidad, prod3_material_a_costo],
    ["Material B", prod3_material_b_precio, prod3_material_b_cantidad, prod3_material_b_costo],
    ["Material C", prod3_material_c_precio, prod3_material_c_cantidad, prod3_material_c_costo],
    ["Mano de Obra", prod3_mano_obra_precio, prod3_mano_obra_cantidad, prod3_mano_obra_costo],
    ["Gastos Indirectos de Fabricación", prod3_gif_precio, prod3_gif_cantidad, prod3_gif_costo],
    ["Costo Unitario", "", "", prod3_costo_unitario],
    ["", "", "", ""],
]

# Impresión de la tabla
print(tabulate(data, tablefmt="rounded_grid"))


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("11. Valuación de Inventarios Finales")
# Variables declaradas
inventario_material_a_unidades = inventario_final_a_2
inventario_material_b_unidades = inventario_final_b_2
inventario_material_c_unidades = inventario_final_c_2

costo_unitario_material_a = prod3_material_a_precio
costo_unitario_material_b = prod3_material_b_precio
costo_unitario_material_c = prod3_material_c_precio

# Cálculo del costo total de cada material
costo_total_material_a = inventario_material_a_unidades * costo_unitario_material_a
costo_total_material_b = inventario_material_b_unidades * costo_unitario_material_b
costo_total_material_c = inventario_material_c_unidades * costo_unitario_material_c

# Cálculo del inventario final de materiales
inventario_final_materiales = costo_total_material_a + costo_total_material_b + costo_total_material_c

# Variables declaradas
inventario_final_prod1_unidades = prod1_inventario_final_2
inventario_final_prod2_unidades = prod2_inventario_final_2
inventario_final_prod3_unidades = prod3_inventario_final_2

costo_unitario_prod1 = prod1_costo_unitario
costo_unitario_prod2 = prod2_costo_unitario
costo_unitario_prod3 = prod3_costo_unitario

# Cálculo del costo total de cada producto terminado
costo_total_prod1 = inventario_final_prod1_unidades * costo_unitario_prod1
costo_total_prod2 = inventario_final_prod2_unidades * costo_unitario_prod2
costo_total_prod3 = inventario_final_prod3_unidades * costo_unitario_prod3

# Cálculo del inventario final de productos terminados
inventario_final_productos = costo_total_prod1 + costo_total_prod2 + costo_total_prod3

# Definición de los datos de la tabla de inventario final de materiales
tabla_inventario_materiales = [
    ["Material A", inventario_material_a_unidades, f"${costo_unitario_material_a:.2f}", f"${costo_total_material_a:.2f}"],
    ["Material B", inventario_material_b_unidades, f"${costo_unitario_material_b:.2f}", f"${costo_total_material_b:.2f}"],
    ["Material C", inventario_material_c_unidades, f"${costo_unitario_material_c:.2f}", f"${costo_total_material_c:.2f}"],
    ["Inventario Final de Materiales", "", "", f"${inventario_final_materiales:.2f}"]
]

# Definición de los datos de la tabla de inventario final de productos terminados
tabla_inventario_productos = [
    ["Producto 1", inventario_final_prod1_unidades, f"${costo_unitario_prod1:.2f}", f"${costo_total_prod1:.2f}"],
    ["Producto 2", inventario_final_prod2_unidades, f"${costo_unitario_prod2:.2f}", f"${costo_total_prod2:.2f}"],
    ["Producto 3", inventario_final_prod3_unidades, f"${costo_unitario_prod3:.2f}", f"${costo_total_prod3:.2f}"],
    ["Inventario Final de Producto Terminado", "", "", f"${inventario_final_productos:.2f}"]
]

# Imprimir la tabla de inventario final de materiales
print("Inventario Final de Materiales")
print(tabulate(tabla_inventario_materiales, headers=["Descripción", "Unidades", "Costo Unitario", "Costo Total"], tablefmt="rounded_grid"))
print("")
# Imprimir la tabla de inventario final de productos terminados
print("\nInventario Final de Producto Terminado")
print(tabulate(tabla_inventario_productos, headers=["Descripción", "Unidades", "Costo Unitario", "Costo Total"], tablefmt="rounded_grid"))

####################################################################################################################################################################################################
########################################## PRESUPUESTO FINANCIERO ##################################################################################################################################
####################################################################################################################################################################################################

print('II. Presupuesto Financiero.')
print('Estado de Costo de Producción y Ventas')

# Saldo Inicial de Materiales
saldo_inicial_materiales = inventario_materiales

# Compras de Materiales
compras_materiales = total_compras_total

# Material Disponible
material_disponible = saldo_inicial_materiales + compras_materiales

# Inventario Final de Materiales
inventario_final_materiales = inventario_final_materiales

# Materiales Utilizados
materiales_utilizados = material_disponible - inventario_final_materiales

# Mano de Obra Directa
mano_obra_directa = total_mod_total

# Gastos de Fabricación Indirectos
gastos_fabricacion_indirectos = total_gif_total

# Costo de Producción
costo_produccion = materiales_utilizados + mano_obra_directa + gastos_fabricacion_indirectos

# Inventario Inicial de Productos Terminados
inventario_inicial_productos_terminados = inventario_producto_terminado

# Total de Producción Disponible
total_produccion_disponible = costo_produccion + inventario_inicial_productos_terminados

# Inventario Final de Productos Terminados
inventario_final_productos_terminados = inventario_final_productos

# Costo de Ventas
costo_ventas = total_produccion_disponible - inventario_final_productos_terminados

tabla = [
    ["Saldo Inicial de Materiales", "", "", f"${saldo_inicial_materiales:,}"],
    ["(+) Compras de Materiales", "", "", f"${compras_materiales:,}"],
    ["(=) Material Disponible", "", "", f"${material_disponible:,}"],
    ["(-) Inventario Final de Materiales", "", "", f"${inventario_final_materiales:,}"],
    ["(=) Materiales Utilizados", "", "", f"${materiales_utilizados:,}"],
    ["(+) Mano de Obra Directa", "", "", f"${mano_obra_directa:,}"],
    ["(+) Gastos de Fabricación Indirectos", "", "", f"${gastos_fabricacion_indirectos:,}"],
    ["(=) Costo de Producción", "", "", f"${costo_produccion:,}"],
    ["(+) Inventario Inicial de Productos Terminados", "", "", f"${inventario_inicial_productos_terminados:,}"],
    ["(=) Total de Producción Disponible", "", "", f"${total_produccion_disponible:,}"],
    ["(-) Inventario Final de Productos Terminados", "", "", f"${inventario_final_productos_terminados:,}"],
    ["(=) Costo de Ventas", "", "", f"${costo_ventas:,}"],
]

# Imprimir la tabla
print(tabulate(tabla, tablefmt="rounded_grid"))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print('Estado de Resultados')
ventas = total_ventas_anual
costo_ventas = costo_ventas
utilidad_bruta = ventas - costo_ventas
gastos_operacion = total_gav_total
utilidad_operacion = utilidad_bruta - gastos_operacion
isr = utilidad_operacion * 0.3
ptu = utilidad_operacion * 0.1
utilidad_neta = utilidad_operacion - isr - ptu

tabla = [
    ["Ventas", "", "", f"${ventas:,}"],
    ["(-) Costo de Ventas", "", "", f"${costo_ventas:,}"],
    ["(=) Utilidad Bruta", "", "", f"${utilidad_bruta:,}"],
    ["(-) Gastos de Operación", "", "", f"${gastos_operacion:,}"],
    ["(=) Utilidad de Operación", "", "", f"${utilidad_operacion:,}"],
    ["(-) ISR", "", "", f"${isr:,}"],
    ["(-) PTU", "", "", f"${ptu:,}"],
    ["(=) Utilidad Neta", "", "", f"${utilidad_neta:,}"],
]

# Imprimir la tabla
print(tabulate(tabla, tablefmt="rounded_grid"))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print('Estado flujo de efectivo')
# Definir las variables con los valores proporcionados
saldo_inicial_efectivo = efectivo
cobranza_2016 = por_cobranza_2016
cobranza_2015 = por_cobranza_2015
total_entradas = cobranza_2016 + cobranza_2015
efectivo_disponible = saldo_inicial_efectivo + total_entradas

proveedores_2016 = por_proveedores_2016
proveedores_2015 = por_proveedores_2015
pago_mano_obra_directa = total_mod_total
pago_gastos_indirectos_fabricacion = total_gif_total - depreciacion_gif_total
pago_gastos_operacion = total_gav_total - depreciacion_gav_total
compra_activo_fijo_maquinaria = 85000 # **
pago_isr_2015 = isr_por_pagar
pago_isr_2016 = isr

# Calcular los totales
total_salidas = (
    proveedores_2016 + proveedores_2015 + pago_mano_obra_directa +
    pago_gastos_indirectos_fabricacion + pago_gastos_operacion +
    compra_activo_fijo_maquinaria + pago_isr_2015 + pago_isr_2016
)

flujo_efectivo_actual = efectivo_disponible - total_salidas

# Crear la tabla con las variables
tabla = [
    ["Saldo Inicial de Efectivo", "", "", f"${saldo_inicial_efectivo:,}"],
    ["Entradas:", "", f"${cobranza_2016:,}", ""],
    ["", "", f"${cobranza_2015:,}", ""],
    ["Total de Entradas", "", "", f"${total_entradas:,}"],
    ["Efectivo Disponible", "", "", f"${efectivo_disponible:,}"],
    ["Salidas:", "", "", ""],
    ["Proveedores 2016", "", f"${proveedores_2016:,}", ""],
    ["Proveedores 2015", "", f"${proveedores_2015:,}", ""],
    ["Pago Mano de Obra Directa", "", f"${pago_mano_obra_directa:,}", ""],
    ["Pago Gastos Indirectos de Fabricación", "", f"${pago_gastos_indirectos_fabricacion:,}", ""],
    ["Pago de Gastos de Operación", "", f"${pago_gastos_operacion:,}", ""],
    ["Compra de Activo Fijo (Maquinaria)", "", f"${compra_activo_fijo_maquinaria:,}", ""],
    ["Pago ISR 2015", "", f"${pago_isr_2015:,}", ""],
    ["Pago ISR 2016", "", f"${pago_isr_2016:,}", ""],
    ["Total de Salidas", "", "", f"${total_salidas:,}"],
    ["Flujo de Efectivo Actual", "", "", f"${flujo_efectivo_actual:,}"],
]

# Imprimir la tabla
print(tabulate(tabla, tablefmt="rounded_grid"))


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Balance General")
# Definir las variables con los valores proporcionados
efectivo = flujo_efectivo_actual
clientes = total_clientes_2016 - (por_cobranza_2015 + por_cobranza_2016)
deudores_diversos = deudores_diversos
funcionarios_empleados = funcionarios_empleados
inventario_materiales = inventario_final_materiales
inventario_producto_terminado = inventario_final_productos
terreno = terreno
planta_equipo = planta_equipo + compra_activo_fijo_maquinaria
depreciacion_acumulada = depreciacion_acumulada + depreciacion_gif_total + depreciacion_gav_total
proveedores = saldo_proveedores_2016
documentos_por_pagar = documentos_por_pagar
ptu_por_pagar = ptu
prestamos_bancarios = prestamos_bancarios
capital_aportado = capital_contribuido
capital_ganado = capital_ganado
utilidad_ejercicio = utilidad_neta

# Calcular totales
total_activos_circulantes = efectivo + clientes + deudores_diversos + funcionarios_empleados + inventario_materiales + inventario_producto_terminado
total_activos_no_circulantes = terreno + planta_equipo - depreciacion_acumulada
total_activos = total_activos_circulantes + total_activos_no_circulantes

total_pasivo_corto_plazo = proveedores + documentos_por_pagar + ptu_por_pagar
total_pasivo_largo_plazo = prestamos_bancarios
total_pasivo = total_pasivo_corto_plazo + total_pasivo_largo_plazo

total_capital_contable = capital_aportado + capital_ganado + utilidad_ejercicio

suma_pasivo_capital = total_pasivo + total_capital_contable

# Crear la tabla con las variables
tabla = [
    ["ACTIVO", "", "", ""],
    ["Circulante", "", "", ""],
    ["Efectivo", "", f"${efectivo:,}", ""],
    ["Clientes", "", f"${clientes:,}", ""],
    ["Deudores Diversos", "", f"${deudores_diversos:,}", ""],
    ["Funcionarios y Empleados", "", f"{funcionarios_empleados:,}", ""],
    ["Inventario de Materiales", "", f"${inventario_materiales:,}", ""],
    ["Inventario de Producto Terminado", "", f"${inventario_producto_terminado:,}", ""],
    ["Total de Activos Circulantes:", "", "", f"${total_activos_circulantes:,}"],
    ["", "", "", ""],
    ["No Circulante", "", "", ""],
    ["Terreno", "", f"${terreno:,}", ""],
    ["Planta y Equipo", "", f"${planta_equipo:,}", ""],
    ["Depreciación Acumulada", "", f"-${abs(depreciacion_acumulada):,}", ""],
    ["Total Activos No Circulante", "", "", f"${total_activos_no_circulantes:,}"],
    ["", "", "", ""],
    ["ACTIVO TOTAL", "", "", f"${total_activos:,}"],
    ["", "", "", ""],
    ["PASIVO", "", "", ""],
    ["Corto Plazo", "", "", ""],
    ["Proveedores", "", f"${proveedores:,}", ""],
    ["Documentos por Pagar", "", f"${documentos_por_pagar:,}", ""],
    ["ISR por Pagar", "", "", ""],
    ["PTU por Pagar", "", f"${ptu_por_pagar:,}", ""],
    ["Total de Pasivo Corto Plazo:", "", "", f"${total_pasivo_corto_plazo:,}"],
    ["", "", "", ""],
    ["Largo Plazo", "", "", ""],
    ["Préstamos Bancarios", "", f"${prestamos_bancarios:,}", ""],
    ["Total de Pasivo Largo Plazo:", "", "", f"${total_pasivo_largo_plazo:,}"],
    ["", "", "", ""],
    ["PASIVO TOTAL", "", "", f"${total_pasivo:,}"],
    ["", "", "", ""],
    ["CAPITAL CONTABLE", "", "", ""],
    ["Capital Aportado", "", f"${capital_aportado:,}", ""],
    ["Capital Ganado", "", f"${capital_ganado:,}", ""],
    ["Utilidad del Ejercicio", "", f"${utilidad_ejercicio:,}", ""],
    ["Total de Capital Contable", "", "", f"${total_capital_contable:,}"],
    ["", "", "", ""],
    ["SUMA DE PASIVO Y CAPITAL", "", "", f"${suma_pasivo_capital:,}"]
]

# Imprimir la tabla
print(tabulate(tabla, tablefmt="rounded_grid"))

print("\nGracias por usar el sistema.")

