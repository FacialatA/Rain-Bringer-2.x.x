import os
from bs4 import BeautifulSoup

# Carpeta actual (donde se encuentra el script)
carpeta = os.getcwd()

# Función para realizar la modificación en un archivo HTML
def modificar_archivo_html(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()

    # Parsea el contenido HTML con BeautifulSoup y usa formatter=None
    soup = BeautifulSoup(contenido, 'html.parser')

    # Encuentra todas las etiquetas <section> con class="display-7" sin otros atributos
    secciones = soup.find_all('section', class_='display-7', attrs={'class': False, 'id': False})

    for seccion in secciones:
        # Comenta la sección
        comentario_inicio = soup.new_string('<!--')
        comentario_fin = soup.new_string('-->')
        seccion.insert_before(comentario_inicio)
        seccion.insert_after(comentario_fin)

    # Guarda el contenido modificado en el archivo
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify(formatter=None)))

# Recorre los archivos en la carpeta y modifica los archivos HTML
for directorio_actual, _, archivos in os.walk(carpeta):
    for archivo in archivos:
        if archivo.endswith('.html'):
            ruta_completa = os.path.join(directorio_actual, archivo)
            modificar_archivo_html(ruta_completa)

print('Modificación completada en archivos HTML en la carpeta actual.')

