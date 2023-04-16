from modules.features import Transaction

prompt_name = input("Hello, what's your name?\n")
app = Transaction(prompt_name)

while True:
    try:
        prompt = input(f"Hello, {app.customer_name}! What do you want to do with your transaction?\n").lower()
        if prompt == "add" or prompt == "a":
            while True:
                item, quantity, price = [], [], []
                
                item.append(input("Enter the item's name: "))
                quantity.append(int(input("Enter the quantity: ")))
                price.append(float(input("Enter the price: ")))
                try:
                    app.add_item(items=item, quantities=quantity, prices=price)
                    break
                except Exception as err:
                    print(err)
                    print("Please, enter the suitable data type\n")
                    pass
            continue
        elif prompt == "update" or prompt == "u":
            item = input("What item do you want to update?\n")
            if item in app.cart_of_items:
                update_prompt = input("What do you want to update?\n")
                if update_prompt == "name":
                    new_name = input("What'll be the new name?\n")
                    app.update_item_name(item, new_name)
                elif update_prompt == "quantity":
                    new_quantity = int(input("What'll be the new quantity?\n"))
                    app.update_item_qty(item, new_quantity)
                elif update_prompt == "price":
                    new_price = float(input("What'll be the new price?\n"))
                    app.update_item_price(item, new_price)
            else:
                print("Item not yet in cart. Add it first")
                continue
        elif prompt == "check" or prompt == "c":
            print(app.cart_of_items)
            app.check_order()
        elif prompt == "quit" or prompt == "q":
            break
        else:
            raise Exception()
    
    except Exception:
        print("\n====================INSTRUCTION====================")
        print("Type \"add\" or \"a\" to add a new item to the cart")
        print("Type \"update\" or \"u\" to update an item from the cart")
        print("Type \"check\" or \"c\" to check the items in cart")
        print("Type \"quit\" or \"q\" to quit")
        print("====================INSTRUCTION====================\n")
        pass