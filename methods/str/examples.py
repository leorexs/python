# class str
# --------------------------------------------------------------------------------

CADENA = "lorem IPsum doloR sIT amet"

# .capitalize()
# Devuelve una copia de la cadena con la primera letra en mayúscula.
copia_cadena = CADENA.capitalize()
print(CADENA)
print(copia_cadena)

# .upper()
# Devuelve una copia de la cadena con todas las letras en mayúscula.
copia_cadena = CADENA.upper()
print(CADENA)
print(copia_cadena)

# .casefold()
# Devuelve una copia de la cadena en minúsculas.
copia_cadena = CADENA.casefold()
print(CADENA)
print(copia_cadena)

# .center()
# Devuelve una copia de la cadena con espacios en blanco centrados.
copia_cadena = CADENA.center(20)
print(CADENA)
print(copia_cadena)

# .count()
# Devuelve el número de veces que aparece una subcadena en una cadena.
count_character = CADENA.count("o")
print(CADENA)
print(count_character)

count_character = CADENA.count("m", 0, 12)
print(count_character)

# .encode()
# Devuelve una cadena codificada en bytes.
copia_cadena = CADENA.encode(encoding="utf-8")
print(CADENA)
print(copia_cadena)

# .endswith()
# Devuelve True si la cadena termina con la subcadena dada, False en caso contrario.
end_o = CADENA.endswith("o")
print(CADENA)
print(end_o)

end = CADENA.endswith("o", 0, 2)
print(end)

# expandtabs()
# Devuelve una copia de la cadena con tabulaciones expandidas.
copia_cadena = "\tHola\tmundo\tTabs".expandtabs(tabsize=6)
print(CADENA)
print(copia_cadena)

# .find()
# Devuelve la posición de la primera aparición de una subcadena en una cadena.
posicion = CADENA.find("amet")
print(CADENA)
print(posicion)

posicion = CADENA.find("lorem", 10, 15)
print(posicion)

# .format()
# Devuelve una cadena con los argumentos reemplazados.
cadena_formateada = "{} * {}".format("Hola", "mundo")
print(cadena_formateada)

# .format_map()
# Devuelve una cadena con los argumentos reemplazados.
cadena_formateada = "mi nombre es {nombre} {apellido}"\
    .format_map({"apellido": "Perez", "nombre": "Juan"})
print(cadena_formateada)

# .index()
# Devuelve la posición de la primera aparición de una subcadena en una cadena.
posicion = CADENA.index("amet")
print(CADENA)
print(posicion)

# posicion = CADENA.index("lorem", 10, 15)
# print(posicion)

# isalnum()
# Devuelve True si la cadena contiene sólo caracteres alfanuméricos, False en caso contrario.
isalnum = CADENA.isalnum()
print(CADENA)
print(isalnum)

print("115661156asdaasdae".isalnum())

# isalpha()
# Devuelve True si la cadena contiene sólo caracteres alfabéticos, False en caso contrario.
isalpha = CADENA.isalpha()
print(CADENA)
print(isalpha)

print("sdaasdae".isalpha())

# isdecimal()
# Devuelve True si la cadena contiene sólo caracteres numéricos, False en caso contrario.
isdecimal = CADENA.isdecimal()
print(CADENA)
print(isdecimal)

print(u"15".isdecimal())

# isdigit()
# Devuelve True si la cadena contiene sólo caracteres numéricos, False en caso contrario.
isdigit = CADENA.isdigit()
print(CADENA)
print(isdigit)

print("56456".isdigit())

# isidentifier()
# Devuelve True si la cadena es un identificador, False en caso contrario.
isidentifier = CADENA.isidentifier()
print(CADENA)
print(isidentifier)

print("mi_nombre_de_variable".isidentifier())

# islower()
# Devuelve True si la cadena contiene sólo caracteres en minúsculas, False en caso contrario.
islower = CADENA.islower()
print(CADENA)
print(islower)

print("hola".islower())

# isnumeric()
# Devuelve True si la cadena contiene sólo caracteres numéricos, False en caso contrario.
isnumeric = CADENA.isnumeric()
print(CADENA)
print(isnumeric)

print("156464".isnumeric())

# isprintable()
# Devuelve True si la cadena contiene sólo caracteres imprimibles, False en caso contrario.
isprintable = CADENA.isprintable()
print(CADENA)
print(isprintable)

print("\t".isprintable())

# isspace()
# Devuelve True si la cadena contiene sólo caracteres de espacio, False en caso contrario.
isspace = CADENA.isspace()
print(CADENA)
print(isspace)

print("\r".isspace())

# istitle()
# Devuelve True si la cadena contiene sólo caracteres de título, False en caso contrario.
istitle = CADENA.istitle()
print(CADENA)
print(istitle)

print("Mi Nombre".istitle())

# isupper()
# Devuelve True si la cadena contiene sólo caracteres en mayúsculas, False en caso contrario.
isupper = CADENA.isupper()
print(CADENA)
print(isupper)

print("HOLA".isupper())

# join()
# Devuelve una cadena con una lista de elementos separados por un separador.
cadena_join = ",".join(["Hola", "mundo", "tabs"])
print(cadena_join)

# ljust()
# Devuelve una copia de la cadena con el número de caracteres especificado a la izquierda.
cadena_ljust = 'hola mundo'.ljust(30, '*')
print(cadena_ljust)

# lower()
# Devuelve una copia de la cadena en minúsculas.
cadena_lower = CADENA.lower()
print(CADENA)
print(cadena_lower)

# .lstrip()
# Devuelve una copia de la cadena con los espacios iniciales eliminados.
espaciado = "    hola mundo    "
cadena_lstrip = espaciado.lstrip()
print(CADENA)
print(cadena_lstrip)

# rstrip()
# Devuelve una copia de la cadena con los espacios finales eliminados.
espaciado = "    hola mundo    "
cadena_rstrip = espaciado.rstrip()
print(CADENA)
print(cadena_rstrip)

# .strip()
# Devuelve una copia de la cadena con los espacios iniciales y finales eliminados.
espaciado = "    hola mundo    "
cadena_strip = espaciado.strip()
print(CADENA)
print(cadena_strip)

# .partition()
# Devuelve una tupla con la cadena partida en dos partes, la primera hasta el primer caracter de separación, y la segunda parte.
cadena_partition = '15 + 15 =  15 + 15'.partition("+")
print(CADENA)
print(cadena_partition)

cadena_partition = '15 + 15 =  15 + 15'.partition("/")


# .removeprefix()
# Elimina el prefijo de una cadena.
cadena_removeprefix = "hola mundo".removeprefix("hola")
print(CADENA)
print(cadena_removeprefix)

print("hola".removeprefix("h"))

# .removesuffix()
# Elimina el sufijo de una cadena.
cadena_removesuffix = "hola mundo desde python".removesuffix("python")
print(CADENA)
print(cadena_removesuffix)

print("hola".removesuffix("a"))

# .replace()
# Devuelve una copia de la cadena con todas las apariciones de una subcadena reemplazadas por otra subcadena.
cadena_replace = "hola mundo".replace("hola", "HOLA!!")
print(CADENA)
print(cadena_replace)

# .rfind()
# Devuelve la posición de la última aparición de una subcadena en una cadena.
cadena_rfind = "hola mundo".rfind("o")
print(CADENA)
print(cadena_rfind)

# .rindex()
# Devuelve la posición de la última aparición de una subcadena en una cadena.
cadena_rindex = "hola mundo".rindex("o")
print(CADENA)

# .rjust()
# Devuelve una copia de la cadena con el número de caracteres especificado a la derecha.
cadena_rjust = 'hola mundo'.rjust(30, '*')
print(CADENA)
print(cadena_rjust)

# .rpartition()
# Devuelve una tupla con la cadena partida en dos partes, la segunda parte hasta el último caracter de separación, y la primera parte.
cadena_rpartition = '15 + 15 =  15 + 15'.rpartition("+")
print(CADENA)
print(cadena_rpartition)

print("15 + 15 =  15 + 15".rpartition("/"))

# .split()
# Devuelve una lista con las subcadenas separadas por un separador.
cadena_split = "h o l a m u n d o".split(" ", maxsplit=2)
print(CADENA)
print(cadena_split)

# rsplit()
# Devuelve una lista con las subcadenas separadas por un separador.
cadena_rsplit = "h o l a m u n d o".rsplit(" ", maxsplit=2)
print(CADENA)
print(cadena_rsplit)


# .splitlines()
# Devuelve una lista con las líneas de una cadena.
cadena_splitlines = "hola\nmundo hola\nmundo".splitlines(keepends=False)
print(CADENA)
print(cadena_splitlines)

# .startswith()
# Devuelve True si la cadena comienza con la subcadena especificada, False en caso contrario.
cadena_startswith = "hola mundo".startswith("hola")
print(CADENA)
print(cadena_startswith)

# .swapcase()
# Devuelve una copia de la cadena en minúsculas o mayúsculas, dependiendo de si la cadena ya está en minúsculas o en mayúsculas.
cadena_swapcase = CADENA.swapcase()
print(CADENA)
print(cadena_swapcase)

# title()
# Devuelve una copia de la cadena con todas las palabras en minúsculas y las palabras que comienzan con mayúscula en mayúsculas.
cadena_title = "hola mundo".title()
print(CADENA)
print(cadena_title)

# translate()
# Devuelve una copia de la cadena con todas las apariciones de una subcadena reemplazadas por otra subcadena.
traslate_table = str.maketrans("abcdefghijklmnopqrstuvwxyz,", "4BCDEFGHIJKLMNOPQRSTUVWXYZ*")
copia_cadena = 'hi, this is a message'.translate(traslate_table)
print(CADENA)
print(copia_cadena)


# zfill()
# Devuelve una copia de la cadena con el número de caracteres especificado a la izquierda.
cadena_zfill = "15".zfill(10,)


