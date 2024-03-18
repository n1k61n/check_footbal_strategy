"""This Python code simulates a gambling scenario with an uncertain outcome. 
It calculates potential winnings based on an initial investment and the number of "games" played.
"""

from random import choice

def calc_stats(bank:int, earn:int):

    coef = [1.50, 1.55, 1.60, 1.65, 1.70, 1.75, 1.80, 1.85,  1.90, 1.95, 2.0]
    times = 0
    while bank < earn and bank > 0:
        times += 1
        kef = choice(coef)
        if choice((True, True, False)):
            bank = round((bank // 2) + ((bank / 2) * kef))
            print(f"[{times}] Win -  {kef} - {bank}")
        else:
            bank -= (bank // 2)
            print(f"[{times}] Lose {kef} - {bank}")
        
    return (bank, times)


def main():
    money = int(input("Enter now many money do you spent: "))
    times = int(input("How much money you want earn: "))
    total = 0

    res, count  = calc_stats(money, times)
    total += res
    print(f"You earn money: {res}")
    spent = money * times
    print(f"Total spent: {spent}")
    print(f"Total win: {total}")
    win_chanse = (total // spent) * 100
    print(f"Win chanse: {win_chanse}%")
    print(f"Total run {count}")





if __name__=="__main__":
    main()
