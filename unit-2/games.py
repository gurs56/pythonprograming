#ask user to guess your secret number

#loop as long as users input is not equal to secret number

#print a message if it is equal, then end loop

#if guess is 2 less or greater, print almost there

#if guess is greater or less than secret by 2, print to far
secret = 7
guess = int(input("guess my secret number: "))
while guess != secret:
    print("Not correct")
    guess = int(input("guess my secret number: "))
print("got it")
