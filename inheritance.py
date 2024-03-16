"""#class Data_Science:
 #   def __init__(self,f_name,operations,f_id):
  #      self.name  = name
   ##    self.id = no
#def info():
 #   print("Faculty","Details")
  #  print("Name",self.f_name)
   # print("Department",self.dept)
    #print("Id:",self.no)
#class Data_Science:
#obj = Data_Science("Saiee","Ds",4448)
#obj.info()
#create a class of name Placements which has functio info which displays no of placements.
#create another class of name Department with function display which will display the names of thr department present in the college.
#Create calss Pragati with the functon welcome which displays the msg welcome to pragati Engineering college we are glad to here.#
#Pragati class should also  displays the details about depatments anfd placements."""
"""class Placements:
    def info(self):
        print("This year 2024 placements are 623 and counting................")
class Departments:
    def display(self):
        print("####################The depatments of the Pragti Engineering College are:#####################")
        print("DS")
        print("CSE")
        print("ECE")
        print("AI")
        print("MECH")
        print("CIVIL")
        print("CS")
        print("ML")
class Pragati:
    def welcome(self):
        print("****************Welcome to the Pragati Engineering College*******************")
        
obj1 = Placements()
obj1.info()
obj2 = Departments()
obj3 = Pragati()
obj3.welcome()
obj2.display()"""
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Product:
    def __init__(self, name, price, category, stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product):
        self.items.append(product)

    def clear_cart(self):
        self.items = []

class Order:
    def __init__(self, user, cart):
        self.user = user
        self.cart = cart

    def generate_bill(self):
        total = sum(product.price for product in self.cart.items)
        return total

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

def list_products():
    print("Available Products:")
    for product in products:
        print(f"Name: {product.name}, Price: {product.price}, Category: {product.category}, Stock: {product.stock}")

def add_to_cart(cart):
    product_name = input("Enter the product name you want to add to cart: ")
    for product in products:
        if product.name.lower() == product_name.lower() and product.stock > 0:
            cart.add_to_cart(product)
            print(f"{product.name} added to cart.")
            return
    print("Product not found or out of stock.")

def place_order(user, cart):
    order = Order(user, cart)
    total_price = order.generate_bill()
    cart.clear_cart()
    print(f"Order placed successfully. Total amount: {total_price}")

users = {}
products = [
    Product("Laptop", 1000, "Electronics", 10),
    Product("Phone", 500, "Electronics", 20),
    Product("Headphones", 100, "Electronics", 5)
]

while True:
    print("\n1. Register\n2. Login\n3. View Products\n4. Add to Cart\n5. Place Order\n6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        register()
    elif choice == '2':
        current_user = login()
        if current_user:
            cart = Cart()
    elif choice == '3':
        list_products()
    elif choice == '4':
        if not current_user:
            print("Please login first.")
        else:
            add_to_cart(cart)
    elif choice == '5':
        if not current_user:
            print("Please login first.")
        elif not cart.items:
            print("Your cart is empty. Please add items to your cart first.")
        else:
            place_order(current_user, cart)
    elif choice == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
1