from ..words import directions

# player verbs with synonyms
verbs = (
    *tuple((w, 0) for w in directions.words),
    (
        ('move',
         'move to',
         'go',
         'go to'),
        1,
    ),
    (
        ('move back',
         'move back to',
         'go back',
         'go back to'),
        (0, 1),
    ),
    (
        ('inventory',
         'my inventory',
         'list items in inventory',
         'list items in my inventory',
         'items in inventory',
         'items in my inventory'),
        0,
    ),
)
