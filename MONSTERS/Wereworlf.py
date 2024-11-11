from Monster import Monster

class Werewolf(Monster):

    def __init__(self, coords: list):
        super().__init__('H', 1000, 200, 5, 5, coords)


    