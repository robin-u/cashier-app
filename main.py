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
            update_prompt = input("What do you want to update?\n")
            
        elif prompt == "quit" or prompt == "q":
            break
        else:
            raise Exception()
    
    except Exception:
        print("\n====================INSTRUCTION====================")
        print("Type \"add\" or \"a\" to add a new item to the cart")
        print("Type \"quit\" or \"q\" to quit")
        print("====================INSTRUCTION====================\n")
        pass