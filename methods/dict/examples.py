# class dict:
# -----------------------------------------------------------------------------


diccionario = {
    'a': 1,
    'b': 2,
    'c': 3
}

# .clear()
# Elimina todos los elementos del diccionario
print(diccionario)
diccionario.clear()
print(diccionario)

# .copy()
diccionario = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 30
}

diccionario_copia = diccionario.copy()
print(diccionario_copia)

nombre = diccionario_copia["nombre"]
print(nombre)

nombre = diccionario_copia
print(nombre)

direccion = diccionario_copia.get("direccion", "No encontrado")
print(direccion)


# .items()
items = diccionario_copia.items()
# for key, value in items:
#     print(key, value)

# .keys()
keys = diccionario_copia.keys()
print(keys)
# for key in keys:
#     print(key)

# .values()
values = diccionario_copia.values()
print(values)
# for value in values:
#     print(value)


# .pop()
item_pop = diccionario_copia.pop("nombre", "No encontrado")
print(item_pop)
print(diccionario_copia)
item_pop = diccionario_copia.pop("nombre", "No encontrado")
print(item_pop)
print(diccionario_copia)

# .setdefault()
field = {'nombre': "Juan"}
diccionario_copia.setdefault('nombre', field['nombre'])

por_defecto = diccionario_copia.setdefault('nombre', "Leonardo")
print(por_defecto)

# .update()
diccionario_copia.update({
    'nombre': "Pepe",
    'edad': 50
})

# .update()
diccionario_copia.update({
    'direccion': "Calle falsa 123"
})

# .fromkeys()
# Crea un diccionario con las claves indicadas
dic_key = dict.fromkeys(['nombre', 'apellido', 'edad'])


dic_value = dict.fromkeys(['nombre', 'apellido', 'edad'], "")

# .popitem()
# Elimina un elemento del diccionario
diccionario_copia.popitem()
print(diccionario_copia)
