from character import Character

class Warrior():
  def __init__(self, weapon = 'sword', attack_limit = 1, **kwargs):
    self.weapon = weapon
    self.attack_limit = self.rage()
    for key, value in kwargs.items():
      setattr(self, key, value)


  def rage(self):
    attack_limit = 20
    return attack_limit

  def __str__(self):
    print("Warrior, {}, {}".format(self.weapon, self.attack_limit))
    return "Warrior, {}, {}".format(self.weapon, self.attack_limit)


Warrior().__str__()
