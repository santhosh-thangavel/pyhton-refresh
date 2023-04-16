def average_marks(marks, name):
    for i, j in marks.items():
        if name in i:
            average_marks  = sum(j)/len(j)
            print(format(average_marks, '.2f'))
        else:
            print("Marks of the specified name is not available")
if __name__ == '__main__':

    average_student_marks = average_marks({"beta": [30, 60, 70]}, name = "alpha")