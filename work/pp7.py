items=input("write fruit name: ").split()
unique_item = {"apple", "banana", "orange", "mango"}
for fruit in items:
    if fruit in unique_item:
        print(fruit," Is already in Unique items")
        break
    else:
        unique_item.add(fruit)
        print(unique_item)