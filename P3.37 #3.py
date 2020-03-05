#Write a program to simulate a bank transaction. There are two bank accounts: checking and savings. First, ask for the initial balances of the bank accounts; reject negative balances. Then ask for the transaction; options are deposit, withdrawal, and transfer. Then ask for the account; options are checking and savings. Then ask for the amount; reject transactions that overdraw an account. At the end, print the balances of both accounts.

#first ask for the inital balances of the banks accounts, reject negative balances
print("What is the inital balance of your Checking account")
InitialBalanceChecking = int(input())

if InitialBalanceChecking < 0:
  print ("Sorry , you can not input negative numbers")

print("What is the inital balance of your Savings account")
InitialBalanceSavings = int(input())

if InitialBalanceSavings < 0:
  print ("Sorry you can not input a negative number")

#ask for the transacation; deposit, withdrawl, transfer
print ("Would you like to deposit, transfer or withdrawl")
TransactionAsString = str(input())

if TransactionAsString == "deposit" :
#ask for the account ; checking or savings
  print ("What account would you want to go to, checkings or savings")
  AccountAsString = str(input())

  if AccountAsString == "checkings":
#then ask for the amount, reject transactions that overdraw an account.abs
    print ("deposit amount for checkings")
    DepositAmount = int(input())
    InitialBalanceChecking= DepositAmount + InitialBalanceChecking #add the deposit amount with the checkings

  elif AccountAsString == "savings":
    print ("Deposit amount for savings")
    DepositAmount = int(input())
    InitialBalanceSavings= DepositAmount + InitialBalanceSavings #same thing, add deposit amount with checkings

#withdrawl portion of the code 
elif TransactionAsString == "withdrawl":
    print("What account would you like to go to, checkings or savings")
    AccountAsString = str(input()) #account string is important!
 
    if AccountAsString == "checkings": #the == helps the program know that if the users input the exact "_" then to grab it and run it
      print ("With draw amount for checkings")
      WithDrawAmount = int(input())

      if WithDrawAmount > InitialBalanceChecking : #okay so this is just my little error message
        print("Sorry you can not input a value that overdraws the account")

      InitialBalanceChecking = InitialBalanceChecking - WithDrawAmount #subract the withdraw amount from checking

    elif AccountAsString == "savings":
      print("Withdrawl amount for savings")
      WithDrawAmount = int(input())

      if WithDrawAmount > InitialBalanceSavings :
        print ("Sorry you can not input a value that overdraws the account")
      InitialBalanceSavings = InitialBalanceSavings - WithDrawAmount #now we have to with it from the savings
         
elif TransactionAsString == "transfer": #transfer section of the code
    print("What account would you like to go, checkings or savings")
    AccountAsString = str(input())

    if AccountAsString == "checkings":
      print("Transfer amount for checkings")
      TransferAmount = int(input())

      if TransferAmount > InitialBalanceChecking:
        print("Sorry you can not input a value that over draws the account")

      InitialBalanceChecking = InitialBalanceChecking - TransferAmount
      InitialBalanceSavings = TransferAmount + InitialBalanceSavings #we got 2 math problems going on, so i need one that subtracts the transfer amount then another one that adds it back to the other account

    elif AccountAsString == "savings":        
      print("Transfer amount for savings")
      TransferAmount = int(input()) #ask for users input

      if TransferAmount > InitialBalanceSavings:
        print("Sorry you can not input value that over draws the account")

      InitialBalanceSavings = InitialBalanceSavings - TransferAmount
      InitialBalanceChecking = TransferAmount + InitialBalanceChecking 

#okay so now print the balances of both accounts
print ("Checking Balance: " ,InitialBalanceChecking)
print ("Savings Balance: ",InitialBalanceSavings)

#then ask for the amount, reject transactions that overdraw an account

#Error that i need to fix List #fixed 
#-deposit to savings - runs to the last line of code #fixed - tabbing needed to be moved and i misnamed a variable
#-transfer to savings- runs to last line of code#fixed- didnts name it correct, i put savings instead of checkings
#-just typing in withdrawl - sends an error #fixed - I missspelled withdrawl to withdrawal

