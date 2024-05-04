base64_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

for T in range(int(input())):
    l = input()
    s = ''
    result = ''
    for i in l:
        tmp = bin(base64_table.find(i))[2:]
        s += tmp.zfill(6)
    for j in range(0, len(s), 8):
        result += chr(int(s[j:j+8], 2))

    print(f'#{T+1} {result}')