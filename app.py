import game_functions as func


def main():                                             
    print(func.welcome_message())
    while True:
        print(func.menu())
        game_type_choice = input("> ")
        if game_type_choice == "1":
            game_type_1()
        elif game_type_choice == "2":
            game_type_2()
        elif game_type_choice == "q":
            print(func.quit_game_message())
            break
        else:
            print("Felaktig inmatning, försök igen!")


# Function for game-type 1 where the player will guess the word
def game_type_1():
    random = func.random_word_generator()
    print("\nDatorns ord: _ _ _ _ _\n")
    guess_counter = 0

    while True:
        guess = func.player_guess()
        guess_counter += 1
        guess_check = func.guess_check_if_correct(random, guess, guess_counter)
        if guess_check == "check chars":
            print(func.char_checker(guess, random))
        else:
            print(guess_check)
            break


# Function for game-type 2 where the player will think of a word
def game_type_2():
    word = func.player_think_of_word()
    game_list = func.create_word_list()
    while True:
        guess = func.computer_guess(game_list)
        print(guess)
        if guess == "Jag ger upp":
            print(func.quit_game_message())
            break

        # lets the player manually check if the computers guess is right or wrong
        player_correction = func.player_right_wrong_prompt()
        if player_correction == "f":
            total_right_chars = func.player_right_char_prompt()
            game_list = func.remove_wrong_words_from_list(
                game_list, guess, total_right_chars)
        elif player_correction == "r":
            print(func.right_guess_message())
            break
        elif player_correction == "q":
            print(func.quit_game_message())
            break


if __name__ == "__main__":
    main()
