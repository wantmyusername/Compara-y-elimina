# Abrimos el archivo archivo.txt en modo lectura
with open("db.txt", "r") as archivo:
  # Abrimos el archivo texto_remover.txt en modo lectura
  with open("texto_remover.txt", "r") as texto_remover:
    # Leemos el contenido de texto_remover.txt y lo almacenamos en una lista
    textos_remover = texto_remover.readlines()

    # Abrimos el archivo archivo_modificado.txt en modo escritura
    with open("archivo_modificado.txt", "w") as archivo_modificado:
      # Recorremos cada línea del archivo archivo.txt
      for linea in archivo:
        # Verificamos si la línea comienza con algún texto de la lista de textos a remover
        remover = False
        for texto in textos_remover:
          if linea.startswith(texto):
            remover = True
            break
        # Si la línea no comienza con ningún texto de la lista, escribimos la línea en el archivo archivo_modificado.txt
        if not remover:
          archivo_modificado.write(linea)
