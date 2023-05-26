class Student:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id

class Course:
    def __init__(self,name,teacher):
        self.name=name
        self.teacher=teacher

class Teacher:
    def __init__(self,name,course):
        self.name=name
        self.course=course

class School:
    def __init__(self,name,teachers,courses,students):
        self.name=name
        self.teachers=teachers
        self.courses=courses
        self.students=students
    
    def get_students(self):
        for student in self.students:
            print(student.name)
        
        
school_name="Phitron"
teacher_1=Teacher('Einstein','Data Structure')
ds_course=Course('data structure',teacher_1)
teacher_2=Teacher('Edison','algo_course')
algo_course=Course('Algorithm',teacher_2)

student_1=Student('Rohomot',19,45)
student_2=Student("keramot",20,65)

teachers=[teacher_1,teacher_2]
courses=[ds_course,algo_course]
students=[student_1,student_2]

my_school=School(school_name,teachers,courses,students)
# print(my_school.__dict__)
my_school.get_students()