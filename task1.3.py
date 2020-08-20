from sys import stdout

i = 0
arr = [10, 8, 7, 16, 9, 43]
ans = [0, 0, 0, 0, 0, 0]
queries = []
while i < 2:
    print(i, i+1)
    stdout.flush()
    q = int(input())
    queries.append(q)
    i += 1
i = 3
while i < 5:
    print(i, i+1)
    stdout.flush()
    q = int(input())
    queries.append(q)
    i += 1
for j in arr:
    if queries[0]*queries[1] % (j**2) == 0:
        ans[1] = j
    if queries[2]*queries[3] % (j**2) == 0:
        ans[4] = j
ans[0] = queries[0] // ans[1]
ans[2] = queries[1] // ans[1]
ans[3] = queries[2] // ans[4]
ans[5] = queries[3] // ans[4]
print(ans)
stdout.flush()
