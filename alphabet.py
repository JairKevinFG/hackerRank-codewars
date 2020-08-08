size= int(input())
list = []
for i in range(97,123):
    list.append(chr(i))

newlist = list[size-1::-1] + list[1:size]
string = len('-'.join(newlist))
for i in range(1,size):
    print('-'.join(list[size-1:size-i:-1] + list[size-i:size]).center(string,'-'))
for i in range(size,0,-1):
    print('-'.join(list[size-1:size-i:-1] + list[size-i:size]).center(string,'-'))



