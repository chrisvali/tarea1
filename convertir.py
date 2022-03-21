import pandas as pd
import openpyxl

def  interfaz_covertir(_archivo):
    leer_archivo =pd.read_excel(_archivo)
    leer_archivo.to_csv('archivo_convertido.csv')
    return leer_archivo