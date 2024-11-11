from Monster import Monster

class Vampire(Monster):

    def __init__(self, coords: list):
        super().__init__('V', 500, 100, 10, 3, coords)


    