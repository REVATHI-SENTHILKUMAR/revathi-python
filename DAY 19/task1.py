class SmartLight:
    def __init__(self, room_name, color="White"):
        self.room = room_name      
        self.color = color         
        self.is_on = False         

    def turn_on(self):
        self.is_on = True
        print(f"The {self.room} light is now ON.")

    def change_color(self, new_color):
        self.color = new_color
        print(f"The {self.room} light changed to {self.color}.")

living_room_bulb = SmartLight("Living Room", "Warm Gold")

living_room_bulb.turn_on()
living_room_bulb.change_color("Neon Blue")

print(f"Final Status: {living_room_bulb.room} is {living_room_bulb.color}.")
