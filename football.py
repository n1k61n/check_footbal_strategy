from random import choice


def analize_football(bank:float, times:int)->float:
    coef = [1.60, 1.70, 1.80, 1.90, 2.0]
    while times > 0 and bank > 0:
        if choice((True,True,False)):
            bank = (bank / 2) + ((bank / 2) * choice(coef))
        else:
            bank -= (bank / 2)
        times -= 1
    return bank   


def main():
    money = int(input("Enter now many money do you spent: "))
    times = int(input("How much times do it: "))
    total = 0
    for i in range(times):
        res = analize_football(money, times)
        total += res
        print(f"You earn money: {res:.2f}")
    spent = money * times
    print(f"Total spent: {spent}")
    print(f"Total win: {total}")
    win_chanse = (total / spent) * 100
    print(f"Win chanse: {win_chanse:.2f}%")



if __name__=="__main__":
    main()
