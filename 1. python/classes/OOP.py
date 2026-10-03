class Animals:
    def __init__(self, name, specie, gender, sound):
        self.name = name
        self.specie = specie
        self.gender = gender
        self.sound = sound

    def call_animal(self):
        return f'Come {self.name}!'

    def verify_specie(self):
        if self.specie.startswith(('A', 'E', 'I', 'O', 'U')):
            return f'It\'s an {self.specie}'
        else:
            return f'It\'s a {self.specie}'

    def reproduce(self):
        if self.gender == 'Male':
            print('If you want an offspring of {self.specie}, you need a Female partner}')
        elif self.gender == 'Female':
            print('If you want an offspring of {self.specie}, you need a Male partner}')

    def make_sound(self):
        return self.sound

class Cat(Animals):
    def __init__(self, name, gender):
        super().__init__(name, 'Cat', gender, 'Miua!')

class Dog(Animals):
    def __init__(self, name, gender):
        super().__init__(name, 'Dog', gender, 'Guau!')


platypus = Animals('Perry', 'Platypus', 'Male', 'Brrrrrr!')

patilla = Cat('Patilla', 'Female')

firulais = Dog('Firulais', 'Male')

ant = Animals('Antony', 'Ant', 'Male', 'idk')

print(platypus.verify_specie())
print(patilla.verify_specie())
print(firulais.verify_specie())
print(ant.verify_specie())


print(platypus.make_sound())
print(patilla.reproduce())
print(firulais.call_animal())