class Location:
    def __init__(self, name: str, weather: str, is_shop: bool, is_outside: bool\
                 , has_activity: bool, activities: list):
        self.name = name                    # Name of the location
        self.weather = weather              # How the weather looks
        self.is_shop = is_shop              # 1 = is a shop, 0 = not a shop
        self.is_outside = is_outside        # 1 = is a outside, 0 = inside
        self.has_activity = has_activity    # 1 = has activities, 0 = no pet activities
        self.activities = activities        # Holds a list of activities

    ### Getters and Setters for when needed
    def get_weather(self):
        if self.is_outside == 1:
            print(f"\nCurrently indoors!\nHowever, the weather outside is: {self.weather}")
        else:
            print(f"Weather: {self.weather}")

    ### Lists the activities of the current location
    def get_activities(self):
        if self.has_activity == 0 or len(self.activities) == 0:
            print("\nNo activities here!")
        else:
            print("\nActivities: ")
            i = 0
            while i < len(self.activities): 
                print(f"{self.activities[i]}")
                i = i+1

### For Testing the File    ###
# testLocation = Location("Park", "Sunny", 0, 1, 1, ["Frisbee", "Running"])
# testShop = Location("Pets Mart", "Sunny", 1, 0, 0, [])

# testLocation.get_weather()
# testShop.get_weather()
# testLocation.get_activities()
# testShop.get_activities()
# print("Park Status:\n", testLocation.name)
# print(testLocation.weather)
# print("Activity?:", bool(testLocation.has_activity))

# print("Activity?:", bool(testShop.has_activity))
# print("\nShop Status:\n" ,testShop.name)
