n = 5432
k = []
num = n
while num > 0:
    digit = num % 10
    k.append(digit)
    # print(digit)
    num = num // 10
# print(k)
print("".join(map(str,k)))