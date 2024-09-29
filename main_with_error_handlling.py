import pandas as pd
import os

data_file = "product_data.csv"


def load_data():
    try:
        if os.path.exists(data_file):
            return pd.read_csv(data_file)
        else:
            return pd.DataFrame(columns=["pid", "name", "description", "price", "rating"])
    except Exception as e:
        print(f"Error reading the data file: {e}")


def save_data(df):
    try:
        df.to_csv(data_file, index=False)
    except Exception as e:
        print(f"Error saving the data: {e}")


def show_data():
    df = load_data()
    if df.empty:
        print("No products available.")
    else:
        print(df)


def get_product(pid):
    df = load_data()
    product = df[df["pid"] == int(pid)]
    if product.empty:
        print(f"Product with ID {pid} not found.")
    return product


def add_product(pid, name, description, price, rating):
    df = load_data()
    if not df[df["pid"] == int(pid)].empty:
        print(f"Product with ID {pid} already exists.")
        return

    product = [pid, name, description, price, rating]
    new_row_index = len(df.index)
    df.loc[new_row_index] = product
    save_data(df)
    print("Product added successfully.")
    show_tail()


def update_product(pid, new_rating):
    df = load_data()
    idx = df[df["pid"] == int(pid)].index
    if idx.empty:
        print(f"Product with ID {pid} not found.")
    else:
        df.loc[idx, "rating"] = new_rating
        save_data(df)
        print("Product rating updated.")
        print(get_product(pid))


def delete_product(pid):
    df = load_data()
    idx = df[df["pid"] == int(pid)].index
    if idx.empty:
        print(f"Product with ID {pid} not found.")
    else:
        df = df.drop(idx)
        save_data(df)
        print(f"Product with ID {pid} deleted.")
        show_tail()


def show_tail():
    df = load_data()
    print(df.tail())


def main():
    while True:
        print("\n1. Show All Products")
        print("2. Add New Product")
        print("3. Delete a Product")
        print("4. Update Product Rating")
        print("5. Exit")
        choice = input("Enter Option to continue: ")

        if choice == '1':
            show_data()
        elif choice == '2':
            # Validate input directly within the code
            try:
                pid = int(input("Enter product ID: "))
                name = input("Enter product name: ")
                description = input("Enter product description: ")
                price = float(input("Enter product price: "))
                rating = float(input("Enter product rating (0-5): "))

                if 0 <= rating <= 5:
                    add_product(pid, name, description, price, rating)
                else:
                    print("Rating should be between 0 and 5.")
            except ValueError:
                print("Invalid input. Please enter valid numbers for product ID, price, and rating.")
        elif choice == '3':
            try:
                pid = int(input("Enter product ID: "))
                delete_product(pid)
            except ValueError:
                print("Invalid input. Please enter a valid product ID.")
        elif choice == '4':
            try:
                pid = int(input("Enter product ID: "))
                rating = float(input("Enter product rating (0-5): "))
                if 0 <= rating <= 5:
                    update_product(pid, rating)
                else:
                    print("Rating should be between 0 and 5.")
            except ValueError:
                print("Invalid input. Please enter valid numbers for product ID and rating.")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")
# Get product list
def get_products():
    return load_data().to_dict('records')

if __name__ == '__main__':
    main()
