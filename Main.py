from Menu import show_menu
from Order import add_order, show_order, remove_order
from Billing import print_invoice

main_menu = ["Menu", "New Order", "Orders", "Remove Order", "Factor", "Exit"]

print("=== WELCOME TO CAFE ===")

while True:

    for number, item in enumerate(main_menu , start=1):
        print(f"{number}. {item}")

    choice = int(input("Enter Number: "))

    if choice == 1:
        while True:
            show_menu()

            back = input("Enter 0 to go back: ")

            if back == "0":
                break

    elif choice == 2:
        add_order()

    elif choice == 3:
        while True:
            show_order()
        
            back = input("Enter 0 to go back: ")
        
            if back == "0":
                 break

    elif choice == 4:
        remove_order()

    elif choice == 5:
        print_invoice()

    elif choice == 6:
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")