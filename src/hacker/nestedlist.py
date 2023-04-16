if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = input()
        records.append([name, score])
        scores.append(score)

    print(records)
    # print(scores)

    sorted_score = list(sorted(set(scores), reverse=True))
    print(sorted_score)
    print(sorted_score[-2])

    names =[]
    for record in records:
        print(record)
        for value in record:
            print(value)
            if value == sorted_score[-2]:
                names.append(record[0])

    print(names)




    # result = []

    # for student in students:
    #     result.append(student[1])
    # # print(students)
    # print(result)

    # first = math.inf
    # second = math.inf
    # # print(first)
    # for i in range(0, len(result)):
    #     if first > result[i]:
    #         first = result[i]
    # # print(first)
    # for i in range(0, len(result)):
    #     if first != result[i] and second > result[i]:
    #         second = result[i]
    # print(second)
    # # print(type(second))

    # # for x in result:
    # #     if second in x:
    # #          print(x)

    # # print(list(enumerate(students[1])))