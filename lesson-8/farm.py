class Animal:
    def __init__(self, name):
        self.name = name
        
    def walk(self):
        return f"{self.name} can walk!"
    
    def eat(self):
        return f"{self.name} can eat"
    
    def __repr__(self):
        return f'Animal, name={self.name}'    

class Cow(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def __repr__(self):
        # You can also call the parent class __repr__ here for consistency
        return f'{self.name} is {self.color} color'    

class Dog(Animal):
    def __init__(self, name, descendant):
        super().__init__(name)
        self.descendant = descendant
    
    def sound(self):
        print('Woof')
    
    def __repr__(self):
        return f'{self.name} is from {self.descendant}'    

class Bird(Animal):
    def __init__(self, name, length_of_wing):   
        super().__init__(name)
        self.length_of_wing = length_of_wing
    
    def __repr__(self):
        return f'{self.name} can fly {self.length_of_wing} meter height'

# Example usage
cow = Cow('Bella', 'brown')
dog = Dog('Jack', 'Bulldog')
bird = Bird('Eagle', 50)

print(cow)  # Output: Bella is brown color
print(dog)  # Output: Jack is from Bulldog
print(bird)  # Output: Eagle can fly 50 meter height
