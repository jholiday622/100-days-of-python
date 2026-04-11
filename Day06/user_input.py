# Day 06 - User Input
# 100 Days of Python - jholiday622

# Build a personal intro program
name = input("Enter your name: ")
age = int(input("Enter your age: "))
years_experience = int(input("Years of experience: "))
goal = int(input("Income goal $: "))
months = int(input("Months to reach goal: "))

print(f"\n--- My Profile ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Experience: {years_experience} years")
print(f"Goal: ${goal} in {months} months")
print(f"Monthly target: ${goal // months}")
print(f"Daily target: ${goal // months // 20}")