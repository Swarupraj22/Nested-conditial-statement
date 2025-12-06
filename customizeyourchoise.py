print("Select your choice: ")
print("1. Bike")
print("2. Car")
choice = int(input("Enter the choice: "))

if choice == 1:
    print("\nWhat type of bike")
    print("1. Scooty")
    print("2. Scooter")
    choice2 = int(input("\nEnter the choice: "))
    if choice2 == 1:
        print("\nThe choice is: Scooty selected\n You can buy now")
    else:
        print("\nThe choice is: Scooter\n You can buy now")

elif choice == 2:
    print("\nWhat type of car")
    print("1. Lamborghani")
    print("2. Toyota\n")
    choice2 = int(input("Enter the choice: "))
    if choice2 == 1:
        print("\nThe choice is: Lamborghani\n You can buy now")
    else:
        print("\nThe choice is: Toyota\n You can buy now")
else:
    print("Wrong Entry")
