from Product import Product
from Supplier import Supplier
class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, size: float, type: int, supplier: Supplier) -> None: #init variables
        super().__init__(product_id, name, price, stock, supplier) #takes variables from Product
        self.__download_size = float(size)
        self.__type = int(type)
        
    def download_size(self) -> float:
        return(self.__download_size)

    def display_information(self) -> None: #option 1 + download size
        super().display_information()
        print(f" | Download Size: {self.__download_size:.2f}")
    
    def to_dict(self) -> dict: #convert Product to dictionary for json
        return {
            "product_id": self.product_id(),
            "name": self.name(),
            "price": self.price(),
            "stock": self.stock(),
            "download size": self.__download_size,
            "product type": self.__type,
            "supplier": {
            "supplier_id": self.supplier().supplier_id(),
            "name": self.supplier().name(),
            "contact_email": self.supplier().contact_email()
            }
        }

    def get_fulfilment_info(self) -> None:
        print("This product will be delivered digitally.")