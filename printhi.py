'''
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f'name: {self.name},age: {self.age}')
    def study(sef,subject):
        print(f'{self.name} is studying {subject}')

s1=student("ravi",11)
s1.display()


class supriya:
    def display(self):
        print("Hi welcome to python")
s1=supriya()
s1.display()

class student:
    def display(self):
        print("Name: hello")
        print("age: 45")
        print("course: python")
s1=supriya()
s1.display()

class student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def display(self):
        print("Name:",self.name)
        print("age:",self.age)
        print("course:",self.course)
s1=student("hello",21,"python")
s1.display()

print("----------------------------------")
class employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
    def display(self):
        print("Name:",self.name)
        print("salary:",self.salary)
        print("department:",self.department)
s1=employee("hello",2145,"programming")
s1.display()

print("----------------------------------")
class bankaccount:
    def __init__(self,balance):
        self._balance=balance

    def deposit(self,amount):
        if amount>0:
            self._balance+=amount

    def get_balance(self):
        return self._balance

account=bankaccount(5000)
account.deposit(200)

print(account.get_balance())

print("----------------------------------")
class animal:
    def dog(self):
        print("welcome to animal kingdom")
class cat(animal):
    def meow(self):
        print("meow meow")

c1=cat()
c1.dog()
c1.meow()

print("----------------------------------")
class cars:
    def brand(self):
        print("this is my car!!")
class electric(cars):
    def brand(self):
            print("BMW")
class racing(cars):
    def brand(self):
            print("rolls roys")

c=cars()
c.brand()
'''
from abc import ABC,abstractmethod

class payment(ABC):

    @abstractmethod
    def pay(self,amount):
        pass
class upi(payment):
    def pay(self,amount):
        print("Paid using upi:",amount)
class card(payment):
    def pay(self,amount):
        print("Paid using card",amount)
u=upi()
c=card()
u.pay(800)
c.pay(100)