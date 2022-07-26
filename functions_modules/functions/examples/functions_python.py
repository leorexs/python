from functools import reduce

funcion_lambda = lambda value: value ** 2
print(funcion_lambda(2))

print(funcion_lambda.__call__(True))
print(funcion_lambda.__call__(15))
# print(funcion_lambda.__call__("Hola"))


# Funciones map
iterador = range(10)
funcion_map = map(lambda value: value ** 2, iterador)
print(list(funcion_map))

# Funciones reduce
iterador = range(5, 10)
funcion_reduce = reduce(lambda value1, value2: value1 + value2, iterador)
print(funcion_reduce)

# Funciones filter
iterador = range(2, 17)
funcion_filter = filter(lambda value: value % 2 == 0, iterador)
print(list(funcion_filter))





