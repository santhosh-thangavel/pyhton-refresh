if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = input()
        records.append([name, score])
        scores.append(score)

    # print(records)
    # print(scores)

    sorted_score = list(sorted(set(scores), reverse=True))
    # print(sorted_score)
    # print(sorted_score[-2])

    names =[]
    for record in records:
        # print(record)
        for value in record:
            # print(value)
            if value == sorted_score[0]:
                names.append(record[0])

    names = sorted(names)
    print(*names,sep="\n")