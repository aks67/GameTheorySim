from Tournament import *


class Observer:

    def __init__(self, tournament) -> None:
        self.t = tournament

    def get_last_played_by(self, name):
        
        return self.t.last_play_history