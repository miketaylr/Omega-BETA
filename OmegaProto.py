all_characters = ['Omega']
print("current characters are:")
move1 = 'N/A'
move2 = 'N/A'
move3 = 'N/A'
move4 = 'N/A'


def character1_check():
    global move1
    global move2
    global move3
    global move4
    P1_character1 = raw_input("what's your first character going to be?")
    if P1_character1 in all_characters:
        if P1_character1 == 'Omega'.lower():
            move1 = 'Dark Slash'
            move2 = 'Shadow Strike'
            move3 = 'Blade Spin'
            move4 = 'Dark Charge'
    print('{}\'s moves are: {}, {}, {}, and {}.'.format(P1_character1, move1, move2, move3, move4))
    else:
        character1_check()
character1_check()
