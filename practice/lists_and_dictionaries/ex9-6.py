lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]
for student in students:
  print student["name"]
  print student["homework"]
  print student["quizzes"]
  print student["tests"]
  
# When you divide an integer by another integer, the result is always an integer (rounded down, if needed).
# When you divide a float by an integer, the result is always a float.
#To divide two integers and end up with a float, you must first use float() to convert one of the integers to a float. So...

# Write a function average that takes a list of numbers and returns the average

def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)
  
# Write a function called get_average that takes a student dictionary (like lloyd, alice, or tyler) \
as input and returns his/her weighted average.

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return 0.1 * average(student["homework"]) + 0.3 * average(student["quizzes"]) + 0.6 * average(student["tests"])
  
# write a get_letter_grade function that takes a number score as input and returns a string with the letter grade that \
the student should receive

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"
  print score
  
print get_letter_grade(get_average(lloyd))
print get_letter_grade(get_average(alice))
print get_letter_grade(get_average(tyler))

# get class average...
def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)
  

class_avg = get_class_average(students)
print class_avg
print get_letter_grade(class_avg)
