#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Atividade 17 - dicionários

    Indique o código do Grupo (deveria ser o mesmo da computador
    que você usou no CEC, como A, B, C etc.).

    GRUPO: X
    
    Liste a seguir os nomes completos dos membros do time que participaram dessa atividade presencialmente:

    - Marina Izabela
    - Eloá Bastos de Sá
    - Bianca Ângelo da Rocha Barreto

'''
    
#--------------------------------------------------------------
class Dicio:
    #-----------------------------------------------
    def __init__(self, chaves=[], valores=[]):
        ''' (Dicio) -> None
        Chamado pelo construtor. 
        RECEBE uma referência self para um objeto Dicio.
        VINCULA os atributos chaves e valores.
        MÉTODO ESPECIAL: usado pelo Python quando escrevemos "objeto_Dicio = Dicio()".
        '''
        self.chaves  = chaves[:]
        self.valores = valores[:]
        
    #---------------------------------------------
    def __str__(self):
        '''(Dicio) -> str 
        RECEBE uma referência self para um objeto Dicio.
        RETORNA uma string que representa o dicionário self.
        MÉTODO MÁGICO/ESPECIAL: usado pelo Python quando 
               escrevemos "print(objeto_Dicio)" ou "str(objeto Dicio)"
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
        '''(Dicio, obj) -> int ou None
        RECEBE um objeto self da classe Dicio e um objeto chave.
        RETORNA a posição de chave na lista self.chaves. 
            Se a chave não está no dicionário, o método retorna None.
        '''
        
        for i in self.chaves:
            if i == chave:
                return self.chaves.index(chave)
            
        return None
    
    #---------------------------------------------        
    def put(self, chave, valor):
        '''(Dicio, obj, obj) -> None
        RECEBE um objeto self da classe Dicio e um par de objetos chave-valor.
        INSERE o par chave-valor no dicionário. 
            Se a chave já estiver no dicionário, apenas valor é atualizado.
        '''
        
        valor_aux = self.get(chave)

        if valor_aux == None:
            self.chaves.append(chave)
            self.valores.append(valor)
        else:
            self.valores[self.indice(chave)] = valor 
        
        return None    
       
    #---------------------------------------------        
    def __setitem__(self, chave, valor):
        '''(Dicio, obj, obj) -> None
        RECEBE um objeto self da classe Dicio e um par de objetos chave-valor.
        INSERE o par chave-valor no dicionário. 
            Se a chave já estiver no dicionário, apenas valor é atualizado.
        MÉTODO MÁGICO/ESPECIAL: usado pelo Python quando 
            escrevemos "objeto_Dicio[chave] = valor".
        '''        
        
        self.put(chave, valor)        
        
    #---------------------------------------------        
    def get(self, chave):
        '''(Dicio, obj) -> int ou None
        RECEBE um objeto self da classe Dicio e um objeto chave.
        RETORNA o valor em self correspondente à chave. 
            Se chave não está no dicionário, o método retorna None.
        '''  
        
        for i in self.chaves:
            if chave == i:
                return self.valores[self.indice(chave)]
            
        return None
    
    #---------------------------------------------        
    def __getitem__(self, chave):
        '''(Dicio, obj) -> obj
        RECEBE um objeto self da classe Dicio e um objeto chave.
        RETORNA o valor do dicionário self associado à chave.
            Se a chave não estiver em self, retorna None.
        MÉTODO MÁGICO/ESPECIAL: usado pelo Python quando 
            escrevemos algo como "valor = objeto_Dicio[chave]".
        '''
        
        self.get(chave)

    #---------------------------------------------        
    def items(self):
        '''(Dicio) -> list
        RECEBE um objeto self da classe Dicio.
        RETORNA uma lista com pares da forma (chave, valor) dos itens em self.
        '''
        lista = []
        
        for i in range(len(self)):
            lista+= (self.chaves[i], self.valores[i]) 
        
        return lista

    #---------------------------------------------
    # os demais métodos são fornecidos completos,
    # não é preciso modificá-los e você pode usá-los se desejar.
    #---------------------------------------------
    def __len__(self):
        '''(Dicio) -> int 
        RECEBE um objeto self da classe Dicio.
        Retorna o número de chaves e self.
        MÉTODO MÁGICO/ESPECIAL: usado pelo Python quando 
            escrevemos "len(objeto_Dicio)".
        '''
        return len(self.chaves)

    #---------------------------------------------    
    def __contains__(self, chave):
        '''
        RECEBE um objeto self da classe Dicio e um objeto chave.
        RETORNA True se chave está em self.chaves e False em caso contrário.
            Se a chave não estiver em self, retorna None.
        MÉTODO MÁGICO/ESPECIAL: usado pelo Python quando 
            escrevemos algo como "if chave in objeto_Dicio[chave]: ..."
        '''
        return chave in self.chaves
    
    #---------------------------------------------
    def __iter__(self):
        '''
        RECEBE um objeto self da classe Dicio.
        RETORNA um iterador para as chaves do dicionário
        MÉTODO MÁGICO/ESPECIAL: usado pelo Python quando 
            escrevemos algo como "for chave in objeto_Dicio[chave]: ..."
        '''
        return iter(self.keys())
    
    #---------------------------------------------        
    def keys(self):
        '''(Dicio) -> list
        RECEBE um objeto self da classe Dicio.
        RETORNA uma cópia da lista com suas chaves.
        ''' 
        return self.chaves[:]

    #---------------------------------------------        
    def values(self):
        '''(Dicio) -> list
        RECEBE um objeto self da classe Dicio.
        RETORNA cópia/clone da lista dos valores em self.
        ''' 
        return self.valores[:]
         
#####################################################################    

def main():
    ''' 
    Unidade de teste para a classe Dicio
    '''
    print("Testes para a classe Dicio")
    print("--------------------------\n")
    
    # __init__() e __str__()
    print("crie um dicionário vazio")
    d = Dicio()
    print(f"d:\n{d}") 
    pause() # aprecie a paisagem
    
    # put()
    print("\nteste put()")
    d.put('fracassei', 3)
    d.put('em', 1)
    d.put('tudo', 1)
    print(f"d:\n{d}") 
    pause() # aprecie a paisagem
    
    # __setitem__()
    print("\nteste __setitem__()")
    d['o'] = 2
    d['que'] = 3
    d['tentei'] = 4
    print(f"d:\n{d}") 
    pause() # aprecie a paisagem

    # put() e __setitem__()
    print("\nteste put() e __setitem__()")
    d.put('o', 2)
    d['que'] = 1
    d['tentei'] = 5    
    print(f"d:\n{d}") 
    pause() # aprecie a paisagem

    # get()
    print("\nteste get()")
    print(f"d.get('fracassei')={d.get('fracassei')}")
    print(f"d.get('em')={d.get('em')}")
    print(f"d.get('tudo')={d.get('tudo')}\n")
    pause() # aprecie a paisagem

    # __getitem__()
    print("\nteste __getitem__()")
    print(f"d['o']={d['o']}")
    print(f"d['que']={d['que']}")
    print(f"d['tentei']={d['tentei']}")
    print(f"d.get('vida')={d.get('vida')}")
    print(f"d['vida']={d['vida']}\n")
    pause() # aprecie a paisagem

    # mais __setitem__()
    print("\nmais teste __setitem__()")
    d[1] = 'na'
    d[2] = 'vida'
    print(f"d:\n{d}") 
    pause() # aprecie a paisagem

    # teste __contains__()
    print("\nteste __contains__()")
    print(f"'tentei' in d={'tentei' in d}")
    print(f"'1' in d={'1' in d}")
    print(f"1 in d={1 in d}")
    print(f"5 in d={5 in d}\n")
    pause() # aprecie a paisagem
    
    # teste __iter__()
    print("\nteste __iter__()")
    for chave in d: print(f"{chave}: {d[chave]}")
    pause() # aprecie a paisagem

    # teste __len__()
    print("\nteste __len__()")
    print(f"len(d)={len(d)}")
    dicio_vazio = Dicio()
    print(f"len(dicio_vazio)={len(dicio_vazio)}\n")
    pause() # aprecie a paisagem

    # teste keys(), values() e items()
    print("\nteste keys(), values() e items()")
    print(f"d.keys()={d.keys()}")
    print(f"d.values()={d.values()}")
    print(f"d.items()={d.items()}\n")
    pause() # aprecie a paisagem

    print("FIM")

#-----------------------------------------------
def pause():
    input("Tecle ENTER para continuar: ")
    
#-----------------------------------------------
if __name__ == "__main__":
    main()
