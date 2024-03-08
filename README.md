#Functionality

This Python code simulates a gambling scenario with an uncertain outcome. It calculates potential winnings based on an initial investment and the number of "games" played.

**Explanation:**

1. **Imports:**
   - `from random import choice`: Imports the `choice` function from the `random` module, which is used to make random selections.

2. **`calc_stats` function:**
   - `bank:int, times:int`: This function takes two integer arguments: `bank` representing the initial amount of money, and `times` representing the number of "games" to play.
   - `coef = [1.60, 1.70, 1.80, 1.90, 2.0]`: Creates a list `coef` containing factors (between 1.6 and 2.0) that will be used to calculate potential winnings.
   - `while times > 0 and bank > 0` : The main loop continues as long as there are remaining "games" (indicated by `times`) and the "bank" (current amount) is positive.
     - `if choice((True,True,False))` : Uses `choice` to randomly select either `True` (with a 2/3 probability) or `False` (with a 1/3 probability).
       - If `True` is chosen:
         - `bank = (bank / 2) + ((bank / 2) * choice(coef))`: The current amount is split in half. One half remains in the "bank," and the other half is multiplied by a randomly chosen factor from `coef`. This represents a potential doubling or increase based on the chosen factor.
       - If `False` is chosen:
         - `bank -= (bank / 2)`: The current amount is simply halved, representing a loss.
     - `times -= 1`: Decrements the number of remaining "games."
   - `return bank`: Returns the final amount of money remaining after all "games" are played.

3. **`main` function:**
   - `money = int(input("Enter now many money do you spent: "))`: Prompts the user to enter the initial amount of money they want to spend.
   - `times = int(input("How much times do it: "))`: Prompts the user to enter the desired number of "games" to simulate.
   - `total = 0.0`: Initializes a variable `total` to keep track of the total amount earned across all "games."
   - `for i in range(times)`: Iterates `times` number of times to simulate each "game."
     - `res = calc_stats(money, times)`: Calls the `calc_stats` function to calculate the outcome of a single "game," passing the initial amount (`money`) and total number of "games" (`times`) for consistency.
     - `total += res`: Adds the result (amount earned) from the current "game" to the `total`.
     - `print(f"You earn money: {res:.2f}")`: Prints the amount earned in the current "game" with two decimal places.
   - `spent = money * times`: Calculates the total amount of money spent by multiplying the initial amount by the number of "games."
   - `print(f"Total spent: {spent}")`: Prints the total spent.
   - `print(f"Total win: {total}")`: Prints the total amount earned across all "games."
   - `win_chanse = (total / spent) * 100`: Calculates the win chance as a percentage by dividing the total earned by the total spent and multiplying by 100.
   - `print(f"Win chanse: {win_chanse:.2f}%")`: Prints the win chance with two decimal places followed by a percentage sign.


**Overall:**

This code simulates a risky scenario where the outcome of each "game" is uncertain. The win chance is not guaranteed and depends on random factors. It's important to understand that gambling is not a reliable way to make money, and this code is for educational purposes only.
