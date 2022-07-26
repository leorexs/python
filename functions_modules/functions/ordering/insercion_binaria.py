def quick_sort(lista=None):
	"""
	El proceso clave en la quickSort es una partición(). El objetivo de las particiones es, dada una matriz y un
	elemento x de un conjunto como el pivote, pon x en su posición correcta en una matriz ordenada y poner todos
	los elementos menores (menor que x) antes de x, y poner todos los elementos de mayor (mayor que x) después de la x.
	Todo esto debe hacerse en tiempo lineal.
	"""

	if len(lista) <= 1:
		return lista
	else:
		pivote = lista[0]
		menores = [x for x in lista[1:] if x <= pivote]
		mayores = [x for x in lista[1:] if x > pivote]
		return quick_sort(menores) + [pivote] + quick_sort(mayores)


if __name__ == '__main__':
	lista_prueba = [1, -15, 48, 2, 15]
	print(f'lista actual: {lista_prueba} ---> lista ordenada: {quick_sort(lista_prueba)}')