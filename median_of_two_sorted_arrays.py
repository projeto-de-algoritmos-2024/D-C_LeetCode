class Suolution(object):    

    def findMedianSortedArrays(self, nums1, nums2): # Funcao de contagem de inversoes com merge sort
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

        resultado = self.mediana(array_final)

        return resultado


    def mediana(self, lista_ordenada):
        x = len(lista_ordenada)
        a = int(x/2)
        if x % 2 == 0:
            c = lista_ordenada[a-1]
            d = lista_ordenada[a]
            return (c+d)/2.0
        else:
            return lista_ordenada[a]


