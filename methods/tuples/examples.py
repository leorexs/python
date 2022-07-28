# class tuple:
# --------------------------------------------------------------------------------------------------------------------

tuple_lista = tuple(num for num in range(5, 16) if num % 2 == 0)

# .index()
print(tuple_lista)
position = tuple_lista.index(10)
print(position)
position = tuple_lista.index(12, 2, len(tuple_lista))
print(position)

# .count()
counter = tuple_lista.count(10)
print(counter)








