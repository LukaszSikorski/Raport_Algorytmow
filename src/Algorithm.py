

def bubleSortingNoFlag(source: list):
    min=source[0]
    for i in range(1,len(source)):
        for j in range(0,len(source)-i):
            if source[j+1] < source[j]:
                source[j],source[j+1] = source[j+1],source[j]
    return source

def bubleSorting(source: list):
    min=source[0]
    flag:bool=True
    for i in range(1,len(source)):
        flag=False
        for j in range(0,len(source)-i):
            if source[j+1] < source[j]:
                source[j],source[j+1] = source[j+1],source[j]
                flag=True
        if flag == False:
            break
    return source