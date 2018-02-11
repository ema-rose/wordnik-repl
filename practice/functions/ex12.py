# review functions...
def shut_down(s):
  if s == "yes":
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"
    
# review modules...
from math import sqrt
print sqrt(13689)

# review built-in functions...
def distance_from_zero(number):
  if type(number) == int or type(number) == float:
    return abs(number)
  else:
    return "Nope"
