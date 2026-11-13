from Product import Product
from Supplier import Supplier
from CanBeShipped import CanBeShipped
class PhysicalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float, type: int, supplier: Supplier) -> None: #init variables
        super().__init__(product_id, name, price, stock, supplier) #takes variables from Product
        self.__weight = float(weight)
        self.__type = int(type)

    def weight(self) -> float:
        return(self.__weight)

    def display_information(self) -> None: #option 1 + weight
        super().display_information()
        print(f" | Weight: {self.__weight:.2f}")

    def to_dict(self) -> dict: #convert Product to dictionary for json
        return {
            "product_id": self.product_id(),
            "name": self.name(),
            "price": self.price(),
            "stock": self.stock(),
            "weight": self.__weight,
            "product type": self.__type
        }

    def get_fulfilment_info(self) -> str:
        print("This product requires physical shipping.")

    def calculate_shipping_cost(self) -> None:
        shipcost = self.stock() * self.__weight * 0.2 + 3
        print(f"Shipping cost: {shipcost:.2f}")
    
CanBeShipped.register(PhysicalProduct) #to register Physical as a virtual class of CanBeShipped