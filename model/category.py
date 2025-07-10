from dataclasses import dataclass

@dataclass
class Category:
    category_id:int
    category_name:str

    def __str__(self):
        return f"CATEGORIA_ID ->{self.category_id}, NOME_CATEGORIA ->{self.category_name}"

    def __hash__(self):
        return hash(self.category_id)

    