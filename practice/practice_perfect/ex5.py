def count(sequence, item):
  amount = 0
  for x in sequence:
    if x == item:
      amount += 1  
  return amount
