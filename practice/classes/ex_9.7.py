class Car(object):
  condition = "new"
  #this is a member variable -- stores info about a class object
  def __init__(self, model, color, mpg):
    # assigning variables...
    self.model = model
    self.color = color
    self.mpg = mpg
my_car = Car(model = "DeLorean",
color = "silver",
mpg = 88)
# we just created a new object -> called instances then modifyed the object (my_car)


# accessing variables in classes (i.e. my_car)....
print my_car.condition

print my_car.model
print my_car.color
print my_car.mpg
