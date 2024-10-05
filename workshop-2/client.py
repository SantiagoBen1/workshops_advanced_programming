"""
This module contains the Client class which represents a simple 
user in the application. Clients can view products but cannot 
add, remove, or edit them.

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

from abstract_client import AbstractProductManager
from product_repository import ProductRepository


class Client(AbstractProductManager):
    """
    Represents a client user in the application.

    The Client class defines the behavior for a simple user who can view products
    but does not have permissions to add, remove, or edit them. Clients can list
    all available products or filter them by category.

    Attributes:
        product_repo (ProductRepository): The repository that manages product data.

    Methods:
        add_product: Denies permission for clients to add products.
        remove_product: Denies permission for clients to remove products.
        edit_product: Denies permission for clients to edit products.
        list_all_products: Lists all products from the repository.
        list_products_by_category: Lists products filtered by category.
    """

    def __init__(self, product_repo: ProductRepository):
        """
        Initializes the Client with access to the product repository.

        Args:
            product_repo (ProductRepository): The repository used to manage products.
        """
        self.product_repo = product_repo

    def add_product(self, product_id: str, name: str, category: str, price: float):
        """
        Denies permission for clients to add products.

        Clients do not have the authority to add new products. Calling this method
        will result in a permission denied message.

        Args:
            product_id (str): The unique identifier for the product.
            name (str): The name of the product.
            category (str): The category to which the product belongs.
            price (float): The price of the product.

        Returns:
            None
        """
        print("Permission denied: Client cannot add products.")

    def remove_product(self, product_id: str):
        """
        Denies permission for clients to remove products.

        Clients do not have the authority to remove products from the repository.
        Calling this method will result in a permission denied message.

        Args:
            product_id (str): The unique identifier of the product to be removed.

        Returns:
            None
        """
        print("Permission denied: Client cannot remove products.")

    def edit_product(self, product_id: str, name: str, category: str, price: float):
        """
        Denies permission for clients to edit products.

        Clients do not have the authority to modify product details. Calling this method
        will result in a permission denied message.

        Args:
            product_id (str): The unique identifier of the product to be edited.
            name (str): The updated name of the product.
            category (str): The updated category of the product.
            price (float): The updated price of the product.

        Returns:
            None
        """
        print("Permission denied: Client cannot edit products.")

    def list_all_products(self):
        """
        Lists all products available in the repository.

        Clients can view all products currently available in the repository.

        Args:
            None

        Returns:
            list: A list of all products stored in the repository.
        """
        return self.product_repo.list_all_products()

    def list_products_by_category(self, category: str):
        """
        Lists products filtered by a specified category.

        Clients can filter products by a category and view the products
        belonging to that category.

        Args:
            category (str): The category to filter products by.

        Returns:
            list: A list of products that match the specified category.
        """
        return self.product_repo.list_products_by_category(category)
