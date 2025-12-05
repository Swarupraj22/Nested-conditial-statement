print("Select your ride: ")
print("1. Bike")
print("2. Car")
choice=int(input("Enter the choice:"))
if(choice==1):
    print("What type of bike")
    print("1. Scooty\n")
    print("2. Scooter\n")
    choice2=int(input("Enter the choice:"))
    if choice2==1:
        print("Scooty selected")
    else:
        print("Scooter selected")