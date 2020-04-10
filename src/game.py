############################################################
#   GAME
############################################################

import re
from printable import printable

from room import Room
from player import Player


#----------------------------------------------------------#


class Game:

    ########################################
    #   METHODS
    ########################################

    def __init__(self, name, rooms=None, player=None):

        if rooms is None:
            rooms = {}

        self.name = name
        self.rooms = rooms
        self.player = player

        self.turns_history = []
        self.inputs_history = {
            "raw": [],
            "trimmed": [],
            "normal": [],
        }

    def __str__(self):

        attr_keys = ("name", "rooms", "player",
                     "turns_history", "inputs_history")

        return printable.to_str(self, attr_keys)

    def __repr__(self):

        attr_keys = ("name", "rooms", "player",
                     "turns_history", "inputs_history")

        return printable.to_repr(self, attr_keys)

    ####################
    #   STATIC
    ####################

    @staticmethod
    def print_room(room):

        if isinstance(room, Room):

            print(f"\n--- {room.name} ---\n")
            print(room.description)

        else:

            print("There is no room there.")

    ####################
    #   move player (silently)
    ####################

    def put_player(self, room):

        it_worked = None
        target_room = None

        if isinstance(room, Room):
            self.player.current_room = room
            it_worked = True
            target_room = self.player.current_room

        elif isinstance(room, str):
            self.player.current_room = self.rooms[room]
            it_worked = True
            target_room = self.player.current_room

        else:
            print("Game(...).put_player -- well, that didn't work...")
            it_worked = False

        return it_worked, target_room

    def move_player(self, direction):

        key, __ = direction
        it_worked = None
        target_room = getattr(self.player.current_room, f"{key}_to", None)

        if isinstance(target_room, Room):
            self.player.current_room = target_room
            it_worked = True

        elif target_room is None:
            it_worked = False

        return it_worked, target_room

    def move_player_north(self):
        return self.move_player(("n", "north"))

    def move_player_east(self):
        return self.move_player(("e", "east"))

    def move_player_south(self):
        return self.move_player(("s", "south"))

    def move_player_west(self):
        return self.move_player(("w", "west"))

    ####################
    #   move player and print
    ####################

    def put_player_and_print(self, room):

        it_worked, target_room = self.put_player(room)

        self.print_room(target_room)

        return it_worked, target_room

    def move_player_and_print(self, direction):

        __, word = direction
        it_worked, target_room = self.move_player(direction)

        if it_worked:
            print(f"You move {word}...")

        else:
            print(f"You can't move {word}.")

        self.print_room(target_room)

        return it_worked, target_room

    def move_player_north_and_print(self):
        return self.move_player_and_print(("n", "north"))

    def move_player_east_and_print(self):
        return self.move_player_and_print(("e", "east"))

    def move_player_south_and_print(self):
        return self.move_player_and_print(("s", "south"))

    def move_player_west_and_print(self):
        return self.move_player_and_print(("w", "west"))

    ####################
    #   game flow
    ####################

    def prompt_user(self):

        # get raw user input
        raw_input = input("\n> ")
        self.inputs_history["raw"].append(raw_input)

        # trim user input
        trimmed_input = re.sub(r"\s+", " ", raw_input.strip())
        self.inputs_history["trimmed"].append(trimmed_input)

        # normalize user input
        normal_input = trimmed_input.lower()
        self.inputs_history["normal"].append(normal_input)

        print()

        return normal_input

    def start(self, initial_room=None):

        self.turns_history.append("/start")

        if initial_room is None:
            initial_room = self.player.current_room

        self.put_player_and_print(initial_room)

    def next_turn(self, prev_turn):
        self.turns_history.append(prev_turn)

    def stop(self):
        self.turns_history.append("/stop")

    ########################################
