# ============Pregunta 2 (8pts)============

def resolviendo_el_mensaje(mensaje_copiado, horas, mensaje_encriptado, R):
  mensaje_desencriptado = ""
  mensaje_ordenado = "" 
  es_copia = False # Usar esta variable para averiguar si es una copia (True) o no (False)

  # Codigo para Pregunta 2 comienza aqui
  import numpy as np

  mensaje_encriptado = [int(ord(i)) for i in mensaje_encriptado]
  arreglo = np.arange(97,123)
  arreglo = arreglo[::-1]

  for i in mensaje_encriptado:
    if i == 36:
      mensaje_desencriptado += "."
    elif i == 38:
      mensaje_desencriptado += ","
    elif i == 47:
      mensaje_desencriptado += " "
    else:
      for j in range(len(arreglo)):
        if i == arreglo[j]:
          z = arreglo[j - horas]
          mensaje_desencriptado += chr(z)

    def mover(mensaje_copiado):
      lista = mensaje_copiado.split(" ")
      palabra = lista[-1]
      lista.pop()
      lista.insert(0, palabra)
      mensaje_copiado2 = ""
      for i in range(len(lista) - 1):
        mensaje_copiado2 = mensaje_copiado2 + lista[i] + " "
      mensaje_copiado2 = mensaje_copiado2 + lista[-1]
      return mensaje_copiado2

    for i in range(R):
      mensaje_copiado = mover(mensaje_copiado)
    print(mensaje_copiado)

  if mensaje_desencriptado == mensaje_copiado:
    es_copia = True
  else:
    es_copia = False
  # Codigo para Pregunta 2 acaba aqui

  resultado_final = [mensaje_desencriptado, mensaje_ordenado, es_copia]
  return resultado_final