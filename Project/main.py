# inputs del usuario
texto = input("Introduce el texto a analizar: ").lower()
letras = [input("Introduce una primera letra: ").lower(),
          input("Introduce una segunda letra: ").lower(),
          input("Introduce una tercera letra: ").lower()]

# analisis de letras (metodo 'count')
print(f"\n -- análisis de letras -- \n la letra '{letras[0]}' aparece: {texto.count(letras[0])} veces, " 
      f"\n la letra '{letras[1]}' aparece: {texto.count(letras[1])} veces, "
      f"\n la letra '{letras[2]}' aparece: {texto.count(letras[2])} veces,")

# analisis de palabras (transformar a una lista)
convertido = texto.split(' ')
print(f"\n -- análisis de palabras -- \n aparecen {len(convertido)} palabras en total,")

# analisis indexacion (indices)
print(f"\n -- análisis de indexación -- \n la primera letra es '{texto[0].upper()}', "
      f"\n la ultima letra es '{texto[-1]}',")

# analisis inverso (recorte inverso)
# (alternativa usando 'reverse' + 'join' ya que te lo saca como una lista)
print(f"\n -- análisis de inverso -- \n el texto original es: '{texto}', "
      f"\n el texto invertido es: '{texto[::-1]}',")

# analisis personalizado (booleanos y diccionarios)
# (sustituto del if-else)
respuestas = {True:"¡Aprender Python es divertido!", False:"Este analizador es un prograama complicado"}
comprobacion = "python" in texto
print(f"\n -- análisis personalizado -- \n la palabra 'python' aparece: '{comprobacion}', "
      f"\n el texto asociado es: '{respuestas[comprobacion]}',")

