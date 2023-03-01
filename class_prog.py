class Person:
# this is the exmaple for class with parameterized methods with initialization
    def __init__(self,name,sex, profession):
        self.name = name
        self.sex = sex
        self.profession = profession

    def show(self):
        print('Name:',self.name , 'Sex:', self.sex, 'Profession:', self.profession)

    def work(self):
        print("I",self.name,'working as', self.profession)

praveen = Person("Praveen", 'Male', "Engineer")
print(praveen)
praveen.show()
praveen.work()

aksh = Person("Akshata", "Female", "House Maker")
aksh.show()
aksh.work()