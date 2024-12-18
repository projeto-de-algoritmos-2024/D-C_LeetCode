from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Função auxiliar para contar inversões e mesclar os arrays
        def conta_inversoes(nums1, nums2):
            i = 0  # Ponteiro do nums1
            j = 0  # Ponteiro do nums2
            conta_invs = 0  # Contador de inversões
            array_final = []  # Array juntando nums1 e nums2 ordenados

            while i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    array_final.append(nums1[i])
                    i += 1
                else:
                    array_final.append(nums2[j])
                    conta_invs += (len(nums1) - i)  # Contar as inversões restantes no nums1
                    j += 1

            # Adicionar os elementos restantes 
            while i < len(nums1):
                array_final.append(nums1[i])
                i += 1
            while j < len(nums2):
                array_final.append(nums2[j])
                j += 1

            return array_final

        # Função auxiliar para calcular a mediana de um array ordenado
        def mediana(lista_ordenada):
            x = len(lista_ordenada)
            if x % 2 == 0:
                return (lista_ordenada[x//2 - 1] + lista_ordenada[x // 2]) / 2.0
            else:
                return lista_ordenada[x//2]

        # Chamando a função auxiliar para mesclar os arrays e encontrar a mediana
        array_final = conta_inversoes(nums1, nums2)
        print(array_final)
        return mediana(array_final)

# Leitura de inputs no formato exigido pelo online judge
if __name__ == "__main__":
    nums1 = input()
    nums2 = input()
    nums1 = nums1.replace('[','').replace(']','')
    nums2 = nums2.replace('[','').replace(']','')
    nums1 = nums1.split(',')
    nums2 = nums2.split(',')
    nums1 = list(map(float,nums1))
    nums2 = list(map(float,nums2))
    # Criando uma instância da classe Solution
    sol = Solution()
    # Chamando o método e imprimindo a mediana
    print(sol.findMedianSortedArrays(nums1, nums2))
