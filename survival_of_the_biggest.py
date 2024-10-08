numbers = input().split()
numbers = [int(number) for number in numbers]
count = int(input())

for num in range(count):
    numbers.remove(min(numbers))

print(*numbers, sep=", ")