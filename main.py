

buy_fruit = True
apples = 0
grapes = 0
oranges = 0

fruits_picked_prices = []

name = input("Welcome to the GC Fruit Market! \nWhat is your name?\n> ")

while buy_fruit:
    number_choice = input(f"\nWelcome {name}. Which Fruit would you like to buy? \n" 
                          "1. Apple $2 \n2. Grape $1 \n3. Orange $3 \n> ")
    if number_choice == '1' or number_choice == '2' or number_choice == '3':
        if number_choice == "1":
            apples += 1
            fruit_choice = "apple"
            cost_choice = 2
        elif number_choice == "2":
            grapes += 1
            fruit_choice = "grape"
            cost_choice = 1
        else:
            oranges += 1
            fruit_choice = "orange"
            cost_choice = 3

        fruits_picked_prices.append(int(cost_choice))
        keep_shopping = input(f"You bought 1 {fruit_choice} at ${cost_choice} \n" 
                              "Would you like to buy another piece of fruit? y/n \n> ")
        if keep_shopping == "y":
            buy_fruit = True
        else:
            buy_fruit = False
    else:
        print("Error, please pick a valid option.")

pre_tax = sum(fruits_picked_prices)
tax = pre_tax * .05
total = pre_tax + tax

print(f"\nOrder for {name} \n"
      f"{apples} apple(s) at $2 apiece \n" 
      f"{grapes} grape(s) at $1 apiece \n" 
      f"{oranges} orange(s) at $3 apiece \n"
      f"Sub Total: ${pre_tax} \n5% Tax: ${tax} \nTotal: ${total}")
