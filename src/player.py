############################################################
#   PLAYER
############################################################

from printable import printable


#----------------------------------------------------------#


class Player:

    ########################################
    #   PROPERTIES
    ########################################

    @property
    def current_room(self): return self.__current_room

    @current_room.setter
    def current_room(self, value): self.__current_room = value

    ########################################
    #   METHODS
    ########################################

    def __init__(self, name, current_room=None, items=None):

        self.name = name
        self.current_room = current_room

        if items is None:
            items = []

        self.items = items

    def __str__(self):

        attr_keys = ("name", "current_room")

        return printable.to_str(self, attr_keys)

    def __repr__(self):

        attr_keys = ("name", "current_room")

        return printable.to_repr(self, attr_keys)

    ########################################
