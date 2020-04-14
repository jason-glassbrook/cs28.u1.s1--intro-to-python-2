############################################################
#   TOOLS
############################################################


def reply(o, f, *args, **kwargs):
    return o.__class__(f(o, *args, **kwargs))


########################################
#   shaping
########################################


def iter_flatten(collection, types=(tuple, list, set)):
    for item in collection:
        if isinstance(item, types):
            yield from iter_flatten(item, types)
        else:
            yield item


def flatten(collection, types=(tuple, list, set)):
    return reply(collection, iter_flatten, types)


########################################
#   selecting
########################################

# by index


def ith(collection, i):
    return collection[i]


def first(collection):
    return collection[0]


def last(collection):
    return collection[-1]


# by slice

def most(collection, stop=-1):
    return collection[:(stop)]


def rest(collection, start=1):
    return collection[(start):]


########################################
#   taking (sub-selecting)
########################################

# generic

def iter_take(collection, iter_subselect, *args, **kwargs):
    return (iter_subselect(item, *args, **kwargs) for item in collection)


def take(collection, iter_subselect, *args, **kwargs):
    return reply(collection, iter_subselect, *args, **kwargs)


# by index

def iter_take_ith(collection, *args):
    return iter_take(collection, ith, *args)


def take_ith(collection, *args):
    return reply(collection, iter_take_ith, *args)


def iter_take_first(collection):
    return iter_take(collection, first)


def take_first(collection):
    return reply(collection, iter_take_first)


def iter_take_last(collection):
    return iter_take(collection, last)


def take_last(collection):
    return reply(collection, iter_take_last)


# by slice

def iter_take_slice(collection, *args):
    return iter_take(collection, lambda c: ith(c, slice(*args)))


def take_slice(collection, *args):
    return reply(collection, iter_take_slice, *args)


def iter_take_most(collection, *args):
    return iter_take(collection, most, *args)


def take_most(collection, *args):
    return reply(collection, iter_take_most, *args)


def iter_take_rest(collection, *args):
    return iter_take(collection, rest, *args)


def take_rest(collection, *args):
    return reply(collection, iter_take_rest, *args)
