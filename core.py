import datetime
import copy

class OutOfStockError(Exception):
    
    def __init__(
        self, 
        product_id: str = "",
        available: int = 0,
        requested: int = 0
    ) -> None:
        
        self.product_id = product_id
        self.available = available
        self.requested = requested
        
        super().__init__(
            f"Stock insuficiente para el producto con product_id {product_id}. Tengo {available} unidades pero me han solicitado {requested}"
        )
        
    def __str__(self) -> str:
        return (
            f"Producto {self.product_id}:"
            f"disponible {self.available}, solicitado: {self.requested}"
        )
        
    def __repr__(self) -> str:
        return (
            f"OutOfStockError('{self.product_id}', '{self.available}', '{self.requested}')"
        )

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
    
    #def consume(self, quantity):
    #    self._quantity -= quantity
        
    def consume(self, quantity: int) -> None:
        
        if quantity < 0:
            raise ValueError("La cantidad a consumir no puede ser engativa")
        
        if quantity > self._quantity:
            raise ValueError(
                f"No se pueden consumir {quantity} unidades porque solo hay {self._quantity} en el lote {self.batch_id}"
            )
            
        self._quantity -= quantity
        

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
    
    def _fefo_consume(
        self, product_id: str, quantity: int
    ) -> list[tuple[str, float]]:
        
        batches = self._inventory.get(product_id, [])
        
        # 1. ORDENAR POR CADUCIDAD
        # obtener los lotes ordenados por fecha de caducidad (de menor a mayor)
        batches.sort(key=lambda b : b.expiration_date)
        
        # 2. CONSUMIR UNIDADES
        breakdown = []
        remaining = quantity
        
        for batch in batches: 
            if remaining < 0:
                break
            available = batch.get_quantity()
            consumed = min(available, remaining)
            batch.consume(consumed)
            
            remaining -= consumed
            breakdown.append(
               (batch.batch_id, consumed, batch.unit_cost) 
            )
            
        return breakdown
    
    def _remove_empty_batches(self, product_id: str) -> None:
        batches = self._inventory.get(product_id, [])
        
        self._inventory = [
            batch for batch in batches if batch.get_quantity() > 0
        ]
        
        
    
    def sell_e21(self, product_id: str, quantity: int) -> None:
        batches = self._inventory.get(product_id, [])
        # como asumo que el primer lote tiene stock suficente, voy a reducir qunatity unidades del primer lote
                
        batches[0].consume(quantity)
        
    def sell_e22(self, product_id: str, quantity: int) -> None:
        batches = self._inventory.get(product_id, [])
        # obtener los lotes ordenados por fecha de caducidad (de menor a mayor)
        batches.sort(key=lambda b : b.expiration_date)
        
        remaining = quantity
        
        for batch in batches: 
            if remaining < 0:
                break
            available = batch.get_quantity()
            consumed = min(available, remaining)
            batch.consume(consumed)
            
            remaining -= consumed
            
    def sell_e23(self, product_id: str, quantity: int) -> None:
        
        batches = self._inventory.get(product_id, [])
        
        # 1. ORDENAR POR CADUCIDAD
        # obtener los lotes ordenados por fecha de caducidad (de menor a mayor)
        batches.sort(key=lambda b : b.expiration_date)
        
        # 2. CONSUMIR UNIDADES
        remaining = quantity
        
        for batch in batches: 
            if remaining < 0:
                break
            available = batch.get_quantity()
            consumed = min(available, remaining)
            batch.consume(consumed)
            
            remaining -= consumed
            
        # 3. ELIMINAR LOTES EMPTY
        self._inventory = [
            batch for batch in batches if batch.get_quantity() > 0
        ]
        
    def sell(self, product_id: str, quantity: int) -> None:
        """E.2.4"""
        
        total_available = self.total_stock(product_id)
        if total_available < quantity:
            raise OutOfStockError(product_id, total_available, quantity)
        
        # consumir
        breakdown = self._fefo_consume(product_id, quantity)
        
        # eliminar lotes vacíos
        self._remove_empty_batches(product_id)
        
        return breakdown
                
                
class Catalog:

    def __init__(self) -> None:
        self._products: dict[str, Product] = {}

    def __str__(self) -> str:
        if not self._products:
            return "Catálogo vacío."
        lines = ["Catálogo de productos:"]
        for product in self._products.values():
            lines.append(f"  - {product}")
        return "\n".join(lines)

    def add_product(self, product: Product) -> None:
        self._products[product.product_id] = product

    def get_products(self) -> list[Product]:
        return list(self._products.values())
    

if __name__ == "__main__":
    product = Product("A-001", "yogur natural", "alimentación")
    print(product)
    
    batch0 = Batch("B-001", "A-001", 5, 10.0, datetime.date(2026, 2, 17))
    print(batch0)

    
    my_stock = Stock()
    
    my_stock.add_shipment(batch0)
    
    my_stock.sell_e21("A-001", 1)