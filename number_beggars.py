money_as_string = input().split(", ")
number_of_beggars = int(input())
#money_as_integer = [int(money) for money in money_as_string]

money_as_integer = []
for money in money_as_string:
    money_as_integer.append(int(money))

final_list = []
for i in range(number_of_beggars):
    sum = 0
    for j in range(i, len(money_as_integer), number_of_beggars):
        sum += money_as_integer[j]
    final_list.append(sum)
print(final_list)