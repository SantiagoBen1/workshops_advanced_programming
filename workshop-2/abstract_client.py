"""
This module contains the AbstractProductManager class which defines 
the behavior for managing products in the application. It serves as 
an abstract base class for the Client and Manager classes.

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

from abc import ABC, abstractmethod


class AbstractProductManager(ABC):
    """
    Abstract base class for managing products.

    This class defines the core operations for managing products such as
    adding, removing, and editing products. It serves as the base class for
    Client and Manager, ensuring that both classes provide concrete implementations
    of these methods.

    Methods:
        add_product: Abstract method for adding a product.
                     To be implemented by subclasses.
        remove_product: Abstract method for removing a product.
                        To be implemented by subclasses.
        edit_product: Abstract method for editing a product's details.
                      To be implemented by subclasses.

    Usage:
        This class cannot be instantiated directly. It should be subclassed by
        specific product manager classes (e.g., Client, Manager) that provide
        concrete implementations of the abstract methods.
    """

    @abstractmethod
    def add_product(self, product_id: str, name: str, category: str, price: float):
        """
        Adds a new product to the product repository.

        This method should be implemented in subclasses to handle the logic for
        adding a product. It takes in the product's ID, name, category, and price.

        Args:
            product_id (str): The unique identifier for the product.
            name (str): The name of the product.
            category (str): The category to which the product belongs.
            price (float): The price of the product.

        Returns:
            None
        """

    @abstractmethod
    def remove_product(self, product_id: str):
        """
        Removes a product from the product repository.

        This method should be implemented in subclasses to handle the logic for
        removing a product by its ID.

        Args:
            product_id (str): The unique identifier of the product to be removed.

        Returns:
            None
        """

    @abstractmethod
    def edit_product(self, product_id: str, name: str, category: str, price: float):
        """
        Edits the details of an existing product.

        This method should be implemented in subclasses to handle the logic for
        updating the name, category, and price of a product based on its ID.

        Args:
            product_id (str): The unique identifier of the product to be edited.
            name (str): The updated name of the product.
            category (str): The updated category of the product.
            price (float): The updated price of the product.

        Returns:
            None
        """
