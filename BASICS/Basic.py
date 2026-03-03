is_true=True

age=18

#can_vote=age>18
#print(can_vote)

is_18=age==18
print(is_18)
print(age!=12)

#print(2+3)*4

myAge=25
hasLicense=True

can_Drive=myAge>=16 and hasLicense
print(can_Drive)    

day="Mondayday"
is_weekend=day=="Saturday" or day=="Sunday"
print(is_weekend)   

is_adult=age>=18
is_child=not is_adult
print(is_child)

score=10

score=score+5
score+=5
print(score)    

name="Leela"
string=f"Hello {name}" 
print(string)   

myfullname="Leelavathi KM"
print(myfullname[1])

myfullname.lower()
print(myfullname.lower())
print(myfullname.upper())

sentence="Python is great"
print(sentence.split()) 
sentence.title()
print(sentence.title())

#If Condition

temperature=30
if temperature>25:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature>20:
    print("It's a nice day")
elif temperature>15:
    print("It's a bit cold")
else:
    print("It's cold")
print("Done") 

childage=12
hasLicense=True

if childage>=18 and hasLicense:
    print("You can drive")      
else:
    print("You cannot drive")
    
    hasTicket=True
    watchAge=15
    
    if hasTicket:
        if watchAge>=18:
            print("You can watch")
        else:
            print("You cannot watch")  
    else: 
        print("Please Buy a Ticket") 