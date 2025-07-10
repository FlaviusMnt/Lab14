from dataclasses import dataclass
import datetime

@dataclass
class Product:
    product_id:int
    product_name:str
    brand_id:int
    category_id:int
    model_year:int
    list_price:float


    def __str__(self):
        return f"PRODOTTO_ID ->{self.product_id}, BRAND_ID ->{self.brand_id}, CATEGORIA_ID -> {self.category_id}"

    def __hash__(self):
        return hash(self.product_id)