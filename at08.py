# -*- coding: utf-8 -*-
'''
    Atividade 08 - usos da estrutura abstrata de dados Pilha

    Indique o código do Grupo (deveria ser o mesmo da computador
    que você usou no CEC, como A, B, C etc.).

    GRUPO: X
    
    Liste a seguir os nomes completos dos membros do time que participaram dessa atividade presencialmente:

    - Bianca Ângelo da Rocha Barreto
    - Marina Izabela 
    - Marcelo de Souza Varges Junior

'''

# CONSTANTES QUE VOCÊ PODE USAR CASO DESEJAR

ADD  = "+"
SUB  = "-"
MUL  = "*"
DIV  = "/"

# ---------------------------------------------------------

def main():
    ''' função para teste da função palindromo(), polonesa()
    e outros testes que desejar.
    '''
    
    TESTE = ['ahlip', 'ala', 'sala', 'salas', 'socorrammesubinoonibusemmarrocos' ]
    ESPERADO = [False, True, False, True, True]

    n = len(TESTE)
    
    print("\n-*- testes da função palindromo -*-\n")
    for t in range( n ):
        s = TESTE[t]
        r = ESPERADO[t]
        print(f'{s}: devolveu {palindromo(s)} e deve ser {r}')
        print('\n')
    
    print("\n-*- testes da função polonesa() -*-\n")
    print(f"polonesa('2 +') = {polonesa('2 +')} deve ser 'Erro: faltam operandos'")
    print("\n")
    print(f"polonesa('2 3 + * 4') = {polonesa('2 3 + * 4')} deve ser 'Erro: faltam operandos'")
    print("\n")
    print(f"polonesa('2 3 + 4') = {polonesa('2 3 + 4')} deve ser 'Erro: faltam operadores'")
    print("\n")
    print(f"polonesa('2 3 + 4 *') = {polonesa('2 3 + 4 *')} deve ser 20")
    print("\n")
    print(f"polonesa('2 3 +') = {polonesa('2 3 +')} deve ser 5")
    print("\n")
    print(f"polonesa('2 3 * 4.0 +') = {polonesa('2 3 * 4.0 +')} deve ser 10.0")


# ---------------------------------------------------------
#  A seguinte classe Pilha deve ser usada pelas funções 
#  palindromo() e polonesa()
#
#  NÃO MODIFIQUE ESSA CLASSE
# ---------------------------------------------------------

class Pilha:
    def __init__(self):
        '''(Pilha) -> None
        Monta um objeto da classe Pilha.
        '''
        self.dados = []

    def __len__(self):
        '''(Pilha) -> int
        Recebe uma Pilha referenciada por self e retorna
        o número de itens na pilha.
        Usado pelo Python quando escrevemos len(Pilha).
        '''
        return len(self.dados)

    def vazia(self):
        '''(Pilha) -> bool
        Recebe uma Pilha referenciada por self e retorna 
        True se ela está vazia e False em caso contrário.
        '''
        return self.dados == []

    def empilhe(self, item):
        '''(Pilha, objeto) -> None
        Recebe uma Pilha referenciada por self e um objeto 
        item e coloca item no topo da pilha.
        ''' 
        self.dados.append(item)

    def desempilhe(self):
        '''(Pilha) -> objeto
        Recebe uma Pilha referenciada por self e desempilha 
        e retorna o objeto no topo da pilha.
        '''
        return self.dados.pop()

    def topo(self):
        '''(Pilha) -> objeto 
        Recebe uma Pilha referenciada por self e retorna
        o objeto no topo da pilha. O objeto não é removido 
        da pilha.
        '''
        return self.dados[-1]

# ---------------------------------------------------------
def palindromo(seq):
    ''' (str) -> bool
    Verifica se a string s é palíndromo.
    Dica: use uma pilha para inverter s.
    '''
    
    inversa = Pilha()
    string = ''
    
    for i in seq:
        inversa.empilhe(i)

    for i in range(len(inversa)):
        string += inversa.desempilhe()

    if string == seq:
        return True
    
    return False 

# ---------------------------------------------------------

def polonesa( exp ):
    ''' (str) -> int|float

    Recebe uma string com uma expressão numérica em notação posfixa 
    e calcula e retorna o valor da expressão.

    Pré-condição: a função supõe que a expressão está
         correta e os operadores e operandos estão separados
         por pelo menos um espaço.

    Exemplos:
    >>> polonesa("2 3 +")
    5
    >>> polonesa("2 3 * 4.0 +")
    10.0
    '''
    
    pilha = Pilha()
    seq = separe(exp)
    tem_float = False
    
    for i in seq:
        if is_int(i):
            pilha.empilhe(int(i))
        elif is_float(i):
            tem_float = True
            pilha.empilhe(float(i))
            
        elif i in [ADD, SUB, MUL, DIV]:
            if (bem_formada(pilha)):  
                item1 = pilha.desempilhe()
                item2 = pilha.desempilhe()
                
                if(tem_float):
                    item1 = float(item1)
                    item2 = float(item2)
                    
                if i == ADD: result = item1 + item2
                if i == SUB: result = item1 - item2
                if i == MUL: result = item1 * item2
                if i == DIV: result = item1 / item2
                pilha.empilhe(result)
            else: 
                return None
        if (i == seq[-1]):
            if is_number(seq[-1]):
                print("Erro: faltam operadores")
                return None
    

    return(pilha.desempilhe())
# ---------------------------------------------------------
# coloque a seguir outras funções caso desejar.
# ---------------------------------------------------------

def is_int(ln):
    try:
        int(ln)
        return True
    except ValueError:
        return False
    
def is_float(ln):
    try:
        float(ln)
        return True
    except ValueError:
        return False

def is_number(ln):
    if is_int(ln) or is_float(ln):
        return True
    return False
    
    
def separe( exp ):
    ''' (str) -> list
    recebe uma expressão exp contendo itens léxicos separados por expaço e 
    retorna uma lista com os itens léxicos da expressão.
    '''
    s = exp.strip()  ## remove brancos das extremidades de exp
    itens = s.split()  ## quebra a expressão nos espaços
    return itens


def bem_formada(pilha): 
    if len(pilha) >= 2:
        return True
    
    print("Erro: faltam operandos!")
    return (False)

# ---------------------------------------------------------
#  chama a main()
# ---------------------------------------------------------
if __name__ == '__main__':
    main()