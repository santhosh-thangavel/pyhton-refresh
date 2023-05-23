def average_marks(*marks, name):
    for key_value in marks:
        for all_name in key_value.items():
            if name in all_name:
                print(name)
                average_marks  = sum(all_name[1])/len(all_name[1])
                print(format(average_marks, '.2f'))
            else:
                print("Marks of the specified name is not available")
                
        # print(i,j)
        # if name in i:
        #     average_marks  = sum(j)/len(j)
        #     print(format(average_marks, '.2f'))
        # else:
        #     print("Marks of the specified name is not available")
if __name__ == '__main__':

    average_student_marks = average_marks({"beta": [30, 60, 70]}, {"alpha": [0, 60, 30]}, name = "alpha")