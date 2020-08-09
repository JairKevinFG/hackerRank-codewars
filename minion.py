def minion_game(string):
    list = ['A','E','I','O','U']
    score1 = 0
    score2 = 0
    for i in range(len(string)):
        if string[i] not in list:
            score1 = score1 + len(string) - i
        else:
            score2 = score2 + len(string) - i
    
    if(score2 > score1):
        print("Kevin", score2)
    elif (score1 == score2):
        print("Draw")
    else:
        print("Stuart", score1) 

def run():
    string = input()
    minion_game(string)

run()

