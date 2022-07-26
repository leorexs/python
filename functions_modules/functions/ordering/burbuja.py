def burbuja(lista):
	"""
	Ordena una lista de forma ascendente

	Consiste en acomodar el vector moviendo el mayor hasta la última casilla comenzando desde la casilla cero del vector
	hasta haber acomodado el número más grande en la última posición del vector.

	@param lista: list -> lista a ordenar
	@return lista: list -> lista ordenada
	@raises TypeError: Si el tipo de dato de la lista no es list
	@raises TypeError: La lista no contiene elementos numericos
	"""

	try:
		if type(lista) is not list:
			raise TypeError('Solo se aceptan listas')

		tamanio = len(lista)

		for i in range(tamanio):
			# print("recorrido: ", i, end='\n')
			for j in range(tamanio - 1):
				# print(f'''
				# Comparacion de valores en lista {lista}:
				#
				# Posicion actual {j}: {lista[j]}
				# Posicion siguiente {j+1}: {lista[j+1]}
				# '''
				# )

				try:
					if lista[j] > lista[j + 1]:
						# print(f'posicion mayor: {lista[j]}')
						lista[j], lista[j + 1] = lista[j + 1], lista[j]
				except Exception as e:
					if isinstance(e, TypeError):
						mensaje = "Tipos de datos a evaluar no son numericos"
						return mensaje
					pass

		return lista
	except Exception as e:
		if isinstance(e, TypeError):
			mensaje = "El tipo de dato de la lista no es list"
			return mensaje
	# finally: # se ejecuta siempre
		# 	pass


if __name__ == '__main__':
	lista_prueba = [1, -15, 48, 2, 15]
	print(f'lista actual: {lista_prueba} ---> lista ordenada: {burbuja(lista_prueba)}')

	tupla_prueba = (5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5)
	print(burbuja(f'Manejo de error --> TypeError {tupla_prueba}'))

	lista_no_homogenea = [1, "hola", False, None]
	print(burbuja(lista_no_homogenea))

