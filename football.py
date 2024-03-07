from random import choice

def calc_stats(iter_times:int, money:int):
    coefficients = [1.50, 1.60, 1.70, 1.80, 1.90]
    bank = money

    for i in range(iter_times):
        chanse = choice((True, True,  False))
        if chanse:
            bank = (bank / 2) +  ((bank / 2) * chanse)
        else:
            bank -= bank / 2
        if bank < 1:
            print("You lose your money!!")
            break

    return bank





def main():
    money = int(input("Enter how many money do you spent: "))
    iteration = int(input("How many times: "))
    result = calc_stats(iteration, money)
    print(f"You earn money {result:.2f}") 




if __name__=="__main__":
    main()