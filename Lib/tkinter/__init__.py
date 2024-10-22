import tkinter as tk
from tkinter import messagebox

# Food menu with items and their prices
food_menu = {
    'Green Canteen': {
        'Chole Bhature': 100.00,
        'Chole Chawal': 50.00,
        'Rajma Chawal': 50.00,
        'Puri Sabji': 50.00,
        'Chilli Potato': 80.00,
        'Spring Roll': 60.00,
        'Chowmein': 60.00
    },
    'Red Canteen': {
        'Samosa': 15.00,
        'Paneer Roll': 80.00,
        'Chowmein Roll': 40.00,
        'Egg Roll': 70.00,
        'Veg Roll': 50.00,
        'Masala Maggi': 50.00,
        'Vegetable Maggi': 40.00
    },
    'Yellow Canteen': {
        'Cheese Sandwich': 45.00,
        'Sandwich': 30.00,
        'Cold Drink': 40.00,
        'Lassi': 25.00,
        'Smoodh': 10.00,
        'Chips': 20.00,
        'Oreo': 10.00
    },
    'Cafe de latte': {
        'Ice Cream': 30.00,
        'Brownie': 50.00,
        'Cold Coffee': 50.00,
        'Burger': 40.00,
        'Pizza Slice': 40.00
    }
}

# Order cart to hold items
order_cart = []

# Function to add item to the cart
def add_to_cart(item, price):
    order_cart.append((item, price))
    messagebox.showinfo("Item Added", f"{item} added to your cart.")

# Function to view the cart
def view_cart():
    if not order_cart:
        messagebox.showinfo("Cart", "Your cart is empty.")
    else:
        cart_details = "\n".join([f"{item} - ₹{price}" for item, price in order_cart])
        total = sum(price for _, price in order_cart)
        cart_details += f"\n\nTotal: ₹{total}"
        messagebox.showinfo("Your Cart", cart_details)

# Function to checkout
def checkout():
    if not order_cart:
        messagebox.showinfo("Cart", "Your cart is empty. Add items to checkout.")
    else:
        total = sum(price for _, price in order_cart)
        messagebox.showinfo("Checkout", f"Your total is: ₹{total}\nPay Cash At The Counter \nThank you for your order!")
        order_cart.clear()

# Function to display items for a selected category
def display_items(category):
    items_window = tk.Toplevel()
    items_window.title(f"{category} Menu")
    items_window.geometry("400x400")

    label = tk.Label(items_window, text=f"{category} Menu", font=("Arial", 16))
    label.pack(pady=10)

    for item, price in food_menu[category].items():
        button = tk.Button(items_window, text=f"{item} - ₹{price}", font=("Arial", 14),
                           command=lambda i=item, p=price: add_to_cart(i, p))
        button.pack(padx=10, pady=5)

# Main application window
def kiosk_food_ordering_system():
    root = tk.Tk()
    root.title("SRM Food Order")
    root.geometry("500x500")

    label = tk.Label(root, text="Welcome to SRM Canteen", font=("Arial", 18))
    label.pack(pady=20)

    # Buttons for food categories
    for category in food_menu.keys():
        button = tk.Button(root, text=category, font=("Arial", 16),
                           command=lambda c=category: display_items(c))
        button.pack(pady=10, padx=10)

    # View Cart button
    view_cart_button = tk.Button(root, text="View Cart", font=("Arial", 16), command=view_cart)
    view_cart_button.pack(pady=20)

    # Checkout button
    checkout_button = tk.Button(root, text="Checkout", font=("Arial", 16), command=checkout)
    checkout_button.pack(pady=10)

    root.mainloop()

# Start the application
kiosk_food_ordering_system()
