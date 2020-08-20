n = int(input())
bin_number = input()
if bin_number == '1'*n:
    print(-1)
else:
    pred = ''
    suc = ''
    i = n - 1
    j = n - 1
    while i >= 0:
        if bin_number[i] == '1':
            pred += bin_number[:i] + '0' + '1'*(n - 1 - i)
            break
        i -= 1
    while j > 0:
        if bin_number[j] == '0':
            suc += bin_number[:j] + '1' + '0'*(n - 1 - j)
            break
        j -= 1
    print(pred, suc)



