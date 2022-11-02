#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    AT16 Amnésia recursiva

    Indique o código do Grupo (deveria ser o mesmo da computador
    que você usou no CEC, como A, B, C etc.).

    GRUPO: X
   
    Liste a seguir os nomes completos dos membros do time que participaram dessa atividade presencialmente:

    - Marina Izabela
    - Bianca Ângelo da Rocha Barreto

'''
import numpy as np

from util import init_matriz, str_matriz, pause

#------------------------------------------------------------------
# sys para controlar o tamanho da pilha de recursão
# configuração da pilha e constantes do experimento.
# Essas constantes podem ser alteradas para adaptá-las a sua máquina
import sys
MAX_PILHA_RECURSAO = 10000
sys.setrecursionlimit(MAX_PILHA_RECURSAO)  

#---------------------------------------------------------
def main():
    print("Teste binomialR():")
    print(f"binomialR(3,2)={binomialR(3,2)} deve ser 3")
    print(f"binomialR(5,1)={binomialR(5,1)} deve ser 5")
    print(f"binomialR(1,5)={binomialR(1,5)} deve ser 0")
    print(f"binomialR(5,2)={binomialR(5,2)} deve ser 10")
    pause()
    
    print("\n----------------\n")
    print("Teste binomialRC():")
    print(f"binomialRC(3,2)={binomialRC(3,2)} deve ser 3")
    print(f"binomialRC(5,1)={binomialRC(5,1)} deve ser 5")
    print(f"binomialRC(1,5)={binomialRC(1,5)} deve ser 0")
    print(f"binomialRC(5,2)={binomialRC(5,2)} deve ser 10")
    pause()
    
    print("\n----------------\n")
    print("Teste binomialI(4,3):")
    binom = binomialI(4, 3)
    print(f"{str_matriz(binom)}")
    pause()
        
    print("\n----------------\n")
    print("Teste binomialRM(5,4):")
    binom = binomialRM(5, 4)
    print(f"{str_matriz(binom)}")
    pause()
    
    print("\n----------------\n")
    print("Teste binomialRCache:")
    
    cache = init_matriz(4, 3, -1)
    print(f"binomialRCache(3,2,cache)={binomialRCache(3,2,cache)} deve ser 3")
    print(str_matriz(cache))
    
    '''
    pause()
    print("\n----------------\n")
    print("Teste outra():")
    print(f"outra(3,2)={outra(3,2)} deve ser 3")
    print(f"outra(5,1)={outra(5,1)} deve ser 5")
    print(f"outra(1,5)={outra(1,5)} deve ser 0")
    print(f"outra(5,2)={outra(5,2)} deve ser 10")
    pause()
    '''

    print("FIM")
    
#---------------------------------------------------------
def binomialR(n, k):
    '''(int,int) -> int
    RECEBE inteiros não-negativos n e k.
    RETORNA o valor do binomial de n, k-a-k.

    NOTA. Função está completa.
          Versão recursiva traduzida da fórmula de Pascal
    '''
    if n < k: return 0
    if n == k or k == 0: return 1
    return binomialR(n-1, k) + binomialR(n-1, k-1)

#-----------------------------------------------------------
def binomialRC(n, k):
    ''' (int, int) -> int
    RECEBE dois inteiros não negativos n e k.
    RETORNA o valor de binomial(n,k) calculado usando a 
         versão recursiva da função binomial com recursão de cauda.
         
    '''
    if k == 1: return n
    
    return int(binomialR(n-1, k-1) * n/k)

#---------------------------------------------------------
def binomialI(n, k):
    '''(int, int) -> matriz
    RECEBE  dois inteiros não negativos n e k.
    RETORNA uma matriz de dimensão (n+1)x(k+1) em que cada 
        posição [i][j] tem o valor do número binomial de i, j-a-j
        para i=0,1,...,n e j=0,1,...,k.

    NOTA. Função iterativa que preenche a matriz usando a fórmula de
          Pascal. Usa init_matriz() que está mais adiante.
    '''
    # matriz de zeros de dimensão (n+1)x(k+1)
    binom = init_matriz(n+1, k+1, 0)
    # escreva sua função a seguir
    
    binom[0][0] = 1
    
    for j in range(1, k+1):
        binom[0][j] = 0
    
    for i in range(1, n+1):
        binom[i][0] = 1
    
    for i in range(1,n +1):
        for j in range(1,k +1):
            binom[i][j] = binom[i - 1][j] + binom[i - 1][j - 1]
    
    return binom
 
#---------------------------------------------------------
def binomialRM(n, k):
    '''(int, int) -> matriz
    RECEBE inteiros não-negativos n e k.
    RETORNA uma matriz de dimensão (n+1)x(k+1) em que cada 
        posição [i][j] (que é necessária para o cálculo de binomial 
        de n, k-a-k!) tem o valor do número binomial de i, j-a-j
        para i=0,1,...,n e j=0,1,...,k.
 
    NOTA. Função está completa.
          Função envoltória para a função recursiva binomialRMCache. 
          Cria a memória cache usada como rascunho por essa função 
          recursiva (Seção 16.6). 
          Usa init_matriz() que está mais adiante.
    '''
    # cache é uma matriz (ou ndarray)  de dimensão (n+1)x(k+1) com -1
    # cache[i][j] == -1 indica que valor correspondente não foi calculado
    cache = init_matriz(n+1, k+1, -1)
    #valor = binomialRCache(n, k, cache) # não usa valor
    return cache

#---------------------------------------------------------
def binomialRCache(n, k, cache):
    '''(int, int, matriz) -> int
    RECEBE inteiros não-negativos n e k e uma matriz cache.
    RETORNA o valor do binomial de n, k-a-k e PREENCHE posições
        [i][j] envolvidas nos cálculos com o valor de binomial de i, j-a-j.

    Em busca de inspiração? 
    Vejam a função fibonacciRCache() da seção 16.6.
    '''

    if n < k: 
        cache[n][k] = 0

    if n == k or k == 0: 
        cache[n][k] = 1

    if cache[n][k] == -1:
        cache[n][k] = binomialRCache(n-1, k-1, cache) + binomialRCache(n-1, k, cache) 
    
    return cache[n][k]
#------------------------------------------------------------
def outra(n, k):
    '''(int, int) -> int
    RECEBE dois inteiros não negativos n e k.
    RETORNA o valor de binomial de n, k-a-k.
    
    NOTA. Para o caso de vocês desejarem implementar
          outra versão.
    '''
    return "Vixe! ainda não fiz a outra função"


#-----------------------------------------------------------    
if __name__ == "__main__":
    main()
