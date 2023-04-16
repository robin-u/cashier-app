class Transaction:
    # A list of dictionary to store item temporarily 
    cart_of_items = dict()

    def __init__(self, customer_name, customer_id):
        self.customer_name = customer_name
        self.customer_id = customer_id
        
    # Customer input a new item to the transaction
    def add_item(self,
                items: list[str],
                quantities: list[int],
                prices: list[float],
                cart: dict[str, dict[str, int or float]] = cart_of_items) -> dict[str, dict[str, int or float]]:
        """
        Add new item with the item quantity & price to the transaction
        
        Args:
            items(list): A list of string containing the name of item(s)
            quantity(list): A list of quantity of item, respective to items(list)
            price(list): A list of of price of item, respective to items(list)
            cart(dict): A dictionary representing the key as item name and\
                        its values to inform the quantity and price per item
        
        Returns:
            cart_of_items(dict): Update the current cart with new item(s)

        """
        
        for item, quantity, price in zip(items, quantities, prices):
            if item in cart:
                cart[item]['quantity'] += quantity
            else:
                cart[item] = {'quantity': quantity, 'price': price}
        
        print(f"{item} has been added to the cart!")
        return self.cart_of_items

    # Customer updates the current item name to a new one
    def update_item_name(current_name, new_name):
        return 1

    # Customer updates the current quantity of the item
    def update_item_qty(current_qty, new_qty):
        return 1

    # Customer updates the current price of the item
    def update_item_price(current_price, new_price):
        return 1

    # Customer deletes an item from the current transaction
    def delete_item(item_name):
        return 1

    # Customer resets the whole transaction and starts from a new empty transaction
    def reset_transaction():
        return 1

    # Customer check their order
    def check_order():
        """
        Check if customer order list (item name, qty, price and total) has been fully inputed.
        
        Check if the total price per item and get discount:
            1. Discount for 5% if total > Rp. 200.000
            2. Discount for 6% if total > Rp. 300.000
            3. Discount for 7% if total > Rp. 500.000
        
        Submit to database if the transaction is completed
        
        Args:
            None 
        
        Returns:
            str: "✅ Order has been completed" or "❌ There's something missing"
            print: List of order(s) in tabular form
        """
        return 1
