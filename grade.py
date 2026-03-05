def main():
    grade = input("Input your grade (%): ").replace("%","")
    grade = int(grade)
    if grade >=90 :
     print("Grade : 5")
    elif grade >= 70:
     print("Grade: 4")
    elif grade >=50:
     print("Grade: 3")
    elif grade >=30:
     print("Grade: 2")
    else:
     print("Grade: 1")
     
main()