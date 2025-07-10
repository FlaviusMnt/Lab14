import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.storeScelto = None
        self.nodoScelto = None



    def handleCreaGrafo(self, e):
        self._view.txt_result.controls.clear()
        durataGiorniTxt = self._view._txtIntK.value
        if durataGiorniTxt ==  "":
            self._view.txt_result.controls.append(ft.Text("NON HAI INSERITO I GIORNI"))
            return

        try:
            durataGiorni = int(durataGiorniTxt)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("INSERITO VALORE NON VALIDO"))
            return

        self._model.buildGraph(self.storeScelto,durataGiorni)
        self.fillDDNodes()

        self._view.txt_result.controls.append(ft.Text(f"GRAFICO CREATO!\n"
                                                      f"NUMERO NODI = {self._model.get_num_of_nodes()}\n"
                                                      f"NUMERO ARCHI = {self._model.get_num_of_edges()}\n"))

        self._view.update_page()

    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass

    def fillDDStore(self):
        listaStore = self._model.getAllStores()
        for store in listaStore:
            self._view._ddStore.options.append(ft.dropdown.Option(text=store.store_id,
                                                                  data=store,
                                                                  on_click=self.readDDValue))
        self._view.update_page()

    def readDDValue(self,e):
        if e.control.data is None:
            print("ERRORE NEL LEGGERE DD VALORE")
            self.storeScelto = None
        else:
            self.storeScelto = e.control.data.store_id

    def fillDDNodes(self):
        self._view._ddNode.options.clear()
        nodi = self._model.get_nodes()

        for nodo in nodi:
            self._view._ddNode.options.append(ft.dropdown.Option(text=nodo.order_id,
                                                                 data=nodo,
                                                                 on_click=self.readDDNode))
        self._view.update_page()

    def readDDNode(self,e):
        if e.control.data is None:
            print("ERRORE NEL LEGGERE DD NODO")
            self.nodoScelto = None
        else:
            self.nodoScelto = e.control.data
