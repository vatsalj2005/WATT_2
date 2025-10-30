"""
Inventory Management System
A simple system to track inventory items and quantities.
"""

import json
from datetime import datetime


# Global variable for stock data
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add item to inventory with specified quantity."""
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove specified quantity of item from inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError as e:
        print(f"Item {item} not found in inventory: {e}")


def get_qty(item):
    """Get quantity of specified item."""
    return stock_data[item]


def load_data(file="inventory.json"):
    """Load inventory data from JSON file."""
    with open(file, "r", encoding='utf-8') as file_handle:
        global stock_data
        stock_data = json.loads(file_handle.read())


def save_data(file="inventory.json"):
    """Save inventory data to JSON file."""
    with open(file, "w", encoding='utf-8') as file_handle:
        file_handle.write(json.dumps(stock_data))


def print_data():
    """Print all inventory items and quantities."""
    print("Items Report")
    for item, quantity in stock_data.items():
        print(item, "->", quantity)


def check_low_items(threshold=5):
    """Check for items with quantity below threshold."""
    result = []
    for item, quantity in stock_data.items():
        if quantity < threshold:
            result.append(item)
    return result


def main():
    """Main function to demonstrate inventory system functionality."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, 10)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print('eval used')


if __name__ == "__main__":
    main()
