def conta_inversoes(nums1, nums2): # Funcao de contagem de inversoes com merge sort
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

    return conta_invs, array_final


def mediana(lista_ordenada):
    x = len(lista_ordenada)
    a = int(x/2)
    if x % 2 == 0:
        c = lista_ordenada[a-1]
        d = lista_ordenada[a]
        return (c+d)/2.0
    else:
        return lista_ordenada[a]


""" arrays = input()
arrays = arrays.replace('nums1 = [','').replace(']','').replace('nums2 = [','')
print(arrays)
aux = arrays.split(", ")
print(aux)
nums1 = aux[0].split(",")
print(nums1)
nums1 = list(map(int,nums1))
nums2 = aux[1].split(",")
print(nums2)
nums2 = list(map(int,nums2)) """
nums1 = input()
nums2 = input()
nums1 = nums1.replace('[','').replace(']','')
nums2 = nums2.replace('[','').replace(']','')
nums1 = nums1.split(',')
nums2 = nums2.split(',')
nums1 = list(map(int,nums1))
nums2 = list(map(int,nums2))
print(nums1)
print(nums2)
conta_invs, array_final = conta_inversoes(nums1, nums2)
print(mediana(array_final))
