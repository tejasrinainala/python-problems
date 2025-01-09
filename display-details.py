class Parent:
    def _init__(self):
        self.name=name
    def inputName(self):
        self.name=input()
    def displayName(self):
        return self.name
class Child(Parent):
    def _init__(self):
        self.age=age
    def inputAge(self):
        self.age=int(input())
    def displayAge(self):
        return self.age
c=Child()
c.inputName()
c.inputAge()
print(c.displayName())
print(c.displayAge())
