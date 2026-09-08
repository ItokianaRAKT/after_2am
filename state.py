class GameState:
    def __init__(self):
        self.day = 1

        self.went_back_to_sleep = False
        self.found_usb = False
        self.opened_usb = False
        self.checked_window = False
        self.usb_file = None

        self.password = None

        self.scene_unlocked = False

        self.watched_video = False
        self.opened_envelope = False
