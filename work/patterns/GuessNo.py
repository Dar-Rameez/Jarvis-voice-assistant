import random
n = random.randint(1, 100)
a = -1
guesses = 0
while(a != n):
    a = int(input("Guess The Number: "))
    if a > n:
        print("print lower number")
    elif a < n:
        print("print higher number")
    guesses+=1
    
print(f"you have guessed the number in {guesses} attempts")
