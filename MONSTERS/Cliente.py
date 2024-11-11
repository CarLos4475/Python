from Monster import Monster
from ShieldSkeleton import ShieldSkeleton

if __name__=='__main__':
        rafa = Monster('Rafa',10,10,10,10,[1,2])
        print(rafa.getLife)
        irving = ShieldSkeleton([0,0])
        print(irving.getLife)
        irving.hurt(500)
        print(irving.getShield)
        irving.hurt(50)
        print(irving.getLife)
