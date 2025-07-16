import numpy as np
list1 = [10 , 20 , 30 , 40 , 50]
A = np.array(list1)
list2 = [5 , 4 , 3 , 2 , 1]
B = np.array(list2)
print("A =" , A)
print("B =",B)
print("Sum =", A + B)
print("Subtraction =" , A - B)
print("Multiplication =" , A * B)
print("Division =" , A / B)
print("The mean number in A is " , A.mean())
print("The maximum number in A is " , A.max())
print("The minimum number in A is " , A.min())
dot = np.dot(A , B)
print("The dot product in A and B is " , dot )
A_reshaped = A.reshape(5 ,1 )
print("Reshaped A = " , A_reshaped)