students = []

def get_students_title():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase
def print_students_titlecase():
      #  students_titlecase = []
  #  for student in students:                       
  #      students_titlecase = student.title()

  # Instead of the above repeated function body we use this instead :
    students_titlecase = get_students_titlecase()
    print(students_titlecase)