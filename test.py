import json
import os
from Product import Product
from DigitalProduct import DigitalProduct
from PhysicalProduct import PhysicalProduct
from Inventory import Inventory
from Supplier import Supplier
from Order import Order
from CanBeShipped import CanBeShipped
supplier1 = Supplier(101, "ABC Supplies", "abc@gmail.com")
supplier2 = Supplier(102, "DEF Supplies", "def@hotmail.com")
inventory_A = Inventory()
inventory_B = Inventory()
inventory_C = Inventory()
order1 = Order("0001")
order2 = Order("0002")
product1 = PhysicalProduct("P001", "Laptop", 1200.00, 15, 37.00, 1, supplier1)
product2 = DigitalProduct("P002", "Mouse", 25.50, 40, 0.50, 1, supplier2)

def show_product_details(product: Product) -> None:
    product.display_information()
    product.get_fulfilment_info()

print("Association & Aggregation Test")
del supplier1
del supplier2
inventory_A.add_product(product1)
inventory_A.add_product(product2)
print("Inventory A")
inventory_A.display_all()
inventory_A.remove_product("P001")
print("P001 removed")
inventory_A.display_all()
print("P001 Info")
product1.display_information()
inventory_B.add_product(product1)
print("Inventory B")
inventory_B.display_all()
inventory_B.remove_product("P001")
print("P001 removed")
inventory_B.display_all()
print("P001 Info")
product1.display_information()
product2.display_information()
product1.get_fulfilment_info()
product2.get_fulfilment_info()
print("End Association & Aggregation Test\n")

if isinstance(product1, CanBeShipped):
    product1.calculate_shipping_cost()

print("\nComposition Test")
order1.add_order_line(product1, 2)
order1.add_order_line(product2, 3)
print("Order 1")
order1.display_order()
order2.add_order_line(product1, 2)
print("Order 2")
order2.display_order()
order1.remove_order_line(0)
print("Order 1")
order1.display_order()
print("End Composition Test\n")

#Lab 8 Part 6.2
print("Part 6.2 Test substitutability")
show_product_details(product1)
show_product_details(product2)
print("End Test substitutability\n")

#Lab 8 part 7.2
inventory_C.add_product(product1)
inventory_C.add_product(product2)
inventory_C.display_all()