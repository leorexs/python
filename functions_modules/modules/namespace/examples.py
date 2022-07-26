

def operaciones(num1=50, num2=25):
	"""
	Función que realiza operaciones matemáticas.
	"""
	def suma():
		result = num1 + num2
		return result

	def resta():
		result = num1 - num2
		return result

	def multiplicacion():
		result = num1 * num2
		return result

	def division():
		result = num1 / num2
		return result

	return suma, resta, multiplicacion, division
	# return dict(
	# 	suma=suma(),
	# 	resta=resta(),
	# 	multiplicacion=multiplicacion(),
	# 	division=division()
	# )


if __name__ == '__main__':
	funcion_sumar, _, _, _ = operaciones(10, 20)
	print(funcion_sumar())

	*_, funcion_dividir = operaciones(40, 20)
	print(funcion_dividir())

	*_, funcion_multiplicar, _ = operaciones(40, 20)
	print(funcion_multiplicar())

	# calculadora = operaciones()
	# print(f"""
	# 	Suma: {calculadora['suma']}
	# 	Resta: {calculadora['resta']}
	# 	Multiplicación: {calculadora['multiplicacion']}
	# 	División: {calculadora['division']}
	# """)
