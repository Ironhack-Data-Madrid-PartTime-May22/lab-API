from operator import index
import pandas as pd # manipulacion de  datos mediante dataframes
pd.options.display.max_columns = None # para que se muestren todas las columnas

import requests # para hacer peticiones a la web y obtener datos 

#import os  # para acceder a las variables de entorno del sistema operativo 
#from dotenv import load_dotenv # para cargar las variables de entorno desde el fichero .env

#load_dotenv()
#api_key es el nombre de la variable que almacena el token  en el archivo .env
#token = os.getenv("api_key")

token = '?'

# funcion para hacer la llamada a la API
def get_api(url):
    """
    Realiza una solicitud HTTP GET a una API utilizando la libreria requests. 
    Si la respuesta tiene un código de estado 200 (éxito), la función devuelve los 
    datos de la respuesta en formato JSON; de lo contrario, devuelve un mensaje 
    de error con el código de estado.

    Args:
        url (str): Endpoint de la API a la que se realiza la solicitud. 

    Returns:
        dict o str: datos de la respuesta en formato JSON o mensaje de error con el código de estado.
    """
    res = requests.get(url) # realizamos la llamada a la API

    if res.status_code == 200: # si la respuesta es correcta 
        return res.json() # devolvemos los datos en formato JSON
    
    else: # si la respuesta no es correcta 
        return f"Error {res.status_code}" # devolvemos un mensaje de error con el código de estado
    
eu_iso = ['AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL', 'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE']
informacion = {"ID":[],"Country":[],"Language":[],"Sales level":[],"Date":[],"Name":[],"Class":[],"Product group":[],"Net price":[],"Currency":[]}

for iso in eu_iso:

    try:
        url = f'https://api.mercedes-benz.com/configurator/v1/markets?country={iso}&apikey={token}'

        res_api = get_api(url)
        print(res_api)

        url = res_api[0]['_links']['models']
        res_api = get_api(url)

        for car in range(0, len(res_api)):

            informacion['ID'].append(res_api[car]['vehicleSortId'])
            informacion['Country'].append(res_api[car]['context']['market']['country'])
            informacion['Language'].append(res_api[car]['context']['market']['language'])
            informacion['Sales level'].append(res_api[car]['context']['salesLevel'])
            informacion['Date'].append(res_api[car]['context']['pricingDate'])
            informacion['Name'].append(res_api[car]['name'])
            informacion['Class'].append(res_api[car]['vehicleClass']['className'])
            informacion['Product group'].append(res_api[car]['productGroup'])
            informacion['Net price'].append(res_api[car]['priceInformation']['netPrice'])
            informacion['Currency'].append(res_api[car]['priceInformation']['currency'])

    except:
        pass

df = pd.DataFrame(informacion)
df.to_csv(index=False)









