# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Astronaut")
define g1 = Character("Gloop")


# The game starts here.



label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene cockpit

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # Affection Begin
    $gloop_one_aff = 0
    # show eileen happy

    # These display lines of dialogue.



    #insert backstory stuff here
    $ player_name = renpy.input("What is your name, Captain?")

    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="Jojo"
    "The rockets bore down on the planet, stopping with a shutter as the engines turned off."
    "I, [player_name], am the proud captain of the research vessel PatentPending"
    "I make sure that everything is still in working order before I head out, just in case the life below me has less than friendly intentions."
    "As I make my way down the steel steps, I am greeted with a lush and vibrant planet, with purple trees and red grass."
    scene forest
    "The only animals I see are various gelatinous-like balls, almost like slimes from jrpgs."
    "As the Goop approaches my shuttle, I debate on how to initiate contact."
    jump main
    label main: 
    menu:
        "Reach out to touch it":
            jump it_bites_you
        "Leave":
            jump leave
        "Feed it":
            $gloop_one_aff += 10
            jump snacks
        "Prepare for a fight":
            $gloop_one_aff -= 10
            jump fight
    label fight:
        "I recall all my most important training, the long hours, the sweat and tears I've shed."
        "In order to level up and defeat the demon lord, I must gain xp! I, [player_name], have come face to face with my first foe!"
        "Before I attack, I must decide how. What's the best way to kill this gloop child?"
        menu:
            "Kick it":
                jump kick
            "Throw something":
                jump throw
            "Punch it":
                jump punch
            "test leave" if gloop_one_aff >=-10000 and gloop_one_aff <=-19:
                jump leave
            "test more neg karma":
                $gloop_one_aff -= 10
                jump fight
        label kick:
            "I ready my good leg, and prepare to kill this beast!"
            "..."
            "..."
            "My leg is stuck in the beast."
            call screen game_over_screen
        label throw:
            "I decide to throw something heavy at it."
            "Being from space, the nerds back home decided to bolt everything down in the ship so that it wouldn't fly off and hit me."
            "Like I said, nerds."
            "Leaving me to find some rock to chuck."
            "After finding the biggest rock I could, I take aim and fire."
            "The rock is absorbed into the goop, and then the slime slowly turns to me with an almost evil grin."
            "The rock is now tiny, the size of a bullet"
            "Is what you would have thought, if you had survived and not had a slime covered rock embedded in your brain."
            call screen game_over_screen
        label punch:
            "After many years of..."
            "....practicing......"
            "with my right arm, I ready a solid punch to the goop child."
            "..."
            "..."
            "I am stuck in the goop child."
            call screen game_over_screen

    label snacks:
        "I think it looks hungry. Maybe I should feed it something?"
        "I go back into the spaceship, rummaging around my pantry. I find some triangular, off brand blue chips I don't particularly mind parting ways with."
        "Heading back out to greenure pastures, I open the bag and dump the chips in front of the goop."
        "It seems to dislike them, and somehow messages me that it strongly prefers the red ones."
        menu:
            "Reach out to touch it":
                jump it_bites_you
            "Leave":
                jump leave



    label leave:
        "I suddenly decided I didn't get paid enough to make revolutionary scientific discoveries."
        scene cockpit
        "I got back in my ship and returned to Earth."
        "Upon returning, my boss was furious and, considering he was the president of Earth and had the power, banished me like a 13 year old fire prince."
        "I begrudgingly set out to find the planet, but to my dismay I forgot how to get there!"
        "..."
        "..."

        "...I'm still looking for it to this day."
        call screen game_over_screen

        return




    label it_bites_you:
        "It bites you!"

        menu:
            "Bite it back":
                jump bite_it_back
            "Observe the wound":
                jump observe_the_wound
            "Comfort it":
                jump comfort_it


    label bite_it_back:
        "Tastes like green apples and regret."
        "...At least, that's what you assume it tastes like. Your helmet prevents you from actually taking a bite."
        "Instead, you've splattered the goop all over your visor."
        jump note_creature_hostility

    label observe_the_wound:
        "The wound is tender, but no bleeding."
        "Seems it hasn't developed teeth yet thankfully."
        jump note_creature_hostility

    label comfort_it:
        "You reach out to touch it again, but hold your hand for it to observe."
        "After a few seconds it relaxes and you pet it back."
        "It's cold and gelatinous. Like Jello, but pulsating with life."
        "Seems to appreciate it in its own goopy way."

        "You note the creatures friendliness. It seems to be a social creature and reciprocates your love. Perhaps treating it kindly will yield favorable results?"
        call screen game_over_screen

    label note_creature_hostility:
        "You note the creatures hostility. It seems afraid of you to say the least; perhaps this creature doesn't have the capacitiy to comprehend affection; regardless, you feel you should be cautious with any further interaction."
        call screen game_over_screen

    label main_hub:

    # This ends the game.

    return
