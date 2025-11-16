
# Wayback Machine Historical Search

Este programa trata de realizar búsquedas personalizas sobre el buscador Wayback Machine mediante la consulta otorgada por el usuario.
## Instalación

Antes de llevar a cabo la instalación requerimos previamente que se encuentre instalado Python en el equipo:

[Download Python](https://www.python.org/downloads/)

Para la ejecución del programa basta con instalar los paquetes necesarios referenciados en el fichero **requirements.txt**.

A continuación, el comando de instalación de dichos paquetes:

```bash
pip install requests waybackpy
```



## Funcionalidades

- **Búsquedas personalizadas**: Al ejecutar el programa "historicalsearch.py" se le indicará al usuario la url o el nombre del sitio web que desee consultar.

- **Snapshots**: En función del año desde cuando se desea realizar la búsqueda, el programa con la integración de Wayback Machine en python irá registrando snapshots que esten disponibles en el momento de la búsqueda encagando en el filtro indicado.

- **Descarga de sitios web**: Tras haber localizado una snapshot válida, si se indica previamente el programa procederá a la descarga del sitio web y lo almacena dentro del fichero donde se encuentre el programa bajo el nombre que se le indique (por defecto: "snapshot.html").

- **Descarga de archivos según su formato**: Podemos especificar el formato del archivo que deseemos almacenar localmente y si el programa lo encuentra inciará con su descarga.
## Posibles errores durante la ejecución del programa

- Si el programa tarda demasiado en buscar resultados al hacer una consulta y devuelve un **error 504**: 


**"waybackpy.exceptions NoCDXRecordFound: Wayback Machine's CDX server did not return any records for the query. The URL may not have any archives  on the Wayback Machine or the URL may have been recently archived and is still not available on the CDX server."**

**"requests.exceptions.RetryError: HTTPSConnectionPool(host='web.archive.org', port=443): Max retries exceeded with url: /cdx/search/cdx?from=20241112&to=20241212&gzip=false&matchType=domain&filter=urlkey%3A%28.%2A%5C.pdf%24%7C.%2A%5C.doc%24%7C.%2A%5C.docx%24%7C.%2A%5C.ppt%24%7C.%2A%5C.xls%24%7C.%2A%5C.xlsx%24%7C.%2A%5C.txt%24%29&url=udemy.com&showResumeKey=true&limit=25000 (Caused by ResponseError('too many 504 error responses'))"**

Suele tratarse de una limitación del buscador de Waybackmachine no del script.

- Es posible que al encontrar una snapshot y llevar a cabo su almacenamiento el script devuelva un **error 403**:

**"Error al descargar el fichero. Error: 403"**

Si llega a ocurrir ese caso prueba a buscar otra snapshot en una franja de tiempo diferente.
# Ejemplos de uso

Buscar una snapshot de un sitio web desde el 2020 en adelante, descarga el sitio web en formato html llamándolo "ejemplo.html" y abre el navegador para visualizarlo:

```bash
  └─$ python historicalsearch.py
Dime la URL del sitio web a investigar: "SITIO WEB"
Desea buscar una snapshot y almacenarlo como formato HTML (Y/N): y
¿Desde cuando desea realizar la búsqueda? (Año): 2020
Fecha: 20201116113557, URL: "URL DEL SITIO WEB"
Dime como nombrar el archivo descargado: ejemplo
Documento guardado satisfactoriamente en ejemplo.html
Abriendo archivo ...
```
## Tech Stack

Todos los archivos necesarios para el correcto funcionamiento de ambos programas presentados se encuentran desarrollados en **Python**.
