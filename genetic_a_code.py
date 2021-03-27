import numpy as np
import random
import secrets

popuNum = 4 #numero de personas que conformarán la poblacion

class Person:
  def __init__(self):
      self.chromosome = np.random.randint(2, size=8) #una persona tiene un cromosoma de 8 genes, aleatoriamente 0s y 1s
      self.fitness = self.fitnessFunction() #tiene fitness que se calcula con fitnessFFunction y depende del numero de 1s que tenga su cromosoma
      self.numberxd = 0 #numero de persona, se definirá cuando se inicialice la poblacion


  def fitnessFunction(self): #funcion para obtener el fitness de una persona
      contador = 0
      i = 0
      while i < 8:
          if self.chromosome[i] == 1:
              contador = contador + 1
          i += 1
      return contador

def redefineFitness(population): #funcion para obtener el fitness de una persona
    longitud = len(population)
    uwu = 0  # contador del ciclo while
    while uwu < longitud:
        contador = 0
        i = 0
        while i < 8:
            if population[uwu].chromosome[i] == 1:
                contador = contador + 1
            i += 1
        population[uwu].fitness = contador
        uwu += 1


def createPopulation(numPersonas): #creamos la poblacion
    popu = [] #lista que almacenará la poblacion
    auxPersona = None #auxiliar que ayudará a meter a cada pesona a la poblacion

    uwu = 0 #contador del ciclo while
    while uwu < numPersonas:
        auxPersona = Person()
        auxPersona.numberxd = uwu
        popu.append(auxPersona) #añadimos a la persona a la poblacion
        uwu += 1
    return popu #retornamos a la población generada

def printPopu(population,popuNum): #imprimimos a la poblacion
    unu = 0
    while unu < popuNum:
        print(population[unu].chromosome)
        unu += 1

def printPopuFitness(population,popuNum):
    unu = 0
    while unu < popuNum:
        print(population[unu].fitness)
        unu += 1

def printPopuNumber(population,popuNum):
    unu = 0
    while unu < popuNum:
        print(population[unu].numberxd)
        unu += 1

def eliminarInadaptados(population): #vamos a eliminar los 2 individuos con el menor fitness y agregar 2 nuevos aleatorios
    x = 0
    while x < 2:
        listafitness = [] #lista que contendrá al fitnes de todas las personas de la poblacion
        element = 0   #auxiliar que contendrá la posición del elemento con el menor fitness
        posicion = 0 #para inicializar el ciclo
        while posicion < len(population): #ciclo que recorre a toda la lista de la población
            listafitness.append(population[posicion].fitness) #añadimos el fitness de cada elemento a la lista
            posicion = posicion + 1

        minVal = min(listafitness) #obtenemos el mínimo de la lista

        for i in range(len(listafitness)): #buscamos la posición del mínimo de la lista
            if listafitness[i] == minVal: #cuando encontramos su posición
                element = i #guardamos el valor de esa posición
                break
        population.pop(element)
        x += 1


    #nuevo ciclo para añadir a los 2 nuevos elementos a la población
    i = 0
    while i < 2:
        auxperson = Person()
        population.append(auxperson)  # añadimos a la persona a la poblacion
        i += 1


    #ahora tenemos que redefinir el numberxd y el fitness de cada elemento de la población
    longitud = len(population)
    uwu = 0  # contador del ciclo while
    while uwu < longitud:
        population[uwu].numberxd = uwu
        uwu += 1



def rouletteWheel(population, popuNum): #usamos la roulette wheel en la poblacion
    roulette = [] #esta lista contendrá el numero de persona n veces dependiendo de su fitness
    #por ejemplo, una persona con un fitness de 6 aparecerá su número de persona 6 veces en esta lista
    n = 0 #auxiliar para el numero de la persona
    f = 0 #auxiliar para el fitness de la persona

    unu = 0
    while unu < popuNum:
        n = population[unu].numberxd
        f = population[unu].fitness
        aux = 0
        while aux < f:
            roulette.append(n)
            aux += 1
        unu += 1
    #print(roulette)
    #random.shuffle(roulette) #reacomodamos la lista aleatoriamente
    #print(roulette)
    return roulette

def crossover(population, roulette):
    newPopulation = []
    hijo = Person()


    #print("ruleta inicial")
    #print(roulette)
    person1 = secrets.choice(roulette)
    #print("persona 1")
    #print(person1)
    #ahora hacemos un ciclo while para quitar a la persona 1 de la ruleta, lo hacemos en un ciclo ya que puede aparecer varias veces
    posicion = 0
    while posicion < len(roulette):
        if roulette[posicion] == person1:
            roulette.pop(posicion)
        else:
            posicion = posicion + 1
    #print("ruleta quitando persona 1")
    #print(roulette)

    #ahora si podemos encontrar a la persona 2 con quien aparearse
    person2 = secrets.choice(roulette)
    #print("persona 2")
    #print(person2)

    #tambien eliminamos a la persona 2 de la ruleta
    posicion = 0
    while posicion < len(roulette):
        if roulette[posicion] == person2:
            roulette.pop(posicion)
        else:
            posicion = posicion + 1
    #print("ruleta quitando persona 2")
    #print(roulette)

    """
    print("mami 1")
    print(population[person1].chromosome)
    print("mami 2")
    print(population[person2].chromosome)
    """

    #HIJO 1
    aux0 = 0  # auxiliar del ciclo while 1
    aux1 = 4  # auxiliar del ciclo while 2
    while aux0 < 4:
        hijo.chromosome[aux0] = population[person1].chromosome[aux0]
        aux0 += 1
    while aux1 < 8:
        hijo.chromosome[aux1] = population[person2].chromosome[aux1]
        aux1 += 1
    #print("hijo1 antes de append")
    #print(hijo.chromosome)
    hijo.fitness = hijo.fitnessFunction()
    newPopulation.append(hijo)

    #HIJO 2
    aux2 = 4
    aux3 = 0
    while aux2 < 8:
        hijo.chromosome[aux2] = population[person1].chromosome[aux2]
        aux2 += 1
    while aux3 < 4:
        hijo.chromosome[aux3] = population[person2].chromosome[aux3]
        aux3 += 1
    #print("hijo2 antes de append")
    #print(hijo.chromosome)
    hijo.fitness = hijo.fitnessFunction()
    newPopulation.append(hijo)
    return newPopulation




def mainuwu():
    population = createPopulation(popuNum)
    print("orig")
    printPopu(population,popuNum)
    eliminarInadaptados(population)
    print("new")
    printPopu(population,popuNum)
    r = rouletteWheel(population,popuNum)
    print("cross")
    n = crossover(population, r)
    printPopu(n,popuNum-2)

mainuwu()

#print(population[0].chromosome)
#print(population[0].chromosome[0])

