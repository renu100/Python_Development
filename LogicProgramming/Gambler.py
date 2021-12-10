import random


def gambler(stake, goal, times):
    bet = 1
    win = loss = temp = 0
    for i in range(1, times + 1):
        if (random.random() >= 0.5):  # if generated random is gt 0.5 games wins then stake incremnts by 1  and bets again
            win = win + 1
            stake = stake + bet
            if (stake == goal):
                break
        else:  # if generated random is lt 0.5 games loose then stake decrements by 1
            loss = loss + 1
            stake = stake - bet
            if (stake == 0):
                break
        temp = i

    print("No.of Wins:", win)
    print("Win percentage:", win * 100 / temp)  # prints winning percentage
    print("No.of Loss:", loss)
    print("Loss percentage", loss * 100 / temp)  # prints loss percentage


if __name__ == '__main__':
    stake = int(input("Enter stake amount: "))
    goal = int(input("Enter Goal to be reached: "))
    times = int(input("Enter number of times to be played: "))
    gambler(stake, goal, times)  # calls gambler function
