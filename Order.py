from Menu import show_menu , menu

orders = []

def add_order():
    while True:
        show_menu()
        print("Enter 0 to go back")

        choice = int(input("Choose number: "))

        if choice == 0:
            break

        elif 1 <= choice <= len(menu):

            product = list(menu)[choice - 1]
            quantity = int(input("Enter quantity: "))

            found = False

            for order in orders:
                if order["product"] == product:
                    order["quantity"] += quantity
                    found = True
                    break

            if not found:
                order = {
                    "product": product,
                    "price": menu[product],
                    "quantity": quantity
                }

                orders.append(order)

            print("Order added successfully!")

        else:
            print("Invalid product number!")


def show_order():

    print("============= Your orders =============")

    for number, item in enumerate(orders , start=1):
        print(f"{number}. {item['product']} | Quantity: {item['quantity']} | Price: {item['price']:,}")

    if len(orders) == 0:
        print("Your order list is empty!")

def remove_order():
    while True:
        show_order()
        print("Enter 0 to go back")

        choice = int(input("Choose number: "))

        if choice == 0:
            break

        elif 1 <= choice <= len(orders):
            order = orders[choice - 1]

            quantity = int(input("Enter quantity: "))

            if quantity < order["quantity"]:
                order["quantity"] -= quantity
                print("Order quantity updated successfully!")

            elif quantity >= order["quantity"]:
                orders.remove(order)
                print("Order removed successfully!")

            else:
                print("Invalid quantity!")

        else:
            print("Invalid product number!")