"""
This module contains the ShoppingCart class, which is responsible 
for managing a shopping cart. It provides functionalities to add 
products, calculate the total price, and list the items in the cart.

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

from typing import List
from product import Product


class ShoppingCart:
    """
    This class manages the shopping cart operations, such as adding product and calculating totals.
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
