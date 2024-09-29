import pandas as pd
data_file= "product_data.csv"


def show_data():
    df = pd.read_csv("product_data.csv")

    return df
def get_product(pid):
    df = pd.read_csv("product_data.csv")
    product = df[df["pid"]==int(pid)]

    return product
def add_product(pid,name,description,price,rating):
    df = pd.read_csv("product_data.csv")
    product = [pid,name,description,price,rating]
    new_row_index = len(df.index)
    df.loc[new_row_index]=product
    df.to_csv(data_file,index=False)
    show_tail()
def update_product(pid,new_rating):
    df = pd.read_csv("product_data.csv")
    idx=df[df["pid"]==int(pid)].index
    df.loc[idx,"rating"]=new_rating
    df.to_csv(data_file,index=False)
    print(get_product(pid))
def delete_product(pid):
    print(pid)
    df = pd.read_csv("product_data.csv")
    idx=df[df["pid"] == int(pid)].index
    print("Deleteing ",idx)
    updated_df= df.drop(idx)
    updated_df.to_csv(data_file,index=False)
    show_tail()
def show_tail():
    df = pd.read_csv(data_file)
    print(df.tail())
def main():
    while True:
        print("1. Show All Products")
        print("2. Add New Product")
        print("3. Delete a Product")
        print("4. Update Product Rating")
        print("5. Exit")
        choice = input("Enter Option to continue: ")

        if choice == '1':
            show_data()
        elif choice == '2':
            pid = input("Enter product ID: ")
            name = input("Enter product name: ")
            description = input("Enter product description: ")
            price = float(input("Enter product price: "))
            rating = float(input("Enter product rating (0-5): "))

            add_product(pid,name,description,price,rating)
        elif choice == '3':
            pid = input("Enter product ID: ")
            delete_product(pid)
        elif choice == '4':
            pid = input("Enter product ID: ")
            rating = float(input("Enter product rating (0-5): "))
            update_product(pid,rating)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()

