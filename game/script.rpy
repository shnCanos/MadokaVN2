init python:
    def message_beep(event, interact=True, **kwargs):
        if interact and event == "show_done":
            renpy.sound.play("audio/snd_dialogue_1.wav")

    def message_beep_2(event, interact=True, **kwargs):
        if interact and event == "show_done":
            renpy.sound.play("audio/snd_dialogue_2.wav")

define m = Character("Madoka Higuchi", callback=message_beep)
define e = Character("Egas KyUwUn", who_color="#ff7700", callback=message_beep_2)
define n = Character("")
define p = Character("Peidro", what_suffix="{fast}")

### Audios
define audio.discord_ping = "audio/discord.mp3"

### Images
# Bg
define fade_black = { "master" : Fade(1.0, 0.0, 0.0) }
image bg black = Solid("#000")

define fade_white = { "master" : Fade(1.5, 0.0, 0.0, color="#fff") }
image bg white = Solid("#fff")

# Madoka
image madoka maid curious = "MadokaHiguchiMaid(UwU might be needed).png"

# Movies
image phone scroll = Movie(play="phone_scroll.webm", side_mask=True, loop=False, image="phone scroll still.png", start_image="phone safe.png")
###

# Flags
default good_ending = False

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

    play sound snd_splash
    with fade_black
    show bg black
    n "Your vision starts getting foggy..."
    
    
    jump wakeywakey

label wakeywakey:
    play music "audio/hanging_with_the_boys.mp3"
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
    with { "master" : Dissolve(1.5) }
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
    play music "audio/youkoso_toroimehe.mp3"
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

            call ending("Saitei")

        "ononono let's not":
            e "We... we better not."

            m "Mmm. Sure."
    
    m "Why are you in Japan tho? You don't look like you belong here."
    e "Wow, that sounded kinda racist tbh"
    
    show madoka maid mad:
        ycenter 0.7
        zoom 0.9
    m "What no I did not mean that"
    
    show madoka maid curious at center:
        ycenter 0.6
        zoom 0.7
    menu:
        m "But really though. Why are you here?"
        "To practice Japanese":
            e "I'm actually farming some Japanese XP"
            e "{s}I'm actually farming some Japanese XP{/s}{fast}\nI mean, I'm practicing my Japanese!"
    
            m "Chotto matte... You speak Japanese?"
            e "{font=DejaVuSans.ttf}hai hai hai (insert some actual Japanese here Idk)" # ええ、俺は日本語を話すよ！え、驚いた？
            p "{font=DejaVuSans.ttf}sumimasen sumimasen! ofutari wa nihonjin desuka?"
            m "{font=DejaVuSans.ttf}('ºΔº) * shakes head *{fast}"
            e "{font=DejaVuSans.ttf}more, 1 nen ka 2 nenkan nihongo o kanari benkyōshitekita n da." # 漏れ、1年か2年間日本語をかなり勉強してきたんだ。

            m "..."

            show madoka maid disgust
            m "{font=DejaVuSans.ttf}Did you just say \"more\"" # 漏れ
            e "oh.{w} OH. {w}{size=-10}I guess I did."

            m "{i}Disgusting."

            call ending("More Bad")
        "This a dream":
            e "tbh this is probably a dream, so I guess there is no logic to it really"
            m "... A dream? Why do you think this is a dream?"
            
            e "Because Madoka Higuchi becoming real is my dream!!!!"
            show madoka maid blush:
                ycenter 0.75
                zoom 0.9
            m "-!!!"
            m "Of course it is a dream!! And you should-{w}\nYou should wake up right now! {size=-10}... Baka."

            hide madoka
            with { "master": Dissolve(1.5) }
            e "Wait it really is a dream?!?! {p=0.5}{nw}"
            with { "master": vpunch }
            e "Wait it really is a dream?!?! {fast}{cps=20}noooo{size=+1}OOO{size=+4}OOO{size=+4}OOO{size=+4}OOO{size=+4}OOOO{size=+4}OOOO{size=+4}OOOO"

            call ending("Snap Back to Reality")
        "Idk":
            e "Honestly... I'm not really sure."
            show madoka maid mad:
                ycenter 0.7
                zoom 0.9
            m "What"
            m "Are you sure you weren't knocking yourself out with drinks"
            e "N-No I'd never do that!!"

            e "But now that you mention it, I do like Japan a lot.\nEspecially your culture!"

            show madoka maid curious at center:
                ycenter 0.6
                zoom 0.7
            menu:
                m "Hmmm? What about your culture that you like then?"
                "Idols and stuff":
                    e "something something I like idols"
                    e "AND I LIKE U2!!!"

                    m "Wait U2 is a Japanese idol group now?"

                    "this conversation is just nonsense"
                "Anime":
                    e "{i}Actually,{/i} I'm a big fan of anime"
                    
                    show madoka maid mad:
                        ycenter 0.7
                        zoom 0.9
                    m "... So you're a weeb?"
                    
                    e "Well..."

                    m "I mean, a foreigner in Japan, because they really like anime..."
                    show madoka maid disgust:
                        ycenter 0.6
                        zoom 0.7
                    m "That sounds kinda basic tbh."

                    e "Wha"
                    e "I just got called \"basic\" by Madoka Higuchi???"

                    m "Basically, yeah"
                    with { "master": vpunch }
                    e "{cps=30}noooo{size=+1}OOO{size=+4}OOO{size=+4}OOO{size=+4}OOO{size=+4}OOOO{size=+4}OOOO{size=+4}OOOO{size=+4}OOOO{size=+6}OOOO{size=+6}OOOO"

                    call ending("Basic")
                "Cookies":
                    e "Me like cookies!!!!"

                    m "Wtf does that have to do with Japan"
    
                    e "{size=+66}ME LIKE{w=0.5} COOKIES !!!!!!!!!!!!!!!!!!!!!!!!!!!"
    
    
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

label ending(ending=""):
    stop music fadeout 1.5
    play sound snd_vaporized
    with fade_white
    show bg white
    hide madoka
    hide phone

    n "{cps=20}Your mind goes blank..."

    play sound snd_break1
    n "{cps=20}[ending] Ending.{w}{cps=60}\nGo back a few options to try again..."
    ender "[ending] Ending.\nGo back a few options to try again... {size=-10}(scroll up){fast}"