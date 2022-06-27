print("-----------------CASHIER  PROGRAM-----------------")
buyer = input("input your name : ")
print("buyer's name :", buyer)


def food():
    global total_food
    global portion
    global foods
    print(
        """\n----------------- FOOD MENU -----------------")
        1. Fried Rice - IDR 15000
        2. Meatball - IDR 9000
        3. Smoke Beef - IDR 21000"""
    )
    number = int(input("input your choice number in menu : "))
    portion = int(input("How many servings : "))

    if number == 1:
        total_food = portion * 15000
        print(portion, " Portion of Fried Rice = IDR", total_food)
        foods = "Fried Rice"
    elif number == 2:
        total_food = portion * 9000
        print(portion, " Portion of Meatball = IDR", total_food)
        foods = "Meatball"
    elif number == 3:
        total_food = portion * 11000
        print(portion, " portion of Smoke Beef = IDR", total_food)
        foods = "Smoke Beef"
    else:
        print("there is no option, please enter again!!")
        food()


def baverage():
    global total_drinks
    global drink
    global glass
    print(
        """\n----------------- DRINK MENU -----------------")
        1. Matcha - IDR 10000
        2. V60 - IDR 7000
        3. Red velvet  - IDR 9000"""
    )
    numbers = int(input("nput your choice number in menu: "))
    glass = int(input("How many glasses : "))

    if numbers == 1:
        total_drinks = glass * 2000
        print(glass, " Matcha = IDR", total_drinks)
        drink = " Matcha "
    elif numbers == 2:
        total_drinks = glass * 3500
        print(glass, " V60 = IDR", total_drinks)
        drink = "V60"
    elif numbers == 3:
        total_drinks = glass * 4000
        print(glass, " Redvelvet  = IDR", total_drinks)
        drink = "Redvelvet"
    else:
        print("here is no option, please enter again!!")
        baverage()


food()
baverage()
all_total = total_food + total_drinks

print("\n Total to be paid: IDR", all_total)
payment = int(input("Buyer Cash : IDR "))
change = int(payment - all_total)
print("change :", change)

print("\n==================================")
print("========== BILL  PAYMENT =========")
print("==================================")
print("Name\t\t:", buyer)
print("Purchase\t\t:", portion, foods, "( IDR", total_food, ")")
print("\t\t ", glass, drink, "( IDR", total_drinks, ")")
print("Bill\t\t: IDR", all_total)
print("Payment\t\t: IDR", payment)
print("Change\t: IDR", change)
print("==================================")
print("==================================")

