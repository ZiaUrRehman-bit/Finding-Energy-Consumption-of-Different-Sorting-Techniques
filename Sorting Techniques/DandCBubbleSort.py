
list = [2,7,1,0,4,6,12,5,8,9]


def Partition(A, B):
    global ll, lh, rl, rh
    try:
        ll, lh = 0, len(A)
        rl, rh = 0, len(B)
    except:
        pass
    for k in B:
        A.append(k)
    bb = len(A)
    if (lh - ll + 1) <= b:
        for i in range(rl, rh):
            for j in range(ll,lh-1):
                if A[j] > A[j+1]:
                    temp = A[j]
                    A[j] = A[j+1]
                    A[j+1] = temp
            if A[lh] > A[i]:
                temp1 = A[lh]
                A[lh] = A[i]
                A[i] = temp1
    else:
        lm = int((ll + lh)/2)
        rm = int((rl + rh)/2)
        Partition(A[ll:lm], A[rl:rm])
        Partition(A[lm+1:lh], A[rm+1:rh])
        Partition(A[ll:lm], A[rm+1:rh])
        Partition(A[lm+1:lh], A[rl:rm])

def BubbleSort(A):
    # print(A[0], A[-1])

    l, h = 0, len(A)
    global b 
    b = len(A)
    # print(b)

    if (h-l+1) <= b:
        for i in range(l, h-1):
            for j in range(l, l+h-i-1):
                if A[j] > A[j+1]:
                    temp = A[j]
                    A[j] = A[j+1]
                    A[j+1] = temp
    else:
        m = int((l + h)/2)
        Partition(A[l:m], A[m+1:h])
        BubbleSort(A[l:m])
        BubbleSort(A[m+1:h])
    print(A)

print(list)
BubbleSort(list)
