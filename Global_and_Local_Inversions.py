class Solution:
    def isIdealPermutation(self, nums):
    
        lista_ordenada, inversoes, local = self.merge(nums)

        print(inversoes, local)

        return inversoes == local

    def merge(self, lista):

        #volta para quem chamou
        if len(lista)<=1:
            
            return lista, 0, 0
        
        #faz o meio da função como inteiro
        meio = len(lista)//2

        esquerda = lista[:meio]
        direita = lista[meio:]

        esquerda_ordenada, contador_esquerda, local_esquerda = self.merge(esquerda)
        direita_ordenada, contador_direita, local_direita = self.merge(direita)

        # junta a direita com a esquerda
        lista_ordenada, num_contador, num_contador_local = self.merge_and_conut(esquerda_ordenada, direita_ordenada)

        total_inversoes_local = num_contador_local + local_direita + local_esquerda
        total_inversoes = contador_esquerda + num_contador + contador_direita
        return lista_ordenada, total_inversoes, total_inversoes_local

    def merge_and_conut(self, esquerda, direita):
        i=0
        j=0
        ordenado = []
        num_inversoes = 0
        inversoes_local = 0
        print("----------------")
        print(esquerda)
        print(direita)
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] <= direita[j]:
                ordenado.append(esquerda[i])
                print(esquerda[i], direita[j])
                i+=1

            elif direita[j] < esquerda[i]:
                print("direita")
                ordenado.append(direita[j])
                print(esquerda[i], direita[j])
                j+=1
                num_inversoes += len(esquerda[i:])
                if esquerda[0] and direita[0] and len(esquerda)==1:
                    inversoes_local +=1
                print("fim direita")
                
        print("fim while")  

        ordenado.extend(esquerda[i:])
        ordenado.extend(direita[j:])
        return ordenado, num_inversoes, inversoes_local


entrada = [1,0,2]
    
contador = Solution()

resultado = contador.isIdealPermutation(entrada)

print(resultado)

