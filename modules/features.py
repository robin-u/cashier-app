from tabulate import tabulate

class Transaction:
    # A list of dictionary to store item temporarily 
    cart_of_items = dict()
    
    def __init__(self, customer_name):
        self.customer_name = customer_name
        
    # Customer input a new item to the transaction
    def add_item(self,
                items: list[str],
                quantities: list[int],
                prices: list[float],
                cart: dict[str, dict[str, float]] = cart_of_items) -> dict[str, dict[str, float]]:
        """
        Add new item with the item quantity & price to the transaction
        
        Args:
            items(list): A list of string containing the name of item(s)
            quantities(list): A list of quantity of item, respective to items(list)
            prices(list): A list of of price of item, respective to items(list)
            cart(dict, optional): A dictionary representing the key as item name and\
                        its values to inform the quantity and price per item
        
        Returns:
            # cart_of_items(dict): Update the current cart with new item(s)
            None
        """

        for item, quantity, price in zip(items, quantities, prices):
            if item in cart:
                cart[item][0] = quantity
            else:
                cart[item] = [quantity, price]
        
        print(f"{item} has been added to the cart!\n")

    # Customer updates the current item name to a new one
    def update_item_name(self, current_name: str, new_name: str):
        """
        Update an item name that has been added to the cart
        
        Args:
            current_name(str): An item name
            new_name(str): New name for the item
        
        Returns:
            None
        """

        try:
            if current_name in self.cart_of_items:
                if type(new_name) == str:
                    self.cart_of_items[current_name] = self.cart_of_items[new_name]
                    print("The item name has been updated!\n")
                else:
                    raise TypeError()
        except TypeError:
            print("Data type is not a str")
        except Exception as err:
            raise Exception("An error occured, see details ->", err.args)
        

    # Customer updates the current quantity of the item
    def update_item_qty(self, item_name: str, new_qty: int):
        """
        Update an item total quantity
        
        Args:
            item_name(str): An item name  
            new_qty(int): New quantity count for the item
        
        Returns:
            None
        """

        try:
            if item_name in self.cart_of_items:
                if type(new_qty) == int:
                    self.cart_of_items[item_name]['quantity'] = new_qty
                    print("The item quantity has been updated!\n")
                else:
                    raise TypeError()
        except TypeError:
            print("new_qty data type needs to be an integer")
        except Exception as err:
            raise Exception("An error occured, see details ->", err.args)

    # Customer updates the current price of the item
    def update_item_price(self, item_name: str, new_price: float):
        """
        Update an item price
        
        Args:
            item_name(str): An item name  
            new_price(float): New price for the item
        
        Returns:
            None
        """

        try:
            if item_name in self.cart_of_items:
                if type(new_price) == float:
                    self.cart_of_items[item_name]['price'] = new_price
                    print("The item price has been updated!\n")
                else:
                    raise TypeError()
        except TypeError:
            print("new_price data type needs to be an integer or a float")
        except Exception as err:
            raise Exception("An error occured, see details ->", err.args)

    # Customer deletes an item from the current transaction
    def delete_item(self, item_name: str):
        """
        Delete an item from the cart
        
        Args:
            item_name(str): An item name  
        
        Returns:
            None
        """

        try:
            if item_name in self.cart_of_items:
                self.cart_of_items.pop(item_name)
                print("The item has been deleted from cart!\n")
        except Exception as err:
            raise Exception("An error occured, see details ->", err.args)

    # Customer resets the whole transaction and starts from a new empty transaction
    def reset_transaction(self):
        """
        Delete the entire cart
        
        Args:
            None
        
        Returns:
            None
        """

        print("Are you sure to reset and start again the transaction?")
        confirmation = input("type \"YES\" or \"NO\" (case sensitive)")

        if confirmation == "YES":
            self.cart_of_items.clear()
        else:
            print("Reset cart has been cancelled")
            pass

    # Customer check their order
    def check_order(self):
        """
        Check if customer order list (item name, qty, price and total) has been fully inputed.
        
        Checkthe total price per item and get discount, only if:
            1. Total > Rp. 200.000 get discount for 5%
            2. Total > Rp. 300.000 get discount for 6%
            3. Total > Rp. 500.000 get discount for 7%
        
        Print the transaction in tabular form.
        
        Submit to database if the transaction is completed
        
        Args:
            None 
        
        Returns:
            None
        """

        print(tabulate(self.cart_of_items, headers="keys", showindex=["quantity", "price"]))