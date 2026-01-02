def process_order(item, quantity):
    try:
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be in number")
        price = {"masala" : 20, "ginger":30}[item]
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError as e:
        print("Error:", e)
    

process_order("ginger", 2)
process_order("elaichi", 2)
process_order("masala", "two")
