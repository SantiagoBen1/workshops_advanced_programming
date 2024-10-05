"""
This module contains the Product class, which represents a product 
with a unique ID, name, category, and price. It is used to handle 
and display information related to individual products.

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
