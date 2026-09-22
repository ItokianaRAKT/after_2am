from time import sleep


def day_two_start(state):
    print("\nNUIT 2")
    sleep(2)

    print("\nTu te réveilles.")
    sleep(2)

    print("\n2:13")
    sleep(2)

    print("\nTu remarques que ton pc est allumé.")
    sleep(2)

    print("\nTu es pourtant bien sur de l'avoir éteint avant d'aller te coucher.")
    sleep(2)

    print("\nTu te lèves pour aller l'éteindre.")
    sleep(2)

    print("\nEn jetant un coup d'oeil a l'horloge numérique, tu remarques qu'il est 2:13.")
    sleep(2)

    print("\nAu moment d'éteindre ton pc, tu remarques qu'une nouvelle application est apparue sur ton bureau")
    sleep(2)

    print("\nC'est la première fois que tu la voies.")
    sleep(2)

    print("\n> SCENE")
    sleep(3)

    input("\nAppuyer sur Entrée pour ouvrir l'application...")

    sleep(2)

    scene_app(state)


def scene_app(state):
    print("\nPASSWORD REQUIRED")
    sleep(3)

    if state.password:
        enter_password(state)
    else:
        password_attempts(state)


def enter_password(state):
    password = input("\nMot de passe : ")

    sleep(2)

    if password.strip().upper() == state.password.upper():
        access_granted(state)
    else:
        print("\nMot de passe incorrect.")
        sleep(2)
        password_attempts(state)


def password_attempts(state):
    for attempt in range(2):
        password = input("\nMot de passe : ")

        sleep(2)

        if state.password and password.strip().upper() == state.password.upper():
            access_granted(state)
            return

        print("\nMot de passe incorrect.")
        sleep(2)

    phone_notification(state)


def phone_notification(state):
    sleep(3)

    print("\n📱 Ton téléphone vibre.")
    sleep(2)

    print("\nUNKNOWN:")
    sleep(1)
    print("Tu cherches encore ?")
    sleep(2)

    print()
    sleep(1)

    print("Regarde ton historique.")
    sleep(3)

    phone_history(state)


def phone_history(state):
    print("\nTu ouvres ton historique.")
    sleep(2)

    print("\nHistorique récent :")
    sleep(2)

    print("02:17  unknown.local")
    sleep(1)

    print("02:18  unknown.local/help")
    sleep(1)

    print("02:19  unknown.local/...")
    sleep(3)

    print("\nTu ouvres la page.")
    sleep(3)

    website_puzzle(state)


def website_puzzle(state):
    print("\nLa page s'ouvre.")
    sleep(3)

    print("\nUn message apparait, puis un texte.")
    sleep(3)

    print("Petit cadeau. Je le trouve particulièrement beau.")
    sleep(2)

    print("Un indice de plus pour te prouver ma générosité: 2 - 2 - 2")
    sleep(3)

    print("""
    La lune s'efface au fond du ciel noir,
    Le vent murmure un étrange espoir,
    Les fenêtres tremblent dans le silence,
    Quelqu'un s'approche avec patience.

    À 2:13, plus rien ne respire,
    Une ombre glisse faisant tout fuir,
    Quelque chose veille au bord du sommeil,
    Et personne ne voit ce qui nous surveille.

    La chambre demeure plongée dans le noir,
    Le temps s'est arrêté sans prévenir ce soir,
    Puis une voix murmure dans l'ombre,
    Et soudain, tout devient plus sombre.
    """)

    sleep(5)

    password = input("\nMot trouvé : ")

    sleep(2)

    if password.strip().upper() == "OMBRE":
        state.password = "OMBRE"
        access_granted(state)
    else:
        print("\nCe n'est pas le bon mot.")
        sleep(3)
        website_puzzle(state)


def access_granted(state):
    print("\nACCESS GRANTED")
    sleep(3)

    print("\nLa scène n'est pas totalement prête.")
    sleep(2)

    print("Patiente un peu.")
    sleep(3)

    print("\nTemps restant : inconnu")
    sleep(4)

    state.scene_unlocked = True
