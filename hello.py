from datetime import datetime
name = input("What is your name? ")
print(f"Hello, {name}!")
print("Welcome to GitHub!")
print("I made my first commit!")

birth_year = int(input("What year were you born? "))
current_year = datetime.now().year

age = current_year - birth_year

print(f"You are approximately {age} years old.")
