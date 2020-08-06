class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f'{self.first}@{self.last}.com'

    def __str__(self):
        return f'Name: {self.first} {self.last}, Email: {self.email}'



print(Person('cody', 'branson'))
