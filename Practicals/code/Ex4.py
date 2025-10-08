from itertools import permutations

def solve_cryptarithmetic():
    letters = 'SENDMORY'
    for perm in permutations(range(10), len(letters)):
        s, e, n, d, m, o, r, y = perm
        if s != 0 and m != 0:  # No leading zeros
            send = s*1000 + e*100 + n*10 + d
            more = m*1000 + o*100 + r*10 + e
            money = m*10000 + o*1000 + n*100 + e*10 + y
            if send + more == money:
                print(f"SOLUTION: {send} + {more} = {money}")
                return

solve_cryptarithmetic()
