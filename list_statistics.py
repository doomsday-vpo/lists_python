n = int(input())

positive = []
negative = []

#list filling
for x in range(n):
    current_number = int(input())

    if current_number >= 0:
        positive.append(current_number)
    else:
        negative.append(current_number)

#count calculation
count_positive = len(positive)
sum_negative = sum(negative)

#printing
print(positive)
print(negative)
print(f"Count of positives: {count_positive}")
print(f"Sum of negatives: {sum_negative}")
