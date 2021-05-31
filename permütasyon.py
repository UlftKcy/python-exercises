# Verilen listeyi [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] formatına dönüştürme.
num = [1,2,3]
num_set = set(num)
solution = [[]]
for index in range(len(num)) :
    solution = [i + [j] for i in solution for j in num_set.difference(set(i))]
    print(solution)
solution
