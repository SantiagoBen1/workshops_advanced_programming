"""
This module contains the Checkout class which handles the
final process of purchasing products from the shopping cart,
including collecting customer information and displaying
order summaries.

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

from shopping_cart import ShoppingCart


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
        print(
            f"Name: {name}, Direction: {direction}, Country: {country}, Email: {email}"
        )
        print("Thank you for your purchase!")
