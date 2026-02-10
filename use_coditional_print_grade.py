marks1=int(input("enter subject marks"))

if(marks1<=100 and marks1>90):
    gread="ex"
elif(marks1<=90 and marks1>80):
       gread="A"
elif(marks1<=80 and marks1>70):
       gread="B"
elif(marks1<=70 and marks1>60):
       gread="C"
elif(marks1<=60 and marks1>50):
       gread="D"
elif(marks1<=50):
       gread="F"
print(gread)
# print("your gread",gread)