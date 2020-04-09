############################################################
#   ADVENTURE
############################################################

import tools
from room import Room
from player import Player

########################################
#   rooms
########################################

# declare rooms

rooms = {

    'outside': Room('Outside Cave Entrance', '''
North of you, the cave mount beckons
'''),

    'foyer': Room('Foyer', '''
Dim light filters in from the south.
Dusty passages run north and east.
'''),

    'overlook': Room('Grand Overlook', '''
A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.
'''),

    'narrow': Room('Narrow Passage', '''
The narrow passage bends here from west
to north. The smell of gold permeates the air.
'''),

    'treasure': Room('Treasure Chamber', '''
You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.
'''),

}

# connect rooms

rooms['outside'].n_to = rooms['foyer']

rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']

rooms['overlook'].s_to = rooms['foyer']

rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']

rooms['treasure'].s_to = rooms['narrow']


############################################################
#   MAIN
############################################################

# Make a new player object that is currently in the 'outside' room.

player = Player('Jason', rooms['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters 'q', quit the game.


def are_synonyms(thesaurus, *words):

    for entry in thesaurus:

        words_in_entry = False

        for word in words:

            if word in entry:

                words_in_entry = True

            else:

                words_in_entry = False
                break

        if words_in_entry:

            # all words in same entry -> they are synonyms
            return True

        # ... next!

    # all words were never in the same entry -> they are not synonyms
    return False


# meta verbs with synonyms
meta_verbs = (
    ('q', 'quit'),
)

# direction verbs with synonyms
direction_verbs = (
    ('n', 'north'),
    ('e', 'east'),
    ('s', 'south'),
    ('w', 'west'),
)

# all the verbs!
verbs = tools.flatten((
    *meta_verbs,
    *direction_verbs,
))

########################################
#   REPL
########################################

turns_count = 0

while True:

    # get user input
    raw_user_input = input('> ').strip()
    user_input = raw_user_input.lower()

    # check validity of user input
    if not user_input.startswith(verbs):

        print(f'"{user_input}" is not a recognized command. Try again.')

    else:

        if user_input.startswith(tools.flatten(meta_verbs)):

            if are_synonyms(meta_verbs, user_input, 'quit'):

                print('Goodbye!')
                break

        elif user_input.startswith(tools.flatten(direction_verbs)):

            if are_synonyms(direction_verbs, user_input, 'north'):

                print('Moving north...')

            if are_synonyms(direction_verbs, user_input, 'east'):

                print('Moving east...')

            if are_synonyms(direction_verbs, user_input, 'south'):

                print('Moving south...')

            if are_synonyms(direction_verbs, user_input, 'west'):

                print('Moving west...')

        else:

            print('HOW DID YOU GET HERE? YOU SHOULD NOT BE HERE!')

        turns_count += 1
