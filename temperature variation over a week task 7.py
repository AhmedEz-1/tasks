import matplotlib.pyplot as plt
plt.figure(figsize=(8 , 6))
days = ["Sunday" , "Monday" , "Tuesday" , "Wednesday" ,"Thursday" ,"Friday" ,"Saturday"]
temp = [27 , 30 , 35 , 39 , 32 , 42 , 45]
plt.plot(days , temp , marker = "o" , linestyle ="-" , color = "green")
plt.xticks(rotation = 45)
plt.title(" temperature variation over a week")
plt.xlabel("Days of the week")
plt.ylabel("Temprature (C)")
plt.show()