a = 0b11101110 
# need a mask the same length as a in which all of the bits are turned on
mask = 0b11111111
desired = a ^ mask

print bin(desired)
