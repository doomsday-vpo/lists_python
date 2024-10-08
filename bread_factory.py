events = input().split("|")
energy = 100
coins = 100
bakery_is_open = True

for event in events:
    event_items = event.split("-")
    type_of_event = event_items[0]
    event_value = int(event_items[1])
    if type_of_event == "rest":
        initial_energy = energy
        energy += event_value
        if energy > 100:
            energy = 100
        gained_energy = energy - initial_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif type_of_event == "order":
        if energy >= 30:
            energy -= 30
            coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            energy += 50
            print("You had to rest!")
        current_coints = coins

    else:
        if coins >= event_value:
            coins -= event_value
            print(f"You bought {type_of_event}.")
        else:
            bakery_is_open = False
            break
if bakery_is_open:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
else:
    print(f"Closed! Cannot afford {type_of_event}.")
