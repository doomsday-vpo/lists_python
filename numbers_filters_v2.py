n = int(input())
command_even = "even"
command_odd = "odd"
command_negative = "negative"
command_positive = "positive"

all_numbers = [int(input()) for _ in range(n)]

filtered_numbers = []

command = input()

for num in all_numbers:
    filter_command = (
            (command == command_even and num % 2 == 0) or
            (command == command_odd and num % 2 != 0) or
            (command == command_negative and num < 0) or
            (command == command_positive and num >= 0)
    )
    if filter_command:
        filtered_numbers.append(num)

print(filtered_numbers)
