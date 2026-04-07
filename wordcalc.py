#ask for user's input ,
punctuation = set(".,!\";()';~-?$%^&*+=_") 
wordcount=0
signcount=0
word=input("Input a sentence:\n")

specials = len(set(word))

for signs in word:
 if signs in punctuation:
  signcount+=1 

for sign in punctuation:
 word=word.replace(sign,"")

cutcount=word.split(" ") 

for i in cutcount:
 if i.isalpha():    
  wordcount+=1 


  
print("Number of words in your sentence: ",wordcount)
print("Number of signs in your sentence: ",signcount)
print("Number of special chars in your sentence: ",specials)