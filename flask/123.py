max = 0
min = 10 ** 10
k = 0
for i in range(2476, 7857):
    if i  % 2 == 0 and i % 8 != 0 and (i % 1000) // 100:
        if i > max:
            max = i
        if i < min:
            min = i
        k += 1
print(k, (min + max) // 2)