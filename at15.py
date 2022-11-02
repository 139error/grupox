'''
    Atividade 15 - Prática recursiva

    Indique o código do Grupo (deveria ser o mesmo da computador
    que você usou no CEC, como A, B, C etc.).

    GRUPO: X
    
    Liste a seguir os nomes completos dos membros do time que participaram dessa atividade presencialmente:
    
        - Marina Izabela
    - Eloá Bastos de Sá
    - Bianca Ângelo da Rocha Barreto

'''


def main():
    print("Testes de fibonacciR():")
    k = fibonacciR(5)  
    print (f'fibonacciR(5) = {k} deve ser 5.')
    k = fibonacciR(6)
    print (f'fibonacciR(6) = {k} deve ser 8.')
    k = fibonacciR(7)
    print (f'fibonacciR(7) = {k} deve ser 13.')
    k = fibonacciR(10)
    print (f'fibonacciR(10) = {k} deve ser 55')

        
    print("\nTestes de somadigitosR():")
    k = somadigitosR(19)  
    print (f'somadigitos(19) = {k} deve ser 10.')
    k = somadigitosR(191)
    print (f'somadigitosR(191) = {k} deve ser 11.')
    k = somadigitosR(1000)
    print (f'somadigitosR(1000) = {k} deve ser 1.')
    
    
    print("\nTestes de palindromoR():")
    k = palindromoR('baba')  
    print (f'palindromoR("baba") = {k} deve ser False.')
    k = palindromoR('baxab')
    print (f'palindromoR("baxab") = {k} deve ser True.')
    k = palindromoR('roma me tem amor')
    print (f'palindromoR("roma me tem amor") = {k} deve ser False.')
    k = palindromoR('romametemamor')
    print (f'palindromoR("romametemamor") = {k} deve ser True')
    
    print("\nTestes de dec2binR():")
    k = dec2binR(10)  
    print (f'dec2binR(10) = {k} deve ser 1010.')
    k = dec2binR(7)
    print (f'dec2binR(7) = {k} deve ser 111.')
    k = dec2binR(15)
    print (f'dec2binR(15) = {k} deve ser 1111.')
    k = dec2binR(16)
    print (f'dec2binR(16) = {k} deve ser 10000')
    
    print("\nTestes de reguaR():")
    k = reguaR(3)  
    #print(k)
    #print('[1, 2, 1, 3, 1, 2, 1]\n')
    print (f'reguaR(3) = {k} deve ser [1, 2, 1, 3, 1, 2, 1].')
    k = reguaR(4)
    #print(k)
    #print('[1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1]\n')
    print (f'reguaR(4) = {k} deve ser [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1].')
    k = reguaR(5)
    #print(k)
    #print('[1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1]\n')
    print (f'reguaR(5) = {k} deve ser [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1].')
    
#------------------------------------------------    
def fibonacciR(n):
    '''(int) -> int
    RECEBE um inteiro não negativos n.
    RETORNA o n-ésimo número de Fibonacci.
    '''
    
    if n == 1 or n== 2:
        return 1
    else:
        return fibonacciR(n-1) + fibonacciR(n-2)
    

#---------------------------------------------------------
def somadigitosR(n):
    '''(int) -> int
    RECEBE um número inteiro não-negativo n.
    RETORNA a soma dos dígitos de n
    '''

    if n == 0:
        return 0

    return (n % 10 + somadigitosR(int(n / 10)))

#---------------------------------------------------------
def palindromoR(s):
    '''(str) -> bool
    RECEBE uma string s.
    RETORNA True se s for palindromo e False em caso contrário
    '''
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    
    return palindromoR(s[1:-1])

    
#---------------------------------------------------------    
def dec2binR(n):
    '''(int) -> str
    RECEBE um número inteiro não-negativo n representado na base 10.
    RETORNA a string com a representação binária de n.
    '''
    if n == 0:
        return ''
    else:
        return dec2binR(n//2) + str(n % 2)
#---------------------------------------------------------    
def reguaR(n):
    '''(int) -> list
    RECEBE um inteiro não negativo n.
    RETORNA uma lista com a sequência de inteiros correspondente a uma 
        régua de ordem n.
    '''
    if n == 0:
        return []
    else:
        lista = reguaR(n - 1)
        lista.append(n)
        return lista + reguaR(n - 1)
        
        

if __name__ == "__main__":
    main()