class Cabeça:
    def __init__(self, tipo):
        self.tipo = tipo
        print(f'Cabeça do tipo {self.tipo} criada.')

    def __del__(self):
        print(f'Cabeça do tipo {self.tipo} destruída.')

class Boneco:
    def __init__(self, nome, tipoCabeça):
        self.nome = nome
        self.cabeça = Cabeça(tipoCabeça)
        print(f'Boneco {self.nome} criado.')

    def __del__(self):
        print(f'Boneco {self.nome} destruído.')

meu_boneco = Boneco("Bob", "Grande")