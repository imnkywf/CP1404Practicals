number_of_items = int(input("Enter the number of items: "))
print("Number of items:", number_of_items)

total = 0
for i in range(number_of_items):
    price = float(input("price of item: "))
    total += price

    if total > 100:
        total = total * 0.9

print("Total price for",number_of_items,"is ${:.2f}".format(total))

