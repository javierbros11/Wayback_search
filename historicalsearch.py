# External Packages

import subprocess
import requests

# Local Packages
import time

# Modules

from waybackpy import WaybackMachineCDXServerAPI
from datetime import datetime,timedelta


class HistoricalSearch:

    def __init__(self,url, user_agent):
        """
        Permite inicializar los atributos de instancia.
        
        Args:
            url(str): URL del sitio web que el usuario desea visitar.
            user_agent(str): Cadena de texto que identifica al software y el dispositivo que se está utilizando para llegar al sitio web.
        """
        self.url = url
        self.user_agent = user_agent

    def search_snapshot(self, years_ago=10):
        """
        Busca y guarda una captura de una fecha especifica.

        Args:
            years_ago(int): Número de años de margen.
            filename(str): Nombre del archivo en donde se quiere almacenar los resultados.
        """

        target_date = datetime.now() - timedelta(days=365 * years_ago)
        year,month,day = target_date.year,target_date.month,target_date.day

        cdx_api = WaybackMachineCDXServerAPI(self.url, self.user_agent)

        snapshot = cdx_api.near(year = year,month = month,day = day)

        if snapshot:
            print(f"Fecha: {snapshot.timestamp}, URL: {snapshot.archive_url}")
            self.download_snapshot(snapshot.archive_url)

        else:
            print(f"No se ha encontrado una snapshot para la fecha solicitada.")

    def download_snapshot(self,url,filename = "snapshot_test.html"):
        """
        Descarga y guarda el contenido de una URL de una snapshot en un fichero.

        Args:
            url(str): URL del sitio web que el usuario desea visitar.
            filename(str): Nombre del archivo en donde se quiere almacenar los resultados.
        """

        response = requests.get(url)
        
        if response.status_code == 200:
            with open(filename,"w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"Documento guardado satisfactoriamente en {filename}")
            print("Abriendo archivo ...")
            time.sleep(5)
            subprocess.run(f"firefox {filename}", shell=True)
            
        else:
            print(f"Error al descargar el fichero. Error: {response.status_code}")
    
    def search_snapshots_by_extensions(self,years_ago=4, days_interval=30, extensions=None,match_type="domain"):
        """
        Permite realizar una búsqueda de una snapshot sobre archivos que contengan una extensión determinada (["pdf","doc","docx","ppt","xls","xlsx","txt"])

        Args:
            years_ago(int, default: 4): Número de años de margen.
            days_interval(int, default: 30): Número de días entre snapashots.
            extensions(list, default: None): Lista que contiene una cantidad determinada de extensiones que se desean consultar.
            match_type(str, default: 'domain')
        """
        if extensions is None:
            extensions = ["pdf","doc","docx","ppt","xls","xlsx","txt"]

        # Calcular las fechas para el periordo especificado
        today = datetime.now()
        start_period = (today - timedelta(days=365 * years_ago)).strftime("%Y%m%d")
        end_period = (today -timedelta(days=(365 * years_ago) - days_interval)).strftime("%Y%m%d")

        cdx_api = WaybackMachineCDXServerAPI(self.url, self.user_agent,
                                             start_timestamp=start_period,end_timestamp=end_period,
                                             match_type=match_type)

        # Aplicamos un filtro mediante expresiones regulares
        regex_filter = "(" + "|".join([f".*\\.{ext}$" for ext in extensions]) + ")"
        cdx_api.filters = [f"urlkey:{regex_filter}"]

        # Realizamos la consulta a wayback machine
        snapshots = cdx_api.snapshots()
        for snapshot in snapshots:
            if snapshot:
                print(f"Fecha: {snapshot.timestamp}, URL: {snapshot.archive_url}")
                self.download_snapshot(snapshot.archive_url)
        else:
            print(f"No se ha encontrado una snapshot para la fecha solicitada.")

user_agent = "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"
try:

    url = str(input("Dime la URL del sitio web a investigar: "))
    option = str(input("Desea buscar una snapshot y almacenarlo como formato HTML (Y/N): "))
    test = HistoricalSearch(url,user_agent)
    
    if option == "Yes" or option == "Y" or option =="yes" or option =="y":
        test.search_snapshot()
    elif option == "No" or option == "N" or option =="no" or option =="n":
        test.search_snapshots_by_extensions(years_ago=1,days_interval=30)
    else:
        print("Respuesta incorrecta, cerrando programa...")

except KeyboardInterrupt:
    print("\nCerrando programa...")
# Si tarda mucho y devuelve un 504, se trata de una limitación del buscador de Waybackmachine no del script.