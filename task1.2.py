n = int(input())
string = input()
count = 0
while n > 1:
    x = (n // 2)
    if string[:x] == string[x:2*x]:
        count += 1
        n //= 2
    else:
        break
print(count)
