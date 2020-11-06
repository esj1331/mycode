#!/usr/bin/env python3

def opening():
    while True:
        print("""
    You wake up alone in an all white room with no windows. On a table in front of you is a magical looking rainbow colored pill. Will you take the pill?""")

        answer_1 = input("yes or no?")

        if answer_1 == "yes":
            yes_to_pill()
            break

        elif answer_1 == "no":
            print("DONT BE A NERD! EAT THE MAGICAL RAINBOW PILL")

        else:
            print("Type YES or NO.")
            
def yes_to_pill():
    while True:
        print("""
    You swallow the pill, and your head begins to spin. Your vision gets blurry , and you feel your begin to morph and change.  You are getting smaller, and somehow greener?? Finally, its done.
    You are now outside in a wonderful forest. You have become a frog. You hear a scream in the distance. Will you hop towards danger?""")

        answer_2 = input("yes or no?")

        if answer_2 == "yes":
            hop_towards_danger()
            break

        elif answer_2 == "no":
            print("You spend the rest of your life as a cowardly frog and nothing exciting happens to you, ever. THE END.")
            break

        else:



            print("Type YES or NO.")

def hop_towards_danger():
    print("""You hop along as fast as you can, and come across an ugly troll about to eat a pretty princess.You must save her! Aferall, you may get a kiss and turn into a prince! How will you defeat the troll? 1. Lick him to death,2. hop on his head a million times , or 3. let him lick you? choose 1,2,or3""")

    while True:
        answer_3 = input("1,2, or 3")

        if answer_3 == "1":
                print("What is wrong with you? This would never work you moron. You are dead.")
        elif answer_3 == "2":
                print("I felt stupid writing this as a choice, you should feel dumber for actually choosing it. You are dead")

        elif answer_3 == "3":
            #frog_nap() 
            print("You let the troll pick you up and go for a tasty lick! Of course! You are a poison frog and one lick of your backside will kill the troll. The troll starts to wobble, and then tumble to the Earth. He is dead.  Apparently you can still talk to humans and ask the princess, May I have a kiss for saving your life? She looks at you joy in her eyes and states, Sorry I have a man and I am late for our date. As you watch her walk away a small tear rolls down your frog cheek. That was the worst magical pill youve ever taken, you think to yourself. You are tired, will you take a frog nap?")

            answer_4 = input("yes or no")
            print("Doesn't matter what you picked, you're taking a nap darn it!!!")
            frog_nap()
            break

        else:
                print("Type 1,2, or 3")


def frog_nap():
    print("You slip into a fever dream of madness. You can hear a faint voice in the distance.  WAKE UP, WAKE UP ASH.  YOU ARE LATE FOR PICKING OUT YOUR FIRST POKEMON FROM PROFESSOR OAK. What the hell is going ???????????????? Who is writing this story????? You stand up, you are not a frog anymore, but ASH FRIGGIN KETCHUM!!!!! You race over to Professor Oaks house ready to make your selection to begin your pokemon journey. Good morning Ash! He says.  I have 3 pokemon left to choose from.  They are 1. Charmander 2.Bulbasaur 3. Squirtle.  Which will you choose?  ")

    while True:
        answer_5 = input("1,2, or 3")

        if answer_5 == "1":
            print("IN THE POKEDEX VOICE. Charmander, the lizard pokemon. It has a preference for hot things. When it rains, steam is said to spout from the tip of its tail.")

        elif answer_5 == "2":
            print("IN THE POKEDEX VOICE. Bulbasaur, the seed pokemon. When the bulb on its back grows large, it appears to lose the ability to stand on its hind legs.")

        elif answer_5 == "3":
            print("IN THE POKEDEX VOICE. Squirtle, the tiny turtle pokemon. When it retracts its long neck into its shell, it squirts out water with vigorous force.")

        print("""
After you make your choice you go on your pokemon journey, training pokemon you catch, making new friends, and dealing with those evil people at Team Rocket. You travel around the land catching new pokemon, and training them up. You also win 8 gym badges and eventually defeat the elite 4 to become a Pokemon trainer legend.  You even beat down your old rival GARY after you beat the elite 4 cementing your status as a Pokemon trainer OG. You get endorsement deals, tons of money and matertial things, and girls.  You buy a mansion on the water in Cerulean City after starring in a movie about your life. Your life is literally the dream.....well its actually A DREAM as the effects of the magical rainbow pill start to subside.  You feel you have lived a whole lifetime starting with being a frog, and then living years as Ash Ketchum.  You go to sleep one night in your mansion by the sea in Cerulean city, and wake up the next day in your small house with your 3 annoying children, and a wife who doesnt love you anymore. Time heals all wounds, but even father time himself doesnt have the cure for this. You spend the rest of your days searching for one more magical rainbow pill. One more chance. Days turn into months, and months fade into years.  You lay down your head one final night and as the life passes from your body you can hear a song in the distance..................................
I want to be the very best,
Like no one ever was.
To catch them is my real test,
To train them is my cause!
(I will travel across the land,
Searching far and wide.
Each Pokemon to understand
The power that's inside!)
Pokemon!
Gotta catch em' all!
It's you and me,
I know it's my destiny!
Pokemon!
Oh, you're my best friend,
In a world we must defend!
Pokemon!
Gotta catch em' all!
(A heart so true,
Our courage will pull us through!)
You teach me and I'll teach you,
Po-ke-mon!
Gotta catch em' all!""") 
        break











if __name__ == "__main__":
    opening()
