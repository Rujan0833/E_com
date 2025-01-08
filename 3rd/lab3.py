from tabulate import tabulate

products = {
    1: {"name": "Laptop", "price": 800},
    2: {"name": "Phone", "price": 500},
    3: {"name": "Headphones", "price": 100},
    4: {"name": "Keyboard", "price": 50},
}

cart = []
purchased_items = []

def display_products():
    print("\nAvailable Products:")
    for id, details in products.items():
        print(f"{id}. {details['name']} - ${details['price']}")

def display_cart():
    if not cart:
        print("\nYour cart is empty!")
    else:
        print("\nItems in your cart:")
        total = 0
        for item in cart:
            print(f"{item['name']} - ${item['price']}")
            total += item["price"]
        print(f"Total Price: ${total}")

def add_to_cart():
    try:
        product_id = int(input("\nEnter the product ID to add to the cart: "))
        if product_id in products:
            cart.append(products[product_id])
            print(f"{products[product_id]['name']} has been added to your cart.")
        else:
            print("Invalid product ID!")
    except ValueError:
        print("Please enter a valid number!")

def checkout():
    if not cart:
        print("\nYour cart is empty! Add items before checking out.")
        return
    display_cart()
    purchased_items.extend(cart)  # Store purchased items
    print("\nThank you for shopping with us!")
    cart.clear()

def show_purchased_items():
    if not purchased_items:
        print("\nNo items were purchased.")
    else:
        table = [[i+1, item['name'], item['price']] for i, item in enumerate(purchased_items)]
        print("\nPurchased Items:")
        print(tabulate(table, headers=["S.N.", "Item Name", "Price"], tablefmt="grid"))

def main():
    while True:
        print("\nMenu:")
        print("1. Display Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_products()
        elif choice == "2":
            display_products()
            add_to_cart()
        elif choice == "3":
            display_cart()
        elif choice == "4":
            checkout()
        elif choice == "5":
            print("Exiting the program. Here is the summary of your purchases:")
            show_purchased_items()
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
