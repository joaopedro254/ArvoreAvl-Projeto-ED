class Node:
    def __init__(self, chave, musica):
        self.__chave = chave
        self.__musica = musica
        self.__esquerda = None
        self.__direita = None

    @property
    def chave(self):
        return self.__chave
    @chave.setter
    def chave(self, novo):
        self.__chave = novo

    @property
    def musica(self):
        return self.__musica
    @musica.setter
    def musica(self, novo):
        self.__musica = novo

    @property
    def esquerda(self):
        return self.__esquerda
    @esquerda.setter
    def esquerda(self, novo):
        self.__esquerda = novo

    @property
    def direita(self):
        return self.__direita
    @direita.setter
    def direita(self, novo):
        self.__direita = novo

    def __str__ (self):
        return '{}'.format(self.musica)