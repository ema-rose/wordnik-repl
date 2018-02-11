class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = "good"
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def description(self):
    print self.name
    print self.age
    
hippo = Animal("Sally", 22)
hippo.description()
sloth = Animal("Minnie", 47)
ocelot = Animal("Mike", 32)

print hippo.health
print sloth.health
print ocelot.health

# member variables are variables that are available to all members of a class (like health)
