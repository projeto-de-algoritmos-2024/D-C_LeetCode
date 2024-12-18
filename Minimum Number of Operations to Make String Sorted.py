class MergeCount:
    def merge(self, lista):
        #volta para quem chamou
        if len(lista)<=1:
            return lista, 0
        
        #faz o meio da função como inteiro
        meio = len(lista)//2

        esquerda = lista[:meio]
        direita = lista[meio:]

        esquerda_ordenada, inversoes_esquerda = self.merge(esquerda)
        direita_ordenada, inversoes_direita = self.merge(direita)

        # junta a direita com a esquerda
        lista_ordenada, num_inversoes = self.merge_and_conut(esquerda_ordenada, direita_ordenada)

        total_inversoes = inversoes_esquerda + num_inversoes + inversoes_direita
        return lista_ordenada, total_inversoes

    def merge_and_conut(self, esquerda, direita):
        i=0
        j=0
        ordenado = []
        num_inversoes = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] <= direita[j]:
                ordenado.append(esquerda[i])
                i=i+1
            elif direita[j] < esquerda[i]:
                ordenado.append(direita[j])
                j=j+1
                num_inversoes=num_inversoes+len(esquerda)-i
            
        ordenado.extend(esquerda[i:])
        ordenado.extend(direita[j:])
        
        return ordenado, num_inversoes


entrada = input()

lista_caracteres = list(entrada)
    
contador = MergeCount()
    
lista_ordenada, inversoes = contador.merge(lista_caracteres)

# Exibe os resultados
#print("\nString original:", entrada)
#print("String ordenada:", lista_ordenada)
print(inversoes)
    




