
#problem2 remove duplication

def remove_dublicates(li):
    unique_list = list(dict.fromkeys(li))
    return unique_list

print("Array after remove duplication:", remove_dublicates([1, 2, 2, 3, 2]))
