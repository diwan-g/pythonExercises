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

###########################
# Method 2 without Sets
###########################

def best_score(arr):
    high_score = 0
    for num in arr:
        if num >= high_score:
            high_score = num
    return high_score

high_score = best_score(scores)
print(high_score)

# remove high score

def remove_ocurrence(num):
    for score in scores:
        if score == high_score:
            scores.remove(score)

remove_ocurrence(high_score)
second_high_score = best_score(scores)
print(second_high_score)
