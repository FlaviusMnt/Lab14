from database.DB_connect import DBConnect
from model.order import Order
from model.store import Store


class DAO():

    @staticmethod
    def getAllStores():
        cnx = DBConnect.get_connection()
        risultato = []

        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)

            query = """select s.store_id,s.store_name
from stores s """

            cursor.execute(query)
            for row in cursor:
                risultato.append(Store(**row))
            cursor.close()
            cnx.close()
            return risultato
        else:
            print("ERRORE NELLA CONNEXIONE")
            return None

    @staticmethod
    def getAllNodes(store):
        cnx = DBConnect.get_connection()
        risultato = []

        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)

            query = """SELECT o.order_id,o.customer_id,o.order_date,o.store_id
from orders o 
where o.store_id = %s"""

            cursor.execute(query,(store,))
            for row in cursor:
                risultato.append(Order(**row))
            cursor.close()
            cnx.close()
            return risultato
        else:
            print("ERRORE NELLA CONNEXIONE")
            return None

    @staticmethod
    def getAllEdges(store,numeroGiorniK,mappa):
        cnx = DBConnect.get_connection()
        risultato = []

        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)

            query = """SELECT DISTINCT o1.order_id AS id1 ,o2.order_id as id2,/*o1.order_date ,o2.order_date */ count(i1.quantity + i2.quantity) as PESO
from orders o1,orders o2 , order_items i1, order_items i2
where o1.store_id = %s
and o1.store_id = o2.store_id
and o1.order_id <> o2.order_id
and o1.order_date > o2.order_date
and i1.order_id = o1.order_id
and i2.order_id = o2.order_id
and DATEDIFF(o1.order_date,o2.order_date ) <= %s
group by o1.order_id,o2.order_id
/*Raggruppa tutte le combinazioni che hanno la stessa coppia di ordini o1 e o2*/
order by o1.order_id ASC, o2.order_id ASC
"""

            cursor.execute(query, (store,numeroGiorniK))
            for row in cursor:
                risultato.append((mappa[row["id1"]], mappa[row["id2"]], row["PESO"]))
            cursor.close()
            cnx.close()
            return risultato
        else:
            print("ERRORE NELLA CONNEXIONE")
            return None


if __name__ ==  "__main__":
    mappa = {}

    print(DAO.getAllStores())
    for store in DAO.getAllStores():
        print(store)

    print("")
    print(len(DAO.getAllNodes(3)))
    for nodo in DAO.getAllNodes(3):
        mappa[nodo.order_id] = nodo


    listaArchi = DAO.getAllEdges(3,1,mappa)
    for arco in listaArchi:
        print(arco)


# SELECT o1.order_id AS id1 ,o2.order_id as id2,/*o1.order_date ,o2.order_date */ count(i1.quantity + i2.quantity) as PESO
# from orders o1,orders o2 , order_items i1, order_items i2
# where o1.store_id = %s
# and o1.store_id = o2.store_id
# and o1.order_id <> o2.order_id
# and o1.order_id > o2.order_id
# and i1.order_id = o1.order_id
# and i2.order_id = o2.order_id
# and abs(DATEDIFF(o1.order_date,o2.order_date )) <= %s
# group by o1.order_id,o2.order_id
# /*Raggruppa tutte le combinazioni che hanno la stessa coppia di ordini o1 e o2*/
# order by o1.order_id ASC, o2.order_id ASC
