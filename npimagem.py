# -*- coding: utf-8 -*-
"""
    Atividade 12 - NPImagem

    Indique o código do Grupo (deveria ser o mesmo da computador
    que você usou no CEC, como A, B, C etc.).

    GRUPO: X
    
    Liste a seguir os nomes completos dos membros do time que participaram dessa atividade presencialmente:

    - Marina Izabela
    - Eloá Bastos
    - Daniel Paulo

"""


## ==================================================================

import numpy as np


def main():
    """Testes da classe NPImagem"""

    lista = list(range(20))
    ar = np.array(lista).reshape(4, 5)
    img1 = NPImagem((0, 0), ar)  #
    print(f"img1:\n{img1}")
    print(f"Shape de img1: {img1.shape}\n")

    img2 = NPImagem((4, 3), 100)
    print(f"img2:\n{img2}")
    print(f"Shape de img2: {img2.shape}\n")

    img2[1, 2] = -10
    print(f"img2[1,2]={img2[1,2]}")
    print(f"img2:\n{img2}\n")

    img3 = img2.crop()  ## cria uma cópia
    print(f"img3:\n{img3}\n")

    img4 = img1.crop(0, 1, 3, 4)
    print(f"img4:\n{img4}\n")

    img5 = NPImagem((3, 2))
    print(f"img5:\n{img5}\n")

    img6 = img1.crop(1, 2)
    print(f"img6:\n{img6}\n")

    img7 = img2 + img3

    print(img7)

    # Inclua abaixo outros testes que desejar

    lista = list(range(30))
    ar = np.array(lista).reshape(5, 6)
    img1 = NPImagem((0, 0), ar)  #
    print(f"img1:\n{img1}")
    print(f"Shape de img1: {img1.shape}\n")

    img2 = NPImagem((3, 2), 100)
    img3 = img2.crop()  ## cria uma cópia
    img2[2, 1] = -10
    print(f"img2[1,2]={img2[2,1]}")
    print(f"img2:\n{img2}\n")
    print(f"img3:\n{img3}\n")

    img1.pinte_retangulo(1, 2, 3, 5, 99)
    print(f"img1.pinte_retangulo(1,2,3,5,99):\n{img1}\n")

    img2.pinte_retangulo(-1, -2, 1, 2, 88)
    print(f"img2.pinte_retangulo(-1,-2,1,2,88):\n{img2}\n")

    img3.pinte_retangulo(1, 0, 3, 4, 77)
    print(f"img3.pinte_retangulo(1,0,3,4,77):\n{img3}\n")

    img1.paste(img2, 1, 2)
    print(f"img1.paste(img2,1,2):\n{img1}\n")

    img1.paste(img3, 3, 5)
    print(f"img1.paste(img3,3,5):\n{img1}\n")

    img1.paste(img3, -1, -1)
    print(f"img1.paste(img3,-1,-1):\n{img1}\n")

    print(img2.blend_iterativo(img3, 0.5))
    print(img2.blend(img3, 0.5))


# ===================================================================


class NPImagem:
    """Complete os métodos da classe NPImagem"""

    ### Parte I ---------------------------------------

    def __init__(self, shape=(0, 0), val=0):
        """Construtor da classe NPImagem"""
        if type(val) is np.ndarray:
            self.data = val.copy()  ## compartilha dados com val
        else:
            self.data = np.full(shape, val)

        self.shape = self.data.shape

    def __str__(self):
        return str(self.data)

    def __getitem__(self, key):
        """(NPImagem, tuple) -> val"""
        return self.data[key[0]][key[1]]

    def __setitem__(self, key, val):
        """(NPImagem, tuple, val) -> None"""
        self.data[key[0]][key[1]] = val

    def crop(self, sup=0, esq=0, inf=None, dir=None):
        """(NPImagem, int, int, int, int) -> NPImagem
        Recorta uma região retangular da NPImagem. A região é definida pelos
        cantos superior-esquerdo (sup,esq) e inferior-direito (inf,dir) de
        um retângulo.

        Esse método cria e retorna uma NPImagem de dimensão
        (inf-sup) x (dir-esq), com conteúdo igual ao do retângulo
        (sup,esq)x(inf,dir).
        """

        if (inf is None) or (inf > self.shape[0]):
            inf = self.shape[0]

        if (dir is None) or (dir > self.shape[1]):
            dir = self.shape[1]

        return NPImagem((inf - sup, dir - esq), self.data[sup:inf, esq:dir])

    ### Parte II ---------------------------------------

    def pinte_retangulo(self, sup, esq, inf, dir, v=0):
        """(NPImagem, int, int, int, int, int) -> None
        Recebe 4 inteiros que definem o canto superior-esquerdo (sup, esq) e
        o canto inferior-direito (inf,dir) de uma região retangular com
        relação a posição (0,0) de self, ou seja, os cantos são "deslocamentos"
        em pixeis com relação à origem.
        Esse método pinta, com o valor v, os pixeis de self que tenham sobreposição com o retângulo (sup,esq)x(inf,dir).
        """
        if sup < 0:
            sup = 0
        if esq < 0:
            esq = 0

        if inf > self.shape[0]:
            inf = self.shape[0]

        if dir > self.shape[1]:
            dir = self.shape[1]

        for i in range(sup, inf):
            for j in range(esq, dir):
                self.data[i, j] = v

    ### Parte III  ---------------------------------------

    def paste(self, other, sup, esq):
        """(NPImagem, NPImagem, int, int) -> None
        Recebe um objeto NPImagem other e um par de inteiros (sup, esq)
        que indica um deslocamento em relação à origem de self (posição (0,0))
        onde a NPImagem other deve ser sobreposta sobre self. Observe que
        esse deslocamento pode ser negativo. Caso não existir sobreposição,
        a imagem self fica inalterada.
        """

        if sup < 0:
            sup = 0
        if esq < 0:
            esq = 0

        nlin = min(self.shape[0] - sup, other.shape[0])
        ncol = min(self.shape[1] - esq, other.shape[1])

        aux = self.crop(sup, esq, nlin + sup, ncol + esq)

        for i in range(nlin):
            for j in range(ncol):
                aux[i, j] = other[i, j]

    ### Parte IV ----------------------------------------------

    def __add__(self, other):
        """(NPImagem, NPImagem ou int ou float) -> NPImagem
        Quando recebe dois objetos NPImagem, retorna a soma, elemento-a-elemento,
        dos pixels de self e other.
        Quando other for int ou float, todos os elementos de self são adicionados de other.
        """
        if type(other) is float or type(other) is int:
            return NPImagem(self.shape, self.data + other)

        res = self.data + other.data
        return NPImagem(val=res)

    def __mul__(self, other):
        """(NPImagem, NPImagem ou int ou float) -> NPImagem
        Quando recebe dois objetos NPImagem, retorna o produto, elemento-a-elemento,
        dos pixels de self e other.
        Quando other for int ou float, todos os elementos de self são multiplicados por other.
        """
        if type(other) is float or type(other) is int:
            return NPImagem(self.shape, self.data * other)

        res = self.data * other.data
        return NPImagem(val=res)

    def blend(self, other, alfa):
        """(NPImagem, NPImagem, float) -> NPImagem
        Retorna uma nova NPImagem com conteúdo igual a uma combinação linear
        dos conteúdos de self e other, com pesos alfa e 1-alfa, respectivamente.
        """
        res = self.data * alfa + other.data * (1 - alfa)
        return NPImagem(val=res)

    def add_iterativo(self, other):
        """(NPImagem, NPImagem) -> NPImagem"""
        nl, nc = self.shape
        res = NPImagem(self.shape, 0.0)
        if type(other) is int or type(other) is float:
            for lin in range(nl):
                for col in range(nc):
                    res[lin, col] = self[lin, col] + other
        else:
            for lin in range(nl):
                for col in range(nc):
                    res[lin, col] = self[lin, col] + other[lin, col]
        return res

    def mul_iterativo(self, other):
        """(NPImagem, NPImagem) -> NPImagem"""
        nl, nc = self.shape
        res = NPImagem(self.shape, 0.0)
        if type(other) is int or type(other) is float:
            for lin in range(nl):
                for col in range(nc):
                    res[lin, col] = self[lin, col] * other
        else:
            for lin in range(nl):
                for col in range(nc):
                    res[lin, col] = self[lin, col] * other[lin, col]
        return res

    def blend_iterativo(self, other, alfa):
        """(NPImagem, NPImagem, float) -> NPImagem
        usando add_iterativo e mul_iterativo
        """
        return self.mul_iterativo(alfa).add_iterativo(other.mul_iterativo(1 - alfa))


if __name__ == "__main__":
    main()
