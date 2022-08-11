# objective : asks user for his name and say hello

name = input("What is your name? ")
age = int(input("How old are you? "))

#normal way
print("Hello", name, "you are", age, "years old")

# f-string 
print(f"Hello {name}, you are {age} years old")

# f-string more example

print(5+5)
print(f"{5+5}")