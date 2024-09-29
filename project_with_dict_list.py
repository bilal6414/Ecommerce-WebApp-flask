products = {
    1001: ["Laptop", "Laptop has many features", 88, 4.5],
    1002: ["Mobile Phone", "Mobile has many features", 880, 3],
    1003: ["Watch", "Watch has many features", 33, 2]
}

next_product_id = max(products.keys()) + 1 if products else 1001


def showAllProducts():
    if not products:
        print("\nNo products available.\n")
    else:
        print("\n--- All Products ---")
        for product_id, details in products.items():
            print(f"ID: {product_id}, Name: {details[0]}, Description: {details[1]}, Price: {details[2]}, Rating: {details[3]}")
        print()


def addNewProduct():
    global next_product_id
    print("\n--- Add New Product ---")
    product=[]
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = float(input("Enter product price: "))
    rating = float(input("Enter product rating (0-5): "))

    products[next_product_id] = [name,description,price,rating]
    print(f"Product '{name}' added successfully with ID {next_product_id}.\n")

    next_product_id += 1


def deleteProduct():
    print("\n--- Delete Product ---")
    product_id = int(input("Enter product ID to delete: "))

    if product_id in products:
        del products[product_id]
        print(f"Product with ID {product_id} deleted successfully.\n")
    else:
        print("Product ID not found.\n")



def updateProductRating():
    print("\n--- Update Product Rating ---")
    product_id = int(input("Enter product ID to update rating: "))

    if product_id in products:
        new_rating = float(input("Enter new product rating (0-5): "))
        products[product_id][3] = new_rating
        print(f"Rating for product ID {product_id} updated to {new_rating}.\n")
    else:
        print("Product ID not found.\n")



def mainMenu():
    while True:
        print("1. Show All Products")
        print("2. Add New Product")
        print("3. Delete a Product")
        print("4. Update Product Rating")
        print("5. Exit")
        choice = input("Enter Option to continue: ")

        if choice == '1':
            showAllProducts()
        elif choice == '2':
            addNewProduct()
        elif choice == '3':
            deleteProduct()
        elif choice == '4':
            updateProductRating()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")



if __name__ == "__main__":
    mainMenu()
