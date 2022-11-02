#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    AT16 Amnésia recursiva

    Neste arquivo vocês podem selecionar alguns valores
'''

# cronometro()
from util import cronometro

# maxI() e maxR()
from at16 import binomialR, binomialRC, binomialI, binomialRM, outra


# ATRIBUA True para as funções que deseja cronometrar
BINOMIALR  = False
BINOMIALI  = False
BINOMIALRC = False
BINOMIALRM = False
OUTRA      = False

# ESCOLHA o número de testes
NO_TESTES = 10 # Hmm. Talvez seja bom nã aumentar muito

# ESCOLHA os valores iniciais
N = 3
K = 2

#------------------------------------------------------
def main():
    #------------------------------------------------
    # imprima cabeçalho 
    print("     n     k", end="")
    if BINOMIALR : print("   binomialR()", end="")
    if BINOMIALRC: print("  binomialRC()", end="")
    if BINOMIALI : print("   binomialI()", end="")
    if BINOMIALRM: print("  binomialRM()", end="")
    if      OUTRA: print("       outra()", end="")
    print()

    # n e k são os argumentos, você pode escolher outros 
    n = N
    k = K
    for i in range(NO_TESTES):
        # cronometre as funções
        if BINOMIALR:   t_R,  resp_R = cronometro( binomialR, n, k)
        if BINOMIALRC: t_RC, resp_RC = cronometro(binomialRC, n, k)
        if BINOMIALI:   t_I,  resp_I = cronometro( binomialI, n, k)
        if BINOMIALRM: t_RM, resp_RM = cronometro(binomialRM, n, k)
        if      OUTRA:  t_O,  resp_O = cronometro(     outra, n, k)
   
        print(f"{n:6}{k:6}", end="")    
        if BINOMIALR : print(f"{t_R:10.2f}   ", end="")
        if BINOMIALRC: print(f"{t_RC:10.2f}    ", end="")
        if  BINOMIALI: print(f"{t_I:10.2f}   ", end="")
        if BINOMIALRM: print(f"{t_RM:10.2f}   ", end="")
        if      OUTRA: print(f"{t_O:10.2f}   ", end="")
        print()
        
        # valores de n e k são dobrados para a próxima iteração
        n *= 2
        k *= 2
 
    print("Tempos em segundos.\n")

#---------------------------------------------------------    
if __name__ == "__main__":
    main()
