#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Atividade 19 - Bolhinhas, bolhas e bolhonas

'''

#-------------------------------------------------------------------------
def main():
    ''' 
    Unidade de teste: coloque aqui os teste das suas funções.
    '''
    print("Testes de borbulheX():")
    v = [7, 4, 11, 5, 3]
    t, u = borbulheX(v, 3)
    print(f"v={v} deve ser v=[4, 7, 11, 5, 3]")
    print(f"t={t} deve ser t=1")
    print(f"u={u} deve ser u={1}")
    
    print("\nTestes de bubblesortX():")
    v = [7, 4, 11, 5, 3]
    t, c = bubblesortX(v)
    print(f"v={v} deve ser v=[3, 4, 5, 7, 11]")
    print(f"t={t} deve ser t=7")
    print(f"c={c} deve ser c={10}")

    print("\nTestes de borbulhe_de_luxe():")
    v = [7, 4, 11, 5, 3]
    t, u = borbulhe_de_luxe(v, e=0, d=3, passo=1)
    print(f"v={v} deve ser v=[4, 7, 11, 5, 3]")
    print(f"t={t} deve ser t=1")
    print(f"u={u} deve ser u={1}")

    print("\nTestes de shakersort():")
    v = [7, 4, 11, 5, 3]
    t, c = shakersort(v)
    print(f"v={v} deve ser v=[3, 4, 5, 7, 11]")
    print(f"t={t} deve ser t=7")
    print(f"c={c} deve ser c={12}")

    v = [3, 4, 5, 7, 11]
    t, c = shakersort(v)
    print(f"v={v} deve ser v=[3, 4, 5, 7, 11]")
    print(f"t={t} deve ser t=0")
    print(f"c={c} deve ser c={4}")
    
#-------------------------------------------------------------------------    
def borbulhe(v, n):
    ''' (list, int) -> int
    RECEBE uma lista v e um inteiro n.
    PERCORRE sequencialmente, do início até o fim, a lista v[0:n] desfazendo através
       de trocas todas as inversões encontradas ao logo do caminhoCANDO de posição
    RETORNA o número de trocas realizadas durante o percurso.
    '''
    trocas = 0
    for j in range(1, n):
        if v[j] < v[j-1]:
            v[j], v[j-1] = v[j-1], v[j]
            trocas += 1
    return trocas

#-------------------------------------------------------------------------    
def bubblesort(v):
    '''(list) -> int
    RECEBE uma lista v.
    REARRANJA os elementos de v para que fique crescente.
    RETORNA o número de trocas feitas durante o processo.
    '''
    total_de_trocas = 0   
    n = len(v)
    for i in range(n, 1, -1):  #1#
        total_de_trocas += borbulhe(v, i)
    return total_de_trocas

#-------------------------------------------------------------------------
def borbulheX(v, n):
    '''(list, int) -> int, int
    RECEBE uma lista v e um inteiro n.
    PERCORRE sequencialmente, do início até o fim, a lista v[0:n] desfazendo através
       de trocas todas as inversões encontradas ao logo do caminho.
    RETORNA o número de trocas realizadas durante o percurso e também
        RETORNA o maior índice de uma posição de v que foi alterada durante
        o percurso. Se nenhum posição de v é alterada a função deve retorna o
        par (0, 0).
    '''
    indice = 0
    trocas = 0
    for j in range(1, n):
        if v[j] < v[j-1]:
            v[j], v[j-1] = v[j-1], v[j]
            trocas += 1
            indice = j
            
    return (trocas, indice)
    
#-------------------------------------------------------------------------
def bubblesortX(v):
    '''(list) -> int, int
    RECEBE uma lista v.
    REARRANJA os elementos de v para que fique crescente.
    RETORNA o número de trocas e RETORNA o número de comparações 
        feitas durante o processo.
    '''
    
    n = len(v)
    trocas = 0
    trocas_total = 0
    comparacoes = (n-1)
    
    while (n > 1):
        trocas, n = borbulheX(v, n)      
        comparacoes += (n-1)
        trocas_total += trocas
        
    return (trocas_total, comparacoes)
    
    
    
#-------------------------------------------------------------------------
def borbulhe_de_luxe(v, e, d, passo):
    '''(list, int, int, int) -> int, int
    RECEBE uma lista v e três inteiros e e d e passo em que 
        e <= d e passo é +1 ou -1.
    PERCORRE sequencialmente a sublista v[e:d] desfazendo através
       de trocas todas as inversões encontradas ao logo do caminho.
       Se passo é +1 o percurso é feito da esquerda para a direita.
       Se passo é -1 o percurso é feito da direita para a esquerda.
    RETORNA o número de trocas realizadas durante o percurso e também
        RETORNA o maior índice da última  posição de v que foi alterada durante
        o percurso. Se passo é +1 o índice deve ser o maior possível e 
        se passo é -1 o índice deve ser o menor possível. Se nenhuma troca é 
        realizada a função RETORNA (0, e) se passo é +1 e RETORNA  (0, d) 
        se passo é -1.
    '''
    
    trocas = 0
        
    if passo == 1: 
        indice = e
    
        for j in range(e + 1, d):
            if v[j] < v[j-1]:
                v[j], v[j-1] = v[j-1], v[j]
                trocas += 1
                indice = j
                
    elif passo == -1: 
        indice = d 
    
        for j in range(d, e - 1, -1):
            if v[j] < v[j-1]:
                v[j], v[j-1] = v[j-1], v[j]
                trocas += 1
                indice = j-1 
            
    return (trocas, indice)

#-------------------------------------------------------------------------
def shakersort(v):
    '''(list) -> int, int
    RECEBE uma lista v.
    REARRANJA os elementos de v para que v fique crescente
    '''
    total_trocas = 0
    total_cmps   = 0
    e = 0
    d = len(v)
    passo = 1
    while d > e+1:
        total_cmps += d - e - 1
        trocas, ult = borbulhe_de_luxe(v, e, d, passo)
        total_trocas += trocas
        if passo == 1: d = ult
        else: e = ult+1
        passo *= -1
    return total_trocas, total_cmps    

## ==================================================================    
if __name__ == '__main__':
    main()
