secret = 10
guess = int(raw_input("secret: "))
wrong = "Nope! Again please!"
right =  "Wow!!! Great!"

if guess == secret:
    print right
else:
    print wrong