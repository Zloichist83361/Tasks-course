numbers = 0
a = int(input())
for i in range(1, a+1):
    if a % i == 0:
        numbers = numbers + 1
        print(i, end=" ")
print()
if numbers > 2:
    print('простое')
else:
    print('нет')
