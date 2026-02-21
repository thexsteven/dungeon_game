from Game import Game

YES_ANSWERS = {"y", "yes"}
NO_ANSWERS = {"n", "no"}

def ask_yes_no(prompt):
    """Ask the user and only accept y/yes/n/no."""
    while True:
        answer = input(f"{prompt} (y/n): ").strip().lower()
        if answer in YES_ANSWERS:
            return True
        if answer in NO_ANSWERS:
            return False
        print("Please enter 'y' or 'n'.")

def main():
    print("You are now entering the Dungeon Game, BE CAREFUL!\n")
    
    while True:
        game = Game()
        game.start()
        game.run_game()
        
        print("\n" + "="*30)
        if not ask_yes_no("Wanna play again?"):
            print("Thanks for playing the Dungeon Game. Goodbye!")
            break

if __name__ == "__main__":
    main()