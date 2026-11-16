menu = {
"Coffee": 80000,
"Tea": 50000,
"Cake": 120000,
"Latte": 100000}

def show_menu():
    
    print("===== CAFE MENU =====")

    for number, (product, price) in enumerate(menu.items() , start=1):
        print(f"{number}.{product}: {price:,}")