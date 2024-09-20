#!/usr/bin/env python
# coding: utf-8

# In[4]:


import datetime
x = datetime.datetime.now()

menu = {
    'pizza': 500,
    'burger': 200,
    'samosa': 50,
    'shake': 100,
    'ice cream': 150,
    'fries': 120,
    'coldrinks': 150,
    'water': 50,
    'shawarma': 300,
    'pasta': 250,
    'tacos': 180,
    'spring rolls': 70,
    'chicken wings': 300,
    'salad': 120,
    'nachos': 150,
    'dumplings': 220,
    'grilled cheese sandwich': 180,
    'fruit salad': 130,
    'cupcake': 90,
    'cheesecake': 200,
    'brownie': 110,
    'hot dog': 150,
    'paneer tikka': 250,
    'biryani': 350
}

print("Welcome to MyRestaurant")

print("Our menu is:")
for item, price in menu.items():
    print(f" *{item.capitalize()}: Rs.{price}")

total_order = 0
name = input("What is your name: ")

#track items ordered and their prices
ordered_items = []

#multiple orders using commas, split into list of items
item1 = input(f"Dear sir/maam {name}, what do you want to order? Enter items with commas: ").split(',')

#flags to track if pizza and burger are ordered
burger_ordered = False
pizza_ordered = False

# Loop through each item in the order
for item in item1:
    item = item.strip().lower()  # Strip spaces and convert to lowercase for consistency
    if item in menu:
        total_order += menu[item]
        ordered_items.append((item, menu[item]))  # Append item and price to ordered_items list
        print(f"Your {item} is added")
        if item == 'burger':
            burger_ordered = True
        if item == 'pizza':
            pizza_ordered = True
    else:
        print(f"Sorry, {item} is not available")

#check for the free coldrink offer
if burger_ordered and pizza_ordered:
    print("Since you've ordered both pizza and burger, you get a free coldrink!")
    print("Your coldrink is added to your order for free.")
    ordered_items.append(('coldrinks', 0))  # Add free coldrink to ordered_items

#additional orders
while True:
    order = input("Do you want to order more? (yes/no): ").lower()
    if order == "yes":
        item2 = input("What is your next order? Enter items separated by commas: ").split(',')
        for item in item2:
            item = item.strip().lower()  # Handle each item separately
            if item in menu:
                total_order += menu[item]
                ordered_items.append((item, menu[item]))
                print(f"{item} is also added")
                if item == 'burger':
                    burger_ordered = True
                if item == 'pizza':
                    pizza_ordered = True
            else:
                print(f"Sorry, {item} is not available")
        # Check again for the free coldrink offer
        if burger_ordered and pizza_ordered:
            print("Offer: Since you've ordered both pizza and burger, you get a free coldrink!")
            print("Your coldrink is added to your order for free.")
            ordered_items.append(('coldrinks', 0))  # Add free coldrink
            burger_ordered = False  #reset the flag so that coldrink is not added multiple times
            pizza_ordered = False
    elif order == "no":
        print("Thank you! Have a good day.")
        break
    else:
        print("Invalid input, please enter 'yes' or 'no'.")

#display bill
print("\n--- Your Bill ---")
print(f"Date and Time: {x.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Customer: {name}\n")
print("Items Ordered:")
for item, price in ordered_items:
    print(f" - {item.capitalize()}: Rs.{price}")

#apply discount if applicable
if total_order >= 1500:
    discount = total_order * 0.1  # 10% discount
    before_discount = total_order
    total_order -= discount
    print(f"\nTotal before discount: Rs.{before_discount}")
    print(f"Discount applied: Rs.{discount:.2f}")
    print(f"Total after discount: Rs.{total_order:.2f}")
else:
    print(f"\nTotal bill: Rs.{total_order}")

print("\n--- Thank You! Please come again! ---")

#Greet the customer
def greet(name):
    print(f"Thank you, Mr/Mrs {name}, do come again :)")

greet(name)


# In[ ]:




