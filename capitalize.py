def solve(s):
    newlist = []
    for i in s.split(' '):
        newlist.append(i.capitalize())
    newstring = ' '.join(newlist)
    return newstring

def run():
    s = input()
    resp = solve(s)
    print(resp)
run()




