define m = Character("Madoka Higuchi")
define e = Character("Egas KyUwUn")
define n = Character("")
define p = Character("Peidro", what_suffix="{fast}")

### Audios
define audio.discord_ping = "audio/discord.mp3"

### Images
# Bg
define fade_black = { "master" : Fade(1.0, 0.0, 0.0) }
image bg black = Solid("#000")

define fade_white = { "master" : Fade(1.0, 0.0, 0.0, color="#fff") }
image bg white = Solid("#fff")

# Madoka
image madoka maid curious = "MadokaHiguchiMaid(UwU might be needed).png"

# Movies
image phone scroll = Movie(play="phone_scroll.webm", side_mask=True, loop=False, image="phone scroll still.png", start_image="phone safe.png")
###

# Flags
default good_ending = False
define ending = ""

label start:
    show bg discord
    n "It's 4am. You have just finished your latest madoka drawing, and sent it to your friends through discord"
    play sound discord_ping
    p "...4 am?"
    play sound discord_ping
    p "Again?"
    play sound discord_ping
    p "...really?"
    play sound discord_ping
    p "And for what? To draw madoka drawings?"
    play sound discord_ping
    p "What the heck man"
    play sound discord_ping
    p "You'll have to wake up at 7 tomorrow..."
    play sound discord_ping
    p "I'm disappointed :pensive:"

    voice "<from 0 to 0.4>audio/keyboard_typing.wav"
    e "You're awake too"

    play sound discord_ping
    p "Yes, but I'm awake because I need to go to school..."

    voice "<from 0 to 0.2>audio/keyboard_typing.wav"
    e "..."
    voice "<from 0 to 1>audio/keyboard_typing.wav"
    e "I shouldn't have watched Okayu for 5 hours"
    voice "<from 1 to 2.5>audio/keyboard_typing.wav"
    e """{cps=30}
    Is this the real life?
    Is this just fantasy?
    """
    voice "<from 1 to 2.5>audio/keyboard_typing.wav"
    e """{cps=30}
    Is Madoka my wife?
    I'm losing my sanity...
    """

    with fade_black
    show bg black
    n "Your vision starts getting foggy..."
    
    
    jump wakeywakey

label wakeywakey:
    show bg cafe sky
    show madoka bunny stepped at center:
        zoom 0.35 # Sad 420
    with Fade(0.0, 0.0, 1.0)
    m "What are you doing, sleeping there?"
    m "...Disgusting"
    
    e "Madoka Higuchi???!!!?!??!?!"
    show bg cafe outside
    show madoka bunny flustered at center:
        zoom 1.2
    with dissolve
    m "You know me? Ew."
    m "At least pretend we have never met"

    e "Madoka. Higuchi!"
    e "Is this a birthday present?"

    show madoka maid curious at center:
        ycenter 0.6
        zoom 0.7
    m "What it's your birthday? I didn't even know."
    show madoka bunny flustered:
        ycenter 0.5
        zoom 1.2
    m "Like why would I know. Pftt."

    m "But since it is your birthday, we can go to the café I work on. On me."

    hide cafeoutside
    jump cafe

label cafe:
    show bg cafe inside # onlayer overlay 

    show madoka maid curious at center:
        ycenter 0.6
        zoom 0.7
    with dissolve

    m "So why were you lying in the middle of the street?"
    e "M-Madoka Higuchi..."

    show madoka maid mad:
        ycenter 0.7
        zoom 0.9

    m "Can you even say anything besides Madoka Higuchi"
    e "h-h- sorry..."
    e "I think I was on the floor because I was drawing too much."
    
    show madoka maid curious at center:
        ycenter 0.6
        zoom 0.7
    m "Wdym drawing?"
    m "Can I see it?"

    menu:
        "What say you?"
        "I'll show you":
            show phone safe at right:
                ycenter 1.5
                easein 0.7 ycenter 0.5
            e "Ok sure... I'll let you see one of them"
            
            show phone scroll
            m "Huh. Not bad. You actually are good at this-"
            show madoka maid disgust

            n "She scrolled too much"
            e "{i}shoot{/i} she scrolled too much"
            m "I clearly have scrolled too much. {w}Disgusting."
            with fade_white
            show bg white
            hide madoka
            hide phone

            n "Your mind goes blank..."

            $ ending = "Saitei"
            jump ending

        "ononono let's not":
            e "We... we better not."
    
    
menu:
    m "What say you?"
    "Bandana dee is the greatest":
        jump ba
    "Nothing":
        jump beh

label ba:
    show madoka maid floor at left:
        zoom 0.69
    m "nice"
    return

label beh:
    m "You son of a"
    return

define ender = Character("", advance=False)

label ending:
    n "{cps=20}[ending] Ending.{w}{cps=60}\nGo back a few options to try again."
    ender "[ending] Ending.\nGo back a few options to try again {size=-10} (scroll up){fast}"