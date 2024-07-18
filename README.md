# Extractor de música
<!-- ![GitHub ultimo commit](https://img.shields.io/github/last-commit/MGCcoder/extractor-de-musica) -->

### Instalación

> `pip install emusica`
### Requisitos

- Python 3
- Ffmpeg

### Sistemas Operativos compatibles

- Windows
- Linux
- MacOS

### Tutorial

Con este programa puedes extraer las pistas de canciones que están unidas en un solo archivo de audio a partir de un archivo de texto donde este la lista de cancionoes y sus marcas de tiempo, también permite agregar los metadatos de la canción como el nombre de artista o album.

La lista debe tener la siguiente estructura:

```txt
00:00 Nombre de canción 1
15:00 Nombre de canción 2
30:00 Nombre de canción 3
```

> Nota: El nombre no puede contener guiones

Si quieres agregar información del artista o album se usan las opciones -a y -b

Por ejemplo usando la opción -a la estructura de la lista sería la siguiente:

```txt
00:00 Nombre de artista 1 - Nombre de canción 1
15:00 Nombre de artista 2 - Nombre de canción 2
30:00 Nombre de artista 3 - Nombre de canción 3
```

Usando la opción -b la estructura sería:

```txt
00:00 Nombre de album 1 - Nombre de canción 1
15:00 Nombre de album 2 - Nombre de canción 2
30:00 Nombre de album 3 - Nombre de canción 3
```

Si se unen las 2 opciones -ab la estructura sería:

```txt
00:00 Nombre de album 1 - Nombre de artista 1 - Nombre de canción 1
15:00 Nombre de album 2 - Nombre de artista 2 - Nombre de canción 2
30:00 Nombre de album 3 - Nombre de artista 3 - Nombre de canción 3
```

### Opciones del comando

```txt
  -h,     --help     show this help message and exit
  
  --list    LIST     Es el nombre del archivo donde esta la lista de muscia con las marcas de tiempo.
  
  --music   MUSIC    Es el nombre del archivo de música con las canciones unidas
  
  --album,  -b       Si el archivo contiene albumes puedes agregar esta bandera. 
                     El formato del archivo para cada línea debera ser: 
                     [tiempo] [album] - [nombre]
                     
  --artist, -a       Si el archivo contiene artistas puede agregar esta bandera. 
                     El formato del archivo para cada línea debera ser: 
                     [tiempo] [artista] - [nombre]
```
