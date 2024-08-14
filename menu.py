# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []



# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order == True:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input("Please select an item number. ")
          # print(f"menu items dictionary: {menu_items}")
            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                # Convert the menu selection to an integer4
                menu_selection = int(menu_selection)

                # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items.keys():
                    # Store the item name as a variable
                    item_name = menu_items[menu_selection]["Item name"]
                   
                    # Ask the customer for the quantity of the menu item
                    item_quantity = input(f"You chose {item_name}. How many do do want? ")

                    # Check if the quantity is a number, default to 1 if not
                    if item_quantity.isdigit():
                         item_quantity = int(item_quantity)
                         print(f"Okay got it, you want {item_quantity} of the {item_name}.")
                         item_price = menu_items[menu_selection]["Price"]
                         print(f"the price of your selection is ${item_price}")

                    else:
                        item_quantity = 1
                        print(f"That is not a valid quantity, you will get {item_quantity} {item_name}")
                    # Add the item name, price, and quantity to the order list
                    order = {
                        "Item name": item_name,
                        "Price": item_price,
                        "Quantity": item_quantity
                    }    
                    order_list.append(order)
                    #print(order_list)                                 #############test
                    # Tell the customer that their input isn't valid
                else:
                     print("Error: That is not a valid item number.") 

                # Tell the customer they didn't select a menu option
            else:
                 print("Error: That is not a valid item number")
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")


  
    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        keep_ordering = keep_ordering.lower()
        #print(keep_ordering)
        # 5. Check the customer's input           
        match keep_ordering:
                 # Keep ordering
            case "y":
                print("Please continue ordering.")
                place_order = True
                break
               
            case "n":
                # Since the customer decided to stop ordering, thank them for
                # their order
                print(" ") #skipping a line to make it look nice
                print("Thank you for your order!")
                place_order = False
                break
                    
            case _:
                # Tell the customer to try again
                print("Try again. Please respond with a (Y)es or a (N)o.")                     

               
                # Exit the keep ordering question loop

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order

# makings lists for step 11
price_list = []
quantity_list = []


for item in order_list:
    
    # 7. Store the dictionary items as variables
    name, price, quantity = item["Item name"], item["Price"], item["Quantity"]
    #print(f"Item name is {name}. Item price is {price}. Item quantity is {quantity}.") #############test
    price_list.append(price) 
    quantity_list.append(quantity)

    # 8. Calculate the number of spaces for formatted printing
    num_name_spaces = 26 - len(name)
    num_price_spaces = 6 - len(str(price))
    
    # 9. Create space strings
    name_spaces = " " * num_name_spaces
    price_spaces = " " * num_price_spaces

    # 10. Print the item name, price, and quantity
    print(f"{name}{name_spaces}| ${price:.2f}{price_spaces}| {quantity}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
price_per_order = [x * y for x,y in zip(price_list, quantity_list)] 
final_price = sum(price_per_order)

# and print the prices.
print(" ") #for a blank line
print(f"Your total is ${final_price:.2f}")
print("Enjoy your meal!")
