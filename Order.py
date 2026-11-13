from Product import Product
from OrderLine import OrderLine
class Order:
    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self):
        total = 0.0
        for order in self.order_lines:
            total += order.calculate_subtotal()
        return(total)

    def display_order(self):
        print("Order Id:", self.order_id)
        for order_line in self.order_lines:
            print("Subtotal: $", order_line.calculate_subtotal())
        print("Total: $", self.calculate_total())

    def remove_order_line(self, index: int) -> None:
        if 0 <= index < len(self.order_lines):
            self.order_lines.pop(index)
        else:
            print("Invalid order line index")