import openpyxl
import shutil

original = 'backend\excel\Caso 2 Presupuesto Maestro.xlsx'
copia = 'backend\excel\Copia.xlsx'

shutil.copyfile(original, copia)

def presupuesto_ventas_1():
  wb = openpyxl.load_workbook(copia)
  hoja = wb['Desarrollo']
  hoja['B10'] = '696969'

  wb.save(copia)  # Save the changes to the Excel file

presupuesto_ventas_1()

def saldo_clientes_flujo_entradas_2():
  pass

def presupuesto_produccion_3():
  pass

def presupuesto_requerimiento_materiales_4():
  pass

def presupuesto_compra_materiales_5():
  pass

def saldo_proveedores_flujo_salidas_6():
  pass

def presupuesto_mano_obra_7():
  pass

def presupuesto_gif_8():
  pass

def presupuesto_gastos_operacion_9():
  pass

def costo_unitario_10():
  pass

def valuacion_inventarios_finales_11():
  pass

def exportar_excel():
  pass