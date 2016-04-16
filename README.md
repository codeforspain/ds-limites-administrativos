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
 

###Comunidades, Provincias y Municipios.
 1. Descargar los datos de Centro Geografico Nacional ([enlace directo] (http://centrodedescargas.cnig.es/CentroDescargas/equipamiento/lineas_limite.zip))
 o bien desde [datos.gob.es] (http://datos.gob.es/catalogo/lineas-limite-jurisdiccionales-de-espana-0).
 
 2. Al descomprimir el archivo Zip nos econcontramos con los shapefiles formados por las líneas que delimitan los límites adminstrativos y otras carpetas con los shapefiles de los recintos. Nos quedaremos con estos últimos. 
 
 3. Convertimos los shapefiles a GeoJSON.
   + Intalamos [gdal] (http://www.gdal.org/). En Mac: $ brew install gdal
   + cd en el directorio donde tengamos descomprimidos los Shapefiles
   + Ejecuta (sustituyendo [nombre] por el nombre del Shapefile a convertir): `$ ogr2ogr -f GeoJSON -t_srs crs:84 [nombre].geojson [nombre].shp`
   
   Nota: para los usuarios de Windows [un manual] (http://blog.thematicmapping.org/2013/06/converting-shapefiles-to-topojson.html)
