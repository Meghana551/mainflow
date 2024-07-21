#lists 
student=[ "name" , "rollno" , "dept" , "marks" ]


student.append("phoneno")
student.remove("dept")
student[1]="id"
student.insert(2,"Address")
student.sort()
print("List op=" ,student)

#dictionary 
Fruits={
    "apple" : 3,
    "Banana" : "yellow",
    "Guava" : "green" ,
    "pineapple" : 2
}

Fruits["oranges"] = "orange"
Fruits["strawberry"] = "pink"
Fruits["Banana"] = "pale"
del Fruits["Guava"]
del Fruits["pineapple"]
Fruit = Fruits.copy()
print("Dict op=", Fruit)

#tuples
Squares=(4,25,49,36,81.0,9,100)
Numb=("root")
squar=list(Squares)+list(Numb)
sq=squar[:1]+squar[2:]
print("Tuple op=",squar)
print(sq)
print(Squares)