
grades=[]
def add_grade(list):
 grade = int(input("Enter grade: "))
 list.append(grade)
 print("Grade successfuly added!") 
 
def calculate_average(list):
 print(f"Average Grade: {sum(list)/len(list)}")


def show_grades(list):
 print("Grades: ",end="")
 for i in list:
  print(" ",i,end="")
  

def best_grades(list):
 print("Highest grade: ",max(list))

def worst_grades(list):
  print("Worst grade: ",min(list))


options = {
 "1": add_grade, 
 "2": calculate_average,
 "3": show_grades,
 "4": best_grades,
 "5": worst_grades,
 }
 

 
while True:
 print("\n1.Add grade\n2.Calc Avr\n3.Show grades\n4.Best grade\n5.Worst grade\n6.Exit")
 choice = input("Input your choice: ").strip()
 if choice in options:
  options[choice](grades) 
 elif choice == "6" :
  break
 else:
  print("Wrong option!") 
