import os
import shutil
import zipfile

# Descargar el archivo zip, si hay otro archivo con el mismo nombre lo sobreescribe
os.system("curl -# -f -O http://centrodedescargas.cnig.es/CentroDescargas/equipamiento/lineas_limite.zip")

# Comprobamos que el archivo se ha descargado
if os.path.isfile('lineas_limite.zip'):
    # Se crea el directorio lineas_limite si no existe y si exixte lo vaciamos, ogr2ogr no sobreescribe.
    if not os.path.exists('lineas_limite'):
        os.makedirs('lineas_limite')
    else:
        shutil.rmtree('lineas_limite')
        os.makedirs('lineas_limite')
    # Se descomprime el archivo
    with zipfile.ZipFile('lineas_limite.zip', 'r') as z:
        z.extractall('lineas_limite')
    z.close()
    # Se buscan los archivos shapefile y se convierten a GeoJSON
    for root, dirs, files in os.walk('lineas_limite'):
        for file in files:
            if file.endswith(".shp") and file.startswith("recintos"):
                file = file[:-4]
                path = os.path.join(root, file)
                cmd = 'ogr2ogr --config SHAPE_ENCODING "UTF-8" -f GeoJSON -t_srs crs:84 ' + path + '.geojson ' + path + '.shp'
                os.system(cmd)
                end = "Archivo: " + file + " convertido a GeoJSON!"
                print(end)
else:
    print("El Archivo no se ha descargado correctamente.")
