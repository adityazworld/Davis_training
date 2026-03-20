  ## Question 1) Student Grade Analyzer

  
def calculate_grade(marks):

    if marks > 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 50:
        return "C"

    else :
         return "Fail"

  ##Loop for Student
  
for i in range(1,6):
   print("="*35)
   marks =int(input(f"Enter the mark of student {i}:" ))
   grade= calculate_grade(marks)
   print(f"Student{i} : Grade : {grade}") 


