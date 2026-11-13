from abc import ABC, abstractmethod
from Supplier import Supplier
class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier) -> None: #init variables
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)
        self.__supplier: Supplier = supplier

    def product_id(self) -> str: #return each individual values
        return(self.__product_id)
    
    def name(self) -> str:
        return(self.__name)
    
    def price(self) -> float:
        return(self.__price)
    
    def stock(self) -> int:
        return(self.__stock)

    def supplier(self) -> Supplier:
        return(self.__supplier)

    def display_supplier_information(self) -> None:
        self.__supplier.display_supplier_information()

    def update_stock(self, stock: int) -> int: #update stock quantity
        self.__stock = int(stock)
        return(self.__stock)
    
    def display_information(self) -> None: #option 1, end keeps the print on the same line
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}", end ="")

    def to_dict(self) -> dict: #convert Product to dictionary for json
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.__supplier
        }

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass