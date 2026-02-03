class Product:
    def __init__(
        self, 
        product_id: str, 
        name: str, 
        category:str
    ) -> None:
        self.product_id = product_id
        self.name = name
        self.category = category
        
    def __str__(self):
        return f"Product ID {self.product_id} - Name: {self.name}"
    
if __name__ == "__main__":
    product = Product("A-001", "yogur natural", "alimentación")
    print(product)