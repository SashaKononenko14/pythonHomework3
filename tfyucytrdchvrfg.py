class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"Привіт, мене звуть {self.name}. Я {self.age} років і я {self.gender}."

    def greet(self, other_person):
        return f"Привіт, {other_person.name}! Я {self.name}. Радий познайомитися з тобою."

# Приклад використання класу "Людина"
Sasha = Human("Саня", 30, "чоловік")
Nika = Human("Ніка", 25, "жінка")

print(Sasha.introduce())  # Виведе: Привіт, мене звуть Саня. Я 30 років і я чоловік.
print(Nika.introduce())  # Виведе: Привіт, мене звуть Ніка. Я 25 років і я жінка.