from dataclasses import dataclass

@dataclass
class Store:
    store_id:int
    store_name:str

    def __str__(self):
        return f"STORE_ID ->{self.store_id}, NOME ->{self.store_name}"

    def __hash__(self):
        return hash(self.store_id)


