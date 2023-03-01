class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __init__(self,name,age):
        self.name =name
        self.age = age

s1 = Student("Praveen",32)
s2  = Student("Aks",25)


class Vehicle:

    def __init__(self,engine):
        self.engine = engine

class Car(Vehicle):

    def __init__(self,engine,max_speed):
        super().__init__(engine)
        self.max_speed =max_speed


class Electric_Car(Car):

    def __init__(self,engine,max_speed,km_range):
        super().__init__(engine,max_speed)
        self.km_range = km_range


v1 = Electric_Car("1500CC" , '120 Kmph' , 150)
print(f'Engine=',v1.engine, "MaxSpeed=",v1.max_speed,"Range=",v1.km_range)
