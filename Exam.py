medical_cause=input("enter the medical cause:")
att=int(input("Enter the attandance:"))
if medical_cause=='y':
    print(" allowed")
else:
    if att>=75:
        print(" Allowed")
    else:
        print("Not allowed")
        