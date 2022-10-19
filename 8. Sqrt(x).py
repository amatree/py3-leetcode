import timeit

def sqrt(x: int) -> int:
    if x < 3 and x > 0:
        return 1
    
    r = 2
    while True:
        while r**2 > x:
            r = r - int(r/2)
            print(r)
        if r**2 < (r+1)**2:
            r = r + int(x/2)
        elif r**2 > x - 1 and r**2 < (r+1)**2:
            break
        
    return r

print(sqrt(6))