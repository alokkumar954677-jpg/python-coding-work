marks={"alok":100,
       "raja":150,
       "rohit":50,
       "kran":80
}
print(marks,type(marks))# dictionary ko print karta hai
print(marks["alok"])# name se marks ko find karta hai
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"alok":99,"kunal":100})
print(marks)
print(len(marks))
#diffrec
print(marks.get("alok")) # print none
print(marks["alok"])#return an arror 

# k=marks.pop('alok')# alok ko or alok kr mark   ko hata deta hai 
# print(k)# alok marks print karta 
print(marks)#marks list print