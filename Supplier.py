class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_email: str) -> None:
        self.__supplier_id = supplier_id
        self.__name = name
        self.__contact_email = contact_email

    def supplier_id(self) -> str:
        return(self.__supplier_id)

    def name(self) -> str:
        return(self.__name)

    def contact_email(self) -> str:
        return(self.__contact_email)

    def display_supplier_information(self) -> None:
        print("Supplier Information")
        print("Supplier ID:", self.__supplier_id)
        print("Name:", self.__name)
        print("Contact Email:", self.__contact_email)