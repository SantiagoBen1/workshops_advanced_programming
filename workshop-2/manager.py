"""
This module contains the Manager class which represents a user 
with enhanced permissions to manage products in the application. 
Managers can add, remove, and edit products.

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

import csv
from abstract_client import AbstractProductManager
from product_repository import ProductRepository
from product import Product


class Manager(AbstractProductManager):
    """
    Represents a manager user with elevated permissions.

    The Manager class defines behavior for users who can add,
    remove, and edit products in the product repository. Managers
    also have the ability to save changes to the CSV file that stores
    product data.

    Attributes:
        product_repo (ProductRepository): The repository that manages product data.

    Methods:
        add_product: Adds a new product to the repository.
        remove_product: Removes an existing product from the repository.
        edit_product: Edits an existing product's details.
        _save_products: Saves the current list of products to a CSV file.
    """

    def __init__(self, product_repo: ProductRepository):
        """
        Initializes the Manager with access to the product repository.

        Args:
            product_repo (ProductRepository): The repository used to manage products.
        """
        self.product_repo = product_repo

    def add_product(self, product_id: str, name: str, category: str, price: float):
        """
        Adds a new product to the repository.

        This method allows the manager to create a new product with the given details
        and append it to the product repository. After adding the product, it is saved
        to the CSV file.

        Args:
            product_id (str): The unique identifier for the new product.
            name (str): The name of the new product.
            category (str): The category of the new product.
            price (float): The price of the new product.

        Returns:
            str: A confirmation message indicating that the product was added successfully.
        """
        new_product = Product(product_id, name, category, price)
        self.product_repo.products.append(new_product)
        self._save_products()
        return f"Product '{name}' with id '{product_id}' added successfully."

    def remove_product(self, product_id: str):
        """
        Removes a product from the repository.

        This method allows the manager to remove a product from the repository based on
        its unique ID. After removal, the product list is updated in the CSV file.

        Args:
            product_id (str): The unique identifier of the product to be removed.

        Returns:
            str: A confirmation message indicating that the product was removed successfully.
        """
        self.product_repo.products = [
            product
            for product in self.product_repo.products
            if product.product_id != product_id
        ]
        self._save_products()
        return f"Product with id '{product_id}' removed successfully"

    def edit_product(self, product_id: str, name: str, category: str, price: float):
        """
        Edits the details of an existing product.

        This method allows the manager to update the name, category, and price of
        an existing product based on its unique ID. The changes are saved to the
        CSV file after updating the product details.

        Args:
            product_id (str): The unique identifier of the product to be edited.
            name (str): The updated name of the product.
            category (str): The updated category of the product.
            price (float): The updated price of the product.

        Returns:
            str: A confirmation message indicating that the product was edited successfully,
                 or a message indicating that the product was not found.
        """
        for product in self.product_repo.products:
            if product.product_id == product_id:
                product.name = name
                product.category = category
                product.price = price
                self._save_products()
                return f"Product '{name}' with id '{product_id}' edited successfully"

        return f"Product with ID {product_id} not found."

    def _save_products(self):
        """
        Saves the current list of products to a CSV file.

        This method writes the current state of the product list in the repository
        to a CSV file, ensuring that any changes made by the manager are persisted.
        If an error occurs during the file operation, an error message is displayed.

        Args:
            None

        Returns:
            None
        """
        try:
            with open(self.product_repo.filename, "w", newline="") as csvfile:
                fieldnames = ["id", "Product", "Category", "Price"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for product in self.product_repo.products:
                    writer.writerow(
                        {
                            "id": product.product_id,
                            "Product": product.name,
                            "Category": product.category,
                            "Price": product.price,
                        }
                    )
        except Exception as e:
            print(f"Error saving products to file: {e}")
