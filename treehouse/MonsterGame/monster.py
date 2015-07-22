import random
from combat import Combat


COLORS = ['pink', 'orange', 'yellow', 'purple']


class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = 'sword'
    sound = 'roar'

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self,key, value)

    def __str__(self):
        return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
                                              self.__class__.__name__,
                                              self.hit_points,
                                              self.experience)

    def battlecry(self):
        return self.sound.upper()

class Goblin(Monster):
    max_hit_points = 5
    max_experience = 4
    sound = 'OHHHHHH'


class Troll(Monster):
    max_hit_points = 2
    max_experience = 4
    sound = 'thug'

class Bigfoot(Monster):
    max_hit_points = 6
    max_experience = 2
    sound = 'stomp'