student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
  #print(student_scores[grades])
  #x = student_scores.keys()
  #print("Key is:", x)
  #print(student_scores)
  score = student_scores[student]
  if score > 91:
    student_grades[student] = "Outstanding"
  if score > 81 and score < 90:
    student_grades[student] = "Exceeds Expectations"
  if score > 71 and score < 80:
    student_grades[student] = "Acceptable"
  if score < 70:
    student_grades[student] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)
