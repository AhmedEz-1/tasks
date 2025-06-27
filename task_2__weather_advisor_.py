x = int(input("Enter The Temprature Degree:"))
print(x , "celsuis degree")
if x > 30 or x == 30 :
    print("its a hot day stay hydrated!")
elif x >= 20 and x <= 29 :
    print("its a warm day , enjoy the weather!")
elif x >=10 and x <= 19 :
    print("Its a cool day , Wear a jacket!")
elif x < 10 :
    print("Its a cold day , stay warm!")
