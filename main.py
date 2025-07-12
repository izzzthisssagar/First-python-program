# This my first Python script
print("momo")
print("its really good")



# Variables and formatted strings
first_name = "Sagar"
food = "momo"
email = "sagarthapa2058@gmail.com"
print(f" hello {first_name}, I like {food}")
print(f" You can contact me at {email}") 

#integers
age = 23
quantity = 3
number_of_students = 34
print(f" I am {age} years old")
print(f"you are buying {quantity} plates of {food} from me")
print(f"there are {number_of_students} students in the class")


# Floats 
price = 100.50
gpa = 2.95
distance = 12.5
print(f"the price of {food} is {price} rupees")
print(f"my gpa is {gpa}")
print(f"the distance from my home to college is {distance} km")

# Booleans
is_student = True
for_sale = False
is_online = True
print(f" Are you a student? {is_student}")
print(f" Is the food for sale? {for_sale}")  
print(f" Is the class online? {is_online}")


#typecasting

name = "Sagar"
age = 23
gpa = 2.95
is_student = True


print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))
#type function is used to check the type of variable , it returns the type of the object.                             


gpa = int(gpa)  # converting float to int
age = str(age)  # converting int to str
age = float(age)  # converting str to float

name = bool(name)  # converting str to bool
print (name)  # will print True because non-empty string is considered True



# Input from user
# input function is used to take input from the user, it returns a string
# you can convert the input to int, float, bool or any other type as per your requirement
name = input("what is your name?")  # this will take input from the user
print(f"Hello {name}, welcome to the Python world!")  # this will print the name entered by the user

age = input("How old are you?")  # this will take input from the userer
print(f"You are {age} years old!")  # this will print the age entered by the user

