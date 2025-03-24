# -*- coding: utf-8 -*-
"""
Spyder Editor

MOLSSI Workshop Practice Script
Lesson 1
"""

deltaH = -541.5 #kJ/mole
deltaS =  10.4     #kJ/(mole K)
temp = 298      #Kelvin
deltaG = deltaH - temp * deltaS

#printing value
print(deltaG)

# assigning multiple values at once
deltaH, deltaS, temp = -541.5, 10.4, 298
deltaG = deltaH - temp * deltaS
print(deltaG)

# data types and changing them
type(deltaG)

deltaG_string = str(deltaG)
print(type(deltaG_string))

# Lists
energy_kcal = [-13.4, -2.7, 5.4, 42.1]
energy_length = len(energy_kcal)         # determining length
print('The length of this list is', energy_length)

#print first element on list
print(energy_kcal[0])

#converting units
energy_kilojoules = energy_kcal[1] * 4.184
print(energy_kilojoules)

#slicing
short_list = energy_kcal[0:2]
print(short_list)

# for loops
for number in energy_kcal:
    kJ = number * 4.184
    print(kJ)


# saving to new list by using append
energy_kJ=[]
for number in energy_kcal:
    kJ = number * 4.184
    energy_kJ.appened(kJ)
    
print(energy_kJ)


# logic statements
negative_energy_kJ = []

for number in energy_kJ:
    if number < 0:
        negative_energy_kJ.append(number)

print(negative_energy_kJ)

negative_numbers = []
for number in energy_kJ:
    if number < 0 or number == 0:
        negative_numbers.append(number)

print(negative_numbers)














