def model_name(company_name):
    return f"Welcome to {company_name}! Please enter the model name you're interested in:"

def choose_variant(car_company, car_model):
    return f"Welcome to {car_company}, {car_model}! Please choose the variant (Petrol/Diesel):"

def calculate_price(exshowroom_price):
    central_gst = 0.1 * exshowroom_price  # Assuming 10% central GST
    state_gst = 0.1 * exshowroom_price  # Assuming 10% state GST
    insurance = 0.05 * exshowroom_price  # Assuming 5% insurance
    on_road_price = exshowroom_price + central_gst + state_gst + insurance
    return on_road_price

def main():
    # Ask user to choose car company
    company_name = input("Welcome to our car dealership! Please choose a car company (A/B/C): ")

    # Mapping company names to models
    company_models = {
        'A': ['Model_X', 'Model_Y'],
        'B': ['Model_Z', 'Model_W'],
        'C': ['Model_P', 'Model_Q']
    }

    if company_name in company_models:
        # Display available models for chosen car company
        models = company_models[company_name]
        print(model_name(company_name))
        for model in models:
            print("- " + model)

        # Ask user to choose car model
        car_model = input("Enter the model name: ")

        # Check if the entered model is valid
        if car_model in models:
            # Ask user to choose variant
            variant = input(choose_variant(company_name, car_model)).capitalize()

            # Calculate prices
            exshowroom_price = 1000000  # Example ex-showroom price
            on_road_price = calculate_price(exshowroom_price)

            # Display prices
            print(f"Ex-showroom price for {car_model}: {exshowroom_price}")
            print(f"On-road price for {car_model} ({variant} variant): {on_road_price}")

        else:
            print("Invalid model name!")

    else:
        print("Invalid company name!")

if __name__ == "__main__":
    main()
