#Restautrant bill generator

customer_name = input("Enter the Customer name : ")
if customer_name != "":
    food = input("Enter the food name: ")
    if food != "":
        quantity = int(input("enter quantity: "))
        if quantity > 0:
            price = float(input(f"enter price of {food}: "))
            if price > 0:
                subtotal = quantity * price
                if subtotal >= 100:
                    discount = (10 * subtotal)/ 100
                else:
                    discount = 0
                discounted_subtotal = subtotal - discount
                tax = (13 * discounted_subtotal) / 100
                total_bill = discounted_subtotal + tax
                print("----------bill----------")
                print(f"Customer = {customer_name}")
                print(f"item = {food}")
                print(f"quantity = {quantity}")
                print(f"subtotal before discount = {subtotal}")
                print(f"discount = {discount}")
                print(f"subtotal after discount = {discounted_subtotal}")
                print(f"tax = {tax}")
                print(f"total = {round(total_bill,2)}")
                print("--------------------")
            else:
                print("enter valid amount!")
        else:
            print("Invalid number, enter positive quantity only!")
    else:
        print("You didnot enter food name!")
else:
    print("You didnot enter customer name! ")

