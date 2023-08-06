from gamestrip import Game


def _pre_game():
    print("""
    Lab work №4 - Strip Solitaire,variant 110.Author - Vladislav Zabrovsky, group - K-13.
    Rules: It is allowed to move the bottom cards of the game stacks in ascending or descending sequences on base stacks. 
    Moving cards from one game stack to another game stack is prohibited.Solitaire is done if all  cards are collected 
    on the base stacks in strictly ascending sequences in the suit.
    Examples of ascending sequences: 
    1) ['A of Diamonds', '2 of Diamonds', '5 of Diamonds', '10 of Diamonds', 'J of Diamonds', 'K of Diamonds']
    2) ['A of Spades', '4 of Spades', '6 of Spades', '9 of Spades', 'J of Spades', 'Q of Spades']
    3) ['4 of Hearts', '10 of Hearts',  'K of Hearts']
    Examples of descending sequences:
    1) ['K of Diamonds', 'J of Diamonds', '9 of Diamonds', '6 of Diamonds', '2 of Diamonds', 'A of Diamonds']
    2) ['Q of Spades', '10 of Spades', '3 of Spades', '2 of Spades']
    3) ['8 of Hearts', '7 of Hearts',  '3 of Hearts']
    Strictly ascending sequence means that:
    1) Every card on a base stack has the same suit.
    2) Difference between values of each card = 1.
    3) Sequence is ascending.
    For example: ['A of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds'] is strictly monotone,
                 ['A of Diamonds', '2 of Diamonds', '5 of Diamonds', '6 of Diamonds'] is not strictly monotone.
    """)

    print('--------------------------------------------------------------------')


def _show_menu():
    while True:
        print("Menu:")
        print("1. Play Strip Solitaire")
        print("2. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            main()
        elif choice == '2':
            print('End of the game.Good luck next time!')
            break
        else:
            print("Invalid choice, please try again.")
            print('---------------------------------------------------------------------------------------------')


def main():
    game = Game()
    playing = True
    while playing and not game.is_win():
        game.show_info()
        valid_move = False
        while not valid_move:
            take_stack = input("Take from stack (1-4), or enter 'q' to quit: ")
            if not take_stack.isdigit():
                if take_stack == 'q':
                    playing = False
                break

            put_stack = input("Put on stack (1-6): ")
            if not put_stack.isdigit():
                break

            take_stack = int(take_stack) - 1
            put_stack = int(put_stack) - 1
            valid_move = game.move_card(take_stack, put_stack)
            if not valid_move:
                print("Invalid move, please try again.")
        print('---------------------------------------------------------------------------------------------')

    if game.is_win():
        game.show_info()
        print("You win!Congratulations")
    else:
        print('End of the game.Good luck next time!')
        print('---------------------------------------------------------------------------------------------')


try:
    _pre_game()
    _show_menu()

except KeyboardInterrupt:
    print('\nEnd of the game.Good luck next time!')
except Exception:
    print('\nStop of program.Try again')
