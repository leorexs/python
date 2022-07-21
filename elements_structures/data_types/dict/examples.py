# Diccionarios

persona_1 = {
  "Nombre": "Juan",
  "Edad": 27,
  "Cédula": 2103882
}
print(persona_1)            # {'Nombre': 'Juan', 'Edad': 27, 'Cédula': 2103882}

persona_2 = dict([
      ('Nombre', 'Pepe'),
      ('Edad', 18),
      ('Cédula', 1004582),
])
print(persona_2)            # {'Nombre': 'Pepe', 'Edad': 18, 'Cédula': 1004582}

persona_3 = dict(
    Nombre='Sandra',
    Edad=20,
    Cédula=2503882
)
print(persona_3)            # {'Nombre': 'Sandra', 'Edad': 20, 'Cédula': 2503882}
