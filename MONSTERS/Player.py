from Monster import Monster

class Player(Monster):

    def __init__(self, coords: list):
        super().__init__('P', 700, 50, None, 1, coords)
        self.__items = []
        self.__max_items = 2

    def pick_item(self, item = 'item'):
        self.__items.append(item)

        if len(self.__items) > self.__max_items:
            return self.__items.pop(0)
        
