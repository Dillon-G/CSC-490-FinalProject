
class Pet:
    def __init__(self, name: str, hunger: str, craving: str, hunger_val: int, mood: str, mood_val: int,
                  animal_type: str, age: int, gender: str, location: str, owner: str):
        self.name = name
        self.hunger = hunger
        self.craving = craving
        self.hunger_val = hunger_val
        self.mood = mood
        self.mood_val = mood_val
        self.animal_type = animal_type
        self.age = age
        self.location = location 
        self.gender = gender
        self.owner = owner

    ### If all pet data needs to be displayed, minus integer values like the mood and hunger values
    def get_pet_data(self):
        return f"\nName: {self.name} \nHunger: {self.hunger} \nMood: {self.mood} \Craving: {self.craving}\
              \nLocation: {self.location} \nAnimal Type: {self.animal_type} \nAge: {self.age}\
                \nOwner: {self.owner}, \nGender: {self.gender}\n"

    ### Getters and Setters for when needed
    def get_name(self):
        return f"{self.name}"

    def get_hunger(self):
        return f"{self.hunger}"
    
    def get_craving(self):
        return f"{self.craving}"

    def get_mood(self):
        return f"{self.mood}"

    def get_type(self):
        return f"{self.animal_type}"

    def get_gender(self):
        return f"{self.gender}"

    def get_location(self):
        return f"{self.location}"

    def get_owner(self):
        return f"{self.owner}"
    
    def set_name(self, name_entered):
        if not isinstance(name_entered, str):
            raise TypeError("Err: Name entered is not a string!")
        self._name = name_entered

    def set_type(self, type_entered):
        if not isinstance(type_entered, str):
            raise TypeError("Err: Animal type entered is not a string!")
        self._name = type_entered

    def set_location(self, location_entered):
        if not isinstance(location_entered, str):
            raise TypeError("Err: Location entered is not a string!")
        self._name = location_entered

### For Testing the file    ###
# testPet = Pet("Artemis", "Full", 100, "Happy", "Cat-Dog", 2, "F", "Home", "NO OWNER")

# print(testPet.get_pet_data())
# print(testPet.hunger)
# print(testPet.age)
