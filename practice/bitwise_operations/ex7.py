# &) operator compares two numbers on a bit level and returns a number where the bits \
of that number are turned on if the corresponding bits of both numbers are 1
# the & operator can only result in a number that is less than or equal to the smaller of the two values

print bin(0b1110 & 0b101)

# OR (|) operator compares two numbers on a bit level and returns a number where the bits \
of that number are turned on if either of the corresponding bits of either number are 1
# can only create results that are greater than or equal to the larger of the two integer inputs

print bin(0b1110 | 0b101)
# prints 0b1111



# XOR (^) or exclusive or operator compares two numbers on a bit level and returns a number \
where the bits of that number are turned on if either of the corresponding bits of the two \
numbers are 1, but not both

print bin(0b1110 ^ 0b101)
# prints 0b1011


# NOT operator (~) just flips all of the bits in a single number.
# mathematically, this is equivalent to adding one to the number and then making it negative

print ~1 # prints -2
print ~2 # prints -3
print ~3 # prints -4
print ~42 # prints -43
print ~123 # prints -124
