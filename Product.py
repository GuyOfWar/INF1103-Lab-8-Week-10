from abc import ABC, abstractmethod
from Supplier import Supplier
class Product(ABC):
    def __init__(self, product_id, name, price, stock, supplier: Supplier): #init variables
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)
        self.__supplier: Supplier = supplier

    def product_id(self): #return each individual values
        return(self.__product_id)
    
    def name(self):
        return(self.__name)
    
    def price(self):
        return(self.__price)
    
    def stock(self):
        return(self.__stock)

    def update_stock(self, stock): #update stock quantity
        self.__stock = int(stock)
        return(self.__stock)
    
    def display_information(self): #option 1, end keeps the print on the same line
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")
        self.__supplier.display_information()

    def to_dict(self): #convert Product to dictionary for json
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

    @abstractmethod
    def get_fulfilment_info(self):
        pass