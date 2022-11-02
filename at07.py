# -*- coding: utf-8 -*-
'''
    Atividade 07 - usos da estrutura abstrata de dados Pilha

    Indique o código do Grupo (deveria ser o mesmo da computador
    que você usou no CEC, como A, B, C etc.).

    GRUPO: X
    
    Liste a seguir os nomes completos dos membros do time que participaram dessa atividade presencialmente:

    - Marina Izabela
    - Bianca Ângelo da Rocha Barreto
    - Marcelo de Souza Varges Junior

'''

# CONSTANTES QUE VOCÊ PODE USAR CASO DESEJAR


class Pilha:
    def __init__(self):
        self.dados = []
    def __len__(self):
        return len(self.dados)
    def vazia(self):
        return self.dados == []
    def empilhe(self, item):
        self.dados.append(item)
    def desempilhe(self):
        return self.dados.pop()
    def topo(self):
        return self.dados[-1]

# ---------------------------------------------------------

def bem_formada( seq ):
    ''' (str) -> bool
    Recebe uma string seq contendo uma sequência formada pelos
    caracteres '()[]{}'. 
    Retorna True caso a sequência esteja bem formada e False em
    caso contrário.
    A função deve ignorar caracteres diferentes de '()[]{}' 
    sem resultar em erro.
    Exemplos:
    >>> bem_formada( "(a+ {b })-{2*[3+4]}" )
    True
    >>> bem_formada( "( ( (  ) " )
    False
    >>> bem_formada( " { ( { x } )  } [ y ]" )
    True
    >>> bem_formada( " { ( { x }  } [ y ] )" )
    False
    '''
    
    ABRE = ['(', '[', '{', '$']
    FECHA = [')', ']', '}']


    pilha_aux = Pilha()
    
    for i in seq:
        if i in ABRE:
            pilha_aux.empilhe(i)
            if i == '$':
                ABRE.pop()
                FECHA.append('$')
                
        elif i in FECHA:          
            if i != '$':
                pos = FECHA.index(i)
                if pilha_aux.vazia() is False and ABRE[pos] == pilha_aux.topo():
                    pilha_aux.desempilhe()
                else:
                    return False
            else:
                if pilha_aux.vazia() is False and '$' == pilha_aux.topo():
                    FECHA.pop()
                    ABRE.append('$')
                    pilha_aux.desempilhe()

            
            
    if pilha_aux.vazia():
        return True
    else:
        return False

# ---------------------------------------------------------

def main():
    ''' função para teste da função bem_formada
    '''
    
    
    print("-*- testes bem_formada() -*-")
    print("a função bem_formada((a+ {b })-{2*[3+4]}) deveria voltar True e voltou", bem_formada( "(a+ {b })-{2*[3+4]}" ))
    print("a função bem_formada(( ( (  )) deveria voltar False e voltou", bem_formada( "( ( (  ) " ))
    print("a função bem_formada({ ( { x } )  } [ y ]) deveria voltar True e voltou", bem_formada( " { ( { x } )  } [ y ]" ))
    print("a função bem_formada({ ( { x }  } [ y ] )) deveria voltar False e voltou", bem_formada( " { ( { x }  } [ y ] )" ))
    
    
    print("\n\n-*- testes bem_formada() pt2 -*-")
    print("a função bem_formada([ $ { } $ ] $ ( $ $ $ $ ) $) deveria voltar True e voltou", bem_formada( "[ $ { } $ ] $ ( $ $ $ $ ) $" ))
    print("a função bem_formada($ $ { }) deveria voltar True e voltou", bem_formada( "$ $ { }" ))
    print("a função bem_formada($$$) deveria voltar False e voltou", bem_formada( " $$$" ))
    print("a função bem_formada($ { $ }) deveria voltar False e voltou", bem_formada( "$ { $ }" ))
    print("a função bem_formada(( $ $ $ ) $) deveria voltar False e voltou", bem_formada( "( $ $ $ ) $" ))
    
    
    print("\n-*- testes bin2dec() -*-")
    print("a função bin2dec(11) deveria voltar 3 e voltou", bin2dec(11))
    print("a função bin2dec(1110) deveria voltar 14 e voltou", bin2dec(1110))
    print("a função bin2dec(111101010) deveria voltar 490 e voltou", bin2dec(111101010))
    print("a função bin2dec(1111010111010100) deveria voltar 62932 e voltou", bin2dec(1111010111010100))
    print("a função bin2dec(1110101000101111111101) deveria voltar 3836925 e voltou", bin2dec(1110101000101111111101))
    
    
    print("\n-*- testes dec2bin() -*-")
    print("a função dec2bin(5) deveria voltar 101 e voltou", dec2bin(5))
    print("a função dec2bin(11) deveria voltar 1101 e voltou", dec2bin(11))
    print("a função dec2bin(45) deveria voltar 101101 e voltou", dec2bin(45))
    print("a função dec2bin(666) deveria voltar 1010011010 e voltou", dec2bin(666))
    print("a função dec2bin(45212) deveria voltar 1011000010011100 e voltou", dec2bin(45212))
    print("a função dec2bin(546546) deveria voltar 10000101011011110010 e voltou", dec2bin(546546))
    


# ---------------------------------------------------------

def bin2dec( bin ):
    ''' (int) -> int
    Recebe um inteiro que representa um número na base binária e 
    retorna outro inteiro que representa o mesmo número na base decimal.
    Exemplo:
    >>> bin2dec( 11 )
    3
    >>> bin2dec( 1110 )
    14
    '''
    
    bin1 = bin
    
    decimal, i = 0, 0
    
    while(bin1 != 0):
        dec = bin1 % 10
        decimal = decimal + dec * pow(2, i)
        bin1 = bin1//10
        i += 1
    
    return decimal


def dec2bin( dec ):
    ''' (int) -> int
    Recebe um inteiro que representa um número na base decimal e 
    retorna outro inteiro que representa o mesmo número na base binária.
    Exemplo:
    >>> dec2bin( 11 )
    1101
    >>> dec2bin( 5 )
    101
    '''
    
    pilha_aux = Pilha()

    while dec > 0:
        aux = dec % 2
        pilha_aux.empilhe(aux)
        dec = dec // 2

    binString = ""
    while not pilha_aux.vazia():
        binString = binString + str(pilha_aux.desempilhe())

    return binString


# ---------------------------------------------------------
#  chama a main()
# ---------------------------------------------------------
if __name__ == '__main__':
    main()