class Solution:
    def countSmaller(self, nums):
        inversoes_comeco = {num: 0 for num in nums}
    
        lista_ordenada, inversoes = self.merge(nums, inversoes_comeco)

        valores = list(inversoes.values())

        return valores

    def merge(self, lista, contador):

        #volta para quem chamou
        if len(lista)<=1:
            
            return lista, contador
        
        #faz o meio da função como inteiro
        meio = len(lista)//2

        esquerda = lista[:meio]
        direita = lista[meio:]

        esquerda_ordenada, contador = self.merge(esquerda, contador)
        direita_ordenada, contador = self.merge(direita,contador)

        # junta a direita com a esquerda
        lista_ordenada, contador = self.merge_and_conut(esquerda_ordenada, direita_ordenada, contador)

        #total_inversoes = inversoes_esquerda + num_inversoes + inversoes_direita
        return lista_ordenada, contador

    def merge_and_conut(self, esquerda, direita, num_inversoes):
        i=0
        j=0
        ordenado = []
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] <= direita[j]:
                ordenado.append(esquerda[i])
                i+=1
            elif direita[j] < esquerda[i]:
                ordenado.append(direita[j])
                #como fazer para todos os da esquerda apartir do i
                for num in esquerda[i:]:
                    num_inversoes[num] += 1
                
                j+=1

        ordenado.extend(esquerda[i:])
        ordenado.extend(direita[j:])
        return ordenado, num_inversoes


entrada = [5,2,6,1]
    
contador = Solution()

resultado = contador.countSmaller(entrada)

print(resultado)

