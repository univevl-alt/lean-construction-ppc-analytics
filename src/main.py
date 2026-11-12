import pandas as pd

def calcular_ppc_y_cnc(df_tareas):
    """
    Calcula el PPC semanal y resume las Causas de No Cumplimiento (CNC).
    """
    total_programadas = len(df_tareas)
    completadas = len(df_tareas[df_tareas['estado'] == 'Completado'])
    
    ppc = (completadas / total_programadas) * 100 if total_programadas > 0 else 0
    
    no_completadas = df_tareas[df_tareas['estado'] != 'Completado']
    conteo_cnc = no_completadas['causa_nc'].value_counts()
    
    return ppc, conteo_cnc

if __name__ == "__main__":
    datos = {
        'tarea': ['Vaciado de losa 2º piso', 'Asentado de muro eje A', 'Instalación de tuberías desagüe', 'Colocación de acero en columnas'],
        'sector': ['Sector 1', 'Sector 2', 'Sector 1', 'Sector 3'],
        'estado': ['Completado', 'No Completado', 'Completado', 'No Completado'],
        'causa_nc': [None, 'Falta de material', None, 'Retraso de subcontrata']
    }
    
    df = pd.DataFrame(datos)
    ppc, cnc = calcular_ppc_y_cnc(df)
    
    print(f"=== REPORTE LEAN DE PRODUCCIÓN ===")
    print(f"PPC de la Semana: {ppc:.2f}%")
    print("\nCausas de No Cumplimiento:")
    print(cnc)
