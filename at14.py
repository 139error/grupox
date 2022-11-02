
'''
    Atividade 14 - Mecânica recursiva

    Indique o código do Grupo (deveria ser o mesmo da computador
    que você usou no CEC, como A, B, C etc.).

    GRUPO: X
    
    Liste a seguir os nomes completos dos membros do time que participaram dessa atividade presencialmente:

    - Marina Izabela
    - Eloá Bastos de Sá
    - Bianca Ângelo da Rocha Barreto

'''

# número de espaços usados para indicar a hereditariedade das chamadas
TAB = '    ' # 4 espaços


def main():
    print("Teste fatorialRX():")
    k = fatorialRX(3)
    #print(f"fatorialRX(3) = {k}\n")
    
    print("\nTeste conte_collatz():")
    k = conte_collatz(7)
    print(f"\nconte_collatz(7) = {k}\n")
    
    
    print("Teste HanoiA():")
    k = hanoiA(4,'A','B','C')
    print(f"hanoiA(4,'A','B','C') = {k}\n")


    print("Teste HanoiB():")
    k = hanoiB(4,'A','B','C')
    print(f"hanoiB(4,'A','B','C') = {k}\n")


    print("Teste HanoiC():")
    k = hanoiC(2,'A','B','C')
    print(f"hanoiC(4,'A','B','C') = {k}")

#---------------------------------------------------------------------
def fatorialRX(n, nivel = 0):
    '''(int, int) -> int
    RECEBE um inteiro n e um inteiro nivel indicando a hereditariedade da 
        chamada: 0=mãe, 1=filha, 2=neta, 3=bisneta,...        
    RETORNA n! 
        e IMPRIME o rastro da execução da função.
    '''
    
    # caso base
    if n == 0: 
        print(f'{TAB * nivel}fatorialRX(0) = 1')
        return 1
    else:
        # resolva uma simplificação do problemas e monte a solução da chamada atual
     
        print(f'{TAB * nivel}fatorialRX({n})')
        nivel += 1          
        result = n * fatorialRX(n-1, nivel)
    
        # going out of that level of recursion
        nivel -= 1
        
        # result is printed on the next level
        print(f'{TAB * (nivel)}fatorialRX({n}) = {result}')
    
        return result

#---------------------------------------------------------------------    
def conte_collatz(n, nivel = 0):
    '''(int) -> int
    RECEBE um número inteiro positivo n.
    RETORNA o número de chamadas recursivas de collatz(n) 
        e IMPRIME a sequência de collatz de n.
    '''
    print(f"{n} ", end="")
      
    # caso base
    if n == 1: 
        return nivel
       
    if n % 2 == 0: 
        nivel+=1
        result = conte_collatz(n//2, nivel)
        
    else: 
        nivel +=1
        result = conte_collatz(3*n+1, nivel)
    
    return result

#---------------------------------------------------------------------
def hanoiA(n, origem, auxiliar, destino):
    '''(int, str, str, str) -> int
    RECEBE o número n de discos e os nomes dos pinos origem, auxiliar e destino 
        do quebra-cabeça das Torres de Hanoi.
    RETORNA o número de movimentos feitos para resolver o quebra-cabeça 
        e IMPRIME a sequência das mensagens com os movimentos que o resolve.
    '''
       
    if n == 0: return 1
    else:
        hanoiA(n-1, origem, destino, auxiliar)
    
        print(f"mova o disco {n} do pino {origem} para o pino {destino}")
        
        hanoiA(n-1, auxiliar, origem, destino)
        
    return 2**n-1
    
    
#---------------------------------------------------------------------
def hanoiB(n, origem, auxiliar, destino, nmovs=0):
    '''(int, str, str, str, int) -> int
    RECEBE o número n de discos e os nomes dos pinos origem, auxiliar e destino 
        do quebra-cabeça das Torres de Hanoi e o número nmovs de movimentos 
        feitos até a chamada atual.
    RETORNA o número de movimentos feitos para resolver o quebra-cabeça 
        e IMPRIME a sequência das mensagens com os movimentos que o resolve.
        Na sequência cada mensagem tem em seu início o número do movimento;
    '''
       
    # 1. caso base
    if n == 0: 
        return nmovs
    else:
        # 2. reduza e resolva recursivamente e combine a solução dos subproblemas
    
        nmovs = hanoiB(n-1, origem, destino, auxiliar, nmovs) # reduza e resolva recursivamente
    
        nmovs += 1
        print(f"{nmovs}: mova o disco {n} do pino {origem} para o pino {destino}")
    
        return hanoiB(n-1, auxiliar, origem, destino, nmovs) # reduza e resolva recursivamente


#---------------------------------------------------------------------
def hanoiC(n, origem, auxiliar, destino, nmovs=0, nivel=0):
    '''(int, str, str, str, int, int) -> int
    RECEBE o número n de discos e os nomes dos pinos origem, auxiliar e destino 
        do quebra-cabeça das Torres de Hanoi, o número nmovs de movimentos 
        feitos até a chamada atual e um inteiro nivel indicando a hereditariedade 
        da recursão: 0=mãe, 1=filha, 2=neta, 3=bisneta,...
    RETORNA o número de movimentos feitos para resolver o quebra-cabeça 
        e IMPRIME a sequência das mensagens com os movimentos que o resolve 
        imersa no rastro da execução da função.
        Na sequência cada mensagem tem em seu início o número do movimento;
    '''
    
    print(f'{TAB * (nivel)}hanoiC({n}, {origem}, {auxiliar}, {destino})')
    #print(nmovs)
    # 1. caso base
    if n == 0: 
        print(f'{TAB * (nivel)}hanoiC(0, {origem}, {auxiliar}, {destino}) = 0')
        return nmovs
    else:
        # 2. reduza e resolva recursivamente e combine a solução dos subproblemas
        nmovs = hanoiC(n-1, origem, destino, auxiliar, nmovs, nivel + 1) # reduza e resolva recursivamente
        print(f'{TAB * (nivel+1)}hanoiC({n}, {origem}, {auxiliar}, {destino}) = {nmovs}')
        nmovs +=1
        print(f"{TAB * (nivel+1)}{nmovs}: mova o disco {n} do pino {origem} para o pino {destino}")
        
        return hanoiC(n-1, auxiliar, origem, destino, nmovs, nivel + 1) # reduza e resolva recursivamente

if __name__ == "__main__":
    main()