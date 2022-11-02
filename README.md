## Extractor de música
Con este programa puedes extraer música que está unida en un solo archivo de música a partir de una lista con sus marcas de tiempo,
también permite agregar los metadatos de la canción como el nombre de artista o album.

El formato por defecto para la lista de canciones es:```[tiempo] [nombre]``` por cada línea.

Ejemplo de una línea en el archivo: 
> 00:00 "Nombre de canción"

Si se unen las opciones -a y -b de esta forma -ab. El formato puede debe ser: ```[tiempo] [nombre] [artista] [album]```

Ejemplo de una línea en el archivo: 

> 00:00 "Nombre de canción" "Nombre de artista" "Nombre de album"

### Opciones:
```
  -h,     --help     show this help message and exit
  
  --list    LIST     Es el nombre del archivo donde esta la lista de muscia con las marcas de tiempo.
  
  --music   MUSIC    Es el nombre del archivo de música con las canciones unidas
  
  --album,  -b       Si el archivo contiene albumes puedes agregar esta bandera. 
                     El formato del archivo para cada línea debera ser: 
                     [tiempo] [nombre] [album]
                     
  --artist, -a       Si el archivo contiene artistas puede agregar esta bandera. 
                     El formato del archivo para cada línea debera ser: 
                     [tiempo] [nombre] [artista]
```

