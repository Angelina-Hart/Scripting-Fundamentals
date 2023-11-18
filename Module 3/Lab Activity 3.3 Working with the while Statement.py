name = input("Enter your name: ")
password = "Pas$Word"
correct = False

while not correct:
    inpass = input("Enter your password: ")
    if inpass != password:
        print("Incorrect password, try again...")
    else:
        print(f"Welcome back, {name}")
        correct = True
