#Empty Dictionariy
myDict={}

#dictionary with some key-value pairs
person={
    "name":"Leela",
    "age":25,
    "city":"New York"   
}

person["name"]="Gayathri"
person["license"]=True

del person["license"]

#Different ways to create a dictionary 
scores=dict(math=95, science=90, english=85)

print(person)
print(scores)

#Dictionary Methods
print(person.keys())
print(person.values())
print(person.items())


#check If Key Exists
if "name" in person:
    print("Name exists")
else:
    print("Name does not exist")    
    
#update Multiple Values
person.update({"age":26, "city":"Los Angeles"})

#Tuples
#Empty tuple
myTuple=()  

#Tuple with some values
fruits=("apple", "banana", "cherry")    
print(fruits[0])  
fruits[0]="orange"  #This will raise an error because tuples are immutable

#slicing
point=(2, 3, 4, 5, 6  )
print(fruits[1:3])  #Output: ('banana', 'cherry')       
print(point[0])
print(fruits[-1])  #Output: 'cherry'    


#creating sets
#empty set
mySet=set() 
#Set with some values
colors={"red", "green", "blue"}
print(colors)
colors.add("yellow")
print(colors)
colors.remove("red")
print(colors)
colors.clear()
print(colors)   

#remove duplicates from a list using set
numbers=[1, 2, 3, 2, 4, 1, 5]
uniqueNumbers=set(numbers)
print(uniqueNumbers)        