c = input("Do you like to order FOOD (YES!/NO!)?").lower()
total = 0
if c == "yes":
    print("______MENU______")
    print(" ")
    x = ["Pizza","Burger","Sandwitch"]
    p = [360,150,40]
    q = 1
    for i in range(len(x)):
        print(f"{q}. {x[i]}: ${p[i]}")
        q += 1
    print("________________________________________________")
while c == "yes":
    choice = input("Name of food item : ").capitalize()
    quantity = int(input("Please select quantity : "))
    if choice in x:
        food = x.index(choice)
        price = p[food]
        price_quantity = (price*quantity)
        print(f"Your order is {choice}: ${j}")
        c = input("Do you like to order FOOD (YES!/NO!)?").lower()
        total += price_quantity
        if c == "no":
            print(f"Your Total Bill is ${total}")        
else:
    print("Have A Nice Day!")

