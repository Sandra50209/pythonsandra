secret = 10

for i in range(5):
    guess = int(raw_input("What is your number:"))
    if guess == secret:
        print "Wow!! Great!"
        break
    else:
        if i == 4:
            print "Game over!"
            break
    if guess < secret:
        print "deine Zahl ist zu klein"
    else:
        print "deine Zahl ist zu gross"


