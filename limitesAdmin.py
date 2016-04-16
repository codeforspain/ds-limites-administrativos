import os

for root, dirs, files in os.walk('lineas_limite'):
    for file in files:
        if file.endswith(".shp") and file.startswith("recintos"):
            file = file[:-4]
            path = os.path.join(root, file)
            cmd = 'ogr2ogr -f GeoJSON -t_srs crs:84 ' + path + '.geojson ' + path + '.shp'
            os.system(cmd)
            end = "Archivo: " + file + " convertido a GeoJSON!"
            print(end)
