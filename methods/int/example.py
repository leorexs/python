# class int
# --------------------------------------------------------------------------------
# .as_integer_ratio()
# Devuelve un par de enteros, cuya razón es exactamente igual al int original y con denominador positivo.

print(1.5.as_integer_ratio())
print((1).as_integer_ratio())
print((-1.5).as_integer_ratio())
print((49/7).as_integer_ratio())

# .bit_count()
# Devuelve el número de unos en representacion binaria

num_bin = bin(1561)
print((1561).bit_count())

num_int = int(num_bin, 2)
print(num_int.bit_count())

# .bit_length()
# Devuelve el numero de bits necesarios para representar el int en binario.

num_bin = bin(128)
print((128).bit_length())
print((164).bit_length())
print((189).bit_length())
print((255).bit_length())


# class float
# --------------------------------------------------------------------------------
# .hex()
# Devuelve el int en formato hexadecimal.
num_hex = 2.0.hex()
print(num_hex)

num_hex = float(2).hex()
print(num_hex)

# .fromhex()
# Devuelve el int correspondiente al hexadecimal.
num_hex = '0x2'
print(float.fromhex(num_hex))

# .is_integer()
# Devuelve True si el float es un entero.

num_integer = 2.0.is_integer()
print(num_integer)

num_integer = 2.1.is_integer()
print(num_integer)

# class complex
# --------------------------------------------------------------------------------

# .conjugate()
# Devuelve el int con el mismo valor pero con el signo invertido.

print(15-5j.conjugate())
print(15+5j.conjugate())
print((-15j).conjugate())



