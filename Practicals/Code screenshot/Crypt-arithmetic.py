import itertools
def solve():
    letters=set('SENDMORY')
    for perm in itertools.permutations('0123456789', len(letters)):
        m=dict(zip(letters,perm))
        if m['S']=='0' or m['M']=='0': continue
        SEND=int(''.join(m[c] for c in "SEND"))
        MORE=int(''.join(m[c] for c in "MORE"))
        MONEY=int(''.join(m[c] for c in "MONEY"))
        if SEND+MORE==MONEY: return m,SEND,MORE,MONEY
print(solve())
