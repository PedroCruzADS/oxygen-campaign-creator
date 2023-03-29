class Interest():
    def __init__(self):
        self.calcados = {"id": ""}
        self.moda_feminina = {"id": ""}
        self.infantil = {"id": ""}
        self.roupas_masculinas = {"id": ""}
        self.esportes = {"id": ""}

        self.interests = {"calcados": self.calcados,
                          "moda_feminina": self.moda_feminina,
                          "esportes": self.esportes, 
                          "infantil": self.infantil,
                          "roupas_masculinas": self.roupas_masculinas}
