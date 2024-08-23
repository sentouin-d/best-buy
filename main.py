from products import Product
from store import Store

# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)

def print_menu() -> None:
    print("    Store Menu")
    print("    ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")

def make_order(store: Store) -> list[tuple[Product, int]]:
    print("When you want to complete the order, enter empty text")
    response = "valid"
    current_sku = 0
    order_list = []

    while (response != ""):
        sku = 0
        if current_sku < 1:
            sku_str = input("Which product # do you want?")
            if len(sku_str) <= 0:
                response = ""
                continue

            if not sku_str.isdigit():
                print("Invalid sku")
                continue

            sku = int(sku_str)
            if sku < 1 or sku >= len(store.products):
                print("Invalid sku")
                continue

            current_sku = sku

        quantity_str = input("What amount do you want?")
        if len(quantity_str) <= 0:
            response = ""
            continue
        
        if not quantity_str.isdigit():
            print("Invalid quantity")
            continue

        quantity = max(int(quantity_str), 0)

        product = store.products[sku - 1]

        if quantity > product.get_quantity():
            print("Not enough items in stock")
            continue

        order_list.append((store.products[sku - 1], quantity))
        print("Product added to cart!")
        current_sku = 0

    return order_list



def display_products(store: Store) -> None:
    products = store.get_all_products()
    print("------")
    for idx, prod in enumerate(products):
        print(f"{idx + 1}. {prod.show()}")
    print("------")

def start(store: Store) -> None:
    option = 0

    while(option < 4):
        print_menu()
        option_str = input("Please choose a number: ")
        if not option_str.isdigit():
            print("Error with your choice! Try again!")
            continue

        option = int(option_str)

        if option == 1:
            display_products(store)

        if option == 2:
            print(f"Total of {store.get_total_quantity()} items in store")

        if option == 3:
            display_products(store)
            cart = make_order(store)
            total = store.order(cart)
            if total > 0:
                print(f"Order made! Total payment: ${total}")

start(best_buy)

