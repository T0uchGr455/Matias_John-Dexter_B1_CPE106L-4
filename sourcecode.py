age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age. Please enter a valid age.")
elif age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")