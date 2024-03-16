from user import User
from product import Product
from cart import Cart
from order import Order

users = {"user1": User("user1", "password1")}
products = [
    Product("Laptop", 1000, "Electronics", 10),
    Product("Phone", 500, "Electronics", 20),
    Product("Headphones", 100, "Electronics", 5)
]

def register(username, password):
    if username not in users:
        users[username] = User(username, password)
        print("User registered successfully.")
    else:
        print("Username already exists.")

def login(username, password):
    if username in users and users[username].password == password:
        print("Login successful.")
        return users[username]
    else:
        print("Invalid username or password.")
        return None

def list_products():
    for product in products:
        print(f"Name: {product.name}, Price: {product.price}, Category: {product.category}, Stock: {product.stock}")

def add_to_cart(cart, product_name):
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

# Sample usage
if __name__ == "__main__":
    current_user = login("user1", "password1")
    if current_user:
        user_cart = Cart()
        list_products()
        add_to_cart(user_cart, "Laptop")
        add_to_cart(user_cart, "Phone")
        place_order(current_user, user_cart)
