define m = Character("Madoka Higuchi")

image cafe = "cafe.jpg"
image maid = "MadokaHiguchiMaid(UwU might be needed).png"
default good_ending = False

label start:
    jump cafe

label cafe:
    show cafe # onlayer overlay 

    show maid

    
menu:
    m "What say you?"
    "Bandana dee is the greatest":
        jump ba
    "Nothing":
        jump beh

label ba:
    m "nice"
    return
label beh:
    m "You son of a"
    return