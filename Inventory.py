from Product import Product
from DigitalProduct import DigitalProduct
from PhysicalProduct import PhysicalProduct
class Inventory:
    def __init__(self):
         self.__inventory_list: list[Product] = []

    def load_list(self, data): #converts data from json into Product in Inventory
        self.__inventory_list = []
        for product_data in data:
            if product_data["product type"] == 1:
                product = PhysicalProduct(
                    product_data["product_id"],
                    product_data["name"],
                    product_data["price"],
                    product_data["stock"],
                    product_data["weight"],
                    product_data["product type"]
                )
            elif product_data["product type"] == 2:
                product = DigitalProduct(
                    product_data["product_id"],
                    product_data["name"],
                    product_data["price"],
                    product_data["stock"],
                    product_data["download size"],
                    product_data["product type"]
                )
            self.__inventory_list.append(product)
    
    def find_product(self, product_id: str): #formerly product_id_check
        for product in self.__inventory_list:
            if product.product_id() == product_id: #check if id matches the id in inventory list
                return(product)
        return(None)

    def display_all(self): #option 1
        print("Current Inventory")
        print("-------------------------------------")
        for product in self.__inventory_list: #loop and print
            product.display_information()
        print("-------------------------------------")

    def add_product(self, product: Product): #option 2
        self.__inventory_list.append(product)

    def remove_product(self, product_id: str):
        product = self.find_product(product_id)
        if product is not None:
            self.__inventory_list.remove(product)
            return(True)
        else:
            return(False)
    

    def search_product(self): #option 4
        print("\nSearch Product")
        ProductID= input("Enter Product ID:").capitalize()
        for product in self.__inventory_list:
            if product.product_id() == ProductID: #check if id matches the id in inventory list
                print("\nProduct Found")
                print("-------------------------------------")
                print(f"ID:  {product.product_id()}")
                print(f"Name:  {product.name()}")
                print(f"Price: ${product.price():.2f}")
                print(f"Stock: {product.stock()}")
                if isinstance(product, PhysicalProduct):
                    print(f"Weight: {product.weight()}")
                    product.calculate_shipping_cost()
                    product.get_fulfilment_info()
                elif isinstance(product, DigitalProduct):
                    print(f"Download Size: {product.download_size()}")
                    product.get_fulfilment_info()
                print("-------------------------------------")
                return(product) #stops entire function, using break will only exit the if loop
        print("\nProduct not found.")
        return(None) #stops entire function and indicates no results

    def to_list(self): #converts all Product dictionaries to list of dictionaries for json
        return [product.to_dict() for product in self.__inventory_list]