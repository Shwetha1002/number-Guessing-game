import random
n = random.randint(1,9)
chances = 5

response = int(input("Guess a number!"))

    

if( response>n) and (chances > 0):
    response =   int(input("please guess lower!"))
    chances = chances -1
   
    print(response)

if(response<n) and (chances > 0):
       response = int(input("Guess higher!"))
       chances = chances -1

if(response==n) and (chances>0):
     print("wow! your right..!")
     chances = 0




