## check OCR word enging ##

# list possible endings
# raptor horizontal, vertical, tripod, merlin, MVac
allowed_endings = ["l", "c", "d", "n", "1", "2"]


def check_ending_allowed(word):

    # get last letter of word
    try:
        last_letter = word[-1]
    except IndexError:
        return None

    # check if letter is not allowed
    if last_letter not in allowed_endings:

        # remove letter and start again
        word = word[:-1]
        return check_ending_allowed(word)

    # return the correct word
    return word
