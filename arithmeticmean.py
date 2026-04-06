total=0
up=0
am=0

while(True):
   up = (input("Input grade: "))
   if up=="done":
    break

   up=int(up)
   if 0<up<=6:
     total+=up
     am+=1
   else:
     print("Incorrect input!")
     continue


print("Arithmetic mean: ", total/am)
