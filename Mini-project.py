import csv

class Ecommerence:
    def register(self):
        print("!!!!WELCOME TO THE STORE!!!!!")
        print("$$$$$$$$$$$$$$$$$$$Welcome to Registration form $$$$$$$$$$$$$$$$$$$$$$$")
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        phoneno = input("Enter phone number: ")
        pincode = input("Enter pin code: ")    
        city = input("Enter city: ")

        with open('Amazon.csv', 'a', newline="") as file:
            takein = csv.writer(file)
            takein.writerow([self.username, self.password, phoneno, pincode, city])
            print("Registration successful.")

    def login(self):
        while True:
            print("##############Welcome to login form$$$$$$$$$$$$$$$$$$$$$$$$")
            username = input("Enter the username:")
            pwd = input("Enter the password:")
            if username == self.username and pwd == self.password:
                print("Login successful")
                break
            else:
                print("Please enter valid credentials")
obj = Ecommerence()
obj.register()
obj.login()