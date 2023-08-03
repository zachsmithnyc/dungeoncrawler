class Character:
  # creates a new character
  def __init__(self, name, job, level = 1):
    self.name = name 
    self.job = job
    self.level = level
    self.is_knocked_out = False
    
    if self.job == 'warrior':
      self.hp = round(level * 10)
      self.max_hp = self.hp
      self.power = round(level * 5)
      self.heal_power = 0
    if self.job == 'thief':
      self.hp = round(level * 7)
      self.max_hp = self.hp
      self.power = round(level * 3)
      self.heal_power = 0
    if self.job == 'cleric':
      self.hp = round(level * 5)
      self.max_hp = self.hp
      self.power = round(level * 1)
      self.heal_power = 5
  
  def __repr__(self):
    return f"{self.name} is a level {self.level} {self.job} with {self.hp} hit points and {self.power} power."
  
  # revive method
  def revive(self):
    self.is_knocked_out = False
    if self.hp == 0:
      self.hp = 1
    print(f"{self.name} was revived!")

  # method for knock out
  def knock_out(self):
    # sets knock out status to true 
    self.is_knocked_out = True

    if self.hp != 0:
      self.hp = 0
    
    print(f"{self.name} was knocked out!")

  # method for losing health
  def lose_hp(self, amount):
    self.hp -= amount
    if self.hp <= 0:
      self.hp = 0
      self.knock_out()
    else:
      print(f"{self.name} hp was reduced to {self.hp}")

  # method for gaining health
  def gain_hp(self, amount):
    self.hp += amount

    #checks knock our status and flips it to false on heal 
    if self.is_knocked_out == True:
      self.revive()

    print(f"{self.name} now has {self.hp} hit points!")
  
  # method for attacking
  def attack(self, target):
    print(f"{self.name} attacked {target.name}!")
    target.lose_hp(self.power)

  # method for healing 
  def heal(self, target):
    print(f"{self.name} heals {target.name}")
    target.gain_hp(self.heal_power)

  # method for stealing 
  def steal(self, target):
    pass


class Monster:
  # creates monsters for characters to fight
  def __init__(self, name):
    self.name = name
    
    if self.name == 'ogre':
      self.power = 5
      self.item = 'potion'
    if self.name == 'wolf':
      self.power = 3
      self.item = 'wolf teeth'
    if self.name == 'fairy':
      self.power = 1
      self.item = 'antidote'

  def __repr__(self):
    return "{name} has {power} power and is holding {item}.".format(name = self.name, power = self.power, item = self.item)
  
  #method for attacking 
  def attack(self, target):
    target.lose_hp(self.power)

  #method for aoe attack
  def poison(self, target):
    pass

  #method for healing
  def heal(self, target):
    pass


warrior = Character('Samson', 'warrior')
thief = Character('Clyde', 'thief')
cleric = Character('Sheila', 'cleric')
ogre = Monster('ogre')
wolf = Monster('wolf')
fairy = Monster('fairy')

print(warrior.__repr__())
print(thief.__repr__())
print(cleric.__repr__())
print(ogre.__repr__())
print(wolf.__repr__())
print(fairy.__repr__())


    