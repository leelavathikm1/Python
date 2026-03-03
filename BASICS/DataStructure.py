age=25
hasLicence=False

myList=["Leela",25,age,True,hasLicence]

name=myList[0]
age=myList[1]   

hasLicence=myList[-3]
print(hasLicence)   

myList.append("Python")
print(myList)   
myList.insert(3,"KM")
print(myList)
myList.remove("Leela")
print(myList)

#List Methods

numbers=[1,2,3,4,5]
print(numbers)
numbers.append(6)
print(numbers)
numbers.insert(0,0)
print(numbers)
numbers.remove(3)
print(numbers)
numbers.pop()
print(numbers)
numbers.clear()
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(len(numbers))
print(numbers.count(1))
print(numbers.index(4))

#create a copy of list
newList=numbers.copy()
print(newList)

