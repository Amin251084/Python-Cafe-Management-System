from Order import add_order , show_order , orders

def calculate_total():
    total = 0

    for item in orders:
        total += item['price'] * item['quantity']

    return total

def calculate_discount(price):
    if price >= 1000000:
        return price * 0.1
    else:
        return 0

def print_invoice():
    while True:
        print("================ Factor =================")

        for number, item in enumerate(orders, start=1):
            product_total = item['price'] * item['quantity']

            print(f"{number}. {item['product']} | Quantity: {item['quantity']} | Total Price: {product_total:,}")

        factor_price = calculate_total()
        discount = calculate_discount(factor_price)
        final_price = factor_price - discount

        print("-----------------------------------------")
        print(f"Total factor price: {int(factor_price):,}T")
        print(f"Total factor discount: {int(discount):,}T")
        print(f"Total price with discount: {int(final_price):,}T")

        back = input("Enter 0 to go back: ")

        if back == "0":
            break