# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 16:57:12 2017

@author: 
"""

#define a class representing foods
class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
        
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories
    
    def density(self):
        return self.getValue()/self.getCost()
    
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                + ', ' + str(self.calories) + '>'

#build a menu of type Food
def buildMenu(names, values, calories):
    """names, values, calories are lists of same length.
       name a list of strings
       values and calories lists of numbers
       returns list of Foods"""
       
    menu = []
    for i in range(len(values)):
       menu.append(Food(names[i], values[i], calories[i]))
       
    return menu

#greedy algorithm to solve knapsack problem
def greedy(items, maxCost, keyFunction):
    """Assumes items in a list, maxCost >= 0,
       keyFunction maps elements of items to numbers"""
       
       #get a copy of items sorted by the keyFunction passed in.  Allows
       #for flexibility in determining how to rank the items (cost, cals, etc)
       #Will sort in descending order, so most valueable item comes first
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0
       
    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
               
    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken = ', val)
    for item in taken:
        print(' ', item)
        
def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate ', maxUnits, ' calories')
    testGreedy(foods, maxUnits, Food.getValue) #NOT Food.getValue() because
                                               #the third parameter must be 
                                               #a function.
    
    print('\nUse greedy by cost to allocate ', maxUnits, ' calories')
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    
    print('\nUse greedy by density to allocate ', maxUnits, ' calories')
    testGreedy(foods, maxUnits, Food.density)
    
names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 
         'cake']

values = [89,90,95,100,90,79,50,10]

calories = [123,154,258,354,365,150,95,195]

foods = buildMenu(names, values, calories)
testGreedys(foods, 750)