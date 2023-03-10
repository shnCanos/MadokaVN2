define m = Character("Madoka Higuchi")
define e = Character("Egas KyUwUn")
define n = Character("Narrator")
define p = Character("Peidro")

# Images
# Bg
image cafe = "cafe.jpg"
image cafe_door = "cafeoutside.jpg"
image discord = "discord.png"

# Madoka
image m_curious_maid = "MadokaHiguchiMaid(UwU might be needed).png"
image m_maid_floor = "MadokaMaidSuitFloor.png"
image m_bunny_flustered = "MadokaFlusteredBunnySuit.png"
image m_meh_happy = "MadokaEverSoHappy.jpg"
image m_bunny_stepped_on_pov_egas = "MadokaBunnySuitEgasKyun.png"
image m_maid_angry_egas = "MadokaAngryEgasKyunMaidSuit.jpg"

# Flags
default good_ending = False

label start:
    show discord
    n "It's 4am. You have just finished your latest madoka drawing, and sent it to your friends through discord"
    play sound "audio/discord.mp3"
    p "...4 am?"
    play sound "audio/discord.mp3"
    p "Again?"
    play sound "audio/discord.mp3"
    p "...really?"
    play sound "audio/discord.mp3"
    p "And for what? To draw madoka drawings?"
    play sound "audio/discord.mp3"
    p "What the heck man"
    play sound "audio/discord.mp3"
    p "You'll have to wake up at 7 tomorrow..."
    play sound "audio/discord.mp3"
    p "I'm disappointed :pensive:"

    e "You're awake too"

    play sound "audio/discord.mp3"
    p "Yes, but I'm awake because I need to go to school..."

    e "..."
    e "I shouldn't have watched Okayu for 5 hours"
    e """
    Is this the real life?
    Is this just fantasy?

    Is Madoka my wife?
    I'm losing my sanity...
    """

    n "Your vision starts getting foggy, and you faint"

    #TODO: Vision goes black
    # or maybe not
    hide discord
    with fade
    jump wakeywakey

label wakeywakey:
    show cafeoutside
    show m_bunny_stepped_on_pov_egas at center:
        zoom 0.35 # Sad 420
    m "What are you doing, sleeping there?"
    m "...Disgusting"
    e "Madoka Higuchi???!!!?!??!?!"
    hide m_bunny_stepped_on_pov_egas
    show m_bunny_flustered at center:
        zoom 1.5     
    m "You know me? Ew."
    m "At least pretend we have never met"

    hide cafeoutside
    jump cafe

label cafe:
    show cafe # onlayer overlay 

    show m_curious_maid at center:
        zoom 0.75

    
menu:
    m "What say you?"
    "Bandana dee is the greatest":
        jump ba
    "Nothing":
        jump beh

label ba:
    hide m_curious_maid
    show m_maid_floor at left:
        zoom 0.69
    m "nice"
    return
label beh:
    m "You son of a"
    return