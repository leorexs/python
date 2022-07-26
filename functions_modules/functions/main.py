# funciones sin argumentos
def mi_funcion():
	return "Hola"


# funciones con argumentos posicionales
def mi_funcion_pos(nombre):
	return f"Hola {nombre}"


# funciones con numero de argumentos indefinidos
def mi_funcion_arg(*args):
	for nombre in args:
		print(f"Hola {nombre}")


# funciones con argumentos de clave valor
def mi_funcion_kwargs(**kwargs):
	for key, value in kwargs.items():
		print(f"{key} : {value}")
	pass


# funciones de argumentos posicionales, numero indefinido de argumentos y de clave valor
def mi_funcion_all(pos, *args, **kwargs):
	print(pos)
	for nombre in args:
		print(f"Hola {nombre}")
	for key, value in kwargs.items():
		print(f"{key} : {value}")
	return {
		"pos": pos,
		"args": args,
		"kwargs": kwargs
	}


if '__main__' == __name__:
	print(mi_funcion())
	print(mi_funcion_pos("Juan"))
	mi_funcion_arg("Juan", "Pedro", "Maria")
	mi_funcion_kwargs(nombre="Juan", apellido="Pedro", edad=30)
	print(mi_funcion_all("Hola mundo", "Juan", "Pedro", "Maria", nombre="Juan", apellido="Pedro", edad=30))
