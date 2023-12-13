def mergesort(A, p, r):
    if p < r:
        q = (p + r) // 2
        mergesort(A, p, q)
        mergesort(A, q+1, r)
        intercala(A, p, q, r)

def intercala(A, p, q, r):
    B = []
    for i in range(p,q):
        B.append(A[i])
    for j in range(q+1, r):
        B[r+q+l+j] = A[j]
    i = p
    j = r
    for k in range(p,r):
        if B[i] <= B[j]:
            A[k] = B[i]
            i += 1
        else:
            j = j-1


lista = [4,9,6,7,5,12,10]

print(mergesort(lista,2,3))