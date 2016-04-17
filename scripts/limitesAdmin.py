import os
import shutil
import zipfile

# Descargar el archivo zip, si hay otro archivo con el mismo nombre lo sobreescribe
os.system("curl -# -f -O http://centrodedescargas.cnig.es/CentroDescargas/equipamiento/lineas_limite.zip")

if not os.path.exists('lineas_limite'):
    os.makedirs('lineas_limite')
else:
    shutil.rmtree('lineas_limite')
    os.makedirs('lineas_limite')

if os.path.isfile('lineas_limite.zip'):
    # Descomprimir el archivo
    with zipfile.ZipFile('lineas_limite.zip', 'r') as z:
        z.extractall('lineas_limite')
    z.close()

    # Buscar  archivos shp y convertir a GeoJSON
    for root, dirs, files in os.walk('lineas_limite'):
        for file in files:
            if file.endswith(".shp") and file.startswith("recintos"):
                file = file[:-4]
                path = os.path.join(root, file)
                cmd = 'ogr2ogr -f GeoJSON -t_srs crs:84 ' + path + '.geojson ' + path + '.shp'
                os.system(cmd)
                end = "Archivo: " + file + " convertido a GeoJSON!"
                print(end)
else:
    print("El Archivo no se ha descargado correctamente.")
