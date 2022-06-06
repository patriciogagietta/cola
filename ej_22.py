""" Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino

F) por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
b. mostrar los nombre de los superhéroes femeninos;
c. mostrar los nombres de los personajes masculinos;
d. determinar el nombre del superhéroe del personaje Scott Lang;
e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
con la letra S;
f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
de superhéroes. """

from cola import Cola

class PersonajesMCU (object):
    def __init__ (self, nombre_personaje, nombre_superheroe,genero):
        self.nombre_personaje = nombre_personaje
        self.nombre_superheroe = nombre_superheroe
        self.genero = genero

cola_personajes = Cola()

personaje = PersonajesMCU("carol danvers","capitana marvel","f")
cola_personajes.arribo(personaje)
personaje = PersonajesMCU("tony Stark", "iron Man", "m")
cola_personajes.arribo(personaje)
personaje = PersonajesMCU("steve rogers", "capitán america", "m")
cola_personajes.arribo(personaje)
personaje = PersonajesMCU("scott lang", "ant man", "m")
cola_personajes.arribo(personaje)


for i in range(cola_personajes.tamanio()):
    x = cola_personajes.mover_al_final()

    #a
    if (x.nombre_superheroe == "capitana marvel"):
        print("Nombre de la capitana marvel: " ,x.nombre_personaje)

    #b
    if (x.genero == "f"):
        print("Nombres de los personajes femeninos: " ,x.nombre_personaje)

    #c
    if (x.genero == "m"):
        print("Nombres de los personajes masculinos: " ,x.nombre_personaje)
    
    #d
    if (x.nombre_personaje == "scott lang"):
        print("Nombre del superhéroe del personaje Scott Lang: " ,x.nombre_superheroe)

    #e
    if (x.nombre_personaje[0] == "s"):
        print("Datos de los personajes que empiezan con la letra S: " ,x.nombre_personaje, x.nombre_superheroe, x.genero)

    if (x.nombre_superheroe[0] == "s"):
        print("Datos de los superheroes que empiezan con la letra S: " ,x.nombre_personaje, x.nombre_superheroe, x.genero)

    #f
    if (x.nombre_personaje == "carol danvers"):
        print("Nombre de superheroe del personaje carol denvers: " ,x.nombre_superheroe)
