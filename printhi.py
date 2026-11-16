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
s1.study(maths)