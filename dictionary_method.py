marks={"alok":100,
       "raja":150,
       "rohit":50,
       "kran":80
}
print(marks,type(marks))
print(marks["alok"])
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"alok":99,"kunal":100})
print(marks)
print(len(marks))
#diffrec
print(marks.get("alok")) # print none
print(marks["alok"])#return an arror 

 
print(marks)#marks list print
