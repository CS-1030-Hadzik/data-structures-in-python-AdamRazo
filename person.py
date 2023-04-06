#class is the blue print of object oretented
class Person:
     #calss level atpribiues
    #contructor
    #   self   is used in python other langngues can use   this   
    def __init__(self, name, age, eye_color):
        self.name = name
        self.age = age
        self.eye = eye_color

#outisde of class
#object
Adam = Person('Adam', 20, 'borwn') #intsance_of_the person class
Jill = Person('Jill', 35, 'green')

#tribliess to an object

print (Adam.name, "age is", Adam.age, "eye color is", Adam.eye)

Jill.age = 35

print ("jill's age is", Jill.age)


print (Adam)
