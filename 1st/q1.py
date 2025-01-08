categories = {}

def add_item(category, item):
    if category in categories:
        categories[category].append(item)
    else:
        categories[category] = [item]

def display_categories():
    for category, items in categories.items():
        print(f"{category}:")
        for item in items:
            print(f"- {item}")

add_item("Clothing", "T-Shirt")
add_item("Clothing", "Jeans")
add_item("Electronics", "Smartphone")
add_item("Electronics", "Laptop")
add_item("Home", "Furniture")
add_item("Home", "Kitchenware")
display_categories()
