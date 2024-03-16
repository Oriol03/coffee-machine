from data import *


# TODO print report 
def report (money):
    for coffe in resources :
        print(f"{coffe}: {resources[coffe]}  ")
    print(f"Money : $ {money} ")


# TODO :check ressources sufficient 
def resources_sufficient(drink):
    i=0
    for coffe in resources :
        if resources[coffe]< MENU [drink]["ingredients"][coffe]:
            print(f"Sorry there is not enough {coffe} ")
            i+=1
    if i==0 :
        for  coffe in resources :
            resources[coffe]-= MENU [drink]["ingredients"][coffe]
        return True
    else:
        return False      

# TODO : Process coins
def process_coins():
    total=0
    print("Please insert coins")
    for coin in coins :
        c=int(input(f"How many {coin} ?  "))
        total=total+ coins[coin]*c
    
    return total



# TODO : check transaction succefull
def transaction_succefull(drink,coins):
    global money
    if coins < MENU[drink]["cost"] :
        print("Sorry that's not enough money. Money refunded.")
        return False
    else :
        money+=MENU[drink]["cost"]
        change=round(coins-MENU[drink]["cost"],2)
        print(f"Here is $ {change} in change")
        return True




machin_on= True
money =0
while machin_on: 
    drink=input ("What do you want ? (espresso/latte/cappuccino)   ").lower()
    if drink=="report":
        report(money)

    elif drink =="off":
        machin_on=False
    
    elif drink=="entre":
        for prod in resources:
            resources[prod]+=int(input(f"How much of {prod} (in ml)  "))
        
    elif drink in MENU:
        if resources_sufficient(drink):
            argent=process_coins()
            
# TODO : Make coffee 
            if transaction_succefull(drink,argent):
                print(f"Here is your {drink} .Enjoy  ")
                
    else :
        print(f"\nWe don't have {drink} coffe here \n")
        
        
        
        
    
