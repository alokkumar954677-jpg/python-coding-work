v=input("enter lower and upper =")
if(v>='a'):
    for i in range(ord('a'),ord('z')+1):
     print(chr(i),end=" ")# chr =character  end to use one line print
elif(v>='A'):
    for i in  range(ord('A'),ord('Z')+1):
        print(chr(i),end=" ")
else:
    print("not vailed letter")