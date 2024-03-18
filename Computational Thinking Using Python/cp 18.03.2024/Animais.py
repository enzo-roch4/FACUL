class Animal:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
 
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, idade):
        self._idade = idade


    def fazer_som(self):
        raise NotImplementedError(" todos devem ter esse metodo")
 
class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self._raca = raca
 
    @property
    def raca(self):
        return self._raca
    @raca.setter
    def raca(self, raca):
        self._raca = raca
 

    def fazer_som(self):
        return "auau"

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def fazer_som(self):
        return "miau" 

class Elefante(Animal):
    def __init__(self, nome, idade, tamanho_orelhas):
        super().__init__(nome, idade)
        self.tamanho_orelhas = tamanho_orelhas

        @property
        def tamanho_orelhas(self):
            return self.tamanho_orelhas
        @tamanho_orelhas(self, tamanho_orelhas):
         self.tamanho_orelhas = tamanho_orelhas

    def fazer_som(self):
        return "barulho de elefante"

class Tigre(Animal):
    def __init__(self, nome, idade, tamanho_garras):
        super().__init__(nome, idade)
        self.tamanho_garras = tamanho_garras

        @property
        def tamanho_garras(self):
            return self.tamanho_garras
        @tamanho_garras(self, tamanho_garras):
         self.tamanho_garras = tamanho_garras

    def fazer_som(self):
        return "miau 2"

class Golfinho(Animal):
    def __init__(self, nome, idade, tamanho_nadadeiras):
        super().__init__(nome, idade)
        self.tamanho_nadadeiras = tamanho_nadadeiras

        @property
        def tamanho_nadadeiras(self):
            return self.tamanho_nadadeiras
        @tamanho_nadadeiras(self, tamanho_nadadeiras):
         self.tamanho_nadadeiras = tamanho_nadadeiras

    def fazer_som(self):
        return "AIJSDASDN (barulho de golfinho)"


class Cobra(Animal):
    def __init__(self, nome, idade, tamanho_corpo):
        super().__init__(nome, idade)
        self.tamanho_corpo = tamanho_corpo

        @property
        def tamanho_corpo(self):
            return self.tamanho_corpo
        @tamanho_corpo(self, tamanho_corpo):
         self.tamanho_corpo = tamanho_corpo

    def fazer_som(self):
        return "shshshshshssssssssssss"

class Arara(Animal):
    def __init__(self, nome, idade, cor_penas):
        super().__init__(nome, idade)
        self._cor_penas = cor_penas
 
    @property
    def cor_penas(self):
        return self._cor_penas
    @cor_penas.setter
    def cor_penas(self, cor_penas):
        self._cor_penas = cor_penas
 

    def fazer_som(self):
        return "n sei o som de uma arara"
 
class Peixe(Animal):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self._cor = cor
 
    @property
    def cor(self):
        return self._cor
    @cor.setter
    def cor(self, cor):
        self._cor = cor


    def fazer_som(self):
        return "barulho de peixe"
 
class Lagarto(Animal):
    def __init__(self, nome, idade, escama):
        super().__init__(nome, idade)
        self._escama = escama
 
    @property
    def escama(self):
        return self._escama
    @escama.setter
    def escama(self, escama):
        self._escama = escama


    def fazer_som(self):
        return "ssssss"
 
class Urso(Animal):
    def __init__(self, nome, idade, pelos):
        super().__init__(nome, idade)
        self._pelos = pelos
 
    @property
    def pelos(self):
        return self._pelos 
    @pelos.setter
    def pelos(self, pelos):
        self._pelos = pelos
 

    def fazer_som(self):
        return "AAAAAAAAAAA"
 
def descrever_animal(animal):
    print(f"O {animal.nome} tem {animal.idade} anos e é um {type(animal).__name__}")
    print(f"Ele faz o som: {animal.fazer_som()}")
 
# Testes
elefante = Elefante("jorjão",4,"gigantes")
cachorro = Cachorro("formiga", 5, "Labrador")
passaro = Arara("ararinha", 2, "Vermelho")
peixe = Peixe("Nemo", 1, "Laranja")
réptil = Lagarto("clovis", 10, "Verde")
mamífero = Urso("marcia", 3, "Branco")
gato = Gato("nelson", 3)
tigrinho = Tigre("roberto",6,"imensas")
golfin = Golfinho("Newton", 3,"razoaveis")
cobrinha = Cobra("helena", 2,"grande")


descrever_animal(gato)
descrever_animal(cobrinha)
descrever_animal(golfin)
descrever_animal(tigrinho)
descrever_animal(elefante)
descrever_animal(cachorro)
descrever_animal(passaro)
descrever_animal(peixe)
descrever_animal(réptil)
descrever_animal(mamífero)