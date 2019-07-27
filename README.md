![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Objetivo
El objetivo de este proyecto es:
* Realizar una extracción de todas las leyes promulgadas por el congreso de los diputados desde el año 1977.
* Aplicar técnicas de minería de textos a los títulos de las leyes para obtener unos datos sobre los que poder aplicar otras técnicas de minería de textos.
* Una vez obtenidos y normalizados los datos se pretendía aplicar algún criterio de clasificación que permitiera saber si estas leyes eran de corte progresista o conservador.

# Proceso

Se ha aplicado un ptrón ETL en el que se ha creado un módulo para agrupar todas las funciones que se han necesiado para realizar webscrapping de la página del congreso, ya que no existe ninguna API que permita la extracción de estos datos.

Para continuar con el patrón se ha creado otro módulo en el que se han agrupado las funciones creadas para transformar el texto. La transformación del texto tiene como resultado un data frame en el que se han agrupado las leyes por años y sobre las que se han aplicado métodos de limpieza propios de la minería de texto.

Por último para completar la fase de análisis se ha creado un Notebook de Jupiter sobre el que se ha implementado el análisis de los datos.

# Estructura del proyecto

El proyecto se organiza en las siguientes carpetas:

* src: En este carpeta se incluyen los archivos que contienen el código:
    * Scrapping.py : Este archivo contiene la lógica empleada para extraer todas las leyes de la página del Congreso de los diputados.
    * Transformer.py : Aquí se recoge la lógica implementada para realizar la limpieza y transformación de los datos necesaria para poder aplicar los anáilisis de minería de texto necesarios.
    * Visualization.ipynb: Contiene un Jupyter notebook en el que se implementan los análisis.
* data: En la carpeta data se almacenan los datos extraídos referentes a las leyes para no tener que repetir el proceso de extracción desde la URL del Congreso.
* Output: En esta carpeta se alacenan las salidas de los procesos de análisis, en este caso se almacenarán las nubes de palabras generadas para cada año.

# Cómo ejecutar el proyecto.

El proyecto se ejecuta desde el Jupyter notebook Visualization.ipynb. El resultado final de ejecutar el libro es un archivo normalizado con todas las leyes promulgadas desde 1977, que se guardará en la carpeta data y una serie de imagenes, una para cada año hasta 2019, que se alojaran en la carpeta output.

# Resultados

No se ha conseguido hacer la clasificación del texto, en lugar de eso se han creado nubes de palabras para cada uno de los años para visualizar que asuntos han sido más relevantes desde el punto de vista legislativo para cada uno de los años.

