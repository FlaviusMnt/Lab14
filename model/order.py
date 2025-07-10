from dataclasses import dataclass
import datetime

@dataclass
class Order:
    order_id:int
    customer_id:int
    order_date:datetime.date
    store_id:int

    def __str__(self):
        return f"CODICE_ORDINE ->{self.order_id} CODICE_STORE ->{self.store_id} DATA_ORDINE ->{self.order_date}"

    def __hash__(self):
        return hash(self.order_id)

