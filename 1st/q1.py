class ECommerceStore:
    def __init__(self):
        self.categories = {}

    def create_category(self, category_name):
        if category_name in self.categories:
            print(f"Category '{category_name}' already exists.")
        else:
            self.categories[category_name] = []
            print(f"Category '{category_name}' created successfully.")

    def add_item(self, category_name, item_name):
        if category_name not in self.categories:
            print(f"Category '{category_name}' does not exist. Please create it first.")
        else:
            self.categories[category_name].append(item_name)
            print(f"Item '{item_name}' added to category '{category_name}'.")

    def display_items(self):
        if not self.categories:
            print("No categories or items available.")
        else:
            print("\nItems by Category:")
            for category, items in self.categories.items():
                print(f"- {category}: {', '.join(items) if items else 'No items'}")

# Main execution
def main():
    store = ECommerceStore()

    while True:
        print("\nE-Commerce Store Management")
        print("1. Create Category")
        print("2. Add Item to Category")
        print("3. Display Items by Category")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            category_name = input("Enter the category name: ")
            store.create_category(category_name)
        elif choice == '2':
            category_name = input("Enter the category name: ")
            item_name = input("Enter the item name: ")
            store.add_item(category_name, item_name)
        elif choice == '3':
            store.display_items()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
