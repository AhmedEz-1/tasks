import pandas as pd
Students_data = [["Alice" , 20 , "A" , 85]
        ,["Bob" , 22 , "B" , 78]
        ,["Charlie" , 19 , "A" , 92]
        ,["David" , 21 , "C" , 65]
        ,["Eva" , 20 , "B" , 74]]
df = pd.DataFrame(Students_data , columns=["Name" , "Age" , "Grade" , "Marks"])
print(df)
rows3 = df.head(3)
print(rows3)
name1 = df[['Name' ,'Marks']]
print(name1)
A = df.loc[df["Grade"] == "A"]
print(A)
