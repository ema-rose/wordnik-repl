# A bit mask is just a variable that aids you with bitwise operations

# It should check to see if the fourth bit from the right is on...

def check_bit4(input):
  mask = 0b1000
  desired = input & mask
  if desired > 0:
    return "on"
  else:
    return "off"
