word=""
name = input("Input your name , and last name: ").title() 
name=name.split(" ")

for i in name:
    for _ in i: 
        if _.isupper():
            word+=_+"."
    
print("Initials: ",word)
