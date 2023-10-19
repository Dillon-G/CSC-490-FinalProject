# from player import Player

class Pet:
    def __init__(self, name: str, hunger: str, hunger_val: int, mood: str, animal_type: str, age: int,
                gender: str, location: str, owner: str):
        self.name = name
        self.hunger = hunger
        self.hunger_val = hunger_val
        self.mood = mood
        self.animal_type = animal_type
        self.age = age
        self.location = location 
        self.gender = gender
        self.owner = owner

    def get_pet_data(self):
        return f"\nName: {self.name} \nHunger: {self.hunger} \nMood: {self.mood} \nLocation: {self.location} \nAnimal Type: {self.animal_type} \nAge: {self.age} \nOwner: {self.owner}, \nGernder: {self.gender}\n"

    def get_age(self):
        return f"{self.age}"

# testPet = Pet("Artemis", "Full", 100, "Happy", "Cat-Dog", 2, "F", "Home", "NO OWNER")

# print(testPet.get_pet_data())
# print(testPet.hunger)
# print(testPet.age)
