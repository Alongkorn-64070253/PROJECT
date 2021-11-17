# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("KING 11")
define e = Character("Knight")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene racha1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show invisible

    # These display lines of dialogue.

    k "Hello my knight"

    k "You have a new mission"
    scene racha2
    show invisible
    with fade

    k "You must go kill the Demon Lord"

    k "I have prepared a weapon for you"

    scene racha3
    show invisible
    with fade

    k "Go on  go kill it"

    scene weaponroom
    with fade

    e "choose your weapon"

    menu:
        "sword":
            jump bg1
        "gun":
            jump bg2
        "book":
            jump bg3
        "pokeball":
            jump bg4
    label bg1:
        scene sword
        show invisible
        with fade
        e "good"

        scene door
        show invisible
        with fade
        e "Front door"

        menu:
            "Parachute":
                jump car
            "motorbike":
                jump motorbike
            "taxi":
                jump taxi
            "walk":
                jump walk

        label car:
            scene parachute1
            show invisible
            with fade
            e "You got parachute"
            scene parachute1
            show invisible
            with fade
            e "JUMP!!!"
            scene parachute2
            show invisible
            with fade
            e "UMM"
            scene parachute3
            show invisible
            with fade
            e "ARGH!!!"
            scene parachute4
            show invisible
            with fade
            e "open parachute"
            scene parachute5
            show invisible
            with fade
            e "mung yib pid ai kuy"
            e "chibhay"
            scene parachute6
            show invisible
            with fade
            e "ARKKKK!!!"
            return
        label motorbike:
            scene motorbike1
            show invisible
            with fade
            e "WOW THAT SO COOL!!"
            scene motorbike2
            show invisible
            with fade
            e "ngan ngan"
            scene motorbike3
            show invisible
            with fade
            e "kayasungkom aisus"
            return
        label taxi:
            scene taxi1
            show invisible
            with fade
            e "taxi noy krub"
            scene taxido1
            show invisible
            with fade
            e "ngan ngan"
            scene taxido2
            show invisible
            with fade
            e "chokdeena ai num"
            scene moutain
            show invisible
            with fade
            e "moutain"

            menu:
                "waterfall":
                    jump waterfall
                "climb":
                    jump climb

            label waterfall:
                scene moutain
                show invisible
                with fade
                e "water"
                menu:
                    "swim":
                        jump swim1
                    "walk":
                        jump walkwaterfall
                label swim1:
                    scene swim1
                    show invisible
                    with fade
                    e "you see waterfall"
                    scene swim2
                    show invisible
                    with fade
                    e "you jump"
                    scene swim3
                    show invisible
                    with fade
                    e "toom!!!"
                    scene swim4
                    show invisible
                    with fade
                    e "Hello fish"
                    scene swim5
                    show invisible
                    with fade
                    e "ngam ngam ngam"
                    e "delicious makkub daddy"
                    return
                label walkwaterfall:
                    scene walkwaterfall1
                    show invisible
                    with fade
                    e "walk"
                    scene walkwaterfall2
                    show invisible
                    with fade
                    e "you found goblin"
                    scene walkwaterfall3
                    show invisible
                    with fade
                    e "that so noob fight me"
                    scene walkwaterfall4
                    show invisible
                    with fade
                    e "ngang nagnag!!!"
                    e "what?"
                    scene walkwaterfall5
                    show invisible
                    with fade
                    e "..."
                    scene walkwaterfall6
                    show invisible
                    with fade
                    e "chib hay"
                    scene walkwaterfall7
                    show invisible
                    with fade
                    e "sorry kub just kidding"
                    scene walkwaterfall8
                    show invisible
                    with fade
                    e "ARkkk!!!"
                    return
            label climb:
                scene moutain
                show invisible
                with fade
                e "climb this moutain"
                e "How do I climb this?"
                e "choose your climbing method"

                menu:
                    "your hand":
                        jump hand
                    "suction cup":
                        jump suctioncup
                    "climbing equipment":
                        jump climbing

                label hand:
                    scene sword
                    show invisible
                    with fade
                    e "hand"
                label climbing:
                    scene sword
                    show invisible
                    with fade
                    e "climb"
                label suctioncup:
                    scene sword
                    show invisible
                    with fade
                    e "suctioncup"
                scene sword
                show invisible
                with fade
                e "castle"

                menu:
                    "basement":
                        jump basement
                    "kanghna":
                        jump kanghna
                    "floor":
                        jump floor

                label basement:
                    scene sword
                    show invisible
                    with fade
                    e "beer monster"

                    menu:
                        "fight":
                            jump beerfight
                        "run":
                            jump beerrun

                    label beerfight:
                        scene sword
                        show invisible
                        with fade
                        e"win"

                        scene sword
                        show invisible
                        with fade
                        e"buff"

                        scene sword
                        show invisible
                        with fade
                        e"bossroom"
                    label beerrun:
                        scene sword
                        show invisible
                        with fade
                        e"lose"
                        return
                label kanghna:
                    scene sword
                    show invisible
                    with fade
                    e "chest"

                    scene sword
                    show invisible
                    with fade
                    e"openchest"

                    menu:
                        "dice":
                            jump diceitem
                        "key":
                            jump keyitem

                    label diceitem:
                        scene sword
                        show invisible
                        with fade
                        e "You Got Dice!"
                        e "turnback"
                        menu:
                            "basement":
                                jump basement1
                            "floor":
                                jump floor1
                        label basement1:
                            scene sword
                            show invisible
                            with fade
                            e "beer monster"

                            menu:
                                "fight":
                                    jump beerfight1
                                "run":
                                    jump beerrun1

                            label beerfight1:
                                scene sword
                                show invisible
                                with fade
                                e"win"

                                scene sword
                                show invisible
                                with fade
                                e"buff"

                                scene sword
                                show invisible
                                with fade
                                e"bossroom"
                            label beerrun1:
                                scene sword
                                show invisible
                                with fade
                                e"lose"
                        label floor1:
                            scene sword
                            show invisible
                            with fade
                            e "yanglobman"

                            menu:
                                "fight":
                                    jump yanglobfight1
                                "run":
                                    jump yanglobrun1

                            label yanglobfight1:
                                scene sword
                                show invisible
                                with fade
                                e"lose"
                                return
                            label yanglobrun1:
                                scene sword
                                show invisible
                                with fade
                                e"win"
                                scene sword
                                show invisible
                                with fade
                                e"you Got Item"

                                scene sword
                                show invisible
                                with fade
                                e"bossroom"
                    label keyitem:
                        scene sword
                        show invisible
                        with fade
                        e "You Got The Key!"
                        e "turn back"
                        menu:
                            "basement":
                                jump basement2
                            "floor":
                                jump floor2
                        label basement2:
                            scene sword
                            show invisible
                            with fade
                            e "beer monster"

                            menu:
                                "fight":
                                    jump beerfight2
                                "run":
                                    jump beerrun2

                            label beerfight2:
                                scene sword
                                show invisible
                                with fade
                                e"win"

                                scene sword
                                show invisible
                                with fade
                                e"buff"

                                scene sword
                                show invisible
                                with fade
                                e"bossroom"
                            label beerrun2:
                                scene sword
                                show invisible
                                with fade
                                e"lose"
                        label floor2:
                            scene sword
                            show invisible
                            with fade
                            e "yanglobman"

                            menu:
                                "fight":
                                    jump yanglobfight2
                                "run":
                                    jump yanglobrun2

                            label yanglobfight2:
                                scene sword
                                show invisible
                                with fade
                                e"lose"
                                return
                            label yanglobrun2:
                                scene sword
                                show invisible
                                with fade
                                e"win"
                                scene sword
                                show invisible
                                with fade
                                e"you Got Item"

                                scene sword
                                show invisible
                                with fade
                                e"bossroom"
                label floor:
                    scene sword
                    show invisible
                    with fade
                    e "yanglobman"

                    menu:
                        "fight":
                            jump yanglobfight
                        "run":
                            jump yanglobrun

                    label yanglobfight:
                        scene sword
                        show invisible
                        with fade
                        e"lose"
                        return
                    label yanglobrun:
                        scene sword
                        show invisible
                        with fade
                        e"win"
                        scene sword
                        show invisible
                        with fade
                        e"you Got Item"

                        scene sword
                        show invisible
                        with fade
                        e"bossroom"
        label walk:
            scene walk1
            show invisible
            with fade
            e "dern mang aihere"
            scene walk2
            show invisible
            with fade
            e "la la la"
            scene walk3
            show invisible
            with fade
            e "wat Arrow?"
            scene walk4
            show invisible
            with fade
            e "Hmm"
            scene walk5
            show invisible
            with fade
            e "Arghh!!!"
            scene walk6
            show invisible
            with fade
            e "then I took an arrow in the knee"
            e "I died"
            return
    return
    label bg2:
        scene gun1
        show invisible
        with fade
        e "wow that so cool"
        e "I want to test this"
        e "1"
        e "2"
        e "3"
        scene gun2
        show invisible
        with fade
        e "ARCKK!!!"
        e "this gun is fakegun"
        return
    return
    label bg3:
        scene book1
        show invisible
        with fade
        e "you choose book"
        scene book2
        show invisible
        with fade
        e "open it!"
        scene book3
        show invisible
        with fade
        e "ARCKK!!!"
        scene book4
        show invisible
        with fade
        e "..."
    return
    label bg4:
        e "lazy"
    return

    # This ends the game.

    return
