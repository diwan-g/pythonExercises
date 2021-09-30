## Best Scores
# From a class of n students, find the highest and second-highest scores in the class
# Students can have same scores.

scores = [78,86,66,81,50,81,23,45,79,62,86,33]
# output should be: 86 and 81
best_score = 0
second_best_score = 0

score_set = set(scores)

best_score = max(score_set)
print(best_score)
score_set.remove(best_score)
second_best_score = max(score_set)
print(second_best_score)