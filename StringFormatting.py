n = int(input())
w = len(format(n,'0b'))
for i in range(1,n+1):
    print(str(i).rjust(w," "),format(i,'0o').rjust(w," "),format(i,'0x').upper().rjust(w," "),format(i,'0b').rjust(w," "))

