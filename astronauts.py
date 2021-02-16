candidate = 0
min_candidate = 150
max_candidate = 190
a = input()
while a != '!':
    a: int = int(a)
    if a >= 150 and a <= 190:
        candidate += 1
        if a < min_candidate:
            min_expectan = a
        if a > max_candidate:
            max_candidate = a
    a = input()

print(candidate)
print(min_candidate, max_candidate)
