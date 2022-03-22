class Musica:
    def __init__(self, id, nome, ano, album):
        self.__id = id
        self.__nome = nome
        self.__ano = ano
        self.__album = album

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, novo):
        self.__id = novo
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo):
        self.__nome = novo
    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self, novo):
        self.__ano = novo
    @property
    def album(self):
        return self.__album
    @album.setter
    def album(self, novo):
        self.__album = novo

    def __str__(self):
        texto = f'Id: {self.__id}, Música: {self.__nome}, Album: {self.__album}, Ano: {self.__ano}'
        return texto