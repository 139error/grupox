

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Atividade 18 - DicioB - dicionários ordenados

    Indique o código do Grupo (deveria ser o mesmo da computador
    que você usou no CEC, como A, B, C etc.).

    GRUPO: X
    
    Liste a seguir os nomes completos dos membros do time que participaram dessa atividade presencialmente:

    - Bianca Ângelo da Rocha Barreto
    - Marina Izabela
    - Ana Vitória Chaves Viana

'''

#--------------------------------------------------------------
class DicioB:
    #-----------------------------------------------
    def __init__(self):
        ''' (DicioB) -> None
        Chamado pelo construtor. 
        RECEBE uma referência self para um objeto DicioB.
        VINCULA os atributos chaves e valores.
        MÉTODO ESPECIAL: usado pelo Python quando escrevemos "objeto_DicioB = DicioB()".
        '''
        self.chaves  = []
        self.valores = []
        
    #---------------------------------------------
    def __str__(self):
        '''(DicioB) -> str 
        RECEBE uma referência self para um objeto DicioB.
        RETORNA uma string que representa o dicionário self.
        MÉTODO MÁGICO/ESPECIAL: usado pelo Python quando 
               escrevemos "print(objeto_DicioB)" ou "str(objeto DicioB)"
        '''
        s = ''
        # apelidos
        n = len(self) # usa o método __len__()
        chaves  = self.chaves
        valores = self.valores
        # percorra o dicionário
        for i in range(n):
            s += f"{chaves[i]}: {valores[i]}\n"
        return s    

    #---------------------------------------------        
    def indice(self, chave):
        '''(DicioB, obj) -> int
        RECEBE um objeto self da classe DicioB e um objeto chave.
            Supõe que as chaves em self.chaves estão em ordem crescente.
        RETORNA um índice i tal que:
            * val <= chave para val in self.chaves[0: i] e
            * val >  chave para val in self.chaves[i: n]
              em que n = len(self.chaves)
        NOTAS. Se a chave não está em self.chaves, então i é a posição em 
            self.chaves em que chave deve ser inserida para manter self.chaves 
            em ordem crescente.
            Em particular:
                * se i == 0, então chave deve ser inserida no início de self.chaves
                * se 0 < i <= n e self.chaves[i-1] != chave, então chave deve ser 
                         inserida na posição i de self.chaves 

            Faça o melhor proveito possível do fato que as chaves estão ordenadas 
            implementando uma busca binária.
        '''
        
        low = 0
        high = len(self) - 1
        mid = 0
            
        while low <= high:
            mid = (high + low) // 2
 
            if self.chaves[mid] < chave:
                low = mid + 1
 
            elif self.chaves[mid] > chave:
                high = mid - 1
 
            else:
                return mid
        
        for i in self.chaves:
            if i > chave:
                return self.chaves.index(i)
               
    #---------------------------------------------        
    def put(self, chave, valor):
        '''(DicioB, obj, obj) -> None
        RECEBE um objeto self da classe DicioB e um par de objetos chave-valor.
        INSERE o par chave-valor no dicionário. 
            Se a chave já estiver no dicionário, apenas o valor é atualizado.
        NOTAS. Os elementos da lista self.chaves devem ser mantidos em ordem 
            crescente por meio do método de ordenação por inserção:
            https://panda.ime.usp.br/algoritmos/static/algoritmos/18-busca-ordenacao.html#id2
        '''
        
        valor_aux = self.get(chave)
        index = len(self)
        
        if valor_aux == None:
            for i in self.chaves:
                if i > chave:
                    index = self.indice(i)
                    break
 
            if index == len(self):
                self.chaves.append(chave)
                self.valores.append(valor)
            else:
                self.valores = self.valores[:index] + [valor] + self.valores[index:]
                self.chaves = self.chaves[:index] + [chave] + self.chaves[index:]

        else:
            self.valores[self.indice(chave)] = valor 
        
        return None    

    #---------------------------------------------        
    def get(self, chave):
        '''(DicioB, obj) -> int ou None
        RECEBE um objeto self da classe DicioB e um objeto chave.
        RETORNA o valor em self correspondente à chave. 
            Se chave não está no dicionário, o método retorna None.
        NOTA. Este método pode supor que os elementos da lista 
            self.chaves estão em ordem crescente. 
        '''
        
        low = 0
        high = len(self) - 1
        mid = 0
 
        while low <= high:
            mid = (high + low) // 2
 
            if self.chaves[mid] < chave:
                low = mid + 1
 
            elif self.chaves[mid] > chave:
                high = mid - 1
 
            else:
                return self.valores[mid]
             
        return None  

    #---------------------------------------------
    # os demais métodos são fornecidos completos,
    # não é preciso modificá-los e você pode usá-los se desejar.
    #---------------------------------------------
    def __len__(self):
        '''(DicioB) -> int 
        RECEBE um objeto self da classe DicioB.
        Retorna o número de chaves e self.
        MÉTODO MÁGICO/ESPECIAL: usado pelo Python quando 
            escrevemos "len(objeto_DicioB)".
        '''
        return len(self.chaves)

    #---------------------------------------------        
    def __setitem__(self, chave, valor):
        '''(DicioB, obj, obj) -> None
        RECEBE um objeto self da classe DicioB e um par de objetos chave-valor.
        INSERE o par chave-valor no dicionário. 
            Se a chave já estiver no dicionário, apenas valor é atualizado.
        MÉTODO MÁGICO/ESPECIAL: usado pelo Python quando 
            escrevemos "objeto_DicioB[chave] = valor".
        '''
        self.put(chave, valor)
        return None
    
    #---------------------------------------------        
    def __getitem__(self, chave):
        '''(DicioB, obj) -> obj
        RECEBE um objeto self da classe DicioB e um objeto chave.
        RETORNA o valor do dicionário self associado à chave.
            Se a chave não estiver em self, retorna None.
        MÉTODO MÁGICO/ESPECIAL: usado pelo Python quando 
            escrevemos algo como "valor = objeto_DicioB[chave]".
        '''
        return self.get(chave)

    #---------------------------------------------    
    def __contains__(self, chave):
        ''' (DicioB, obj) -> bool
        RECEBE um objeto self da classe DicioB e um objeto chave.
        RETORNA True se chave está em self.chaves e False em caso contrário.
            Se a chave não estiver em self, retorna None.
        MÉTODO MÁGICO/ESPECIAL: usado pelo Python quando 
            escrevemos algo como "if chave in objeto_DicioB[chave]: ..."
        '''
        return chave in self.chaves
    
    #---------------------------------------------
    def __iter__(self):
        '''  (DicioB) -> iter
        RECEBE um objeto self da classe DicioB.
        RETORNA um iterador para as chaves do dicionário
        MÉTODO MÁGICO/ESPECIAL: usado pelo Python quando 
            escrevemos algo como "for chave in objeto_DicioB[chave]: ..."
        '''
        return iter(self.keys())
    
    #---------------------------------------------        
    def keys(self):
        '''(DicioB) -> list
        RECEBE um objeto self da classe DicioB.
        RETORNA uma cópia da lista com suas chaves.
        ''' 
        return self.chaves[:]

    #---------------------------------------------        
    def values(self):
        '''(DicioB) -> list
        RECEBE um objeto self da classe DicioB.
        RETORNA cópia/clone da lista dos valores em self.
        ''' 
        return self.valores[:]

    #---------------------------------------------        
    def items(self):
        '''(DicioB) -> list
        RECEBE um objeto self da classe DicioB.
        RETORNA uma lista com pares da forma (chave, valor) dos itens em self.
        '''
        lst = []
        # apelidos
        n       = len(self)
        chaves  = self.chaves
        valores = self.valores
        for i in range(n):
            lst += [(chaves[i], valores[i])]
        return lst            
    
#####################################################################    

def main():
    ''' 
    Unidade de teste para a classe DicioB
    '''
    print("Testes para a classe DicioB")
    print("--------------------------\n")
    
    # __init__() e __str__()
    print("crie um dicionário vazio")
    dB = DicioB()
    print(f"dB:\n{dB}") 
    pause() # aprecie a paisagem
    
    # put()
    print("\nteste put()")
    dB.put('fracassei', 3)
    dB.put('em', 1)
    dB.put('tudo', 1)
    print(f"dB:\n{dB}") 
    pause() # aprecie a paisagem
    
    # __setitem__()
    print("\nteste __setitem__()")
    dB['o'] = 2
    dB['que'] = 3
    dB['tentei'] = 4
    print(f"dB:\n{dB}") 
    pause() # aprecie a paisagem

    # put() e __setitem__()
    print("\nteste put() e __setitem__()")
    dB.put('o', 2)
    dB['que'] = 1
    dB['tentei'] = 5    
    print(f"dB:\n{dB}") 
    pause() # aprecie a paisagem

    # get()
    print("\nteste get()")
    print(f"dB.get('fracassei')={dB.get('fracassei')}")
    print(f"dB.get('em')={dB.get('em')}")
    print(f"dB.get('tudo')={dB.get('tudo')}\n")
    pause() # aprecie a paisagem

    # __getitem__()
    print("\nteste __getitem__()")
    print(f"dB['o']={dB['o']}")
    print(f"dB['que']={dB['que']}")
    print(f"dB['tentei']={dB['tentei']}")
    print(f"dB.get('vida')={dB.get('vida')}")
    print(f"dB['vida']={dB['vida']}\n")
    pause() # aprecie a paisagem

    # mais __setitem__()
    print("\nmais teste __setitem__(): chaves devem ser comparáveis por <, <=,...")
    dB['na'] = 1
    dB['vida'] = 1
    print(f"dB:\n{dB}") 
    pause() # aprecie a paisagem

    # teste __contains__()
    print("\nteste __contains__()")
    print(f"'tentei' in dB={'tentei' in dB}")
    print(f"'1' in dB={'1' in dB}")
    print(f"1 in d={1 in dB}")
    print(f"5 in d={5 in dB}\n")
    pause() # aprecie a paisagem
    
    # teste __iter__()
    print("\nteste __iter__(): usado para clonar d")
    clone = DicioB()
    for chave in dB: clone[chave] = dB[chave]
    print(f"clone:\n{clone}")
    pause() # aprecie a paisagem

    # teste __len__()
    print("\nteste __len__()")
    print(f"len(dB)={len(dB)}")
    print(f"len(clone)={len(clone)}")
    dicio_vazio = DicioB()
    print(f"len(dicio_vazio)={len(dicio_vazio)}\n")
    pause() # aprecie a paisagem

    # teste keys(), values() e items()
    print("\nteste keys(), values() e items()")
    print(f"clone.keys()={clone.keys()}")
    print(f"clone.values()={clone.values()}")
    print(f"clone.items()={clone.items()}\n")
    pause() # aprecie a paisagem

    print("FIM")

#-----------------------------------------------
def pause():
    input("Tecle ENTER para continuar: ")
    
#-----------------------------------------------
if __name__ == "__main__":
    main()
