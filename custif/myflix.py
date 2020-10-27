#!/usr/bin/env python3
#!/usr/bin/env python3

message = "Let's find out your grade!"

connection = float(input("What was your numerical score?"))

if connection >= 90:
    message = message + "A"

elif connection >= 80 and connection <= 89: # for all of these, when you use "and" you have to clearly state what both conditions are, which means writing out connection twice.
    message = message + "B"

elif connection >= 70 and connection <= 79: # ditto
    message = message + "C"

elif connection >= 60 and connection <= 69: # ditto
    message = message + "D"

else:
    message = message + "F"

print(message)



