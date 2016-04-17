# Dependencias unrar y rarfile
# Instalar:
  # Mac: brew install unrar | Ubuntu: apt-get install rar unrar
  # pip install rarfile

import os
import shutil
import rarfile

# Descargar el archivo zip, si hay otro archivo con el mismo nombre lo sobreescribe
os.system("curl -# -f -O http://www.magrama.gob.es/es/cartografia-y-sig/ide/descargas/agricultura/ComarcasAgrarias_tcm7-162216.rar")

# Comprobamos que el archivo se ha descargado
if os.path.isfile('ComarcasAgrarias_tcm7-162216.rar'):
    # Se crea el directorio ComarcasAgrarias_tcm7-162216 si no existe y si exixte lo vaciamos, ogr2ogr no sobreescribe.
    if not os.path.exists('ComarcasAgrarias_tcm7-162216'):
        os.makedirs('ComarcasAgrarias_tcm7-162216')
    else:
        shutil.rmtree('ComarcasAgrarias_tcm7-162216')
        os.makedirs('ComarcasAgrarias_tcm7-162216')
    # Se descomprime el archivo rar
    with rarfile.RarFile('ComarcasAgrarias_tcm7-162216.rar') as rf:
        rf.extractall(path='ComarcasAgrarias_tcm7-162216')
    rf.close()
    # Se buscan los archivos shapefile y se convierten a GeoJSON
    for root, dirs, files in os.walk('ComarcasAgrarias_tcm7-162216'):
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
