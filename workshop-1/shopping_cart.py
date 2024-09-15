"""
This module is an example of an abstract class to define a calculator operations.

Copyright (C) 2024  Santiago Andrés Benavides Coral <sabenavidesc@udistrital.edu.co>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import csv
from typing import List

#========== CONCRETE  ==========#

class Product:
    """This class represents a product with an ID, name, category, and price."""
    
    def __init__(self, product_id: str, name: str, category: str, price: float):
        """Initializes a new instance of the Product class

        This method sets up the initial state of a Product object by assigning the given values
        to the instance variables. Each instance represents a product with a unique ID, a name,
        a category, and a price.

        Args:
            product_id (str): Unique identifier for the product.
            name (str): Name of the product.
            category (str): Category to which the product belongs.
            price (float): Price of the product.

        Returns:
            None: This method does not return any value. It initializes the object's attributes.
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        """Returns a string representation of the Product instance.

        This method provides a formatted string that includes the product's ID, name, category,
        and price. It is used to give a description of the Product object, 
        making it easier to understand the instance's attributes in a readable format.

        Returns:
            str: A string containing the product's ID, name, category, and price.
    """
        return f"ID: {self.product_id}, Product: {self.name}, Category: {self.category}, Price: {self.price}"

class ProductRepository:
    """Manages product data loaded from a CSV file."""
    
    def __init__(self, filename: str):
        """Initializes the ProductRepository with a filename and loads the products.

        In this method, the filename of the CSV file containing product data is used to 
        load the list of products into the repository.

        Args:
            filename (str): The path to the CSV file with the product data.

        Returns:
            None: This method initializes the repository with the list of products.
        """

        self.filename = filename
        self.products = self._load_products()

    def _load_products(self) -> List[Product]:
        """Loads products from the CSV file.

        In this method, the products are read from the specified CSV file and parsed 
        into a list of Product objects. If the file is not found or another error occurs, 
        an error message is printed.

        Returns:
            List[Product]: A list containing the products loaded from the file.
        """
        products = []
        try:
            with open(self.filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    product = Product(
                        product_id=row['id'],
                        name=row['Product'],
                        category=row['Category'],
                        price=float(row['Price'])
                    )
                    products.append(product)
        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' was not found.")
        except Exception as e:
            print(f"An error occurred while loading products: {e}")
        return products

    def list_all_products(self) -> List[Product]:
        """Returns a list of all products.

        This method returns the complete list of products that were loaded from the CSV file.

        Returns:
            List[Product]: A list of all products currently loaded in the repository.
        """
        return self.products

    def list_products_by_category(self, category: str) -> List[Product]:
        """Returns a list of products filtered by the specified category.

        This method filters the products by the specified category, performing a case-insensitive
        comparison to return only the products that belong to that category.

        Args:
            category (str): The category to filter the products by.

        Returns:
            List[Product]: A list of products that match the specified category.
        """
        return [product for product in self.products if product.category.lower() == category.lower()]

class ShoppingCart:
    """
    This class manages the shopping cart operations, such as adding products 
    and calculating totals.
    """
    
    def __init__(self):
        """Initializes the ShoppingCart with an empty list of cart items.

        This method sets up the shopping cart by initializing an empty list that will hold 
        the products added to the cart.

        Args:
            None

        Returns:
            None: This method initializes an empty shopping cart.
        """
        self.cart_items: List[Product] = []

    def add_product(self, product: Product):
        """Adds a product to the cart.

        This method takes a product and adds it to the list of items in the cart. 
        It also prints a message indicating that the product was added.

        Args:
            product (Product): The product to be added to the shopping cart.

        Returns:
            None: This method adds the product to the cart and prints a message.
        """
        self.cart_items.append(product)
        print(f"Added {product.name} to cart.")

    def calculate_total(self) -> float:
        """Calculates the total price of items in the cart.

        This method sums up the prices of all products currently in the shopping cart.

        Args:
            None

        Returns:
            float: The total price of all items in the cart.
        """
        return sum(item.price for item in self.cart_items)

    def list_cart_items(self) -> List[Product]:
        """Lists all items currently in the cart.

        This method returns a list of all the products currently added to the shopping cart.

        Args:
            None

        Returns:
            List[Product]: A list of all products in the shopping cart.
        """
        return self.cart_items

class Checkout:
    """Handles the checkout process, including user input for contact details."""
    
    def __init__(self, cart: ShoppingCart):
        """Initializes the Checkout with a shopping cart.

        This method takes a ShoppingCart object as an argument and links it to the 
        checkout process.

        Args:
            cart (ShoppingCart): The shopping cart to be processed during checkout.

        Returns:
            None: Initializes the Checkout instance.
        """
        self.cart = cart

    def process_checkout(self):
        """Processes the checkout by showing cart items, total, and collecting user details.

        This method displays the cart summary including the total price, and collects 
        customer details like name, direction, country, and email through user input.
        If the cart is empty, it informs the user and aborts the process.

        Args:
            None

        Returns:
            None: Completes the checkout process and prints the details.
        """
        if not self.cart.list_cart_items():
            print("Your cart is empty!")
            return

        print("Cart Summary:")
        total = self.cart.calculate_total()
        for item in self.cart.list_cart_items():
            print(item)

        print(f"Total: {total:.2f}")

        # Collecting customer details
        print("\nPlease fill out your checkout details:")
        name = input("Name: ")
        direction = input("Direction: ")
        country = input("Country: ")
        email = input("Email: ")
        
        # Displaying checkout summary
        print("\nCheckout Details:")
        print(f"Name: {name}, Direction: {direction}, Country: {country}, Email: {email}")
        print("Thank you for your purchase!")


#========== CLIENT CLI ==========#

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
    6. Quitting the application.

    Args:
        None

    Returns:
        None: The function runs the menu loop until the user chooses to exit.

    Raises:
        None
    """
    
    # Ensure the path to 'products.csv' is correct. It should be in the same directory as the script
    product_repo = ProductRepository('products.csv')
    cart = ShoppingCart()
    checkout = Checkout(cart)

    # Menu loop for user interaction
    while True:
        print("\nMenu:")
        print("1. List all products")
        print("2. List products by category")
        print("3. Add product to cart")
        print("4. View cart")
        print("5. Checkout")
        print("6. Quit")

        choice = input("Please select an option: ")

        if choice == '1':
            # List all available products
            print("\nList of all products:")
            for product in product_repo.list_all_products():
                print(product)

        elif choice == '2':
            # List products by specified category
            category = input("\nEnter category name: ")
            products_by_category = product_repo.list_products_by_category(category)
            if products_by_category:
                print(f"\nList of products in category '{category}':")
                for product in products_by_category:
                    print(product)
            else:
                print(f"No products found in category '{category}'.")

        elif choice == '3':
            # Add a product to the cart by ID
            product_id = input("\nEnter product ID to add to cart: ")
            product = next((p for p in product_repo.list_all_products() if p.product_id == product_id), None)
            if product:
                cart.add_product(product)
            else:
                print(f"No product found with ID: {product_id}")

        elif choice == '4':
            # View current items in the cart
            if cart.list_cart_items():
                print("\nItems in your cart:")
                for item in cart.list_cart_items():
                    print(item)
            else:
                print("\nYour cart is empty.")

        elif choice == '5':
            # Proceed to checkout
            checkout.process_checkout()

        elif choice == '6':
            # Exit the application
            print("Exiting the program. Goodbye!")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
