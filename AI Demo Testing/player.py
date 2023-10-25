from pet import Pet

class Player:
    def __init__(self, name: str, age: int, location: str, pet_owned: str, money: float):
        self.name = name
        self.age = age
        self.location = location
        self.pet_owned = pet_owned
        self.money = money

    def get_player_data(self):
        return f"Player Data: \nName: {self.name}\nAge: {self.age}\nLocation: {self.location}\nPet Owned: {self.pet_owned}\nMoney: {self.money}"

    ### Getters and Setters for when needed
    ### Generate Pet isnt here since I don't know what to put in for that yet
    def get_name(self):
        return f"{self.name}"

    def get_age(self):
        return f"{self.age}"
    
    def get_location(self):
        return f"{self.location}"

    def get_pet(self):
        return f"{self.pet_owned}"

    def get_money(self):
        return f"{self.money}"
    
    def set_name(self, name_entered):
        if not isinstance(name_entered, str):
            raise TypeError("Err: Name entered is not a string!")
        self._name = name_entered

    def set_location(self, location_entered):
        if not isinstance(location_entered, str):
            raise TypeError("Err: Location entered is not a string!")
        self._name = location_entered


### For Testing the File    ###
# testPlayer = Player("Dillon", 23, "Home", "NONE")

# print(testPlayer.name)
# print(testPlayer.location)
# print(testPlayer.age)
