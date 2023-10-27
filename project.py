balance = 0
def check_balance():
    print('Total balance:',balance)

def deposit(amt):
    global balance
    balance = balance + amt
    print(amt,'Rs.deposited')
    
def withdraw(amt):
    global balance
    if w_amt > balance:
        print('insufficient balance to withdraw')
    else:
        balance = balance - amt
        print(amt,'Rs. withdrawn')

while True:
    choice = int(input('\nEnter choice:\n1.Deposit cash\t2.Withdraw cash\n3.Check balance\t4.Exit'))
    match choice:
        case 1:
            print('Deposit cash')
            d_amt =int(input('Enter amount to Deposit'))
            deposit(d_amt)
        case 2:
            print('Withdraw cash')
            w_amt =int(input('Enter amount to Withdraw'))
            withdraw(w_amt)
        case 3:
            print('Check balance')
            check_balance()
        case 4:
            print('Exiting..')
            break
        case _:
            print('invalid choice')
        
        
