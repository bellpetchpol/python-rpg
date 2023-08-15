def find_average_scores(exam_scores_arg):
    sum_of_scores = 0
    for score in exam_scores_arg.values():
        sum_of_scores += score
    average_score = round(sum_of_scores / len(exam_scores_arg),2)
    print(average_score)