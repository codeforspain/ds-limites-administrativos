# Dependencias urar y rarfile
# Instalar:
  # Mac: brew install unrar | Ubuntu: apt-get install rar unrar
  # pip install rarfile

import os
import shutil
import rarfile

# Descargar el archivo zip, si hay otro archivo con el mismo nombre lo sobreescribe
os.system("curl -# -f -O http://www.magrama.gob.es/es/cartografia-y-sig/ide/descargas/ganaderia/Comarcas_Ganaderas_tcm7-162217.rar")

# Comprobamos que el archivo se ha descargado
if os.path.isfile('Comarcas_Ganaderas_tcm7-162217.rar'):
    # Se crea el directorio Comarcas_Ganaderas_tcm7-162217 si no existe y si exixte lo vaciamos, ogr2ogr no sobreescribe.
    if not os.path.exists('Comarcas_Ganaderas_tcm7-162217'):
        os.makedirs('Comarcas_Ganaderas_tcm7-162217')
    else:
        shutil.rmtree('Comarcas_Ganaderas_tcm7-162217')
        os.makedirs('Comarcas_Ganaderas_tcm7-162217')
    # Se descomprime el archivo rar
    with rarfile.RarFile('Comarcas_Ganaderas_tcm7-162217.rar') as rf:
        rf.extractall(path='Comarcas_Ganaderas_tcm7-162217')
    rf.close()
    # Se buscan los archivos shapefile y se convierten a GeoJSON
    for root, dirs, files in os.walk('Comarcas_Ganaderas_tcm7-162217'):
        for file in files:
            if file.endswith(".shp"):
                file = file[:-4]
                path = os.path.join(root, file)
                cmd = 'ogr2ogr -f GeoJSON -t_srs crs:84 ' + path + '.geojson ' + path + '.shp'
                os.system(cmd)
                end = "Archivo: " + file + " convertido a GeoJSON!"
                print(end)
else:
    print("El Archivo no se ha descargado correctamente.")
