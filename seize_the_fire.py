fire_list = input().split("#")
water = int(input())
total_effort = 0
total_fire_putout = 0
cell_list = []

for fire in fire_list:
    if fire == "":
        continue
    fire_power, cell_value = fire.split(" = ")
    cell_value = int(cell_value)
    if (fire_power == "High" and (81 <= cell_value <= 125)) or \
            (fire_power == "Medium" and (51 <= cell_value <= 80)) or \
            (fire_power == "Low" and (1 <= cell_value <= 50)):
        if water < cell_value:
            continue
        else:
            water -= cell_value
            cell_list.append(cell_value)
            total_effort += cell_value * 0.25
            total_fire_putout += cell_value

print("Cells:")
for cell in cell_list:
    print(f" - {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire_putout}")
