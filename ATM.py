def print_spaced(text):
  print(f"\n {text}  \n")
def input_spaced(text):
   return input(f"\n  {text}  \n")


password = "1234"
mount=0.0
while(True):
 passtry=input("Password: ")
 if  password==passtry:
    while(True):
     print_spaced("1.Deposit money\n2.Withdraw money\n3.take a loan\n4.Check balance\n5.Close the app") 
     choice=input_spaced("Choose one option: ").replace(".","")
     choice=int(choice)

     if choice == 1:
      deposit= input_spaced("Amount to deposit: ").replace("$","")
      deposit=float(deposit)
      mount+=deposit
    
     


     elif choice == 2:
       withdraw= input_spaced("Amount to withdraw: ").replace("$","")
       withdraw=float(withdraw)
       if withdraw > mount:
         print("Too little money!")
         continue 
       mount-=withdraw
       continue
     


     elif choice == 3:
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
       mount+=loan
       continue
         
     elif choice == 4:
       print_spaced(f"Balance: {mount:.2f}$") 

     elif choice == 5:
       break
    break 
 else:
  print_spaced("wrong password!") 

         


       

   

