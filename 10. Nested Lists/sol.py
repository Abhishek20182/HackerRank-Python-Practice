if __name__ == '__main__':
    score_card = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_card.append([name,score])
        
    second_highest = sorted(list(set([marks for name, marks in score_card])))[1]
    for i,j in sorted(score_card):
        if j == second_highest:
            print("{}".format(i))
    
    