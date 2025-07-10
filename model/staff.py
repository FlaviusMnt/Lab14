from dataclasses import dataclass

@dataclass
class Staff:
    staff_id:int
    first_name:str
    last_name:str
    store_id:int

    def __str__(self):
        return f"STAFF_ID ->{self.staff_id} LAVORA NEL NEGOZIO ->{self.store_id}"

    def __hash__(self):
        return hash(self.staff_id)

