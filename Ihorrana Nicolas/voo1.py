def min(t):
    h, m = map(int, t.split(':'))
    return h * 60 + m

def normal(x, m=1440):
    return ((x % m) + m) % m

def main():
    data = input().strip().split()
    if len(data) != 4:
        return

    pA_s, cB_s, pB_s, cA_s = data
    pA = min(pA_s)
    cB = min(cB_s)
    pB = min(pB_s)
    cA = min(cA_s)

    for fuso in range(-11, 13): 
        base = cB - pA - fuso * 60
        D = normal(base, 1440)
        
        if D >= 720:
            continue
        
        if normal(pB + D - fuso * 60 - cA, 1440) == 0:
            print(f"{D} {fuso}")
            return

if __name__ == "__main__":
    main()
