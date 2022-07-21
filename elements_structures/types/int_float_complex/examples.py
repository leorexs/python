# Type int() from Built-in Types

# Variables

# Tipos de datos numéricos
numero_entero = 10
numero_flotante = 17.15
numero_complejo = 3 + 5j

print('numero_entero', type(numero_entero))  # 10 <class 'int'>
print('numero_flotante', type(numero_flotante))  # 17.15 <class 'float'>
print('numero_complejo', type(numero_complejo))  # (3+5j) <class 'complex'>

numero_entero = int(numero_flotante)
numero_flotante = float(numero_entero)
numero_complejo = complex(15, 5)

print('numero_entero', type(numero_entero))  # 17 <class 'int'>
print('numero_flotante', type(numero_flotante))  # 17.0 <class 'float'>
print('numero_complejo', type(numero_complejo))  # (15+5j) <class 'complex'>


# Operadores Aritméticos
a = 35
b = 5

# Adición
print(a + b)  # 40

# Sustracción
print(a - b)  # 30

# Multiplicación
print(a * b)  # 175

# División
print(a / b)  # 7.0

# Módulo
print(a % b)  # 0

# Exponenciación
print(a ** b)  # 52521875

# División entera
print(a // b)  # 7


# Función que devuelve una parte enter y el residuo
print(divmod(15,6))

# Función que devuelve el valor o magnitud
print(abs(-5))

# Función que devuelve la potencia
print(pow(5, 5))
