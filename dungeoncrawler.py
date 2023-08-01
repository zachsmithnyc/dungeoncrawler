class Character:
  # creates a new character
  def __init__(self, name, job, level = 1):
    self.name = name 
    self.job = job
    self.level = level
    
    if self.job == 'warrior':
      self.hp = level * 10
      self.max_hp = self.hp
      self.attack = level * 5
    elif self.job == 'thief':
      self.hp = level * 7
      self.max_hp = self.hp
      self.attack = level * 3
    else:
      self.hp = level * 5
      self.max_hp = self.hp
      self.attack = level * 1
  
  def __repr__(self):
    return f"{self.name} is a level {self.level} {self.job} with {self.hp} hit points."

  # method for attacking 
  def attack (self, monster):
    pass

class Monster:
  # creates monsters for characters to fight
  def __init__(self, name):
    self.name = name
    
    if self.name == 'ogre':
      self.power = 5
    elif self.name == 'wolf':
      self.power = 3
    else:
      self.power = 1
    