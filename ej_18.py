""" Dada una cola con los códigos de turnos de atención (con el formato #@@@, donde # es una
letra de la A hasta la F y “@@@” son tres dígitos desde el 000 al 999), desarrollar un algoritmo
que resuelva las siguientes situaciones:
a. cargar 1000 turnos de manera aleatoria a la cola.
b. separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la letra A, C
y F, y la cola_2 con el resto de los turnos (B, D y E).
c. determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las letras
tiene mayor cantidad.
d. mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de turno sea
mayor que 506. """

from cola import Cola

class turnosAtencion (object):
    def __init__(self,letra,numeros):
        self.letra = letra
        self.numeros = numeros

cola_turnos = Cola()
cola_1 = Cola()
cola_2 = Cola()


turno = turnosAtencion("a",800)
cola_turnos.arribo(turno)
turno = turnosAtencion("b",999)
cola_turnos.arribo(turno)
turno = turnosAtencion("c",666)
cola_turnos.arribo(turno)
turno = turnosAtencion("d",981)
cola_turnos.arribo(turno)
turno = turnosAtencion("e",222)
cola_turnos.arribo(turno)
turno = turnosAtencion("f",111)
cola_turnos.arribo(turno)
turno = turnosAtencion("f",333)
cola_turnos.arribo(turno)


for i in range(cola_turnos.tamanio()):
    x = cola_turnos.mover_al_final()

    #punto b
    if (x.letra[0] == "a" or x.letra[0] == "c" or x.letra[0] == "f"):
        cola_1.arribo(x)

    if (x.letra[0] == "b" or x.letra[0] == "d" or x.letra[0] == "e"):
        cola_2.arribo(x)

#punto c
if (cola_1.tamanio() > cola_2.tamanio()):
    print("la cola 1 tiene mayor cantidad de turnos")
    #punto d
    for i in range(cola_2.tamanio()):
        x = cola_2.mover_al_final()
        if (x.numeros > 506):
            print("turno de la cola con menor cantidad de elementos, cuyo número de turno sea mayor que 506: " ,x.letra, x.numeros)   
else:
    if (cola_2.tamanio() > cola_1.tamanio()):
        print("la cola 2 tiene mayor cantidad de turnos")
        #punto d
        for i in range(cola_1.tamanio()):
            x = cola_1.mover_al_final()
            if (x.numeros > 506):
                print("turno de la cola con menor cantidad de elementos, cuyo número de turno sea mayor que 506: " ,x.letra,x.numeros)


print()
#barrido cola turnos
print("barrido cola turnos")
for i in range(cola_turnos.tamanio()):
    x = cola_turnos.mover_al_final()
    print(x.letra,x.numeros)


print()
#barrido cola 1
print("barrido cola 1")
for i in range(cola_1.tamanio()):
    x = cola_1.mover_al_final()
    print(x.letra,x.numeros)


print()
#barrido cola 2
print("barrido cola 2")
for i in range(cola_2.tamanio()):
    x = cola_2.mover_al_final()
    print(x.letra,x.numeros)
