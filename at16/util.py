#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
AT16 - Arquivo com funções auxiliares.

Não há nada a ser feito neste arquivo.
'''

# para o cronômetro
import time

#-------------------------------------------              
def cronometro(f, n, k):
    '''(callable, int, int) -> float, obj
    RECEBE uma função f e inteiros n e k.
    RETORNA o tempo gasto e valor retornado pela execução de f(n, k).
    '''
    inicio = time.time()
    valor = f(n, k)
    fim = time.time()
    elapsed = fim-inicio
    return elapsed, valor      

#--------------------------------------------------
def init_matriz(nlins, ncols, val=None):
    ''' (int, int, obj) -> matriz (list[list])
    RECEBE dois inteiros nlins, ncols e um valor val.
    RETORNA uma matriz de dimensão nlins x ncols em que 
        todas as posições tem val
    EXEMPLO:
    In [1]: mat = init_matriz(2,3)
    In [2]: mat
    Out[2]: [[None, None, None], [None, None, None]]
    '''
    mt = []
    # crie a matriz
    for i in range(nlins):
        # crie uma linha com ncols itens
        linha = ncols*[val] # [val] + [val] + ... + [val]
        mt   += [linha] 
    return mt

#-------------------------------------------------------
def str_matriz(mt):
    '''(matriz) -> str
    RECEBE uma matriz mt.
    RETORNA uma string que para ser usada por print() para 
        exibir a matriz.
    '''
    # string que criaremos
    s = ""
    # apelidos para a dimensão da matriz
    nlins = len(mt)
    ncols = len(mt[0])

    # pegue o maior número caracteres de um valor
    max_len = 6 # max_len_valor(mt) 

    s += f"Matriz: {nlins} x {ncols}\n"
    for i in range(nlins):
        for j in range(ncols):
            k = len(f"{mt[i][j]}")
            s +=  (max_len-k)*' ' + f"{mt[i][j]}" + ' '
        s += "\n" # nova linha

    return s

#------------------------------------------------------
def pause():
    '''(None) -> None
    PARA a execução até que seja teclado ENTER
    '''
    input("Tecle ENTER para continuar. ")
