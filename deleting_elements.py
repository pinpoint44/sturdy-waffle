myfruits = ["orange" ,"apple" ,"grape" ,"mango" ,"watermelon"]

print("Your list:", myfruits)

x = input("Enter a fruit to remove: ")

if x in myfruits:
    myfruits.remove(x)
    print(f"'{x}' has been removed.")
else:
    print(f"'{x}' is not in the list.")

print("Updated list: ", myfruits)

