items = {category: {} for category in input().split(", ")}
count = 0
avg_quality = 0
for _ in range(int(input())):
    line = input().split(" - ")
    category = line[0]
    name = line[1]
    part1, part2 = line[2].split(";")
    quantity = int(part1.split(":")[1])
    quality = int(part2.split(":")[1])
    items[category][name] = {"quantity": quantity, "quality": quality}
    count += quantity
    avg_quality += quality


print(f"Count of items: {count}")
print(f"Average quality: {avg_quality / len(items):.2f}")
for key, val in items.items():
    print(f"{key} -> {', '.join([el for el in val])}")

