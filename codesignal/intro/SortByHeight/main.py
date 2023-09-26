from heapq import heappush, heappop

def solution(a):
    """
    a =           [-1, 150, 190, 170, -1, -1, 160, 180], 
    solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
    """    
    people = []
    solution = [-1] * len(a)
    
    for p in a:
        if p != -1:
            heappush(people, p)

    pos = 0
    while pos < len(a) and a[pos] == -1:
        pos += 1

    while people:
        p = heappop(people)
        solution[pos] = p
        pos += 1
        while pos < len(a) and a[pos] == -1:
            pos += 1
            
    return solution