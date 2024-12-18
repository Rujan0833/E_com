from prettytable import PrettyTable

# Define the product list
products = [
    {'name': 'iPhone 13', 'price': 999},
    {'name': 'Samsung Galaxy S21', 'price': 799},
    {'name': 'Google Pixel 6', 'price': 699},
    {'name': 'iPad Air', 'price': 599},
    {'name': 'Microsoft Surface Laptop 4', 'price': 999}
]

# Define an empty cart
cart = []

# Function to display the product list
def display_products():
    table = PrettyTable()
    table.field_names = ["No.", "Product Name", "Price ($)"]
    for i, product in enumerate(products):
        table.add_row([i + 1, product['name'], product['price']])
    print("\nProduct List:")
    print(table)

# Function to display the cart contents
def display_cart():
    if not cart:
        print("\nYour cart is empty.")
    else:
        print("\nCart:")
        total = 0
        table = PrettyTable()
        table.field_names = ["Product Name", "Price ($)"]
        for product in cart:
            table.add_row([product['name'], product['price']])
            total += product['price']
        print(table)
        print(f"Total: ${total}")

# Main program loop
while True:
    display_products()
    print("\nEnter the number of the product you want to add to your cart (or enter '0' to exit):")

    # Get user input
    selection = input("Your choice: ")

    # Exit if the user enters 0
    if selection == '0':
        break

    # Validate input
    try:
        selection = int(selection)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Check if the selection is within the valid range
    if 1 <= selection <= len(products):
        product = products[selection - 1]
        cart.append(product)
        print(f"\n{product['name']} has been added to your cart.")
    else:
        print(f"Invalid selection. Please choose a number between 1 and {len(products)}.")

# Display final cart contents
print("\nThank you for shopping with us!")
display_cart()
