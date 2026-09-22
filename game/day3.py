from time import sleep


def day_three_start(state):
    print("\nNUIT 3")
    sleep(2)

    print("\nTon téléphone vibre.")
    sleep(2)
    print("\n02:12")
    sleep(2)

    print("\nUNKNOWN:")
    print("\n'Je suis légèrement en avance mais ce n'est pas grave.")
    sleep(2)

    print("C'est prêt. ")
    sleep(2)

    print("L'application est maintenant débloquée.'")
    sleep(2)

    print("\nTu te lèves.")
    sleep(2)

    print("La pièce est plongée dans le noir.")
    sleep(2)

    print("Seule la lumière de la lune traverse la fenêtre.")
    sleep(3)

    print("\nTu vas à ton bureau et allumes ton PC.")
    sleep(3)

    print("\nSur ton bureau, l'application SCENE est ouverte.")
    sleep(2)

    input("\nAppuyer sur Entrée pour ouvrir l'application...")

    sleep(2)
    scene_player(state)


def scene_player(state):
    print("\nSCENE")
    sleep(2)

    print("\nUn lecteur vidéo apparaît à l'écran.")
    sleep(2)

    print("Aucune barre de progression.")
    sleep(2)

    print("Aucun titre.")
    sleep(2)

    print("Seulement un bouton : PLAY")
    sleep(2)

    print("\nUn message apparaît.")
    sleep(2)

    print("\nUNKNOWN:")
    print("Regarde derrière toi.")
    sleep(2)

    print("\nQue faire ?")
    print("[1] Se retourner")
    print("[2] Ne pas se retourner")

    choice = input("> ")

    if choice == "1":
        look_behind_before_video(state)
    elif choice == "2":
        start_video(state)
    else:
        print("Choix invalide.")
        sleep(1)
        scene_player(state)


def look_behind_before_video(state):
    print("\nTu te retournes.")
    sleep(2)

    print("\nLa pièce est presque entièrement plongée dans le noir.")
    sleep(2)

    print("Ton écran éclaire seulement le bureau.")
    sleep(2)

    print("La lune éclaire faiblement le reste de la chambre.")
    sleep(2)

    print("\nIl n'y a personne.")
    sleep(3)

    start_video(state)


def start_video(state):
    state.watched_video = True

    print("\nTu lances la vidéo.")
    sleep(3)

    print("\nLa vidéo montre ta chambre.")
    sleep(2)

    print("Le même bureau.")
    sleep(2)

    print("La même fenêtre.")
    sleep(2)

    print("La même pièce.")
    sleep(3)

    print("\nNUIT 1.")
    sleep(2)

    print("La chambre est vide.")
    sleep(2)

    print("\nUne horloge apparaît dans un coin de l'écran.")
    sleep(2)
    print("02:09")
    sleep(3)

    print("\nUne silhouette entre dans la chambre.")
    sleep(3)

    print("Elle reste quelques secondes devant ton bureau.")
    sleep(3)

    print("\n02:12")
    sleep(2)

    print("La silhouette glisse une clé USB sous le bureau.")
    sleep(3)

    print("\n02:13")
    sleep(2)

    print("Elle quitte la chambre.")
    sleep(3)

    print("\nQuelques secondes plus tard, tu apparais dans la vidéo.")
    sleep(2)
    print("Tu viens de te lever de ton lit.")
    sleep(3)

    print("\nLa vidéo avance.")
    sleep(3)

    print("\nJour 2.")
    sleep(2)

    print("La chambre est de nouveau vide.")
    sleep(2)

    print("\n02:09")
    sleep(2)

    print("La silhouette entre.")
    sleep(3)

    print("\nElle s'approche de l'armoire.")
    sleep(2)

    print("Elle glisse une enveloppe sous l'armoire.")
    sleep(3)

    print("\n02:12")
    sleep(2)

    print("La silhouette quitte la chambre.")
    sleep(3)

    print("\n02:13")
    sleep(2)

    print("Tu apparais dans la vidéo.")
    sleep(2)
    print("Tu viens de te réveiller.")
    sleep(3)

    print("\nLa vidéo avance encore.")
    sleep(3)

    print("\nJour 3.")
    sleep(2)

    print("La pièce est exactement comme elle l'est maintenant.")
    sleep(3)

    print("\n02:09")
    sleep(2)

    print("La silhouette entre une dernière fois.")
    sleep(3)

    print("Elle s'arrête devant la caméra.")
    sleep(3)

    print("Puis elle regarde directement l'objectif.")
    sleep(4)

    print("\n02:11")
    sleep(2)

    print("Elle quitte la chambre.")
    sleep(3)

    print("\n02:12")
    sleep(2)

    print("Tu apparais dans la vidéo.")
    sleep(2)
    print("Tu viens de te réveiller.")
    sleep(3)

    print("\nLa vidéo ne s'arrête pas.")
    sleep(3)
    print("Elle continue en direct.")
    sleep(4)

    print("\nEt tu comprends.")
    sleep(3)

    print("La caméra filme la pièce où tu te trouves actuellement.")
    sleep(4)

    print("\nLa silhouette apparaît derrière toi.")
    sleep(5)

    print("\nUn message apparaît sur l'écran.")
    sleep(3)

    print("\nUNKNOWN:")
    print("Ne te retourne pas.")
    sleep(3)

    print("\nQue faire ?")
    print("[1] Se retourner")
    print("[2] Ne pas se retourner")

    choice = input("> ")

    if choice == "1":
        turn_around(state)
    elif choice == "2":
        don_t_turn_around(state)
    else:
        print("Choix invalide.")
        sleep(1)
        start_video(state)


def turn_around(state):
    print("\nTu te retournes.")
    sleep(3)

    print("\nL'écran devient noir.")
    sleep(2)

    print("Ton ordinateur s'éteint tout seul.")
    sleep(4)

    print("\nUn nuage passe devant la lune.")
    sleep(3)
    print("La pièce est complètement plongée dans le noir.")
    sleep(4)

    print("\nTu ne vois rien.")
    sleep(4)

    print("\nTu tends la main vers le mur.")
    sleep(2)

    print("\nTu cherches l'interrupteur.")
    sleep(3)

    print("\nLa lumière s'allume.")
    sleep(3)

    print("\nTu regard autour de toi.")
    sleep(4)

    print("\nPuis tu te souviens de la vidéo du jour 2.")
    sleep(3)

    print("L'enveloppe.")
    sleep(2)

    print("Sous l'armoire.")
    sleep(3)

    print("\nTu t'approches de l'armoire.")
    sleep(3)
    print("Tu te penches.")
    sleep(3)

    print("\nTu trouves l'enveloppe.")
    sleep(4)

    print("\nTu l'ouvres.")
    sleep(3)

    print("Une écriture soignée.")
    sleep(2)

    print("\nDes lettres rondes tracées a l'encre noire.")
    sleep(2)

    print("""
You weren't supposed to see me.

But now...

I'll always find you.

02:13
""")

    sleep(4)

    print("\nTu entends quelque chose derrière toi.")
    sleep(5)

    print("\nTu te retournes.")
    sleep(4)

    print("\nL'ordinateur s'allume tout seul.")
    sleep(4)

    print("\nL'écran affiche :")
    sleep(3)

    print("\n02:13")
    sleep(2)

    print("Encore.")
    sleep(5)


def don_t_turn_around(state):
    print("\nTu restes immobile.")
    sleep(4)

    print("La silhouette s'évapore.")
    sleep(2)

    print("\nUn nouveau message apparaît.")
    sleep(3)

    print("\nUNKNOWN:")
    sleep(1)

    print("Ouvre l'enveloppe que je t'ai laissée.")
    sleep(4)

    print("\nTu te souviens de la vidéo du jour 2.")
    sleep(3)

    print("L'enveloppe est sous ton armoire.")
    sleep(3)

    print("\nTu te lèves et vas la chercher.")
    sleep(4)

    print("Tu l'ouvres.")
    sleep(3)

    envelope_message(state)


def envelope_message(state):
    print("Une écriture soignée.")
    sleep(2)

    print("\nDes lettres rondes tracées a l'encre noire.")
    sleep(2)

    print("""
You weren't supposed to see me.

But now...

I'll always find you.

02:13
""")

    sleep(5)

    print("\nTu entends quelque chose derrière toi.")
    sleep(3)

    print("\nTu te retournes.")
    sleep(4)

    print("\n02:13")
    sleep(5)

    print("\nL'ordinateur s'éteint tout seul.")
    sleep(4)
