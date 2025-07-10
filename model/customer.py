from dataclasses import dataclass

@dataclass
class Customer:
    customer_id:int
    first_name:str
    last_name:str

    def __str__(self):
        return f"CLIENTE_ID ->{self.customer_id}, NOME ->{self.first_name}, COGNOME ->{self.last_name}"

    def __hash__(self):
        return hash(self.customer_id)