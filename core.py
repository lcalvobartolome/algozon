import datetime
import copy

class Product: # definir mi clase 
    def __init__( # qué me caracteriza: tú me das unos atributos y yo los guardo en mi estado interno
        self, 
        product_id: str, 
        name: str, 
        category:str
    ) -> None:
        # este es mi estado interno
        self.product_id = product_id
        self.name = name
        self.category = category
        
    def __str__(self):
        return f"Product ID {self.product_id} - Name: {self.name}"
    
class Batch:
    
    def __init__(
        self,
        batch_id: str,
        product_id: str, 
        quantity: int,
        unit_cost: float,
        expiration_date: datetime.date
    ) -> None:
        
        self.batch_id = batch_id
        self.product_id = product_id
        self._quantity = quantity
        self.unit_cost = unit_cost
        self.expiration_date = expiration_date
    
    
    def __str__(self) -> str:
        return (
            f"Batch ID {self.batch_id} - Product ID: {self.product_id} - Quantity {self._quantity} - Expiration Date: {self.expiration_date}"
        )
        
        
    def get_quantity(self) -> int:
        """Getter of quantity"""
        return self._quantity
        
class Stock:
    
    def __init__(self) -> None:
        self._inventory: dict[str, list[Batch]] = {}
        
    
    def get_batches(self, product_id: str) -> tuple[Batch, ...]:
        
        #batches = self._inventory[product_id] 
        batches = self._inventory.get(product_id, []) #esto es equivalente a la línea anterior pero más seguro y ya cumple especificaciones
        
        return tuple(copy.deepcopy(batch) for batch in batches)
    
    def add_shipment(self, batch: Batch) -> None:
        
        """        
        b_product_id = batch.product_id
        
        if b_product_id not in self._inventory:
            self._inventory[b_product_id] = []
            
        self._inventory[b_product_id].append(batch)
        """
        
        self._inventory.setdefault(batch.product_id, []).append(batch)
        
    def total_stock(self, product_id: str) -> int:
        
        """
        total_sum = 0
        if product_id not in self._inventory:
            return total_sum
    
        batches_product_id = self._inventory.get(product_id, [])
        for batch in batches_product_id:
            total_sum += batch.get_quantity()
            
        #return total_sum
        """
    
        return sum([batch.get_quantity() for batch in self._inventory.get(product_id, [])])
    
    
if __name__ == "__main__":
    product = Product("A-001", "yogur natural", "alimentación")
    print(product)
    
    batch0 = Batch("B-001", "A-001", 5, 10.0, datetime.date(2026, 2, 17))
    print(batch0)
