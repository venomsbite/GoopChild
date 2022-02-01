# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    

    #insert backstory stuff here

    "Meet the GOOP"
    
    menu:
        "reach out to touch it...":
            jump it_bites_you
        "leave":
            jump leave

    label leave:
        "I suddenly decided I didn't get paid enough to make revolutionary scientific discoveries."
        "I got back in my ship and returned to Earth."
        "Upon returning, my boss was furious and told me to go back and research."
        "I begrudgingly set out to find the planet, but to my dismay I forgot how to get there!"
        "...I'm still looking for it to this day."

        return




    label it_bites_you:
        "It bites you!"

        menu:
            "bite it back":
                jump bite_it_back
            "observe the wound":
                jump observe_the_wound
            "comfort it":
                jump comfort_it

    label bite_it_back:
        "Tastes like green apple and regret."
        "...That's what you assume it tastes like. Your helmet prevents you from actually taking a bite."
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
        jump main_hub

    label note_creature_hostility:
        "You note the creatures hostility. It seems afraid of you to say the least; perhaps this creature doesn't have the capacitiy to comprehend affection; regardless, you feel you should be cautious with any further interaction."

    label main_hub:

    # This ends the game.

    return
