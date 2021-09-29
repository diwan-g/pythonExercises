#Given a list and steps (int) variable, Perform right rotation of the given list
# eg: [1,2,3,4,5,6] -> 1 right rotation -> [6,1,2,3,4,5]
# 2 right rotation -> [5,6,1,2,3,4]

lst = [1,2,3,4,5,6]
n = len(lst)
steps = 5
for _ in range(steps):
    key = lst[-1]

    for i in range(n-1,0,-1):
        lst[i] = lst[i-1]

    lst[0] = key

print(lst)

