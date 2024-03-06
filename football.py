from random import choice


def analize_football(bank:float, times:int)->float:
    res = 0.0
    coef = [1.50, 1.60, 1.70, 1.80, 1.90]
    while times > 0 and bank > 0:
        if choice((True,True, False)):
            bank = (bank / 2) + ((bank / 2) * choice(coef))
        else:
            bank -= (bank / 2)
        times -= 1
    return bank
        





def main():
    money = int(input("Enter now many money do you spent: "))
    times = int(input("How much times do it: "))
    res = analize_football(money, times)
    print(f"You earn money: {res:.2f}")




if __name__=="__main__":
    main()
