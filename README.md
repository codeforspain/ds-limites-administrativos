# ds-limites-administrativos
Geometría de las líneas límites administrativos de España a escala 1:25.000

**Responsable**: @jalbertoroman
- Comunidades Autónomas, Provincias, Municipios, Comarcas Agrarias, Comarcas Ganaderas.
- GeoJSON
- Actualizado al menos cada año

Éste dataset es parte del proyecto abierto y colaborativo **CodeForSpain**

Puedes obtener más información en:

 + https://github.com/codeforspain/datos/wiki
 + https://twitter.com/codeforspain
 
## Comunidades, Provincias y Municipios.

# Datos 
Los datos los descargaremos del Centro Geográfico Nacional ([enlace directo] (http://centrodedescargas.cnig.es/CentroDescargas/equipamiento/lineas_limite.zip))
 o bien en [datos.gob.es] (http://datos.gob.es/catalogo/lineas-limite-jurisdiccionales-de-espana-0).

Al descomprimir el archivo Zip encontraremos los shapefiles formados por las líneas que delimitan los límites administrativos y otras carpetas con los shapefiles de los recintos. Nos quedaremos con estos últimos y son los que convertiremos a GeoJSON. 

# Preparación
 Ejecutar el script para convertir los shapefiles a GeoJSON.
   + Instalamos [gdal] (http://www.gdal.org/). (p. ej. en Mac: `$ brew install gdal`)
   + Copiar el archivo limitesAdmin.py en la carpetea que se desee descargar los archivos. Ejecuta el script: `$ python limitesAdmin.py ` este script automáticamente descarga los archivos, los descomprime y convierte los shp a GeoJSON. En cada carpeta aparecerá su archivo GeoJSON correspondiente.

# Licencia

