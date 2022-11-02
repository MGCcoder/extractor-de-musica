import argparse
import re
import subprocess


class Cancion:
    tiempo_final = '0'
    def __init__(self, tiempo, nombre, artista='', album=''):
        self.tiempo_inicial = tiempo
        self.nombre = nombre[1:-1]
        self.artista = artista[1:-1]
        self.album = album[1:-1]

def analizar_archivo(archivo_lista_canciones,expresion_regular,artist,album):
    lista_canciones = []
    with open(archivo_lista_canciones, 'r') as f:
        count = 1
        for linea in f:
            #search encuentra el primer match
            coincidencias = re.search(r''+expresion_regular,linea)
            if coincidencias != None:
                if not album and not artist:
                    lista_canciones.append(Cancion(
                        coincidencias.group(1),
                        coincidencias.group(3)
                        ))
                if artist and not album:
                    lista_canciones.append(Cancion(
                        coincidencias.group(1),
                        coincidencias.group(3),
                        coincidencias.group(4)
                        ))
                if album and not artist:
                    lista_canciones.append(Cancion(
                        coincidencias.group(1),
                        coincidencias.group(3),
                        '',
                        coincidencias.group(4)
                        ))
                if artist and album:
                    lista_canciones.append(Cancion(
                        coincidencias.group(1),
                        coincidencias.group(3),
                        coincidencias.group(4),
                        coincidencias.group(5)
                        ))
            else:
                error = "Error en el formato del archivo línea {}"
                raise Exception(error.format(count))
            count += 1
    return lista_canciones

def calcular_tiempo_final(lista_canciones,archivo_de_musica):
    #Obtiene la duracion del archivo
    command = "ffmpeg -i '{0}' 2>&1 | grep 'Duration'".format(archivo_de_musica)
    p = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    result = p.stdout.decode()
    duracion = re.search(r'((\d{1,2}:){1,2}\d{1,2}.\d{1,2})',result).group()

    for i in range(len(lista_canciones)-1):
        lista_canciones[i].tiempo_final = lista_canciones[i+1].tiempo_inicial

    lista_canciones[-1].tiempo_final = duracion
    return lista_canciones

def separar_canciones(lista_canciones,archivo_de_musica):
    lista_canciones = calcular_tiempo_final(lista_canciones,archivo_de_musica)
    print("\n\nVideo: {}\n\n".format(archivo_de_musica))
    nombre_de_directorio = input('Escriba el nombre del nuevo directorio donde se guardaran las canciones: ')
    subprocess.call("mkdir '{}'".format(nombre_de_directorio), shell=True)
    for cancion in lista_canciones:
        #Este comando corta una cancion en un intervalo de tiempo
        separar = "ffmpeg -i '{0}' -c:v copy -c:a libmp3lame -q:a 4 -ss {1.tiempo_inicial}  -to {1.tiempo_final} './{2}/cancion.mp3'".format(archivo_de_musica, cancion, nombre_de_directorio)
        metadatos = "ffmpeg -i './{1}/cancion.mp3' -c copy -metadata album='{0.album}' -metadata artist='{0.artista}' './{1}/{0.nombre}.mp3'".format(cancion, nombre_de_directorio)
        borrar = "rm './{0}/cancion.mp3'".format(nombre_de_directorio)
        print(metadatos)
        subprocess.call(separar, shell=True)
        subprocess.call(metadatos, shell=True)
        subprocess.call(borrar, shell=True)

def main():

    #Analizador de argumentos
    desc = """
        Con este programa puedes extraer música que está unida en un solo archivo de música a partir de una lista con sus marcas de tiempo,
        también permite agregar los metadatos de la canción como el nombre de artista o album.
        
        El formato por defecto para la lista de canciones es:```[tiempo] [nombre]``` por cada línea.
        
        Ejemplo de una línea en el archivo: 
        > 00:00 "Nombre de canción"
        
        Si se unen las opciones -a y -b de esta forma -ab. El formato puede debe ser: ```[tiempo] [nombre] [artista] [album]```
        
        Ejemplo de una línea en el archivo: 
        
        > 00:00 "Nombre de canción" "Nombre de artista" "Nombre de album"
    """
    parser = argparse.ArgumentParser(description=desc)

    lista_desc = """
    Es el nombre del archivo donde esta la lista de múscia con las marcas de tiempo.
    """
    parser.add_argument('--list', help=lista_desc, required=True)

    musica = """
        Es el nombre del archivo de música con las canciones unidas
    """
    parser.add_argument('--music', help=musica, required=True)

    album_desc = """
    Si el archivo contiene albumes puedes agregar esta bandera. 
    El formato del archivo para cada línea debera ser: 
    [tiempo] [nombre] [album]
    """
    parser.add_argument('--album', '-b', help=album_desc, action='store_true')

    artist_desc = """ 
     Si el archivo contiene artistas puede agregar esta bandera. 
     El formato del archivo para cada línea debera ser: 
     [tiempo] [nombre] [artista]
    """
    parser.add_argument('--artist', '-a', help=artist_desc, action='store_true')

    args = parser.parse_args()

    archivo_lista_canciones = args.list
    archivo_de_musica = args.music
    album = args.album
    artist = args.artist
    # Expresión regular para analizar la lista de canciones dependiendo de los argumentos
    expresion_regular = '^((\d{1,2}:){1,2}\d{1,2})\s+("[^"]+")'
    if album != artist:
        expresion_regular += '\s+("[^"]+")'
    if album and artist:
        expresion_regular += '\s+("[^"]+")\s+("[^"]+")'
    try:
        #Regresa un arreglo de objetos con la lista de canciones
        lista_canciones = analizar_archivo(archivo_lista_canciones, expresion_regular, artist, album)
    except Exception as e:
        print(e)
    #
    else:
        separar_canciones(lista_canciones,archivo_de_musica)


if __name__ == '__main__':
    main()

