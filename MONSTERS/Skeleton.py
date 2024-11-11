from Monster import Monster

class Skeleton(Monster):

    def __init__(self, coords: list):
        super().__init__('S', 100, 100, 5, 1, coords)


    