import random

print "GUESS THE NUMBER GAME"


RangeTruth = True
while RangeTruth:
    NumbRang = (input("Please enter the upper boundary of your guessing range:"))
    if isinstance(NumbRang, int):
        list=[]

        for i in range(1,NumbRang+1):
            list.append(i)
        print list   
        cont = True
        Answer = random.choice(list)
        while cont:   
            Guess = (input("Please enter your guess, ensuring that the value is an integer:"))
            if isinstance( Guess, int ):
                if Guess > Answer:
                    print "Guess too high, try again."
                elif Guess < Answer:
                    print "Guess too low, try again."
                else:
                    cont = False 
                    print "Well Done"
            else:
                 print "Guess must be an integer"
    else:
        print "Error - Range Must be an Integer"
        