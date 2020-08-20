n, r, x, y = map(int, input().split())
c = input().split()
s = input().split()
p = 0
d = 0
for i in range(n):
    if c[i] == '1':
        if s[i] == '1':
            p += 1
        else:
            d += 1
ans = r + p*x - d*y
if ans > r:
    print('promoted')
elif ans < r:
    print('demoted')
else:
    print('no change')
