# Copy a list element by element and display the copy.

def copy(lista:list):
    copia = []
    for i in lista:
        copia.append(i)
    return copia

lista_original = [1,2,3,4,5,6]

copia = copy(lista_original)
print(copia)