Contact1 = {"Name" : "Ahmed" , "Phone Number" : "01233445"}
Contact2 = {"Name" : "Youssef" , "Phone Number" : "01049874"}
Contact3 = {"Name" : "Mostafa" , "Phone Number" : "012344542"}
x = "Enter a contact name:"
if input(x) == Contact1["Name"] :
    print(Contact1["Phone Number"])
elif input(x) == Contact2["Name"] :
    print(Contact2["Phone Number"])
elif input(x) == Contact3["Name"] :
    print(Contact3["Phone Number"])
elif input(x) == "All contacts":
    print("Name:", Contact1["Name"] , ",Phone Number:" , Contact1["Phone Number"])
    print("Name:", Contact2["Name"] , ",Phone Number:" , Contact2["Phone Number"])
    print("Name:", Contact3["Name"] , ",Phone Number:" , Contact3["Phone Number"])
else :
    print("Not found")