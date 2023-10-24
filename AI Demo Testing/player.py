from pet import Pet

class Player:
    def __init__(self, name: str, age: int, location: str, pet_owned: str):
        self.name = name
        self.age = age
        self.location = location
        self.pet_owned = pet_owned

    def get_player_data(self):
        return f"\nName: {self.name}, \Age: {self.age}, \Location: {self.location}, \Pet Owned: {self.pet_owned}"

### For Testing the File    ###
# testPlayer = Player("Dillon", 23, "Home", "NONE")

# print(testPlayer.name)
# print(testPlayer.location)
# print(testPlayer.age)
