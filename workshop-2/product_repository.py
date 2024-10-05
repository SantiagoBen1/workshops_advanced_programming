"""
This module contains the ProductRepository class which manages 
product data by loading products from a CSV file, listing them, 
and filtering them by category.

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
from typing import List
from product import Product


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
            with open(self.filename, newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    product = Product(
                        product_id=row["id"],
                        name=row["Product"],
                        category=row["Category"],
                        price=float(row["Price"]),
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
        return [
            product
            for product in self.products
            if product.category.lower() == category.lower()
        ]
