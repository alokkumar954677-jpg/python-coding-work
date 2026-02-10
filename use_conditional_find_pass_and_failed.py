marks1= int(input("enter math marks="))
marks2= int(input("enter english marks="))
marks3= int(input("enter chemistry marks="))
marks4= int(input("enter physics marks="))
total_percentage=((100)*(marks1+marks2+marks3+marks4))/400
if(total_percentage>=40 and marks1>=30 and marks2>=30 and marks3>=30 and marks4>=30):
    print("you are pass ",total_percentage)
else:
    print("you are failed",total_percentage)