import random

from ArvoreAVL import ArvoreAVL
from Musica import Musica

if __name__ == "__main__":
    #Instanciando objetos
    arvoreAVL = ArvoreAVL()
    # musica1 = Musica(1, 'musica1', 2004, 'album1')
    # musica2 = Musica(2, 'musica2', 2016, 'album2')
    # musica23 = Musica(24, 'musica3', 2016, 'album2')
    # musica3 = Musica(3, 'musica3', 2008, 'album3')
    # musica4 = Musica(4, 'musica4', 1997, 'album4')
    # musica5 = Musica(5, 'musica5', 2016, 'album5')
    # arvoreAVL.inserir(musica1.id, musica1)
    # arvoreAVL.inserir(musica2.id, musica2)
    # arvoreAVL.inserir(musica3.id, musica3)
    # arvoreAVL.inserir(musica4.id, musica4)
    # arvoreAVL.inserir(musica5.id, musica5)
    # arvoreAVL.inserir(musica23.id, musica23)

    while(True):
        print('''
________________________________
1 - Inserir música
2 - Buscar música pelo id
3 - Buscar músicas pelo ano
4 - Listar músicas em ordem alfabética
5 - Altura da árvore
6 - Exibir a árvore
7 - Sair do Programa
________________________________''')
        
        test = int(input("Escolha uma opção: "))
        if test == 1:
            id = int(input("Id da música: "))
            musica = input("Nome da música: ")
            album = input("Álbum: ")
            ano = input("Ano da música: ")
            arvoreAVL.inserir(id, Musica(id, musica, ano, album))
            print("Música inserida com sucesso.")

        elif test == 2:
            arvoreAVL.BuscarPorId(int(input("Digite o Id que deseja buscar: ")))

        elif test == 3:
            arvoreAVL.BuscarPorAno(int(input("Digite o ano que deseja buscar: ")))

        elif test == 4:
            musicas = arvoreAVL.PercorreEmOrdem()
            for i in range(len(musicas)):
                arvoreAVL.BuscarPorId(musicas[i])

        elif test == 5:
            print(f'Altura: {arvoreAVL.altura}')

        elif test == 6:
            arvoreAVL.MostrarArvore()

        elif test == 7:
            print("Programa finalizado!")
            break