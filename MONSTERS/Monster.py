
class Monster:
    def __init__(self,id: str,life: int, attack: int, vis_range: int, speed: int, cords: list):
        self.id = id
        self.__life = life
        self.__attack = attack
        self.__vis_range = vis_range
        self.__speed = speed
        self._cords = cords
        pass

    @property
    def getLife(self):
         return self.__life
    
    @property
    def is_alive(self):
         return self.__life > 0
    
    def attack(self, player: 'Player'):
         player.hurt(self.attack)

    def hurt(self, dmg: int):
         self.__life = dmg

    def heal(self, hl: int):
         self.__life += hl

    def move(self, cc: list):
         self._cords = cc
         

