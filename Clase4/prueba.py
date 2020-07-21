fibonacci = [1] * 2
# 1 1

# 1 1 2 3 5 8 13

fibonacci.append(fibonacci[0] + fibonacci[1])
# 1 1 2

fibonacci.append(fibonacci[1] + fibonacci[2])
#1 1 2 3

fibonacci.append(fibonacci[2] + fibonacci[3])
#1 1 2 3 5

fibonacci.append(fibonacci[3] + fibonacci[4])
#1 1 2 3 5 8

fibonacci.append(fibonacci[4] + fibonacci[5])
#1 1 2 3 5 8 13

print(fibonacci)