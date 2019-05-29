print("Hi guys, Welcome to the rock paper scissor game!")

print("Enter the name of first player:")
p1=input()
print("Enter the name of second player:")
p2=input()
print("Hey.... battle begins between %s and %s" %(p1,p2))

while(1):
    print("It's the chance of %s, enter your choice among ROCK, PAPER, SCISSOR:" %p1)
    c1=input()
    c1=c1.lower()
    if c1 not in "rock paper scissor":
        print("%s Please Enter the valid choice" %p1)
        continue
    print("It's the chance of %s, enter your choice among ROCK, PAPER, SCISSOR:" %p2)
    c2=input()
    c2=c2.lower()
    if c2 not in "rock paper scissor":
        print("%s Please Enter the valid choice" %p2)
        continue
    if c1=="rock":
        if c2=="scissor":
            print("here is the victory for %s" %p1)
        elif c2=="rock":
            print("Here is the draw")
        else:
            print("here is the victory for %s" %p2)

    if c1=="paper":
        if c2=="rock":
            print("here is the victory for %s" %p1)
        elif c2=="paper":
            print("Here is the draw")
        else:
            print("here is the victory for %s" %p2)
    if c1=="scissor":
        if c2=="paper":
            print("here is the victory for %s" %p1)
        elif c2=="scissor":
            print("Here is the draw")
        else:
            print("here is the victory for %s" %p2)

    
    print("Do you want to play again ? press enter yes and if you want to resign from game kindly press any other key")
    nextgame=input()
    if nextgame.lower()=="yes":
        continue
    else:
        break

print("Thanks for playing this wonderful game! goodbye %s, %s" %(p1,p2))
            
    
