class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        # Array para armazenar os resultados
        counts = [0] * n
        # Array de índices para acompanhar a posição original dos elementos
        indices = list(range(n))
        
        # Função de merge sort modificada
        def merge_sort(start, end):
            if end - start <= 1:  # Caso base: um único elemento
                return
            mid = (start + end) // 2
            merge_sort(start, mid)
            merge_sort(mid, end)
            merge(start, mid, end)

        def merge(start, mid, end):
            temp = []
            left, right = start, mid
            smaller_count = 0
            
            while left < mid and right < end:
                if nums[indices[right]] < nums[indices[left]]:
                    # O elemento da direita é menor
                    temp.append(indices[right])
                    smaller_count += 1
                    right += 1
                else:
                    # O elemento da esquerda é menor ou igual
                    temp.append(indices[left])
                    counts[indices[left]] += smaller_count
                    left += 1
            
            # Adiciona os elementos restantes
            while left < mid:
                temp.append(indices[left])
                counts[indices[left]] += smaller_count
                left += 1
            while right < end:
                temp.append(indices[right])
                right += 1
            
            # Atualiza o array de índices
            for i in range(len(temp)):
                indices[start + i] = temp[i]
        
        # Chama o merge sort
        merge_sort(0, n)
        return counts

# Testando os exemplos
sol = Solution()
