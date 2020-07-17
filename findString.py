# ABCDCDC
# CDC
#
#   2
def count_substring(string,sub_string):
    array = []
    array2 = []
    count=0
    for i in range(0,len(sub_string)):
        for k in range(0,len(string)-1):
            index = string.find(sub_string[i],k, len(string))
            if index != - 1:
                array.append(index)
    for i in array:
        if i not in array2:
            array2.append(i)
    array2.sort()
    for m in array2:
        newString = string[m:len(sub_string)+m]
        if newString == sub_string:
            count = count + 1
    return count
def run():
    string= input().strip()
    sub_string= input().strip()
    count = count_substring(string,sub_string)
    print(count)
run()
