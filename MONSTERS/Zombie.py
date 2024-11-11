from Monster import Monster

class Zombie(Monster):

    def __init__(self, coords: list):
        super().__init__('Z', 300, 200, 4, 1, coords)


    