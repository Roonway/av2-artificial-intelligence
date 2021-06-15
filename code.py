import random
import numpy as num
import math

# Roney Joab Lemos Mendes - 201751091783

# Funções de criar os parâmetros

def createIdeals():
    return num.random.random((10))

def createWeights():
    arrayWeights = []
   
    for num in range(10) :
        arrayWeights.append(num.random.random((10)))

    return arrayWeights
    
def createInputData():
    return num.random.random((10))


# Funções de manipulação

def cost(results,ideals):
    totalCost = 0
    i = 0
    for result in results:
        totalCost += math.pow((result + ideals[i]), 2)
        i += 1
    totalCost = round(totalCost, 2)

    return totalCost
    
def summation(inputs,weights):
    result = 0
    i = 0

    for inputData in inputs:
        result += inputData * weights[i]
        i += 1
        
    return result

def weightAdjustment(inputs, results):
    newWeights = []
    for result in results:
        weight = num.random.random((10))
        newResult = summation(inputs, weight)
        while result < newResult:
            weight = num.random.random((10))
            newResult = summation(inputs, weight)
        newWeights.append(weight)
    return newWeights


#Main

def main ():
    
    arrayWeights = createWeights()
    inputs = createInputData()
    ideals = createIdeals()
    
    idealCost = 62
    
    results = []
    
    for weights in arrayWeights:
        results.append(summation(inputs,weights))
        
    currentCost = cost(results, ideals)
    newWeights = weightAdjustment(inputs, results)

    secondsResults = []

    for weight in newWeights:
        secondsResults.append(summation(inputs,weight))
        
    newCost = cost(secondsResults, ideals)
    
    i = 0
    while newCost > idealCost:
        newWeights = weightAdjustment(inputs, secondsResults)
        thirdResults = []

        for newWeight in newWeights:
            thirdResults.append(summation(inputs,newWeight))
            
        newCost = cost(thirdResults, ideals)
        
        print("A iteração número {i} tem valor de custo equivalente a {newCost}")
        i +=1
    
    print("O referente ao custo antigo é ", currentCost)
    print("O referente ao novo custo é ", newCost)
    
main()