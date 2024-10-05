"""
This module contains a set of classes to handle
electronic devices using categories, searchs, 
among others functionalities.

Author: Santiago Andrés Benavides Coral <sabenavidesc@udistrital.edu.co>

This file is part of workshop-1.

Workshop-1 is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

Workshop-1 is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with Workshop-1. If not, see <https://www.gnu.org/licenses/>. 
"""

from product_repository import ProductRepository
from shopping_cart import ShoppingCart
from checkout import Checkout
from client import Client
from manager import Manager


def main():
    """Main function to handle user interaction for a product shopping application.

    This method is the entry point for the shopping cart application. It handles
    product listing, product addition to the cart, viewing the cart, and the checkout
    process through a menu-based system. The function interacts with a product
    repository, a shopping cart, and a checkout process.

    The menu options include:
    1. Listing all products.
    2. Listing products by category.
    3. Adding a product to the shopping cart.
    4. Viewing the items in the cart.
    5. Proceeding to checkout.
    6. Adding a new product.
    7. Removing a product.
    8. Editing a product.
    9. Quitting the application.

    Args:
        None

    Returns:
        None: The function runs the menu loop until the user chooses to exit.

    Raises:
        None
    """

    # Ensure the path to 'products.csv' is correct. It should be in the same directory as the script
    product_repo = ProductRepository("products.csv")
    cart = ShoppingCart()
    checkout = Checkout(cart)
    user_type = ""

    while user_type not in ["client", "manager"]:
        user_type = input("Are you a Client or Manager? ").strip().lower()
        if user_type not in ["client", "manager"]:
            print("Invalid user type. Please enter 'Client' or 'Manager'.")

    print(f"You have selected: {user_type.capitalize()}")

    user = Client(product_repo) if user_type == "client" else Manager(product_repo)

    # Menu loop for user interaction
    while True:
        print("\nMenu:")
        print("1. List all products")
        print("2. List products by category")
        print("3. Add product to cart")
        print("4. View cart")
        print("5. Checkout")
        print("6. Add a new product")
        print("7. Remove a product")
        print("8. Edit a product")
        print("9. Quit")

        choice = input("Please select an option: ")

        if choice == "1":
            # List all available products
            print("\nList of all products:")
            for product in product_repo.list_all_products():
                print(product)

        elif choice == "2":
            # List products by specified category
            category = input("\nEnter category name: ")
            products_by_category = product_repo.list_products_by_category(category)
            if products_by_category:
                print(f"\nList of products in category '{category}':")
                for product in products_by_category:
                    print(product)
            else:
                print(f"No products found in category '{category}'.")

        elif choice == "3":
            # Add a product to the cart by ID
            product_id = input("\nEnter product ID to add to cart: ")
            product = next(
                (
                    p
                    for p in product_repo.list_all_products()
                    if p.product_id == product_id
                ),
                None,
            )
            if product:
                cart.add_product(product)
            else:
                print(f"No product found with ID: {product_id}")

        elif choice == "4":
            # View current items in the cart
            if cart.list_cart_items():
                print("\nItems in your cart:")
                for item in cart.list_cart_items():
                    print(item)
            else:
                print("\nYour cart is empty.")

        elif choice == "5":
            # Proceed to checkout
            checkout.process_checkout()

        elif choice == "6":
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            price = float(input("Enter product price: "))
            # Both Client and Manager can call this method
            message = user.add_product(product_id, name, category, price)
            if message:  # Only Managers return a message
                print(message)

        elif choice == "7":
            product_id = input("Enter product ID to remove: ")
            # Both Client and Manager can call this method
            message = user.remove_product(product_id)
            if message:  # Only Managers return a message
                print(message)

        elif choice == "8":
            product_id = input("Enter product ID to edit: ")
            name = input("Enter new product name: ")
            category = input("Enter new product category: ")
            price = float(input("Enter new product price: "))
            # Both Client and Manager can call this method
            message = user.edit_product(product_id, name, category, price)
            if message:  # Only Managers return a message
                print(message)

        elif choice == "9":
            # Exit the application
            if (
                input("Are you sure you want to to exit? (y/n): ").strip().lower()
                == "y"
            ):
                input("Exiting the program. Goodbye!")
                break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
