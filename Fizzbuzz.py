#das mit dem Code fuer die Sonderzeichen funktioniert bei mir nicht, hab beides versucht (Code, u)
guess = int(raw_input("Select a number between 1 and 100:"))

if guess > 100:
    print "error"
elif guess < 1:
    print "error"
else:
    for i in range (1,100):
        if i % 3 != 0 and i % 5 !=0:
            print i
        elif i % 3:
            print "fizz"
        elif i % 5:
            print "buzz"
        elif i % 3 ==0 and i % 5 == 0:
            print "fizzbuzz"
        if i == guess:
            break

