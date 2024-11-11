from Monster import Monster
from Skeleton import Skeleton

class ShieldSkeleton(Skeleton):

    def __init__(self, coords: list):
        super().__init__(coords)
        self.__hp_escudo = 200

    @property
    def getShield(self):
        return self.__hp_escudo
    
    def hurt(self, dmg):
        if (self.__hp_escudo <= 0):
            self.__life -= dmg
        else:
            self.__hp_escudo -= dmg

    