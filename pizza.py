# pizza.py

class Pizza:
    ingredientes_carnicos = ["pollo", "vacuno", "carne vegetal"]
    ingredientes_vegetales = ["tomate", "aceitunas", "champiñones"]
    tipos_de_masa = ["tradicional", "delgada"]

    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        return elemento in valores_posibles

    def __init__(self):
        self.ingrediente_proteico = None
        self.ingrediente_vegetal_1 = None
        self.ingrediente_vegetal_2 = None
        self.tipo_de_masa = None
        self.es_valida = None

    def hacer_pedido(self):
        self.ingrediente_proteico = input("Ingrese el ingrediente proteico: ")
        self.ingrediente_vegetal_1 = input("Ingrese el primer ingrediente vegetal: ")
        self.ingrediente_vegetal_2 = input("Ingrese el segundo ingrediente vegetal: ")
        self.tipo_de_masa = input("Ingrese el tipo de masa (tradicional/delgada): ")

        if (self.validar_elemento(self.ingrediente_proteico, self.ingredientes_carnicos) and
                self.validar_elemento(self.ingrediente_vegetal_1, self.ingredientes_vegetales) and
                self.validar_elemento(self.ingrediente_vegetal_2, self.ingredientes_vegetales) and
                self.validar_elemento(self.tipo_de_masa, self.tipos_de_masa)):
            self.es_valida = True
        else:
            self.es_valida = False
