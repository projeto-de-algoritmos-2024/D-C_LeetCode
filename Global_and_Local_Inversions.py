class Solution:
    def isIdealPermutation(self, nums):
        
        # Conta inversões locais diretamente no loop
        conta = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:  # Inversões locais (pares adjacentes)
                conta += 1
                if nums[i] - nums[i+1] > 1: 
                    return False

        # Calcula as inversões globais usando merge sort
        _, inversoes = self.merge(nums, 0, len(nums))

        # Verifica se globais e locais são iguais
        return inversoes == conta

    def merge(self, lista, inicio, fim):
        # Caso base: lista com 1 ou nenhum elemento
        if fim - inicio <= 1:
            return lista[inicio:fim], 0

        # Calcula o meio da lista
        meio = (inicio + fim) // 2

        # Divide a lista em duas partes e conta inversões em cada uma
        esquerda, contador_esquerda = self.merge(lista, inicio, meio)
        direita, contador_direita = self.merge(lista, meio, fim)

        # Junta as partes e conta inversões globais
        lista_ordenada, num_contador = self.merge_and_count(esquerda, direita)

        # Soma as inversões de ambas as metades e as globais
        total_inversoes = contador_esquerda + contador_direita + num_contador
        return lista_ordenada, total_inversoes

    def merge_and_count(self, esquerda, direita):
        i, j = 0, 0
        ordenado = []
        num_inversoes = 0

        # Junta as listas esquerda e direita, contando inversões
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] <= direita[j]:
                ordenado.append(esquerda[i])
                i += 1
            else:
                ordenado.append(direita[j])
                num_inversoes += len(esquerda) - i
                j += 1

        # Adiciona os elementos restantes
        ordenado.extend(esquerda[i:])
        ordenado.extend(direita[j:])
        return ordenado, num_inversoes