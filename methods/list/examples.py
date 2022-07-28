# class list
# --------------------------------------------------

lista = [-5, 15, -45, 0, 2, 100, 4, 5]

# clear()
# Elimina todos los elementos de la lista
lista.clear()
print(lista)

# .append()
# Añade un elemento al final de la lista
lista = [15, -5, -45, 0, 2, 100, 4, -48]
lista.append(500)
print(lista)

# .copy()
# Copia la lista
lista = [15, -5, -45, 0, 2, 100, 4, -48]
lista_copia = lista.copy()
lista_copia.clear()
print(lista)
print(lista_copia)

# .count()
# Cuenta el número de veces que se repite un elemento
lista = [15, 15, -45, 0, 15, 100, 4, -48]
print(lista.count(15))

# .extend()
# Añade una lista a otra
lista = [15, -5, -45, 0, 2, 100, 4, -48]
lista_extendida = [1, 2, 3, 4, 5]
lista.extend(lista_extendida)
print(lista)

# .index()
# Devuelve el índice del elemento
posicion = lista.index(100)
print(posicion)

# .insert()
# Inserta un elemento en un índice
print(lista)
lista.insert(3, -100)
print(lista)

# .pop()
# Elimina el elemento en un índice
lista = [15, -5, -45, 0, 2, 100, 4, -48]
lista.pop(3)
print(lista)

# .remove()
# Elimina el elemento
print(lista)
lista.remove(-45)
print(lista)

# .reverse()
# Invierte la lista
print(lista)
lista.reverse()
print(lista)

# .sort()
# Ordena la lista
print(lista)
lista.sort()
print(lista)


