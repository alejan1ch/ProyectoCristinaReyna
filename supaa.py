import os
from dotenv import load_dotenv
import supabase

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtiene las variables de entorno
SUPABASE_URL = "https://ymhtktsffxmaajexzney.supabase.co/rest/v1/Productos?select=*"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InltaHRrdHNmZnhtYWFqZXh6bmV5Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NDA0NDcyNCwiZXhwIjoxOTk5NjIwNzI0fQ.aw9AKo_rs39WTNGjorSexD79k-Izt5cmUdDCnBcVXfM"

# Crea una instancia de cliente Supabase
client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)

# Consulta los productos de la tabla Productos
response = client.from_('Productos').select('*').execute()

# Imprime los datos obtenidos
def listar_items(data):
    if 'data' in data:
        items = data['data']
        for index, item in enumerate(items, start=1):
            nombre = item['Nombreproducto']
            precio = item['Precio']
            print(f"{index:02d}. {nombre} = {precio} pesos")
    else:
        print("No se encontraron datos")

listar_items(response)