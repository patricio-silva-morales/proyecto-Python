# 0 1 0 1
# 1 0 1 0
# 0 1 0 1
# 1 0 1 0

for i in range(10):
    for j in range(10):
        print((i + j) % 2, end =" ")
    print()