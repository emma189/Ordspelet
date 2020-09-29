import random


def welcome_message():
    return "\n---Välkommen till Ordspelet!---"


def menu():
    return"""
----------Meny----------
Välj roll 1 eller 2:
Roll 1 - Gissare
Roll 2 - Tänk på ett ord

Q för att avsluta spelet"""


def random_word_generator():
    try:
        with open("words.txt", "r") as file:
            random_word = random.choice(file.readlines()).strip()
        return random_word
    except FileNotFoundError:
        print("Filen words.txt måste finnas med för att köra spelet.")


def create_word_list():
    try:
        with open("words.txt", "r") as file:
            file_content = [word.strip() for word in file.readlines()]
        return file_content
    except FileNotFoundError:
        print("Filen words.txt måste finnas med för att köra spelet.")


def player_think_of_word():
    while True:
        word = input("\nTänkt på ett ord och mata in det: ")
        if len(word) != 5 and not word == "q":
            print("Ordet måste innehålla 5 bokstäver. Försök igen!\n")
        elif word.isalpha() == False:
            print("Ordet får inte innehålla nummer eller specialtecken. Försök igen!\n")
        else:
            return word


def player_guess():
    while True:
        guess = input("\nMata in gissning: ").lower()
        if len(guess) == 5 and guess.isalpha() == True:
            return guess
        elif guess == "q":
            return guess
        else:
            print("Felaktig inmatning, försök igen!\n")
            continue


def computer_guess(game_list):
    if len(game_list) == 0:
        return "Jag ger upp!"
    else:
        guess = random.choice(game_list)
        return f"\nGissning: {guess}"


def guess_check_if_correct(random, guess, guess_counter):
    if random == guess:
        return f"\nDu vann! Antal gissningar: {guess_counter}"
    elif guess == "q":
        return f"\nAvslutar spelet... Det rätta ordet var: {random}\n"
    else:
        return "check chars"


def char_checker(guess, random):
    char_right_place = 0
    char_in_word = 0

    for i, _ in enumerate(guess):
        if guess[i] == random[i]:
            char_right_place += 1
        elif guess[i] in random:
            char_in_word += 1
        else:
            pass
    return f"""
Antal RÄTT bokstäver på RÄTT plats: {char_right_place} 
Antal RÄTT bokstäver men på FEL plats: {char_in_word}\n"""


# Function to let player manually check if computers guess is correct or not
def player_right_wrong_prompt():
    while True:
        player_correction = input(
            "Ange 'r' om gissningen är RÄTT och 'f' om gissningen är FEL:\n> ").lower()
        if player_correction == "r" or player_correction == "f" or player_correction == "q":
            return player_correction
        else:
            print("Felaktig inmatning, försök igen!")
            continue


def right_guess_message():
    return "\nRätt svar! Du vann!"


def player_right_char_prompt():
    while True:
        char_right_place = input(
            "Ange antalet RÄTT bokstäver på RÄTT plats:\n> ")
        if char_right_place.isdigit() == False:
            print("Felaktig inmatning, försök igen!\n")
            continue
        else:
            pass

        char_in_word = input(
            "Ange antalet RÄTT bokstäver på FEL plats:\n> ")
        if char_in_word.isdigit() == False:
            print("Felaktig inmatning, försök igen!\n")
            continue
        else:
            pass

        total_right_chars = int(char_right_place) + int(char_in_word)
        return total_right_chars


def remove_wrong_words_from_list(game_list, guess, total_right_chars):
    if total_right_chars == 0:
        game_list = [word for word in game_list if not len(
            (set(word)).intersection(set(guess))) == 5]
    elif total_right_chars >= 1:
        game_list = [word for word in game_list if len(
            set(word).intersection(set(guess))) >= total_right_chars]
        if guess in game_list:
            game_list.remove(guess)
    return game_list


def quit_game_message():
    return "\nAvslutar spelet..."
