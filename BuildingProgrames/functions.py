def greet():
    print("Hello, welcome to the program!")
    #pass
greet()

def saygoodbye():
    print("Goodbye, see you later!")
    #call it multipletimes
saygoodbye()    
saygoodbye()
saygoodbye()

def checkweather():
    temp=25
    if temp > 30:
        print("It's hot outside!")
    
    else:
        print("The weather is pleasant."    )
        
checkweather()  # Example usage of checkweather function with temperature 35

#without parameters(inflexible)
def greetLeela():
    print("Hello Leela, welcome to the program!")

def greet(first_name, Last_name):
    print(f"Hello {first_name} {Last_name}, welcome to the program!")

greet(first_name="Welcome Gayathri", Last_name="KM")  # Example usage of greet function with parameters

greetLeela()  # This will raise an error because greetLeela does not accept any parameters

def calculate(price,taxrate,discount):
    tax=price*taxrate
    finalPrice=price+tax-discount
    print(f"The final price is: {finalPrice}")
    
calculate(price=100, taxrate=0.1, discount=5)  # Example usage of calculate function with parameters

#with parameters(flexible)
discount=10
def calculateTotal(price):
    
    #default Values
    tax_rate=0.1
    
    #calculation
    discount=10
    tax=price*tax_rate
    finalPrice=price+tax-discount
    
    #print the final price
    print(f"The final price is: {finalPrice}")
    
calculateTotal(price=100)  # Example usage of calculateTotal function with parameters


#Return Operations
def add_print(a, b):
    #result=a+b
    #print(f"The sum is: {result}")
    print(a+b)
add_print(a=5,b= 3) 
# Example usage of add_print function with parameters
def add_return(a, b):
    return a+b
result = add_return(a=5, b=3)
print(f"The returned sum is: {result}")


#def calculate_area(width,height)
