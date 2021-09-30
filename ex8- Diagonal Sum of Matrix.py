a = [[0,1,2,3],[4,5,6,7],[1,1,1,1]]


def diagnol_sum(array):
    result = 0
    for i in range(0, len(array)):
        for j in range(0, len(array)):
            if i == j:
                result += array[i][j]
    return result


print("The sum of diagnols of matrix is: {}".format(diagnol_sum(a)))
