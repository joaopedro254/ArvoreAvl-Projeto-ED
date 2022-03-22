from Node import Node

class ArvoreAVL:
    def __init__(self):
        self.node = None
        self.altura = -1
        self.rotacao = 0
    
    def inserir(self, chave, musica):
        arvore = self.node
        novoNo = Node(chave, musica)

        if arvore == None:
            self.node = novoNo
            self.node.esquerda = ArvoreAVL()
            self.node.direita = ArvoreAVL()

        elif chave < arvore.chave:
            self.node.esquerda.inserir(chave, musica)

        elif chave > arvore.chave:
            self.node.direita.inserir(chave, musica)

        self.BalanceiaNovamente()

    def RotacaoDireita(self):
        raiz = self.node
        esquerdo = self.node.esquerda.node
        direito = esquerdo.direita.node

        self.node = esquerdo
        esquerdo.direita.node = raiz
        raiz.esquerda.node = direito

    def RotacaoEsquerda(self):
        raiz = self.node
        direito = self.node.direita.node
        esquerdo = direito.esquerda.node

        self.node = direito
        direito.esquerda.node = raiz
        raiz.direita.node = esquerdo

    def AtualizarAltura(self, bool=True):
        if self.node != None:
            if bool:
                if self.node.esquerda != None:
                    self.node.esquerda.AtualizarAltura()
                if self.node.direita != None:
                    self.node.direita.AtualizarAltura()

            self.altura = max(self.node.esquerda.altura, self.node.direita.altura) + 1
        else:
            self.altura = -1

    def Balancear(self, bool=True):
        if self.node != None:
            if bool:
                if self.node.esquerda != None:
                    self.node.esquerda.Balancear()
                if self.node.direita != None:
                    self.node.direita.Balancear()

            self.rotacao = self.node.esquerda.altura - self.node.direita.altura
        else:
            self.rotacao = 0

    def BalanceiaNovamente(self):
        self.AtualizarAltura(False)
        self.Balancear(False)
        while self.rotacao < -1 or self.rotacao > 1:
            if self.rotacao > 1:
                if self.node.esquerda.rotacao < 0:
                    self.node.esquerda.RotacaoEsquerda()
                    self.AtualizarAltura()
                    self.Balancear()
                self.RotacaoDireita()
                self.AtualizarAltura()
                self.Balancear()

            if self.rotacao < -1:
                if self.node.direita.rotacao > 0:
                    self.node.direita.RotacaoDireita()
                    self.AtualizarAltura()
                    self.Balancear()
                self.RotacaoEsquerda()
                self.AtualizarAltura()
                self.Balancear()

 
    def PercorreEmOrdem(self):
        if self.node == None:
            return []
        lista = []
        l = self.node.esquerda.PercorreEmOrdem()
        for i in l:
            lista.append(i)
        
        lista.append(self.node.musica.id)

        l = self.node.direita.PercorreEmOrdem()
        for i in l:
            lista.append(i)
        lista = lista
        lista.sort()
        return lista

    def MostrarArvore(self, node=None, tabs=0):
        if not node:
            node = self.node

        if node.direita.node:
            self.MostrarArvore(node.direita.node, tabs + 1)
            print(('\t' * tabs), (' / '))
        print(('\t' * tabs), node.chave)

        if node.esquerda.node:
            print(('\t' * tabs), (' \\ '))
            self.MostrarArvore(node.esquerda.node, tabs + 1)
    

    def BuscarPorId(self, id):
        arvore = self.node
        if arvore == None:
            print('Id não encontrado')

        else:    
            if id == arvore.chave:
                print(f"Id: {arvore.musica.id}, Nome: {arvore.musica.nome}, Álbum: {arvore.musica.album}, Ano: {arvore.musica.ano}")
            
            elif id > arvore.chave:
                arvore.direita.BuscarPorId(id)
            
            elif id < arvore.chave:
                arvore.esquerda.BuscarPorId(id) 
    
    def BuscarPorAno(self, ano):
        if self.node is None:
            return
        arvore = self.node

        if ano == arvore.musica.ano:
            print(f"Id: {arvore.musica.id}, Nome: {arvore.musica.nome}, Álbum: {arvore.musica.album}, Ano: {arvore.musica.ano}")
        
        arvore.direita.BuscarPorAno(ano)
        arvore.esquerda.BuscarPorAno(ano)
            
    def __str__(self):
        return '{}'.format(self.node.musica)       

    

