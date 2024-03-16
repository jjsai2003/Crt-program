from csv import User
from csv import Product
from csv import Cart
from csv import Order

users = {}
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users:
        print("Username already exists. Please choose a different username.")
    else:
        users[username] = User(username, password)
        print("User registered successfully.")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username].password == password:
        print("Login successful.")
        return users[username]
    else:
        print("Invalid username or password.")
        return None

def list_products(products):
    print("Available Products:")
    for product in products:
        print(f"Name: {product.name}, Price: {product.price}, Category: {product.category}, Stock: {product.stock}")

def add_to_cart(cart, products):
    product_name = input("Enter the product name you want to add to cart: ")
    for product in products:
        if product.name == product_name and product.stock > 0:
            cart.add_to_cart(product)
            print(f"{product.name} added to cart.")
            return
    print("Product not found or out of stock.")

def place_order(user, cart):
    order = Order(user, cart)
    total_price = order.generate_bill()
    cart.clear_cart()
    print(f"Order placed successfully. Total amount: {total_price}")

def main():
    products = [
        Product("Laptop", 1000, "Electronics", 10),
        Product("Phone", 500, "Electronics", 20),
        Product("Headphones", 100, "Electronics", 5)
    ]

    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            current_user = login()
            if current_user:
                cart = Cart()
                list_products(products)
                add_to_cart(cart, products)
                place_order(current_user, cart)
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
