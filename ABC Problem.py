sample_blocks = [('B', 'O'),
                 ('X', 'K'),
                 ('D', 'Q'),
                 ('C', 'P'),
                 ('N', 'A'),
                 ('G', 'T'),
                 ('R', 'E'),
                 ('T', 'G'),
                 ('Q', 'D'),
                 ('F', 'S'),
                 ('J', 'W'),
                 ('H', 'U'),
                 ('V', 'I'),
                 ('A', 'N'),
                 ('O', 'B'),
                 ('E', 'R'),
                 ('F', 'S'),
                 ('L', 'Y'),
                 ('P', 'C'),
                 ('Z', 'M')]

sample_words = ["bark", "BooK", "TReAT", "COMMON", "squAD", "conFUSE", "boT", "BoTT"]


def can_make_word(blocks, word=''):
    letter_amounts = {}
    block_indexes = {}
    temp = []
    for letter in word.upper():
        if letter in temp:
            continue
        temp.append(letter)
        letter_amounts[letter] = word.upper().count(letter)
        for block in blocks:
            try:
                if block.count(letter) == 1:
                    try:
                        if block_indexes[letter]:
                            block_indexes[letter].append(blocks.index(block))
                    except:
                        block_indexes[letter] = [blocks.index(block)]
            except:
                continue

    used_blocks = []
    remaining_letters = []

    while letter_amounts is not []:
        for letter, indexes in sorted(block_indexes.items(), key=lambda x: len(x[1])):
            temp_indexes = indexes
            for block_number in used_blocks:
                if temp_indexes.count(block_number) == 1:
                    del temp_indexes[temp_indexes.index(block_number)]
            if len(temp_indexes) < letter_amounts[letter]:
                return False
            elif len(temp_indexes) == letter_amounts[letter]:
                del letter_amounts[letter]
                del block_indexes[letter]
                used_blocks.extend(indexes)
            else:
                for index in temp_indexes:
                    for let in blocks[index]:
                        if let != letter:
                            if let in letter_amounts.keys():
                                continue
                            else:
                                letter_amounts[letter] -= 1
                                used_blocks.append(index)
                    if letter_amounts[letter] == 0:
                        del letter_amounts[letter]
                        del block_indexes[letter]
                        break

        if remaining_letters == sorted(block_indexes.items(), key=lambda x: len(x[1])):
            return True
        else:
            remaining_letters = sorted(block_indexes.items(), key=lambda x: len(x[1]))

    return True


for word in sample_words:
    print(can_make_word(sample_blocks, word))
