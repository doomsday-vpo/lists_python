# Create a program that helps you plan the gifts for your friends and family. First, you are going to receive the gifts you plan on buying on a single line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# •	"OutOfStock {gift}"
# o	Find the gifts with this name in your collection, if any, and change their values to "None".
# •	"Required {gift} {index}"
# o	If the index is valid, replace the gift on the given index with the given gift.
# •	"JustInCase {gift}"
# o	Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with the value "None", separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"
# Input / Constraints
# •	On the 1st line,  you will receive the names of the gifts, separated by a single space.
# •	On the following lines, until the "No Money" command is received, you will be receiving commands.
# •	The input will always be valid.
# Output
# •	Print the gifts in the format described above.

out_of_stock_gift = input().split()
command = input()
# Read the list of gift names
gifts = input().split()

# Read commands until "No Money"
while True:
    command = input().split()
    if command[0] == "No":
        break

    # Handle "OutOfStock" command
    if command[0] == "OutOfStock":
        gift_to_remove = command[1]
        gifts = ["None" if gift == gift_to_remove else gift for gift in gifts]

    # Handle "Required" command
    elif command[0] == "Required":
        gift_to_add = command[1]
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift_to_add

    # Handle "JustInCase" command
    elif command[0] == "JustInCase":
        gift_to_add = command[1]
        gifts[-1] = gift_to_add

# Print the list of gifts, excluding "None"
for gift in gifts:
    if gift != "None":
        print(gift, end=" ")
while command != "No Money":
    command = command.split()
    if command[0] == "OutOfStock":
        for i in range(len(out_of_stock_gift)):
            if out_of_stock_gift[i] == command[1]:
                out_of_stock_gift[i] = "None"
    elif command[0] == "Required":
        if 0 <= int(command[2]) < len(out_of_stock_gift):
            out_of_stock_gift[int(command[2])] = command[1]
    elif command[0] == "JustInCase":
        out_of_stock_gift[-1] = command[1]
    command = input()

for gift in out_of_stock_gift:
    if gift != "None":
        print(gift, end=" ")
print()