#class is the blue print of object oretented
class Person:
     #calss level atpribiues
    #contructor
    #   self   is used in python other langngues can use   this   
    def __init__(self, name, age, eye_color):
        self.name = name
        self.age = age
        self.eye = eye_color

    def print_person_info(self):
        print(print (self.name, "age is", self.age, "eye color is", self.eye))
#outisde of class
#object
Adam = Person('Adam', 20, 'borwn') #intsance_of_the person class
Jill = Person('Jill', 35, 'green')
Sally = Person('Sallt', 39, 'brown')
Greg = Person('Greg', 12, 'black')

#tribliess to an object

Adam.print_person_info()
Jill.print_person_info()
Sally.print_person_info()
Greg.print_person_info()

print (Adam)
