class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_student):
        self.name = name
        self.max_student = max_student
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_student:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


s1 = Student("Gerald", 20, 90)
s2 = Student("Joey", 22, 95)
s3 = Student("Layla", 19, 85)

# print(s1.name)

course = Course("Maths", 2)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3)) # see that the third student is not added as max_student is 2
print(course.students[1].name)
print(course.get_average_grade())
