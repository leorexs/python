# Tipos booleanos

bol_true = True
bol_false = False

print(bol_true and bol_false)  # False
print(bol_true and bol_true)  # True

print(bol_false or bol_false)  # False
print(bol_true or bol_false)  # True

print(not bol_false and not bol_false)  # True
print(not bol_true and not bol_true)  # False

# Parseo
print(bool(0)) # False

print(bool(1)) # True

print(bool(''))
print(bool({}))
print(bool([]))
print(bool(None))

print(bool('contenido'))
print(bool({'contenido': '15'}))
print(bool(['contenido']))
print(bool(16516))

# Comparaciones Logicas

numero_a = 8

numero_b = 15

# menor que 
print(numero_a < numero_b) # True
	
# mayor que
print(numero_a > numero_b) # False
	
# mayor o igual que
print(numero_a >= numero_b) # False
	
# igual que
print(numero_a == numero_b) # False
	
# no es igual que
print(numero_a != numero_b) # True
	
# evaluar si es 
print(type(5) is int)
print(type('5') is str)

# evaluar si no es
print(type(5) is not str)
print(type('5') is not int)
