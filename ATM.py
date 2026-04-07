import sys
def print_spaced(text):
  print(f"\n {text}  \n")
def input_spaced(text):
   return input(f"\n  {text}  \n")



def deposit(balance):
  deposit= input_spaced("Amount to deposit: ").strip().replace("$","")
  deposit=float(deposit)
  if deposit <=0: 
   print("Wrong input!")
  balance+=deposit

  return balance

def withdraw(balance):
  withdraw= input_spaced("Amount to withdraw: ").strip().replace("$","")
  withdraw=float(withdraw)
  if withdraw <=0:
    print("Wrong input!")
  if withdraw > balance:
    print("Too little money!")
  else:
    balance-=withdraw
    return balance



def loan(balance):
  loan = input_spaced("Amount you wish to borrow: ").replace("$","")
  loan = int(loan)
  print_spaced("1. 12-month\n2. 24-month\n3. 36-month\n4.Other")
  loanchoice = input_spaced("Choose a repayment schedule")
  loanchoice = int(loanchoice)
  if loanchoice == 1:
    print_spaced(f"You have to pay {loan*1.14/12:.2f}$ monthly")
  elif loanchoice == 2:
   print_spaced(f"You have to pay {loan*1.20/24:.2f}$ monthly")
  elif loanchoice == 3:
   print_spaced(f"You have to pay {loan*1.25/36:.2f}$ monthly")
  elif loanchoice == 4:
   loanchoice4 = input_spaced("How many months for your repayment schedule do you wish?: ")
   loanchoice4=float(loanchoice4)
   print_spaced(f"You have to pay {loan*1.20/loanchoice4:.2f} ")
  else:
   print_spaced(f"Incorrect input!") 
  loan = float(loan)
  balance+=loan
  return balance


  
def check(balance):
  print_spaced(f"Balance: {balance:.2f}$") 
  return balance

def finish(temp):
 temp
 print("nyoho! byebye!")
 sys.exit()

options= {
  "1": deposit,
  "2": withdraw,
  "3": loan,
  "4": check,
  "5": finish, 
}


password = "1234"
mount=0.0
while(True):
 

 for _ in range (3):
  passtry=input("Password: ")
  if not password==passtry:
   print("Incorrect password")


  else: 
    while(True):
     print_spaced("1.Deposit money\n2.Withdraw money\n3.take a loan\n4.Check balance\n5.Close the app") 
     choice=input_spaced("Choose one option: ").strip().replace(".","")
      mount = options[choice](mount)

     


 else:
   print("Incorrect password! account frozen!")
   break
