# Gradi Tshielekeja Mbuyi
# COP 2500C
# Sep 28 2021

def buyPubSub(meat, cheese):
    price = 6 + meat*1 + cheese*.3
    # base = 6.00
    # extra meat = 1
    # extra cheese = .3

    return price

def buyCookies(num):
    # single cookies = $0.50
    # dozen cookies = $5.00
    # two dozen cookies = $9.00

    price = 0

    while(num>=24):
        price = price + 9
        num = num - 24
    while(num>=12):
        price = price + 5
        num = num - 12
    price = price + num * .5

    return price

def buyCookies2(num):
    # single cookies = $0.50
    # dozen cookies = $5.00
    # two dozen cookies = $9.00

    price = 0
    twoDozens = num // 24
    num = num % 24
    oneDozens = num // 12
    num = num % 12
    
    return twoDozens * 9 + oneDozens * 5 + num * .5


subOrder = buyPubSub(3,2)

print(subOrder)
print(buyCookies(13))
    
timegiven = 1000000
seconds = timegiven % 60
minutes = timegiven // 60
hours = minutes // 60
days = hours // 24

print(seconds)
print(minutes)
print(hours)
print(days)


def publix():
    option = 0
    price = 0
    while(option != 3):
        print("1. Buy Publix Subs")
        print("2. Oatmeal Cs")
        print("3. Checkout")

        option = int(input("pick a number between 1-3"))

        if(option == 1):
            meat = int(input("How much extra meat do you want?\n"))
            cheese = int(input("How much extra cheese do you want?\n"))
            temp_price = buyPubSub(meat, cheese)
            print("You bought a sub for", temp_price)
            price = price + temp_price
        elif(option == 2):
            

publix()
