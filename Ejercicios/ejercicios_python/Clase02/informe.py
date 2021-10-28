import pprint
""""2.15: Lista de tuplas"""
"""def leer_camion(f):
    import csv
    
    total = 0.0
    camion = []
    try:
        
        a = open(f)
        rows = csv.reader(a)
        headers = next(rows)       
        total = 0
        for line in rows:
            try:
                camion.append((line[0], int(line[1]), float(line[2])))
              
            except IndexError:
                print('Una fila se encuentra vacía')                
        return camion
        f.close()
        
    except FileNotFoundError or TypeError: 
          print(f'No corresponde a una direccion válida.') 
        
data = leer_camion('../Data/camion.csv')
print(data) 
total=0
for s in data:
    total += s[1]*s[2]
print[total]"""
from pprint import pprint
def leer_camion(nuevo_archivo):
    import csv
    camion = []
    
    try:
        with open(nuevo_archivo,"rt") as f:
            row =csv.reader(f)
            headers = next(row)        
            for line in row:
                try:#levantamos indexerror
                    fila = [line[0], int(line[1]), float(line[2])]
                    registro = dict(zip(headers,fila))
                    camion.append(registro)
                except IndexError:
                    pass
        return camion
        
        
    except FileNotFoundError or TypeError: 
          print(f'No corresponde a una direccion válida.') 
        
data = leer_camion('../Data/camion.csv')
print( )
print(data)
total = 0.0
for s in data:
    total += s['cajones']*s['precio']
print(f'total:{total}')
print( )
print("Impresión bonita de un diccionario en Python")
pprint(data)
"""Ejercicio 2.17: Diccionarios como contenedores"""
import csv
def leer_precios(nuevo_archivo):
    
    mydict={}
    with open (nuevo_archivo,'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                mydict[row[0]] = float(row[1])
            except:
                pass
    return mydict
precios= leer_precios('../Data/precios.csv')
print(precios)

              