# Shopping Cart Program

This is a simple console-based shopping cart application written in Python, which reads product data from a CSV file and provides functionality to list products, filter them by categories, add them to a shopping cart, and proceed through a basic checkout process; inn addition, it allows you to choose between a common user and an administrator so that you can add, edit or delete products..

## Features

- **List All Products**: Display all available products from a CSV file.
- **List Products by Category**: Filter products by a specific category.
- **Add Product to Cart**: Select a product by its ID and add it to the shopping cart.
- **View Cart**: Show all products currently in the shopping cart.
- **Checkout**: Input personal and contact details to simulate a checkout process.
- **Add, Edit, and Remove Products**: Managers can add, edit, or remove products from the inventory.

## Project Structure

- `Product`: A class representing a product with attributes like ID, name, category, and price.
- `ProductRepository`: Handles loading products from a CSV file and querying them.
- `ShoppingCart`: Manages the addition of products and checking out items stored in the cart.
- `Checkout`: Simulates the checkout process by collecting user information.
- `AbstractProductManager`: An abstract class that defines the methods for managing product operations, implemented by the Manager class.
- `Manager`: Inherits from AbstractProductManager and provides functionalities to add, edit, and remove products.
- `Client`: Represents a user with permissions to interact with products and the shopping cart.
- `main()`: Provides an interactive menu loop to navigate the features.

## Installation

### Prerequisites

- Python 3.x
- The `products.csv` file should be in the same directory as the script, with columns: `id`, `Product`, `Category`, `Price`.

### Steps

1. **Clone the Repository** (if hosted):

   ```bash
   git clone https://github.com/SantiagoBen1/workshops_advanced_programming.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd workshop-1
   ```

3. **Run the Script**:

   Execute the script using Python:

   ```bash
   python shopping_cart.py
   ```

## Usage

1. **Start the Program**: Run the script to access the menu-driven interface.
2. **Interact with the Application**: Choose options from the menu to list products, filter by category, add to cart, view cart, and proceed to checkout.
3. **Exit the Program**: Choose the quit option from the menu to end the session.

## CSV File Format

Ensure the `products.csv` uses the following column headers:

```
id,Product,Category,Price
```

Example:

```
1,Laptop,System Engineering,1200.0
2,Database Management System,System Engineering,800.0
```


