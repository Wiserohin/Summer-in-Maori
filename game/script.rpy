# The script of the game goes in this file.

init python:
    def eyewarp(x):
        return x**1.33
    eye_open = ImageDissolve("images/eye.png", 1, ramplen=128, time_warp=eyewarp)
    eye_shut = ImageDissolve("images/eye.png", 1, ramplen=128, reverse=True, time_warp=eyewarp)
    eye_open_slow = ImageDissolve("images/eye.png", 2, ramplen=128, time_warp=eyewarp)

screen cooking_minigame_screen:
    imagebutton:
        xpos 0.05
        ypos 0.8
        idle "images/aporo.png"
        hover "images/aporo.png"
        action NullAction()

        hovered Show("displaytextbox", displayText = "Add Aporo?", x = 0.04, y = 0.78)
        unhovered Hide("displaytextbox")

    imagebutton:
        xpos 0.15
        ypos 0.8
        idle "images/banana.png"
        hover "images/banana.png"
        action NullAction()

        hovered Show("displaytextbox", displayText = "Add Panana?", x = 0.15, y = 0.78)
        unhovered Hide("displaytextbox")

    imagebutton:
        xpos 0.25
        ypos 0.8
        idle "images/cat.png"
        hover "images/cat.png"
        action NullAction()

        hovered Show("displaytextbox", displayText = "Add Ngeru?", x = 0.26, y = 0.78)
        unhovered Hide("displaytextbox")

    imagebutton:
        xpos 0.35
        ypos 0.8
        idle im.Scale("images/eggplant.png", 145, 145)
        hover im.Scale("images/eggplant.png", 145, 145)
        action NullAction()

        hovered Show("displaytextbox", displayText = "Add Otahua?", x = 0.37, y = 0.78)
        unhovered Hide("displaytextbox")

    imagebutton:
        xpos 0.45
        ypos 0.8
        idle im.Scale("images/watermelon.png", 139, 140)
        hover im.Scale("images/watermelon.png", 139, 140)
        action NullAction()

        hovered Show("displaytextbox", displayText = "Add Merengi?", x = 0.5, y = 0.78)
        unhovered Hide("displaytextbox")

screen displaytextbox:
    default displayText = ""
    default x = 0
    default y = 0
    vbox:
        xalign x
        yalign y
        frame:
            text displayText

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mom")
define d = Character("Dad")
define p = Character("You")
define a = Character("Aroha")
define r = Character("Rangi")

# The game starts here.

image mchouse = im.Scale("images/bg room.png", 1920, 1080)
image femc = "images/aroha_black.png"
image femc_happy = "images/full_aroha_idk.png"
image femc_smile = "images/full_aroha_smile.png"
image femc_sad = "images/full_aroha_sad.png"
define audio.scene_1 = "audio/scene 1.mp3"
define audio.scene_3 = "audio/scene 3.mp3"
define audio.takeoff = "audio/take off noise.wav"
define audio.beep = "audio/plane beep.mp3"
define audio.stairs = "audio/stairs.mp3"
define audio.bonk = "audio/bonk.wav"
define audio.stahp = "audio/car_stop.mp3"
define audio.rain = "audio/rain_loop.wav"
image airplayne = im.Scale("images/planescene.png", 1920, 1080)
image NZAirport = im.Scale("images/AirportScene.jpg", 1920, 1080)
image femchouse = im.Scale("images/room_scene.jpg", 1920, 1080)
image kitchen = im.Scale("images/KitchenScene.jpg", 1920, 1080)
image memc = "images/stoic_boi_transparent.png"

image splash_anim_1:

    "gui/Group5_Logo.png"
    xalign 0.5 yalign 0.5 alpha 0.0
    ease_quad 7.0 alpha 1.0 zoom 2.0

label splashscreen:

    scene black

    ## The first time the game is launched, players can set their accessibility settings.
    if not persistent.caption:

        menu:

            "Do you want sound captions on? They describe music and sound effects in text.{fast}"

            "On":

                $ persistent.sound_captions = True

            "Off":

                pass

        menu:

            "Do you want image captions on? They describe game visuals in text.{fast}"

            "On":

                $ persistent.image_captions = True

            "Off":

                pass

        "These options can be changed at any time in the menu.{fast}"

        ## This message will not appear in subsequent launches of the game when
        ## the following variable becomes true.
        $ persistent.caption = True

    ## Here begins our splashscreen animation.
    show splash_anim_1
    show text "{size=60}Made with Ren'Py [renpy.version_only]{/s}":
        xalign 0.5 yalign 0.8 alpha 0.0
        pause 6.0
        linear 1.0 alpha 1.0

    ## The first time the game is launched, players cannot skip the animation.
    if not persistent.seen_splash:

        ## No input will be detected for the set time stated.
        ## Set this to be a little longer than how long the animation takes.
        $ renpy.pause(8.5, hard=True)

        $ persistent.seen_splash = True

    ## Players can skip the animation in subsequent launches of the game.
    else:

        if renpy.pause(8.5):

            jump skip_splash

    scene black
    with fade

    label skip_splash:

        pass

    return

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music scene_1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show femc

    # These display lines of dialogue.

    p "{i}I’m moving to New Zealand next week.{/i}"
    p "{i}I don’t want to go. I like my friends here a lot, and school’s not bad either.{/i}"
    p "{i}I don’t want everything to change.{/i}"
    centered "A few days earlier"
    scene mchouse
    with fade
    p "{i}I couldn’t sleep and was thirsty, so I went to grab some water. I overheard something disturbing.{/i}"
    d "...’s final now. We’re going to New Zealand."
    p "Huh? I have no time nor intent to go on a vacation."
    m "I thought you went to sleep. Anyway, more importantly, we’re moving to New Zealand! Think about it, the beach, tropical climate, and the food! Your mom grew up there, you know?"
    p "What do you mean “moving”?" with vpunch
    d "I got an offer from a friend’s company. The pay is much better, and there’s more job benefits. I didn’t want to tell you before it got finalized."
    m "We’re moving in 2 weeks. Dad’s friend found us a transport company that’s quick enough, we should have all our stuff in the new place soon after we arrive."
    p "What do you mean!? Why wasn’t I told about this? Just 2 weeks!? I don’t even want to go, and now I don’t have enough time to even enjoy with my friends anymore!" with hpunch
    scene black
    with dissolve
    play sound stairs
    p "{i}I ran back to my room and tried to go to sleep, hoping it was all a dream.{/i}"
    p "{i}However, I woke up the next morning, and gave in.{/i}"


    # This ends the game.
    # return
    stop music fadeout 1.0
    stop sound
    jump airplane
    with fade

label airplane:

    scene airplayne
    with fade
    play sound takeoff

    if (renpy.music.is_playing("sound")):
        while (renpy.music.is_playing("sound")):
            pause 1

        play sound beep
        "ANNOUNCEMENT" "Good morning, ladies and gentlemen, boys and girls. Welcome
        aboard XX airlines flight to New Zealand."
        "ANNOUNCEMENT" "Your pilot today is Captain Jeihan Sugimoto Neti and co-pilot Jerome Yoshimura Malefane..."

    "ANNOUNCEMENT" "Morena koutou, e aku rangatira, e tama, e aku kotiro. Haere
    mai i runga i te rererangi rererangi XX ki Aotearoa. Ko to paerata i tenei
    ra ko Kapene Jeihan Sugimoto Neti..."
    p "Maori, huh… Been a while since I heard that."
    p "{i}Mom made me learn it as a kid, but I got bored of it soon. I don’t remember much, maybe I would’ve kept learning if there was a fun language learning app for it.{/i}"
    m "Do you still remember? You used to enjoy it so much as a child, I wonder what happened…"
    p "Oh stop, I only learned it because you made me."
    m "That’s not how I remember it. Besides, knowing it now is going to be quite important, we’re moving into a Maori neighborhood."
    p "Damn it..."
    d "Don't worry about it, I'm sure everything will be fine."
    p "I sure hope so..."
    "You begin to fall asleep, as the plane cruises through the sky."
    scene black with fade
    centered "A few hours later"
    scene airplayne with fade
    play sound beep
    "ANNOUNCEMENT" "We will be landing at XX Airport in about 20 minutes. The local time is 9:30 in the morning. The latest weather information reports fair conditions in…"
    "ANNOUNCEMENT" "Ka tau atu maatau ki te taunga rererangi XX mo te 20 minute. Ko te waa o te takiwa ko te 9:30 i te ata. Ko nga korero hou o te rangi e pa ana ki nga ahuatanga tika i roto…"
    p "We're here, huh..."

    jump airport
    with fade


label airport:

    scene NZAirport
    with fade

    play music scene_3
    "ANNOUNCEMENT" "Tena koutou! Haere mai! Welcome to New Zealand! Some places to go are..."
    p "Tena koutou is the greeting...right?"
    m "Yep. And Haere mai means welcome."
    m "Knowing Maori here will be essential. You can come to me whenever you need help."
    "Note" "Go to mom whenever you need a refresher on topics that have already been covered."
    p "Got it, thanks."
    d "...I understand. I'll come over right away."
    m "What's up?"
    d "Work emergency. Say, can you come with me? I don't know the language, and I might need help."
    m "Sure. You can go home on your own, can't you? You should remember a bit of Maori, at least."
    p "Eh? I don't want to go there alone!"
    m "Stop whining. Almost everyone speaks English, so there's going to be no problem."
    m "Take this dictionary of basic maori words in case you're stuck somewhere."
    centered "{b}{i}Note: Obtained dictionary of basic words and phrases.{/i}{/b}"
    d "All the best, and see you!"
    m "In case you need it, {b}'E hiahia ana ahau ki te haere ki te kāinga'{/b} is what to tell the taxi driver."
    p "bruh"
    p "Alright then, let me ask someone..."
    p "{i}I think 'Excuse me, Do you know where I can get a taxi' went something like..."
    p "Arohaina mai, E mohio ana koe te wahi e taea te tiki e ahau i te tēkihi?"
    "Man" "Why are you talking to me in Maori?"
    p "Oh, uh, do you know where I can get a taxi?"
    "Man" "Yeah, sure, just go over there."
    p "Thanks."
    stop music fadeout 1.0
    scene black with dissolve
    play sound stahp
    p "I went and got a taxi to the new place. I got off and paid the driver. But then..."
    stop sound
    play sound bonk
    scene black
    with vpunch

label house:
    scene black
    play music rain
    p "..."
    scene femchouse
    with eye_open
    p "...?"
    scene black
    with eye_shut
    p "Where..."
    scene femchouse
    with eye_open
    scene black
    with eye_shut
    scene femchouse
    with eye_open_slow

    p "Where...am I?"
    "???" "Ah, you've finally woken up."
    show femc_happy
    "???" "Are you okay? Can you see?"
    p "Where is this? Who are you?"
    a "Kia ora! I'm Aroha! He pai te tātaki ki a koe!"
    p "What's going on?"
    show femc
    a "You collapsed outside our house. My brother Rangi picked you up. He's out right now."
    hide femc
    hide femc_happy
    show femc_smile
    a "You might not recognize us, but our mothers are friends. I've seen pictures of you."
    "???" "Kia ora! Kia ora! It seems you've woken up!"
    show memc
    with moveinleft
    hide femc_smile
    with moveoutright
    r "Hey, you. You're finally awake!"
    a "Hā! What are you doing!?"
    p "Everything's going too quick, please, give me a moment to calm down."
    scene black with fade
    centered "A few minutes later"
    scene femchouse with fade
    show memc
    r "Kei te pēhea koe? How's it going?"
    p "Kei te pai. I'm fine."
    a "I'm making dinner! Haere mai! Come here!"
    r "You should move around a bit. It'll do you good."
    p "Okay..."

    stop music fadeout 1.0
    jump minigame_1
    with fadeout


label minigame_1:

    scene kitchen with fade
    call screen cooking_minigame_screen
