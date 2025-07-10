from dataclasses import dataclass

@dataclass
class Brand:
    brand_id:int
    brand_name:str


    def __str__(self):
        return f"BRAND_ID ->{self.brand_id}, NOME_BRAND ->{self.brand_name}"

    def __hash__(self):
        return hash(self.brand_id)