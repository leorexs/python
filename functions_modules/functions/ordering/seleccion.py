def seleccion(lista: list) -> list:
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
		for i in range(len(lista)):
			pos = i
			for j in range(i+1, len(lista)):
				if lista[j] < lista[pos]:
					pos = j
			lista[i], lista[pos] = lista[pos], lista[i]
		return lista
	except Exception as e:
		pass


if __name__ == '__main__':
	lista_prueba = [1, -15, 48, 2, 15]
	print(f'lista actual: {lista_prueba} ---> lista ordenada: {seleccion(lista_prueba)}')

	tupla_prueba = (5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5)
	print(seleccion(f'Manejo de error --> TypeError {tupla_prueba}'))

	lista_no_homogenea = [1, "hola", False, None]
	print(seleccion(lista_no_homogenea))
