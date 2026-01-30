import time

# greeting
print("hello there welcome to cafe network")
time.sleep(2)
print("\nIm Mack...and I will take your order")
time.sleep(1)


while True :
    try:
        print("Before that,will you like to be our member to have discounts ??!!")

        mem_per = input("~ ")

        if mem_per == "yes":
            print("ok lets do a quick from...")
            break
        if mem_per == "no":
            print("ok no problem but,I can say soon you will change your mind...")
            break
    except ValueError :
        print("")
# from
if mem_per ==  "yes" :
    time.sleep(2)
    print("\nMEMBERSHIP FROM")
    nam = input(str("\nName  : "))
    if nam == "BUG" or nam =="bug" or nam == "BUGX" or nam == "bugx" :
        print("your not the dev ")
        exit()

    age = input(str("Age   : "))
    num = input(str("Number: "))
    print("Thanks for your valuable time "+ nam)
    time.sleep(2)
    print("\nSaving From to Data Base...")
    time.sleep(6)
    print("Downloading completed...")
time.sleep(2)
# from means no
if mem_per == "no":
    time.sleep(3)
    print("let me get the menu...")
    time.sleep(2)

print("\nHere is our menu...")

#menu
time.sleep(1)
menu=("""          Coffee        - 15 $
          Tea           - 10 $
          Bread         - 05 $
          Donut         - 10 $
            
          {more will be add soon}""")
print(menu)

#order
menu_list=["coffee","tea","bread","donut"]
time.sleep(1)
print("\nso..what would you like to take ??")
order = input(str("~ "))


#amount
if order.lower() in menu_list :
    print("ok.." + order.lower() + " is a nice choose...")
    time.sleep(1)
    print("How many " + order.lower() + " will you need ?")
    amount = int(input("~"))
if order.lower() not in menu_list :
    print("Error   >_<")
    exit()

#need more
time.sleep(2)
print("By the way will you like something more ??")
more = input(str("~ "))

if more == "yes" :
    print(menu)
    order_2nd =input(str("And what else can I bring for you??\n~ "))
    if order_2nd.lower() in menu_list :
        amount_2nd = int(input("How many ?\n~ "))
    if order_2nd.lower() not in menu_list :
        print("Error >_<")
        exit()

if more == "no" :
    print("ok...")


# order review
time.sleep(2)

print("Now...reviewing the order...")
time.sleep(1)
print("Loading chat values...")
time.sleep(5)
if more == "yes":
    print("\nYou have ordered "+str(amount)+" "+order+" and")
    print("also "+str(amount_2nd)+" "+ order_2nd+" ....")
if more == "no":
    print("\nYou have ordered "+str(amount)+" "+order+" ...")

# cooking
time.sleep(1)
print("\nstarting process...")
time.sleep(1)

if more == "yes" :
    time_need = amount + amount_2nd
    if time_need < 10:
        print("order is being processed...")
        time.sleep(15)
    if time_need > 10:
        print("order is being processed...please wait..")
        time.sleep(30)

elif more == "no" :
    if amount < 10:
        print("order is being processed...")
        time.sleep(15)
    if amount > 10:
        print("order is being processed...please wait..")
        time.sleep(30)

print("\nhere is your order...")
print(" <served>")

# price (function)
coffee = 15
tea    = 10
donut  = 10
p_b    = 5

if more == "no" :
    if order == "coffee" :
        price = (coffee * amount)
    if order == "tea" :
        price = (tea * amount)
    if order == "donut" :
        price = (donut * amount)
    if order == "bread" :
        price = (p_b * amount)

if more == "yes" :
    if order == "coffee" :
        hey = (coffee * amount)
    if order == "tea" :
        hey = (tea * amount)
    if order == "donut" :
        hey = (donut * amount)
    if order == "bread" :
        hey = (p_b * amount)

    if order_2nd == "coffee" :
        hey2 = (coffee * amount_2nd)
        price = (hey + hey2)
    if order_2nd == "tea" :
        hey2 = (tea * amount_2nd)
        price = (hey + hey2)
    if order_2nd == "donut" :
        hey2 = (donut * amount_2nd)
        price = (hey + hey2)
    if order_2nd == "bread" :
        hey2 = (p_b * amount_2nd)
        price = (hey + hey2)

# bill
time.sleep(1)
print("\n\nyour bill is " + str(price) +" $")

if mem_per == "yes" :
    time.sleep(2)
    print("\nAs a member you have got some %discount%")
    bill = price - 5
    print("so your bill is now " + str(bill) +(" $"))

# payment method
time.sleep(1)
print("\nplease select payment method...")
time.sleep(1)
print("1 _ Cash\n2 _ Card\n3 _ Network pay")
time.sleep(1)
print("Noted : Network pay is only for members !! ")
pay_mth = int(input("enter the number : "))

# type 1

if mem_per == "yes" :
    bx = bill
if mem_per == "no" :
    bx = price

total_pay = 0
if pay_mth == 1 :
    while total_pay < bx :
        try:
            print("your bill is "+ str(bx))
            payment = int(input("pay : "))
            total_pay += payment

            if total_pay < bx:
                need = bx - total_pay
                print("still need " + str(need) + " money")

        except ValueError:
            print("please pay with numbers not abc")

    time.sleep(1)
    print("thanks")
    print("here is your change..." + str(total_pay - bx))



# (mem only )
if mem_per == "yes" :
    if pay_mth == 3 :
        time.sleep(1)
        print("ok.."+ nam +" your bill is "+ str(bill) +" $")
        time.sleep(2)
        print("Authenticating...")
        time.sleep(2)
        print("connected to your account..")
        time.sleep(1)
        print("payment saved ")
        print("now you can pay with any bank or next time before order...")
if mem_per == "no" :
    if pay_mth == 3 :
        print("Error >_<")
        print("Not a member...")
        print("resting all progress... ")
        time.sleep(3)
        exit()

# type 2
if pay_mth == 2 :
    time.sleep(1)
    print(" < inserted card >")
    time.sleep(2.5)
    while True :
        try:
            bnk_pwd = int(input("Password : "))
            if 1000 <= bnk_pwd <= 9999 :
                print(" <verifying> ")
                time.sleep(4)
                print("the bill is paid ...")
                break
            else:
                print("{password must be 4 numbers..}")

        except ValueError :
                print("password is made of NUMBERS !!")


# last

time.sleep(1)
print("THANKS FOR VISITING CAFE NETWORK")
time.sleep(1)
print("I Mack is always at ur service...")
time.sleep(1)
print("feel free to visit anytime again...")
time.sleep(2)
print("\nBye")

# completed
# 14/09/2024  to  18/09/2024  (11:56 pm)




