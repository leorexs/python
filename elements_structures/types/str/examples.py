# Tipos cadenas de caracteres

vocal = "u"
print(vocal, type(vocal))

cadena_caracteres = 'aeio'
print(cadena_caracteres, type(cadena_caracteres))

cadena_palabra = "Hola mundo"
print(cadena_palabra, type(cadena_palabra))

comillas_simples = 'cadena de "caracteres" en comillas simples'
print(comillas_simples, type(comillas_simples))

comillas_dobles = "cadena de 'caracteres' en comillas simples"
print(comillas_dobles, type(comillas_dobles))

comillas_tiples = """ cadenas de '''caracteres '''"""
print(comillas_tiples, type(comillas_tiples))

# Formateo %-string
print('formateo: %s * %s =  %s ' % (15, 2, 30))

# Formateo por método de str
print('formateo por metodo: {} +  {} = {} '.format(9, 9, 18))

# Formateo: f-string
num_a, num_b, = 5, 9
print(f'formateo por metodo: {num_a} *  {num_b} = {num_a * num_b} ')

# Formato por Template
# url: https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting

print('%(msg_1)s otro' % {'msg_1': "este es un mensaje"})
