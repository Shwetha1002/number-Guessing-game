import random
n = random.randint(1,9)
chances = 5

response = int(input("Guess a number!"))

    
while (chances > 0)
  if( response>n):
    response =   int(input("please guess lower!"))
    
   
   

  elif(response<n):
       response = int(input("Guess higher!"))
      

  else:
     print("wow! your right..!")
     break
 chances = chances -1
if(chances == 0):
 print("your chances are over sorry :/")



