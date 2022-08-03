from clases import (
    MiClaseDefinida,
    MiClaseDefinida2,
    MiClaseDefinida3,
)


mi_clase_definida = MiClaseDefinida()
mi_clase_definida2 = MiClaseDefinida2()
mi_clase_definida3 = MiClaseDefinida3("instancia")


# Verificaciones de tipo de dato
print(type(mi_clase_definida))
print(type(mi_clase_definida2))
print(type(mi_clase_definida3))


# A que modulo pertenecen las clases
print(mi_clase_definida.__module__)
print(mi_clase_definida2.__module__)

# Que clase hereda
print(mi_clase_definida.__class__)
print(mi_clase_definida2.__class__)


# manipulaciones
print(mi_clase_definida2.atributo_de_clase)
mi_clase_definida2.cambiar_atributo("un valor nuevo")
print(mi_clase_definida2.obtener_atributo())

# print(mi_clase_definida3.__atributo_de_clase)
mi_clase_definida3.cambiar_atributo_clase("otro valor nuevo")
print(mi_clase_definida3.obtener_atributo_clase())

# print(mi_clase_definida3._atributo_de_instancia)
mi_clase_definida3.cambiar_atributo_instancia("valor nuevo")
print(mi_clase_definida3.obtener_atributo_instancia())


mi_object = object.__new__(MiClaseDefinida3)
print(mi_object.obtener_atributo_clase())
print(mi_object.__dict__)
# print(mi_object.obtener_atributo_instancia())
mi_object.__init__('instancia')
print(mi_object.obtener_atributo_instancia())
print(mi_object.__dict__)

# # getter y setter

mi_clase_definida3.atributo_de_instancia = "valor por setter"
print(mi_clase_definida3.atributo_de_instancia)

print(mi_clase_definida3.__dict__)


