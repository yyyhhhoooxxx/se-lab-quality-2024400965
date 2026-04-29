# before.py - 有代码坏味道
def calculate_order_price(order_type, quantity, unit_price, discount):
    tax_rate = 0.13
    log_level = "debug"
    
    if order_type == "food":
        subtotal = quantity * unit_price
        if discount > 0:
            subtotal = subtotal * (1 - discount)
        if subtotal < 0:
            subtotal = 0
        print(f"Calculated food order: {subtotal}")
        return subtotal
    elif order_type == "book":
        subtotal = quantity * unit_price
        if discount > 0:
            subtotal = subtotal * (1 - discount)
        if subtotal < 0:
            subtotal = 0
        print(f"Calculated book order: {subtotal}")
        return subtotal
    elif order_type == "electronic":
        subtotal = quantity * unit_price
        if discount > 0:
            subtotal = subtotal * (1 - discount)
        if subtotal < 0:
            subtotal = 0
        print(f"Calculated electronic order: {subtotal}")
        return subtotal
    elif order_type == "clothes":
        subtotal = quantity * unit_price
        if discount > 0:
            subtotal = subtotal * (1 - discount)
        if subtotal < 0:
            subtotal = 0
        print(f"Calculated clothes order: {subtotal}")
        return subtotal
    else:
        return 0

def print_order_info(order_id, order_type, quantity, price):
    print(f"Order ID: {order_id}")
    print(f"Type: {order_type}")
    print(f"Quantity: {quantity}")
    print(f"Price: {price}")
    print("-------------------")

if __name__ == "__main__":
    print(calculate_order_price("food", 2, 15, 0.1))
    print(calculate_order_price("book", 3, 20, 0.2))
    print(calculate_order_price("electronic", 1, 100, 0.05))
