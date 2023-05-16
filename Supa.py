import supabase

def datos(url, clave):
    client = supabase.create_client(url, clave)
    response = client.from_('Productos').select('*').execute()
    lista= str(response)
    texto_formateado= lista
    inicio_datos = texto_formateado.index("[{")
    fin_datos = texto_formateado.index("}]")
    datos_texto = texto_formateado[inicio_datos:fin_datos+2]
    datos_lista = eval(datos_texto)
    print(datos_lista)
    (type(datos_lista))
    return(datos_lista)




