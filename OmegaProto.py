allCharacters = 'Omega'
print("current characters are:")
print allCharacters
P1_character1 = input("what's your first character going to be?")
def character1_check():
    #checking what character is and what moves should be
    if P1_character1 == ("Omega".lower()):
        P1_character1_move1 = "Dark Slash"
        P1_character1_move2 = "Shadow Strike"
        P1_character1_move3 = "Blade Spin"
        P1_character1_move4 = "Dark Charge" 
    else:
        character1_check
character1_check ()
print(P1_character1 + "\'s moves are," + P1_character1_move1 + ", " + P1_character1_move2 +", " + P1_character1_move3 + ", " + P1_character1_move4 + ". ")
