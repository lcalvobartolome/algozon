from abc import ABC, abstractmethod

"""
def final_price(customer_type: str, gross_price: float) -> float:
    if customer_type == "GUEST":
        return gross_price
    elif customer_type == "BUSINESS":
        return gross_price / 1.21
""" 

"""
class Customer:
    def __init__(self, customer_id: str, name: str, email: str) -> None:
        self.customer_id = customer_id
        self.name = name
        self.email = email 
    
    def __str__(self) -> str:
        return f"Customer ID {self.customer_id}, Name: {self.name}"
    
    def final_price(self, gross_price: float) -> float:
        return gross_price
    
class GuestCustomer(Customer):
    
    def final_price(self, gross_price: float) -> float:
        return gross_price

class BusinessCustomer(Customer):
    
    def final_price(self, gross_price: float) -> float:
        return gross_price / 1.21
"""


class Customer(ABC): 
    def __init__(self, customer_id: str, name: str, email: str) -> None:
        self.customer_id = customer_id
        self.name = name
        self.email = email 
    
    def __str__(self) -> str:
        return f"Customer ID {self.customer_id}, Name: {self.name}"
    
    @abstractmethod
    def final_price(self, gross_price: float) -> float:
        pass
    
    @abstractmethod
    def label(self) -> str:
        pass
    
    @abstractmethod
    def is_eligible_for_minigame(self) -> bool:
        pass

class GuestCustomer(Customer):
    
    def final_price(self, gross_price: float) -> float:
        return gross_price
    
    def label(self) -> str:
        return "INVITADO"
    
    def is_eligible_for_minigame(self) -> bool:
        return True

class BusinessCustomer(Customer):
    
    def final_price(self, gross_price: float) -> float:
        return gross_price / 1.21
    
    def label(self) -> str:
        return "EMPRESA"
    
    def is_eligible_for_minigame(self) -> bool:
        return False    

class TaxExemptBusinessCustomer(BusinessCustomer):
    
    def final_price(self, gross_price: float) -> float:
        super().final_price(gross_price) * 0.98
        
    def label(self) -> str:
        return "EMPRESA_EXENTA"
    
    def is_eligible_for_minigame(self) -> bool:
        return False
    
class IndividualCustomer(Customer):
    
    def final_price(self, gross_price: float) -> float:
        return gross_price * 0.9
    
    def label(self) -> str:
        return "PARTICULAR"
    
    def is_eligible_for_minigame(self) -> bool:
        return True    
    
class EmployeeCustomer(Customer):
    
    def final_price(self, gross_price: float) -> float:
        return gross_price * 0.85
    
    def label(self) -> str:
        return "EMPLEADO"
    
    def is_eligible_for_minigame(self) -> bool:
        return False    
    

my_c = GuestCustomer("1234", "yo", "yo@gmail.com")
print(my_c)
