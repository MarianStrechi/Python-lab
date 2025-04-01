#2)
# Lista inițială de tupluri
tuples_list = [(3, 11), (1, 7), (7, 8), (16, 88), (23, 15), (5, 2), (10, 20)]

# Sortăm lista după al doilea element din fiecare tuplu
sorted_list = sorted(tuples_list, key=lambda x: x[1])

# Afișare
print(sorted_list)

#3)
#Filtrarea numerelor pare dintr-o listă
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) #filter(lambda x: x % 2 == 0, numbers) → filtrează doar numerele pare (x % 2 == 0). list(filter(...)) → convertește rezultatul într-o listă.

print(even_numbers) 

#4) a)
#Fără parametri
def greet():
    print("Hello! Welcome to hotel")

greet() 


#Cu parametri
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")  

#Cu parametri predefiniți
def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

greet_with_default()      
greet_with_default("Tom")  


#4 b)
#Cu return

def square(x):
    return x ** 2

result = square(5)  
print(result)


#Fara return

def show_square(x):
    print(f"Square of {x} is {x ** 2}")

show_square(5)  



#5
#Cu parametri: Calculul ariei unui dreptunghi

def rectangle_area(length, width):
    return length * width

area = rectangle_area(5, 10)
print(f"Area of the rectangle is {area}") 



#Fara return, cu parametru predefenit: Afișarea unui mesaj pentru utilizator

def welcome_message(user="Guest"):
    print(f"Welcome, {user}! Have a great day!")

welcome_message()        
welcome_message("Alex")  


#Cu return și cu parametru: Sumarea numerelor dintr-o listă

def sum_list(numbers):
    return sum(numbers)

nums = [1, 2, 3, 4, 5]
total = sum_list(nums)
print(f"Sum is {total}")  









