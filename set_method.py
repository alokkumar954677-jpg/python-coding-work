a={1,2,3,4,7,8,"alok"}
print(a,type(a))
a.add(10)# add new word or digit
print(a,type(a))
a.remove(4)# remove to word or digit
print(a,type(a))
print(len(a))
a.pop()# rondam numer ko remov karta hai koi fix nahi hota hai
print(a,type(a))
b={1,6,7,8}
print(a.union(b))# a or b ko jod kar ek list banata hai pr sem ko nhi likhe ga
print(a.intersection(b))#a or b ke list se commn ko print karta hai 
a.clear()# all list ko clear kar deta hai
print(a)