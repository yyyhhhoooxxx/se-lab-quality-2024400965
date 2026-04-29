# before.py - 有代码坏味道的示例
def calculate_order_price(order_type, quantity, unit_price, discount):
    # 未使用的变量：tax_rate
    tax_rate = 0.13
    if order_type == "food":
        # 重复逻辑：计算总价
        subtotal = quantity * unit_price
        if discount > 0:
            subtotal = subtotal * (1 - discount)
        if subtotal < 0:
            subtotal = 0
        return subtotal
    elif order_type == "book":
        # 几乎完全重复的计算逻辑
        subtotal = quantity * unit_price
        if discount > 0:
            subtotal = subtotal * (1 - discount)
        if subtotal < 0:
            subtotal = 0
        return subtotal
    elif order_type == "electronic":
        # 重复逻辑，且函数过长
        subtotal = quantity * unit_price
        if discount > 0:
            subtotal = subtotal * (1 - discount)
        if subtotal < 0:
            subtotal = 0
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
