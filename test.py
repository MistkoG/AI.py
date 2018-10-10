import random
Answer1 = ["I do not understood what you just said", "I  didn't get you", ]
Answer2 = [" Hi there ! Kindly introduce yourself ", " Hello there, I'm your personal assistant", "Hello, what's your good name"]

print("\n"*5)

while True :
      UserInput = input(">>> ")
      if UserInput.lower()== "hi" :
         print("Jarvis : ",random.choice(Answer2))
      else :
         print("Jarvis : ",random.choice(Answer1))
