from time import sleep
from game.day2 import day_two_start


def day_one_start(state):
    sleep(2)
    print("Bienvenu dans cette mini histoire interractive")
    sleep(2)

    print("\nIci, tu incarnes un jeune lycéen ordinaire dont l'identité n'est pas précisée.")
    sleep(3)

    print("\nDébut.")
    sleep(2)

    print("\nTu te réveilles.")
    sleep(2)

    print("\n02:13")
    sleep(3)

    print("Après quelques secondes, tu te lèves machinalement et marches vers ton bureau.")
    sleep(3)

    print("\nQue faire ?")
    print("[1] S'asseoir au bureau")
    print("[2] Retourner dormir")

    choice = input("> ")

    if choice == "1":
        desk(state)
    elif choice == "2":
        sleep_branch(state)
    else:
        print("Choix invalide.")
        sleep(1)
        day_one_start(state)


def sleep_branch(state):
    state.went_back_to_sleep = True

    sleep(2)

    print("\nTu retournes te coucher.")
    sleep(3)

    print("\n📱 Ton téléphone vibre.")
    sleep(2)

    print("\nUNKNOWN:")
    sleep(1)
    print("Bonsoir. J'ai déposé un petit quelque chose près de ton bureau.")
    sleep(2)
    print("Va voir ce que c'est.")
    sleep(2)

    print()
    sleep(2)

    print("Ça pourrait t'intéresser.")
    sleep(3)

    print("\nQue faire ?")
    print("[1] Se lever et aller vers le bureau")
    print("[2] Poser le téléphone et se rendormir")

    choice = input("> ")

    if choice == "1":
        desk(state)
    elif choice == "2":
        second_notification(state)
    else:
        print("Choix invalide.")
        sleep(1)
        sleep_branch(state)


def second_notification(state):
    print("\nTu poses ton téléphone.")
    sleep(2)

    print("Tu fermes les yeux.")
    sleep(4)

    print("\n📱 Ton téléphone vibre à nouveau.")
    sleep(2)

    print("\nUNKNOWN:")
    sleep(1)
    print("Tu ne veux vraiment pas savoir ?")
    sleep(2)

    print()
    sleep(1)

    print("Ça me chagrine...")
    sleep(2)

    print("Mais sache que c'est toi qui en sortiras perdant.")
    sleep(3)

    print("\nTu te lèves.")
    sleep(2)

    desk(state)


def desk(state):
    print("\nTu t'assois à ton bureau.")
    sleep(2)

    print("\nQue faire ?")
    print("[1] Allumer le PC")
    print("[2] Jouer avec le stylo")

    choice = input("> ")

    if choice == "1":
        computer(state)
    elif choice == "2":
        usb_found(state)
    else:
        print("Choix invalide.")
        sleep(1)
        desk(state)


def computer(state):
    print("\nTu appuies sur le bouton d'alimentation.")
    sleep(3)

    print("\nRien.")
    sleep(2)

    print("Tu appuies une seconde fois.")
    sleep(3)

    print("\nLe PC refuse de démarrer.")
    sleep(2)

    print("\nTu te penches pour vérifier le branchement de la prise.")
    sleep(3)

    print("\nQuelque chose attire ton attention.")
    sleep(3)

    print("\nUne clé USB.")
    sleep(2)

    print("Elle est posée sous le bureau.")
    sleep(2)

    print("Tu la récupères.")
    sleep(2)

    print("\nQue faire ?")
    print("[1] La brancher au PC")
    print("[2] La prendre et l'examiner")

    choice = input("\n> ")

    if choice == "1":
        usb_menu(state)
    elif choice == "2":
        examine_usb(state)
    else:
        print("Choix invalide.")
        sleep(1)
        computer(state)


def usb_found(state):
    state.found_usb = True

    print("\nLe stylo tombe.")
    sleep(2)

    print("En te penchant pour le récupérer, tu remarques quelque chose.")
    sleep(3)

    print("\nUne clé USB.")
    sleep(2)

    print("\nQue faire ?")
    print("[1] Allumer le PC et brancher la clé")
    print("[2] Poser la clé sur le bureau")
    print("[3] L'examiner près de la fenêtre")

    choice = input("> ")

    if choice == "1":
        usb_menu(state)
    elif choice == "2":
        put_usb_away(state)
    elif choice == "3":
        examine_usb(state)
    else:
        print("Choix invalide.")
        sleep(1)
        usb_found(state)


def put_usb_away(state):
    print("\nTu poses la clé sur le bureau.")
    sleep(2)

    print("Tu décides de ne pas t'en occuper maintenant.")
    sleep(3)

    print("\nTu retournes te coucher.")
    sleep(4)

    print("\n📱 Ton téléphone vibre.")
    sleep(2)

    print("\nUNKNOWN:")
    sleep(1)
    print("Tu as bien fait.")
    sleep(2)

    print()
    sleep(1)

    print("À demain.")
    sleep(3)


def examine_usb(state):
    state.checked_window = True

    print("\nTu vas près de la fenêtre.")
    sleep(3)

    print("La lumière de la lune éclaire la clé.")
    sleep(4)

    print("\nUne inscription est gravée sur le dos de la clé :")
    sleep(2)

    print("/UNKNOWN/")
    sleep(4)

    print("\nTu retournes à ton bureau.")
    sleep(3)

    print("\nQue faire ?")
    print("[1] Allumer le PC et brancher la clé")
    print("[2] Poser la clé sur le bureau")

    choice = input("\n> ")

    if choice == "1":
        usb_menu(state)
    elif choice == "2":
        put_usb_away(state)
    else:
        print("\nChoix invalide.")
        sleep(1)
        examine_usb(state)


def usb_menu(state):
    state.opened_usb = True

    print("\nLe PC détecte la clé USB.")
    sleep(2)

    print("Elle contient 3 fichiers.")
    sleep(2)

    print("\n/UNKNOWN/01")
    sleep(1)
    print("/UNKNOWN/02")
    sleep(1)
    print("/UNKNOWN/03")
    sleep(3)

    print("\nUNKNOWN:")
    sleep(2)

    print("Tu ne peux en ouvrir qu'un.")
    sleep(2)

    print("Choisis bien.")
    sleep(3)

    choice = input("\n> ")

    if choice == "1":
        usb_file_01(state)
    elif choice == "2":
        usb_file_02(state)
    elif choice == "3":
        usb_file_03(state)
    else:
        print("\nChoix invalide.")
        sleep(1)
        usb_menu(state)


def usb_file_01(state):
    state.usb_file = "01"
    state.password = "OMBRE"

    print("\n/UNKNOWN/01")
    sleep(2)

    print("\nUn fichier texte s'ouvre.")
    sleep(4)

    print("\nPASSWORD:")
    sleep(2)

    print("OMBRE")
    sleep(4)

    print("\nLe fichier disparaît.")
    sleep(2)

    print("La clé USB est vide.")
    sleep(3)


def usb_file_02(state):
    state.usb_file = "02"

    print("\n/UNKNOWN/02")
    sleep(2)

    print("\nUNKNOWN:")
    sleep(2)

    print("Tu pensais vraiment que j'allais te donner la réponse directement ?")
    sleep(3)

    print("\n2 - 2 - 2")
    sleep(3)

    print("""
La lune s'efface au fond du ciel noir,
Le vent murmure un étrange espoir,
Les fenêtres tremblent dans le silence,
Quelqu'un s'approche avec patience.

À 2:13, plus rien ne respire,
Une ombre glisse, faisant tout fuir,
Quelque chose veille au bord du sommeil,
Et personne ne voit ce qui nous surveille.

La chambre demeure plongée dans le noir,
Le temps s'est arrêté sans prévenir ce soir,
Puis une voix murmure dans l'ombre,
Et soudain, tout devient plus sombre.
""")

    sleep(5)

    print("\nLe fichier disparaît.")
    sleep(3)

    state.password = "OMBRE"


def usb_file_03(state):
    state.usb_file = "03"

    print("\n/UNKNOWN/03")
    sleep(3)

    print("\nMauvais choix.")
    sleep(2)

    print("Pas de chance.")
    sleep(4)

    print("\nLe fichier disparaît.")
    sleep(2)

    print("La clé USB est vide.")
    sleep(3)
