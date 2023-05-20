import requests

# Lista de sitios web a verificar
sitios_web = ['https://sitio1.com', 'https://sitio2.com', 'https://sitio3.com']

# Obtener el contenido de la noticia
url_noticia = 'https://example.com/noticia'
response_noticia = requests.get(url_noticia)
contenido_noticia = response_noticia.text

# Bandera para rastrear la existencia en múltiples sitios
existencia_multiple = False

# Verificar la existencia en cada sitio web
for sitio in sitios_web:
    try:
        response_sitio = requests.get(sitio)
        contenido_sitio = response_sitio.text

        if contenido_noticia in contenido_sitio:
            existencia_multiple = True
            break
    except requests.exceptions.RequestException as e:
        print (f"Error al acceder a {sitio}: {e}")

# Determinar el resultado finalS
if existencia_multiple:
    print ("La noticia es legítima, existe en múltiples sitios.")
else:
    print ("La noticia es ilegítima, no se encontró en los sitios verificados.")


