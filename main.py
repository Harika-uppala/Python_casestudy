class MiraApp: 
    def __init__(self):
        
        self.products = [
            {"pid": 101, "name": "Laptop", "category": "Electronics", "price": 60000},
            {"pid": 102, "name": "Phone", "category": "Electronics", "price": 30000},
            {"pid": 103, "name": "Shoes", "category": "Fashion", "price": 2000},
        ]


    def get_all_products(self):
        for product in self.products:
            print(product)


    def add_product(self):
        pid = int(input("Enter Product ID: "))
        name = input("Enter Product Name: ")
        category = input("Enter Product Category: ")
        price = float(input("Enter Product Price: "))
        new_product = {"pid": pid, "name": name, "category": category, "price": price}
        self.products.append(new_product)
        print(f"Product {name} added successfully!")

    # Method to update an existing product by PID
    def update_product(self):
        pid = int(input("Enter Product ID to update: "))
        for product in self.products:
            if product["pid"] == pid:
                name = input("Enter new name (leave empty to skip): ")
                category = input("Enter new category (leave empty to skip): ")
                price = input("Enter new price (leave empty to skip): ")
                if name:
                    product["name"] = name
                if category:
                    product["category"] = category
                if price:
                    product["price"] = float(price)
                print(f"Product {pid} updated successfully!")
                return
        print(f"Product {pid} not found!")

    # Method to delete a product by PID
    def delete_product(self):
        pid = int(input("Enter Product ID to delete: "))
        self.products = [product for product in self.products if product["pid"] != pid]
        print(f"Product {pid} deleted successfully!")

    # Method to get product by PID
    def get_product_by_pid(self):
        pid = int(input("Enter Product ID: "))
        for product in self.products:
            if product["pid"] == pid:
                print(product)
                return
        print(f"Product {pid} not found!")

    # Method to get products by category
    def get_products_by_category(self):
        category = input("Enter Product Category: ")
        category_products = [product for product in self.products if product["category"].lower() == category.lower()]
        if category_products:
            for product in category_products:
                print(product)
        else:
            print(f"No products found in category {category}.")

    # Method to get products between a price range
    def get_products_between_prices(self):
        min_price = float(input("Enter minimum price: "))
        max_price = float(input("Enter maximum price: "))
        range_products = [product for product in self.products if min_price <= product["price"] <= max_price]
        if range_products:
            for product in range_products:
                print(product)
        else:
            print(f"No products found between {min_price} and {max_price}.")

    # Method to display menu and process user selection
    def menu(self):
        while True:
            print("\nMira App - Product Management")
            print("1. Add Product")
            print("2. Update Product")
            print("3. Delete Product")
            print("4. Get Product by PID")
            print("5. Get All Products")
            print("6. Get Product by Category")
            print("7. Get Products between Prices")
            print("8. Exit")

            choice = int(input("Choose an option (1-8): "))
            
            if choice == 1:
                self.add_product()
            elif choice == 2:
                self.update_product()
            elif choice == 3:
                self.delete_product()
            elif choice == 4:
                self.get_product_by_pid()
            elif choice == 5:
                self.get_all_products()
            elif choice == 6:
                self.get_products_by_category()
            elif choice == 7:
                self.get_products_between_prices()
            elif choice == 8:
                print("Exiting Mira App.")
                break
            else:
                print("Invalid option, please choose again.")


# Create an instance of MiraApp and start the menu
app = MiraApp()
app.menu()
