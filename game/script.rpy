init python:
    def message_beep(event, interact=True, **kwargs):
        if interact and event == "show_done":
            renpy.sound.play("audio/snd_dialogue_1.wav")

    def message_beep_2(event, interact=True, **kwargs):
        if interact and event == "show_done":
            renpy.sound.play("audio/snd_dialogue_2.wav")
    
    def make_discord_character(name, icon, instant = False):
        char = Character(name, kind=nvl, who_color="#fff", who_prefix=f"{{size=40}}{{image=pfp {icon}.webp}} {{font=DejaVuSans.ttf}}", what_prefix="{color=#ddd}{font=DejaVuSans.ttf}")
        if instant:
            char.what_suffix = "{fast}"
        return char

### Characters
# Discord
define discord_n = Character("", window_background="gui/nvl.png")
define discord_e = make_discord_character("Egas KyUwUn", "doggu", False)
define discord_p = make_discord_character("Peidro", "soulspark", True)
define discord_v = make_discord_character("{size=16}BandanaDeeIsTheGreatestOfAllTime", "shnawblle", True)

define m = Character("Madoka Higuchi", callback=message_beep)
define e = Character("Egas KyUwUn", who_color="#ff7700", callback=message_beep_2)
define p = Character("Peidro", what_suffix="{fast}")
define narrator = Character("")

define ending_narrator = Character("", kind=nvl, what_prefix="{color=#fff}")

### Audios
define audio.discord_ping = "audio/discord.mp3"

### Images
# Bg
define fade_black = { "master" : Fade(1.0, 0.0, 0.0) }
image bg black = Solid("#000")
image solid_black = Solid("#000")

define fade_white = { "master" : Fade(1.5, 0.0, 0.0, color="#fff") }
image bg white = Solid("#fff")
image solid_white = Solid("#fff")

# Madoka
image madoka maid curious = "MadokaHiguchiMaid(UwU might be needed).png"

# Movies
image phone scroll = Movie(play="phone_scroll.webm", side_mask=True, loop=False, image="phone scroll still.png", start_image="phone safe.png")
###

# Flags
default good_ending = False

label start:
    show bg discord
    show top discord zorder 10 onlayer screens
    with Fade(1.5, 0.5, 1.5)
    $ renpy.pause(1.0, True)
    
    show text "It's 5am. You have just finished your latest madoka drawing, and sent it to your friends through discord." at truecenter
    with Dissolve(1.0)
    
    with Pause(1000000)
    
    hide text
    with Dissolve(1.0)

    show madoka sketch:
        xcenter 0.3
        ycenter 0.5
        zoom 1.0
    
    # $ gui.nvl_height = 300
    # $ style.rebuild()

    nvl_narrator "\n{fast}{nw}"
    nvl_narrator "\n{fast}{nw}"
    nvl_narrator "\n{fast}{nw}"
    nvl_narrator "\n{fast}{nw}"
    nvl_narrator "\n{fast}{nw}"
    nvl_narrator "\n{fast}{nw}"
    nvl_narrator "\n{fast}{nw}"
    nvl_narrator "\n{fast}{nw}"
    nvl_narrator "\n{fast}{nw}"
    nvl_narrator "\n{fast}{nw}"
    voice "<from 0 to 0.4>audio/keyboard_typing.wav"
    discord_e "sketch going"
    with Pause(1000000)

    show madoka sketch zorder 0:
        ycenter 0.4
    play sound discord_ping
    discord_p "...5 am?"

    show madoka sketch:
        ycenter 0.3
    play sound discord_ping
    discord_p "again?"
    
    show madoka sketch:
        ycenter 0.2
    play sound discord_ping
    discord_p "...really?"

    show madoka sketch:
        ycenter 0.1
    play sound discord_ping
    discord_p "and for what? to draw madoka drawings?"
    
    show madoka sketch:
        ycenter 0.0
    play sound discord_ping
    discord_p "what the heck man"
    
    show madoka sketch:
        ycenter -0.1
    play sound discord_ping
    discord_p "you'll have to wake up at 7 tomorrow..."

    show madoka sketch:
        ycenter -0.2
    play sound discord_ping
    discord_p "I'm disappointed :pensive:"


    show madoka sketch:
        ycenter -0.3
    voice "<from 0 to 0.4>audio/keyboard_typing.wav"
    discord_e "you're awake too"

    play sound discord_ping
    discord_p "yes, but I'm awake because I need to go to school..."

    voice "<from 0 to 0.2>audio/keyboard_typing.wav"
    discord_e "..."

    voice "<from 0 to 1>audio/keyboard_typing.wav"
    discord_e "i shouldn't have watched Okayu for 5 hours"

    play sound discord_ping
    discord_v "welp"
    
    play sound discord_ping
    discord_v "wanna play owowatch then"

    play sound discord_ping
    discord_p "no way you woke up just for this"
 
    play sound discord_ping
    discord_v "don't doubt me"
    
    voice "<from 0 to 1>audio/keyboard_typing.wav"
    discord_e "bruh... what even is overwatch"
    
    voice "<from 0 to 1>audio/keyboard_typing.wav"
    discord_e "idk anymore"

    show solid_black onlayer screens zorder 3:
        alpha 0.0
        ease 1.0 alpha 0.3

    voice "<from 1 to 2.5>audio/keyboard_typing.wav"
    discord_e """{cps=30}Is this the real life?
    Is this just fantasy?
    """

    show solid_black onlayer screens zorder 3:
        ease 1.0 alpha 0.7
    voice "<from 1 to 2.5>audio/keyboard_typing.wav"
    discord_e """{cps=30}Is Madoka my wife?
    I'm losing my sanity...
    """
    hide top discord onlayer screens
    hide madoka
    with None

    play sound snd_splash
    with fade_black
    show bg black

    show solid_black onlayer screens zorder 3:
        linear 1.0 alpha 0.0
    
    discord_n "{cps=20}Your vision {cps=10}gets {cps=5}foggy..."
    nvl clear
    
    jump wakeywakey

label wakeywakey:
    play music "audio/hanging_with_the_boys.mp3"
    show bg cafe sky
    show madoka bunny stepped at center:
        zoom 0.35 # Sad 420
    with Fade(0.0, 0.0, 2.0)
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

    m "But since it is your birthday, we can go to the café I work on. Come, it's on me."

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
        "What say you?\nShow Madoka your drawings?"
        "I'll show you":
            show phone safe at right:
                ycenter 1.5
                easein 0.7 ycenter 0.5
            e "Ok sure... I'll let you see one of them"
            
            show phone scroll
            m "Huh. Not bad. {w=0.5}You actually are good at this-{nw}"
            show madoka maid disgust
            stop music
            extend ""
            

            "She scrolled too much"
            e "oh no. she scrolled too much"
            m "I clearly have scrolled too much. {w}Disgusting."

            call ending("Saitei")

        "ononono let's not":
            e "We... we better not."

            m "Mmm. Sure."
    
    m "Why are you in Japan tho? You clearly don't belong here."
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
    
            m "Wait a chotto... You speak Japanese?"
            e "{font=DejaVuSans.ttf}hai hai hai (insert some actual Japanese here Idk)" # ええ、俺は日本語を話すよ！え、驚いた？
            p "{font=DejaVuSans.ttf}sumimasen sumimasen! ofutari wa nihonjin desuka?"
            m "{font=DejaVuSans.ttf}('ºΔº) * shakes head *{fast}"
            e "{font=DejaVuSans.ttf}more, 1 nen ka 2 nenkan nihongo o kanari benkyōshitekita n da." # 漏れ、1年か2年間日本語をかなり勉強してきたんだ。

            m "..."

            show madoka maid disgust
            stop music
            m "{font=DejaVuSans.ttf}Did you just say \"more\"" # 漏れ
            e "oh.{w} OH. {w}{size=-10}Guess I'll die."

            show madoka maid disgust:
                easein_back 0.2 zoom 0.8
            m "{i}Disgusting."

            call ending("More Bad")
        "This a dream":
            e "tbh this is probably a dream, so I guess there is no logic to it really"
            m "... A dream? Why do you think this is a dream?"
            
            e "Because Madoka Higuchi becoming real is my dream!!!!"
            show madoka maid blush:
                ycenter 0.75
                zoom 1
            m "-!!!"
            m "Of course it is a dream!! And you should-{w}\nYou should wake up right now! {size=-10}... Baka."

            hide madoka
            with { "master": Dissolve(1.5) }
            stop music fadeout 1.5
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
            e "I really like idols."
            e "Ahem- one idol, actually."

            m "Mmm? That's interesting."
            m "You do know that... I am a part of an idol group?"
            e "O-Of course I do!!"
            e "My favorite thing about Japan{w=0.5} {b}IS Madoka Higuchi!!!{/b}"

            show madoka maid blush:
                ycenter 0.75
                zoom 1
            m "-!!!"

            m "That's really weird!!{w=0.5}{nw}"
            extend " But also... kinda cute."
            e "????"

            # I'm not sure about this ending yet either
            call ending("Weird")
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
            stop music
            m "That sounds kinda basic tbh."

            e "Wha"
            e "I just got called \"basic\" by Madoka Higuchi???"

            m "Basically, yeah"
            with { "master": vpunch }
            # Oh so this is how you did it you little twerp
            e "{cps=30}noooo{size=+1}OOO{size=+4}OOO{size=+4}OOO{size=+4}OOO{size=+4}OOOO{size=+4}OOOO{size=+4}OOOO{size=+4}OOOO{size=+6}OOOO{size=+6}OOOO"

            call ending("Basic")
        "Cookies":
            e "Me like cookies!!!!"

            m "Wtf does that have to do with Japan"

            e "{size=+66}ME LIKE{w=0.5} COOKIES !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

            m "Are cookies not a thing in your culture?"
            
            e "Well they are but..."

            show madoka maid disgust:
                ycenter 0.6
                zoom 0.7
            stop music
            
            m "Then why didn't you just eat the ones in your country?"
            m "Did you travel to Japan just for cookies?"

            e "...{w}...{w}I JUST LIKE COOKIES GOD DAMN IT!!!"
            "Before you knew it, you'd ran away from her..."
            "And now she hates you"

            call ending("Cookies > Madoka")
        "J-Pop":
            e "I actually like J-Pop songs a lot."
            m "mmm, J-Pop?"
            
            e "Yea, like E ve,{w=0.5} and Kenshi Yonezu,{w=0.5} and Zutomayo, and-{w=0.5}{nw}"

            show madoka maid mad:
                ycenter 0.7
                zoom 0.9
            m "Mister,{w=0.5} I {i}know{/i} what J-Pop is."

            show madoka maid blush:
                ycenter 0.75
                zoom 1
            m "But ngl, you have {w=0.5}very {b}based{/b} taste for that"

            e "-!! Right!?! J-Pop is the best!!!"
            show madoka maid happy:
                ycenter 0.7
                zoom 0.7

            m "...{w=0.5}Which one is your favorite artist though?"

            e "T-That's a tough question...{w=0.5} maybe..."
            
            show madoka maid happy:
                easein_back 0.3 zoom 0.75
            m "Eve is a great choice."

            
            show madoka maid happy:
                easeout 0.3 zoom 0.7
            e "Ohh yes, definitely!"
            e "Like, have you listened to Raison d'être? {w=0.5}\nThat song is{w=0.5}{nw}"
            with { "master": vpunch }
            extend " {b}FIRE{/b}{fast} wtf!?"

            m "So true... {w=0.5}Eve's voice always sounds so amazing~"
            e "fr fr ong fr fr no cap"
            m "Yeah, and what do you think about ..."

            stop music fadeout 1.5
            with Fade(1.5, 0.5, 1.0)
            "You and Madoka kept talking for a long time."
            "It was a long, joyful chat."

            e "phew, that was so much fun! I really enjoyed talking to you, Madoka Higuchi!!"
            m "yeah, I feel the same..."

            m "I hope you enjoyed your birthday."
            
            play music "audio/early_riser.mp3" fadein 4.0
            discord_n "{w=3.0}{nw}"

            show madoka maid blush:
                ycenter 0.75
                zoom 1
            with Dissolve(0.5)
            m "Oh.{w=0.5} It seems like it's time for you to wake up."
            with Pause(1.0)
            m "But don't you worry about it..."
            
            show madoka maid happy:
                ycenter 0.7
                zoom 0.7
            with Dissolve(0.5)
            extend " I'll be waiting for you in your dreams."
            $ renpy.music.set_volume(0, 0, "music")
            e "wow, that's truly a VN line of all times"
            $ renpy.music.set_volume(1, 0, "music")

            e "but- who cares!! Please stay with me, Madoka!!"
            
            with Pause(1.0)
            "The alarm is ringing."

            e "Oh no. It's actually happening, isn't it?"

            show solid_white
            with { "master": Dissolve(5.0) }
            stop music fadeout 5.0
            m "{cps=20}Don't worry.{w=0.5}{cps=10} I'll always be with you...{w=0.5} {cps=80}or smth idk this is just another cheesy VN line so yeah       . . . . . . . . . . . . . . . . . . .{nw}"

            # "{cps=20}Your mind goes blank..."
            jump happy_ending

label ending(ending=""):
    stop music fadeout 1.5
    play sound snd_vaporized
    with fade_white
    show bg white
    hide madoka
    hide phone

    "{cps=20}Your mind goes blank..."

    play sound snd_break1
    "{cps=20}[ending] Ending.{w}{cps=60}\nGo back a few options to try again..."
    Character("", advance=False) "[ending] Ending.\nGo back a few options to try again... {size=-10}(scroll up){fast}"
    jump final

label happy_ending:
    ending_narrator "{w=1.0}{nw}"
    hide madoka
    with None

    hide solid_white
    show bg room
    # with { "master": Dissolve(1.0) }
    # $ renpy.music.set_volume(1.0)
    play music "audio/birds_are_singing.mp3"
    ending_narrator "{w=1.0}{nw}"

    
    ending_narrator """
    You're laying on your desk.

    The sun is already shining into your room.
    
    {cps=3}...{/cps  }

    Madoka stayed in your dreams.

    But another great days starts!

    And you feel like {size=-10}FECES{/size}.{w=.5}\nYou slept 5 hours again.
    """

    nvl clear

    ending_narrator "{nw}"

    ending_narrator """
    Still...

    You have a positive feeling.

    That from now on, Madoka will visit you every night.

    And for just a bit... you'll see her again.

    Not in your drawings...{w=1.0}\nBut in your dreams.

    ...

    And Hopefully...
    """

    nvl clear
    show bg sakura
    ending_narrator "{nw}"
    ending_narrator "{nw}"
    ending_narrator "{nw}"

    stop music
    show madoka maid happy:
        zoom 0.4
        ycenter 1.2
        easein_back 0.4 ycenter 0.75
    show madoka maid curious as madoka1:
        zoom 0.4
        xcenter 0.8
        ycenter 1.2
        easein_back 0.6 ycenter 0.75
    show madoka maid floor as madoka2:
        zoom 0.4
        xcenter 0.4
        ycenter 1.2
        easein_back 0.7 ycenter 0.75
    
    ending_narrator "{color=#000}That will make you actually want to sleep"

label final:
    play sound "audio/party_horn.mp3"
    show madoka maid happy:
        easein_back 0.4 zoom 0.5
    show madoka maid curious as madoka1:
        easein_back 0.6 zoom 0.5
    show madoka maid floor as madoka2:
        easein_back 0.7 zoom 0.5 ycenter 0.6

    "Happy birthday, Egas-kun!"
    with Fade(4.0, 0.0, 0.0)