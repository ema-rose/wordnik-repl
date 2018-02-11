def product(lst):
  num = 1
  # we're multiplying, don't start @ 0!
  for x in lst:
    num *= x
  return num
