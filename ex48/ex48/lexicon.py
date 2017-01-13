direction = ['north', 'south', 'east', 'west']
verb = ['go', 'kill', 'eat']
stop = ['in', 'the', 'of']
noun = ['bear', 'princess']
number = [1234, 3, 91234]

list_of_words = {'direction': direction, 'verb': verb, 'stop': stop, 'noun': noun, 'number': number}


def scan(sentence):
    results = sentence.split(' ')
    final_list = []
    for word in results:
        found = False
        number = is_number(word)
        if number is True:
            word = int(word)
        for key, value in list_of_words.iteritems():
            if found is False and word in value:
                final_list.append((key, word))
                found = True
        if found is False:
            final_list.append(('error', word))
    return final_list


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False