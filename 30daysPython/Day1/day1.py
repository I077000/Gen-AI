# Day1 Excersise

""" Excersise 1 :Write strings on the python interactive shell. The strings are the following:
    Your name
    Your family name
    Your country
    I am enjoying 30 days of python
"""
import math
from operator import truediv


name = "shrijan"
lastName = "Shrivastav"
country = "India"
thought = "I am enjoying 30days of python"
print(name)
print(lastName)
print(country)
print(thought)
print("Total human description"+ "name is: "+ name + " country is  " +country)

"""
Excersise 2:
Check the data types of the following data:
10
9.8
3.14
4 - 4j
['Asabeneh', 'Python', 'Finland']
Your name
Your family name
Your country

"""

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['x','y','z']))
print(type(name))

"""
Excersise 3:
Write an example for different Python data types such as 
Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
"""

intdatatype = 3
floatdatatype = 3.4
complexDataType = (3+4j) #only j is allowed
stringDataType = "shrijan"
booleanDataType = False
booleanDataType1 = True
listDataType = ["sh","fg","fr",2.3,1,4+3j]
tupleDataType = ('sh',3.3,'ed')
setDataType = {'sh',3.2,3.2,4,'sh'}
dictDataType ={"key":"sh","id":555}
print(type(listDataType))
print(type(tupleDataType))
print(type(setDataType))
print(type(dictDataType))
print(dictDataType)

"""
Excersise 3:
Find an Euclidian distance between (2, 3) and (10, 8)
"""

p1 = 2
q1 = 3
p2 = 10
q2 = 8
## Eucleadiam Distance = Sqrroot of (p1-p2)^2+(q1-q2)^2

## Using Basic Math Function

diff1 = (p2-p1)
diff2 = (q2-q1)
euddistance1 = math.sqrt(math.pow(diff1,2)+ math.pow(diff2,2))
print(euddistance1)

## Using math inbuilt function

euddistance2 = math.dist((2,3),(10,8))
print(euddistance2)
